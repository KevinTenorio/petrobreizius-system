from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from uuid import uuid4

from domain.models.generic import GenericBase

class Employee(GenericBase):
    __tablename__ = "employees"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)
    email = Column("email", String)
    birthdate = Column("birthdate", String)
    phone = Column("phone", String)
    avatar = Column("avatar", String)

    events = relationship("Event", secondary="employees_events", back_populates="employees")