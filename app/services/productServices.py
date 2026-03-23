import db
columns = ["id", "name", "url", "price", "last_checked"]

def format(row):
    res = dict(zip(columns, row)) 
    return res

def format_all(rows):
    res = [dict(zip(columns, rows))]
    return res

def add_product(name, url, price):
    product = db.add_product(name, url, price)
    formatted_product = format(product)
    return formatted_product

def update_price(product_id, new_price):
    product = db.update_price(product_id, new_price)
    formatted_product = format(product)
    return formatted_product

def get_product(product_id):
    product = db.get_product(product_id)
    formatted_product = format(product)
    return formatted_product

def get_all_products():
    products = db.get_all_products()
    formatted_products = format_all(products)
    return formatted_products

def delete_product(product_id):
    product = db.delete_product(product_id)
    formatted_product = format(product)
    return formatted_product