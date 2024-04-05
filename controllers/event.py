from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.event import EventCreate, Event
from services import event as event_service
from uuid import UUID

router = APIRouter()

TAGS = ["Events"]


## Events -------------------------------------------------------------------
@router.get("/events", tags=TAGS, summary='Fetch a list of all events', response_model=list[Event])
def get_events_list(db: Session = Depends(get_session)):
    return event_service.get_events(db)

@router.post("/events", tags=TAGS, summary='Add a new event', status_code=201, response_model=Event)
def add_event(event: EventCreate, db: Session = Depends(get_session)):
    return event_service.post_event(db, event)

@router.get("/events/{id}", tags=TAGS, summary='Fetch an event', response_model=Event)
def get_event(id: UUID, db: Session = Depends(get_session)):
    return event_service.get_event(db, id)

@router.put("/events/{id}", tags=TAGS, summary='Update an event', response_model=Event)
def update_event(id: UUID, event: EventCreate, db: Session = Depends(get_session)):
    return event_service.put_event(db, id, event)

@router.delete("/events/{id}", tags=TAGS, summary='Delete an event', response_model=Event)
def delete_event(id: UUID, db: Session = Depends(get_session)):
    return event_service.delete_event(db, id)

@router.post("/events/{event_id}/invite/{employee_id}", tags=TAGS, summary='Invite an employee to an event')
def invite_to_event(event_id: UUID, employee_id: UUID, db: Session = Depends(get_session)):
    return event_service.invite_to_event(db, event_id, employee_id)