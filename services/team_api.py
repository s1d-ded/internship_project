from fastapi import FastAPI,APIRouter, HTTPException
from services import team_service

router = APIRouter()

@router.get("/")
def get_all_teams():
    return team_service.get_team()

@router.post("/")
def add_new_team(team: dict):
    return team_service.add_team(team)

@router.put("/{team_id}")
def update_team(team_id: int, update_data: dict):
    return team_service.update_team(team_id, update_data)

@router.delete("/{team_id}")
def delete_team(team_id: int):
    status = team_service.delete_team(team_id)
    if status == 404:
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team deleted successfully"}
