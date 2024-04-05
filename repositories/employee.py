from sqlalchemy.orm import Session
from fastapi import HTTPException
from domain.models.employee import Employee
from domain.schemas.employee import EmployeeCreate
from uuid import UUID

def get_employees(db: Session):
    return db.query(Employee).all()

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

