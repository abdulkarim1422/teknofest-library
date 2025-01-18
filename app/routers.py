from fastapi import APIRouter, Query
from app.services import teams
from app.services.competitions import links_service, scrape
from app.services.dates import call
from app.services import announcements

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

@router.get("/competition-scrape")
async def scrape_competition(
    link: str = Query(..., description="competition link")
):
    scrape.scrape_link(link)
    return

@router.get("/competition-scrape-all")
async def scrape_all_competitions(
    lang: str = Query("tr", description="language")
):
    scrape.scrape_all_links(lang)
    return

@router.get("/competition-links")
async def get_competition_links(
    lang: str = Query("tr", description="language")
):
    return links_service.get_all_links(lang)

@router.get("/competition-names")
async def get_competition_names(
    lang: str = Query("tr", description="language")
):
    return links_service.get_all_names(lang)

@router.get("/competition-dates-csv")
async def get_competition_dates(
    lang: str = Query("tr", description="language")
):
    call.process_links(lang)
    return

@router.get("/announcements-files")
async def download_announcements_files(
    year: int = Query(2025, description="year"),
    firstpage: int = Query(1, description="first page number"),
    lastpage: int = Query(3, description="last page number"),
    lang: str = Query("tr", description="language")
):
    announcements.call.main(year, firstpage, lastpage, lang)
    return
