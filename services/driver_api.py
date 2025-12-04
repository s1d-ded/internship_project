from fastapi import APIRouter, HTTPException
from services import driver_service

router = APIRouter()

@router.get("/")
def get_all_drivers():
    return driver_service.get_driver()

@router.post("/")
def add_new_driver(driver: dict):
    return driver_service.add_driver(driver)

@router.put("/{driver_id}")
def update_driver(driver_id: int, update_data: dict):
    return driver_service.update_driver(driver_id, update_data)

@router.delete("/{driver_id}")
def delete_driver(driver_id: int):
    status = driver_service.delete_driver(driver_id)
    if status == 404:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"message": "Driver deleted successfully"}
