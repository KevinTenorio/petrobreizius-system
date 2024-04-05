from pydantic import Field, UUID4, EmailStr
from domain.schemas.generic import GenericModel
from datetime import datetime
from domain.schemas.event import Event

class EmployeeBase(GenericModel):
    name: str = Field(example="João Petrobreizius", title="Employee name")
    email: EmailStr | None = Field(example="joao_petrobreizius@email.com.br", title="Employee email")
    birthdate: datetime | None = Field(example="1980-01-01T00:00:00", title="Employee birthdate")
    phone: str | None = Field(example="+55 21 99999-9999", title="Employee phone number")
    avatar: str | None = Field(example="https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50", title="Employee avatar")

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: UUID4 = Field(example="123e4567-e89b-12d3-a456-426614174000", title="Employee UUID")
    events: list[Event] = Field(example=[], title="List of events UUIDs")
    class Config:
        from_attributes = True
