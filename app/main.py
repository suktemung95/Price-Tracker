import scrape

url = 'https://www.amazon.com/Monster-Energy-Variety-Pipeline-Pacific/dp/B0CGMF1J8Z?ref_=pd_bap_d_grid_rp_0_1_ec_t'
res = scrape.get_price_from_url(url)

print(res)