from sqlalchemy.orm import Session
from fastapi import HTTPException
from domain.models.employee import Employee
from domain.models.employee_event import EmployeeEvent
from domain.models.event import Event
from domain.schemas.employee import EmployeeCreate
from uuid import UUID

def get_employees(db: Session):
    db_employees = db.query(Employee).all()
    for db_employee in db_employees:
        db_employee.events = db.query(Event).filter(Event.id.in_([employee_event.eventid for employee_event in db.query(EmployeeEvent).filter(EmployeeEvent.employeeid == db_employee.id).all()])).all()
    return db_employees

def post_employee(db: Session, employee: EmployeeCreate):
    request_dict = employee.model_dump()
    new_employee = Employee(**request_dict)
    db.add(new_employee)

    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_employee(db: Session, employee_id: UUID):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail=f'Employee of id={employee_id} not found')
    db_employee.events = db.query(Event).filter(Event.id.in_([employee_event.eventid for employee_event in db.query(EmployeeEvent).filter(EmployeeEvent.employeeid == db_employee.id).all()])).all()
    return db_employee

def put_employee(db: Session, employee_id: UUID, employee: EmployeeCreate):
    db_employee = get_employee(db, employee_id)
    request_dict = employee.model_dump()
    for key, value in request_dict.items():
        setattr(db_employee, key, value)
    db.commit()
    return db_employee

def delete_employee(db: Session, employee_id: UUID):
    db_employee = get_employee(db, employee_id)
    db.delete(db_employee)
    db.commit()
    return db_employee

def get_events_list(db: Session, employee_id: UUID):
    employee_events_ids = db.query(EmployeeEvent).filter(EmployeeEvent.employeeid == employee_id).all()
    employee_events = db.query(Event).filter(Event.id.in_([employee_event.eventid for employee_event in employee_events_ids])).all()
    return employee_events

