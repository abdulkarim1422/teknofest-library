from fastapi import APIRouter, Request, Query
from app.services import teams

router = APIRouter()

@router.get("/teams-page")
async def download_teams_files(
    page: int = Query(..., description="page number")
):
    teams.scrape_page(page)
    return

@router.get("/teams-all")
async def download_all_teams_files(
    first_page: int = Query(..., description="first page number"),
    last_page: int = Query(..., description="last page number")
):
    teams.scrape_all_links(first_page, last_page)
    return