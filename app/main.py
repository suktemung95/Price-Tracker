from scrape import get_product_from_url
from selScrape import get_amazon_price
from db import add_product, initialize_db

# initialize_db()

url = 'https://www.amazon.com/Monster-Energy-Variety-Pipeline-Pacific/dp/B0CGMF1J8Z?ref_=pd_bap_d_grid_rp_0_1_ec_t'
name, price = get_product_from_url(url)

add_product(name, url, price)