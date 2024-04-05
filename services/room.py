from sqlalchemy.orm import Session

from repositories import room as room_repository


def get_rooms(db: Session):
    return room_repository.get_rooms(db)

def post_room(db: Session, room):
    return room_repository.post_room(db, room)

def get_room(db: Session, room_id):
    return room_repository.get_room(db, room_id)

def put_room(db: Session, room_id, room):
    return room_repository.put_room(db, room_id, room)

def delete_room(db: Session, room_id):
    return room_repository.delete_room(db, room_id)