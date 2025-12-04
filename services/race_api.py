from fastapi import APIRouter, HTTPException
from services import race_service

router = APIRouter()

@router.get("/")
def get_all_races():
    return race_service.get_race()

@router.post("/")
def add_new_race(race: dict):
    return race_service.add_race(race)

@router.put("/{race_id}")
def update_race(race_id: int, update_data: dict):
    return race_service.update_race(race_id, update_data)

@router.delete("/{race_id}")
def delete_race(race_id: int):
    status = race_service.delete_race(race_id)
    if status == 404:
        raise HTTPException(status_code=404, detail="Race not found")
    return {"message": "Race deleted successfully"}
