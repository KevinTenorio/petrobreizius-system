from sqlalchemy.orm import Session

from repositories import employee as employee_repository


def get_employees(db: Session):
    return employee_repository.get_employees(db)

def post_employee(db: Session, employee):
    return employee_repository.post_employee(db, employee)

def get_employee(db: Session, employee_id):
    return employee_repository.get_employee(db, employee_id)

def put_employee(db: Session, employee_id, employee):
    return employee_repository.put_employee(db, employee_id, employee)

def delete_employee(db: Session, employee_id):
    return employee_repository.delete_employee(db, employee_id)