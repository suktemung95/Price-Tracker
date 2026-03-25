from urllib.parse import urlparse
from .aula import AulaScraper

SCRAPERS = {
    # key, scraper
    "aula": AulaScraper,
}

def get_scraper(url: str):
    domain = urlparse(url).netloc.lower()

    for key, scraper_class in SCRAPERS.items():
        if key in domain:
            return scraper_class()
    
    raise Exception(f"No scraper found for domain: {domain}")