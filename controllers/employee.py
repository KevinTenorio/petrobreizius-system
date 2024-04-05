from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.employee import EmployeeCreate, Employee
from services import employee as employee_service
from uuid import UUID

router = APIRouter()

TAGS = ["Employees"]


## Employees -------------------------------------------------------------------
@router.get("/employees", tags=TAGS, summary='Fetch a list of all employees', response_model=list[Employee])
def get_employees_list(db: Session = Depends(get_session)):
    return employee_service.get_employees(db)

@router.post("/employees", tags=TAGS, summary='Add a new employee', status_code=201, response_model=Employee)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_session)):
    return employee_service.post_employee(db, employee)

@router.get("/employees/{id}", tags=TAGS, summary='Fetch an employee', response_model=Employee)
def get_employee(id: UUID, db: Session = Depends(get_session)):
    return employee_service.get_employee(db, id)

@router.put("/employees/{id}", tags=TAGS, summary='Update an employee', response_model=Employee)
def update_employee(id: UUID, employee: EmployeeCreate, db: Session = Depends(get_session)):
    return employee_service.put_employee(db, id, employee)

@router.delete("/employees/{id}", tags=TAGS, summary='Delete an employee', response_model=Employee)
def delete_employee(id: UUID, db: Session = Depends(get_session)):
    return employee_service.delete_employee(db, id)