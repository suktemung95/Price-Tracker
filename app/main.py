from scrape import get_product_from_url
from db import add_product, initialize_db, update_price, get_all_products

# initialize_db()

url = 'https://www.amazon.com/Monster-Energy-Variety-Pipeline-Pacific/dp/B0CGMF1J8Z?ref_=pd_bap_d_grid_rp_0_1_ec_t'
name, price = get_product_from_url(url)

# product = add_product(name, url, price)
# print(product)
# product = update_price(product, 500)
# print(product)

print(get_all_products())