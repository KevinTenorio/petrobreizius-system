from pydantic import Field, UUID4
from domain.schemas.generic import GenericModel
from datetime import datetime

class EventBase(GenericModel):
    name: str = Field(example="Reunião 00", title="Event name")
    roomid: UUID4 | None = Field(example="123e4567-e89b-12d3-a456-426614174000", title="Room UUID")
    start: datetime = Field(example="1980-01-01T00:00:00", title="Event start datetime")
    finish: datetime = Field(example="1980-01-01T00:00:00", title="Event finish datetime")

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: UUID4 = Field(example="123e4567-e89b-12d3-a456-426614174000", title="Event UUID")
    class Config:
        from_attributes = True
