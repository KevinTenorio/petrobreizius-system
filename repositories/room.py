from sqlalchemy.orm import Session
from fastapi import HTTPException
from domain.models.room import Room
from domain.schemas.room import RoomCreate
from uuid import UUID


def get_rooms(db: Session):
    return db.query(Room).all()

def post_room(db: Session, room: RoomCreate):
    request_dict = room.model_dump()
    new_room = Room(**request_dict)
    db.add(new_room)

    db.commit()
    db.refresh(new_room)
    return new_room

def get_room(db: Session, room_id: UUID):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if db_room is None:
        raise HTTPException(status_code=404, detail=f'Room of id={room_id} not found')
    return db_room

def put_room(db: Session, room_id: UUID, room: RoomCreate):
    db_room = get_room(db, room_id)
    request_dict = room.model_dump()
    for key, value in request_dict.items():
        setattr(db_room, key, value)
    db.commit()
    return db_room

def delete_room(db: Session, room_id: UUID):
    db_room = get_room(db, room_id)
    db.delete(db_room)
    db.commit()
    return db_room