from sqlalchemy import Column, String, UUID
from uuid import uuid4
from sqlalchemy.orm import relationship
from domain.models.generic import GenericBase

class Room(GenericBase):
    __tablename__ = "rooms"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)