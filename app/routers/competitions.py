from fastapi import APIRouter, Query
from app.services.competitions import links_service, scrape

router = APIRouter()

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