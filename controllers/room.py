from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.room import RoomCreate, Room
from services import room as room_service
from uuid import UUID

router = APIRouter()

TAGS = ["Rooms"]


## Rooms -------------------------------------------------------------------
@router.get("/rooms", tags=TAGS, summary='Fetch a list of all rooms', response_model=list[Room])
def get_rooms_list(db: Session = Depends(get_session)):
    return room_service.get_rooms(db)

@router.post("/rooms", tags=TAGS, summary='Add a new room', status_code=201, response_model=Room)
def add_room(room: RoomCreate, db: Session = Depends(get_session)):
    return room_service.post_room(db, room)

@router.get("/rooms/{id}", tags=TAGS, summary='Fetch a room', response_model=Room)
def get_room(id: UUID, db: Session = Depends(get_session)):
    return room_service.get_room(db, id)

@router.put("/rooms/{id}", tags=TAGS, summary='Update a room', response_model=Room)
def update_room(id: UUID, room: RoomCreate, db: Session = Depends(get_session)):
    return room_service.put_room(db, id, room)

@router.delete("/rooms/{id}", tags=TAGS, summary='Delete a room', response_model=Room)
def delete_room(id: UUID, db: Session = Depends(get_session)):
    return room_service.delete_room(db, id)

@router.post("/rooms/find_free", tags=TAGS, summary='Find free rooms', response_model=list[Room])
def find_free_rooms(start: str, finish: str, db: Session = Depends(get_session)):
    return room_service.find_free_rooms(db, start, finish)