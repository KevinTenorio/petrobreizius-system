from sqlalchemy.orm import Session
from fastapi import HTTPException
from domain.models.room import Room
from domain.models.event import Event
from domain.schemas.room import RoomCreate
from uuid import UUID
from datetime import datetime
from commons.check_meeting_collision import check_meeting_collision


def get_rooms(db: Session):
    return db.query(Room).all()

def post_room(db: Session, room: RoomCreate):
    request_dict = room.model_dump()
    new_room = Room(**request_dict)
    db.add(new_room)

    db.commit()
    db.refresh(new_room)
    return new_room

def get_room(db: Session, room_id: UUID):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail=f'Room of id={room_id} not found')
    return db_room

def put_room(db: Session, room_id: UUID, room: RoomCreate):
    db_room = get_room(db, room_id)
    request_dict = room.model_dump()
    for key, value in request_dict.items():
        setattr(db_room, key, value)
    db.commit()
    return db_room

def delete_room(db: Session, room_id: UUID):
    db_room = get_room(db, room_id)
    db.delete(db_room)
    db.commit()
    return db_room

def find_free_rooms(db: Session, start: datetime, finish: datetime):
    db_rooms = get_rooms(db)
    free_rooms = []
    for db_room in db_rooms:
        room_events = db.query(Event).filter(Event.roomid == db_room.id).all()
        room_times = []
        for room_event in room_events:
            room_times.append((datetime.strptime(room_event.start, "%Y-%m-%d %H:%M:%S"), datetime.strptime(room_event.finish, "%Y-%m-%d %H:%M:%S")))
        if not check_meeting_collision(datetime.strptime(start, "%Y-%m-%dT%H:%M:%S"), datetime.strptime(finish, "%Y-%m-%dT%H:%M:%S"), room_times):
            free_rooms.append(db_room)
    return free_rooms

