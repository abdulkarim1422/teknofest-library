from fastapi import APIRouter, Query
from app.services.scrape.competitions import links_service, scrape

router = APIRouter()

@router.get("/competition-scrape")
async def scrape_competition(
    link: str = Query(..., description="competition link"),
    update_database: bool = Query(False, description="update database"),
    year: str = Query(None, description="year")
):
    scrape.scrape_link(link=link, update_database=update_database, year=year)
    return

@router.get("/competition-scrape-all")
async def scrape_all_competitions(
    lang: str = Query("tr", description="language"),
    update_database: bool = Query(False, description="update database"),
    year: str = Query(None, description="year")
):
    scrape.scrape_all_links(lang=lang, update_database=update_database, year=year)
    return

@router.get("/competition-links")
async def get_competition_links(
    lang: str = Query("tr", description="language")
):
    return links_service.get_all_links(lang)

@router.get("/competition-link-names")
async def get_competition_names(
    lang: str = Query("tr", description="language")
):
    return links_service.get_all_link_names(lang)

@router.get("/competition-names")
async def get_competition_names(
    lang: str = Query("tr", description="language")
):
    return links_service.get_all_name(lang)