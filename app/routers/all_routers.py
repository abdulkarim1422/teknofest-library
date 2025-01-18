from fastapi import APIRouter, Query
from app.routers import competitions, dates, teams, announcements

router = APIRouter()

router.include_router(competitions.router)
router.include_router(dates.router)
router.include_router(teams.router)
router.include_router(announcements.router)

@router.get("/")
async def root():
    return {"message": "Hello World"}