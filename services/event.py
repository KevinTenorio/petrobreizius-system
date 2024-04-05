from sqlalchemy.orm import Session

from repositories import event as event_repository


def get_events(db: Session):
    return event_repository.get_events(db)

def post_event(db: Session, event):
    return event_repository.post_event(db, event)

def get_event(db: Session, event_id):
    return event_repository.get_event(db, event_id)

def put_event(db: Session, event_id, event):
    return event_repository.put_event(db, event_id, event)

def delete_event(db: Session, event_id):
    return event_repository.delete_event(db, event_id)

def invite_to_event(db: Session, event_id, employee_id):
    return event_repository.invite_to_event(db, event_id, employee_id)

def find_time_for_event(db: Session, employees_ids):
    return event_repository.find_time_for_event(db, employees_ids)