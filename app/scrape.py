import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Failed to fetch page")

    return response.text

def parse_html(html):
    return BeautifulSoup(html, 'html.parser')

# amazon extract price
def extract_price(soup):

    cost = soup.find('span', class_='a-offscreen')

    if not cost:
        print("Cost was", cost)
        raise Exception("Price not found")
    return f"{cost.text}"

def clean_price(price_text):
    return float(price_text.replace("$", "").strip())

def get_price_from_url(url):
    html = fetch_page(url)
    soup = parse_html(html)
    raw_price = extract_price(soup)
    return clean_price(raw_price)