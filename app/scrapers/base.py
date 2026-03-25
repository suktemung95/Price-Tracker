from bs4 import BeautifulSoup
import requests

class BaseScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }
    
    def get_product(self, url: str):
        html = self.fetch(url)
        soup = self.get_soup(html)
        return self.parse(soup)

    def fetch(self, url: str) -> str:
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200: 
            raise Exception(f"Failed to fetch page: {response.status_code}")
        
        return response.text
    
    def get_soup(self, html: str):
        return BeautifulSoup(html, "html.parser")
    
    def parse(self, soup):
        raise NotImplementedError("Each scraper much implement parse()")
    
    def get_meta_content(self, soup, prop):
        tag = soup.find("meta", property=prop)
        if tag and tag.get("content"):
            return tag["content"]
        return None