from pydantic import Field, UUID4
from domain.schemas.generic import GenericModel

class RoomBase(GenericModel):
    name: str = Field(example="Sala 00", title="Room name")

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: UUID4 = Field(example="123e4567-e89b-12d3-a456-426614174000", title="Room UUID")
    class Config:
        from_attributes = True
