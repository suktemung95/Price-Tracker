from fastapi import APIRouter
from scrapers.scraper_selector import get_scraper
import services.productServices as s
from pydantic import BaseModel

class ScrapeRequest(BaseModel):
    url: str

router = APIRouter()

@router.post("/")
def scraper(req: ScrapeRequest):
    # get data
    scraper = get_scraper(req.url)
    name, price = scraper.get_product(req.url)

    # post data onto database
    return s.add_product(name, req.url, price)