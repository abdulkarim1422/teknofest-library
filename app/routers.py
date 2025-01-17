from fastapi import APIRouter, Query
from app.services import teams
from app.services.competitions import scrape, links

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

@router.get("/scrape-competition")
async def scrape_competition(
    link: str = Query(..., description="competition link")
):
    scrape.scrape_link(link)
    return

@router.get("/scrape-all-competitions")
async def scrape_all_competitions(
    lang: str = Query("tr", description="language")
):
    scrape.scrape_all_links(lang)
    return