from fastapi import APIRouter, Query
from app.routers import scrape_routers

router = APIRouter()

router.include_router(scrape_routers.router, prefix="/api/scrape")

@router.get("/")
async def root():
    return {"message": "Hello World"}