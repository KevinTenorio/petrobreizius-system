from sqlalchemy import Column, String, UUID, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4
from domain.models.generic import GenericBase

class Event(GenericBase):
    __tablename__ = "events"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column("name", String, nullable=False)
    roomid = Column("roomid", UUID(as_uuid=True), ForeignKey("rooms.id"), nullable=False)
    start = Column("start", DateTime, nullable=False)
    finish = Column("finish", DateTime, nullable=False)

    employees = relationship("Employee", secondary="employees_events", back_populates="events")
