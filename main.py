from fastapi import FastAPI
from services import driver_api, team_api, race_api

app = FastAPI(title="F1 Project API")

app.include_router(driver_api.router, prefix="/drivers", tags=["Drivers"])
app.include_router(team_api.router, prefix="/teams", tags=["Teams"])
app.include_router(race_api.router, prefix="/races", tags=["Races"])
