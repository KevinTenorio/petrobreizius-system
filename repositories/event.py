from sqlalchemy.orm import Session
from fastapi import HTTPException
from domain.models.event import Event
from domain.models.room import Room
from domain.models.employee import Employee
from domain.schemas.event import EventCreate
from uuid import UUID
from commons.check_meeting_collision import check_meeting_collision
from datetime import datetime
from domain.models.employee_event import EmployeeEvent
from commons.merge_overlapping_events import merge_overlapping_events

def get_events(db: Session):
    return db.query(Event).all()

def post_event(db: Session, event: EventCreate):
    db_room = db.query(Room).filter(Room.id == event.roomid).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail=f'Room of id={event.roomid} not found')
    room_events = db.query(Event).filter(Event.roomid == event.roomid).all()
    room_times = []
    for room_event in room_events:
        room_times.append((datetime.strptime(room_event.start, "%Y-%m-%d %H:%M:%S"), datetime.strptime(room_event.finish, "%Y-%m-%d %H:%M:%S")))
    if check_meeting_collision(event.start, event.finish, room_times):
        raise HTTPException(status_code=400, detail='Event time collides with existing events in the room. Please choose another time or room.')
    request_dict = event.model_dump()
    new_event = Event(**request_dict)
    db.add(new_event)

    db.commit()
    db.refresh(new_event)
    return new_event

def get_event(db: Session, event_id: UUID):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail=f'Event of id={event_id} not found')
    return db_event

def put_event(db: Session, event_id: UUID, event: EventCreate):
    db_room = db.query(Room).filter(Room.id == event.roomid).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail=f'Room of id={event.roomid} not found')
    room_events = db.query(Event).filter(Event.roomid == event.roomid).filter(Event.id != event_id).all()
    room_times = []
    for room_event in room_events:
        room_times.append((datetime.strptime(room_event.start, "%Y-%m-%d %H:%M:%S"), datetime.strptime(room_event.finish, "%Y-%m-%d %H:%M:%S")))
    if check_meeting_collision(event.start, event.finish, room_times):
        raise HTTPException(status_code=400, detail='Event time collides with existing events in the room. Please choose another time or room.')
    db_event = get_event(db, event_id)
    request_dict = event.model_dump()
    for key, value in request_dict.items():
        setattr(db_event, key, value)
    db.commit()
    return db_event

def delete_event(db: Session, event_id: UUID):
    db_event = get_event(db, event_id)
    db.delete(db_event)
    db.commit()
    return db_event

def invite_to_event(db: Session, event_id: UUID, employee_id: UUID):
    db_event = get_event(db, event_id)
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail=f'Employee of id={employee_id} not found')
    employee_events_ids = db.query(EmployeeEvent).filter(EmployeeEvent.employeeid == employee_id).all()
    employee_events = db.query(Event).filter(Event.id.in_([employee_event.eventid for employee_event in employee_events_ids])).all()
    employee_times = []
    for employee_event in employee_events:
        employee_times.append((datetime.strptime(employee_event.start, "%Y-%m-%d %H:%M:%S"), datetime.strptime(employee_event.finish, "%Y-%m-%d %H:%M:%S")))
    if check_meeting_collision(datetime.strptime(db_event.start, "%Y-%m-%d %H:%M:%S"), datetime.strptime(db_event.finish, "%Y-%m-%d %H:%M:%S"), employee_times):
        raise HTTPException(status_code=400, detail='Employee cannot attend to this event because of time collision.')
    db_employee_event = EmployeeEvent(employeeid=employee_id, eventid=event_id)
    db.add(db_employee_event)
    db.commit()
    return db_employee_event

def find_time_for_event(db: Session, employees_ids: list[UUID]):
    employees_events = db.query(EmployeeEvent).filter(EmployeeEvent.employeeid.in_(employees_ids)).all()
    employees_events_ids = [employee_event.eventid for employee_event in employees_events]
    employees_events = db.query(Event).filter(Event.id.in_(employees_events_ids)).all()
    employees_times = []
    for employee_event in employees_events:
        employees_times.append((datetime.strptime(employee_event.start, "%Y-%m-%d %H:%M:%S"), datetime.strptime(employee_event.finish, "%Y-%m-%d %H:%M:%S")))
    merged_times = merge_overlapping_events(employees_times)
    return merged_times