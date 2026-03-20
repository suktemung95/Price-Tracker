import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    HEADERS = ({'User-Agent':
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        'Accept-Language': 'en-US, en;q=0.5'})

    # Making the HTTP Request
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception("Failed to fetch page")
    return response.text

def parse_html(html):
    return BeautifulSoup(html, 'html.parser')

# amazon extract price
def extract_price(soup):

    cost = soup.find('span', class_='a-offscreen')

    name = soup.find('span', id='productTitle')

    if not cost:
        raise Exception("Price not found")
    if not name:
        raise Exception("Name not found")

    res = [cost.text, name.text]

    return res

def clean_text(price_text, name_text):

    name_text = name_text.split(',')[0]

    return (float(price_text.replace("$", "").strip()), name_text)

def get_product_from_url(url):
    html = fetch_page(url)
    soup = parse_html(html)
    cost, name = extract_price(soup)
    return clean_text(cost, name)