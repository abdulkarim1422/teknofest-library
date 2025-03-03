from fastapi import APIRouter, Query
from app.services.scrape.teams import call, scrape

router = APIRouter()

@router.get("/teams-page")
async def download_teams_files(
    page: int = Query(..., description="page number")
):
    scrape.scrape_page(page)
    return

@router.get("/teams-all")
async def download_all_teams_files(
    first_page: int = Query(..., description="first page number"),
    last_page: int = Query(..., description="last page number"),
    update_database: bool = Query(False, description="update database")
):
    call.scrape_all_links(first_page, last_page, update_database)
    return
