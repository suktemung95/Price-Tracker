# from scrape import get_product_from_url
# from db import add_product, initialize_db, update_price, get_all_products
from scrapers.aula import AulaScraper
# initialize_db()

url = 'https://aulagear.com/products/aula-a700'
aula = AulaScraper()

name, price = aula.get_product(url)
print(name, price)

# product = add_product(name, url, price)
# print(product)
# product = update_price(product, 500)
# print(product)
