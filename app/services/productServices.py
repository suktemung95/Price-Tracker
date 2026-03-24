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

def get_products(min_price, max_price, name, min_id, max_id):

    conditions = []
    values = []

    if min_price:
        conditions.append("price >= %s")
        values.append(min_price)
    if max_price:
        conditions.append("price <= %s")
        values.append(max_price)
    if name:
        conditions.append("name ILIKE %s")
        values.append(f"%{name}%")
    if min_id:
        conditions.append("id >= %s")
        values.append(min_id)
    if max_id:
        conditions.append("id <= %s")
        values.append(max_id)

    products = db.get_products(conditions, values)
    formatted_products = format_all(products)
    return formatted_products

def delete_product(product_id):
    product = db.delete_product(product_id)
    formatted_product = format(product)
    return formatted_product