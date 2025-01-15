from fastapi import APIRouter, Request, Query
from app.services import teams

router = APIRouter()

@router.post("/teams-page")
async def download_teams_files(
    page: int = Query(..., description="page number")
):
    teams.scrape_link(page)
    return

