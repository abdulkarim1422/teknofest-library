from fastapi import APIRouter, Request, Query
from app.services import teams

router = APIRouter()

@router.post("/teams")
async def download_teams_files(
    link: str = Query(..., description="link")
):
    teams.scrape_link(link)
    return

