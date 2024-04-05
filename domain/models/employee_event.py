from sqlalchemy import Column,  UUID, ForeignKey
from sqlalchemy.orm import relationship
from domain.models.generic import GenericBase

class EmployeeEvent(GenericBase):
    __tablename__ = "employees_events"

    employeeid = Column("employeeid", UUID(as_uuid=True), ForeignKey("employees.id"), primary_key=True)
    eventid = Column("eventid", UUID(as_uuid=True), ForeignKey("events.id"), primary_key=True)
