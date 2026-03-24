import psycopg2
def execute(query, values=None):
    con = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )

    cur = con.cursor()

    try:
        # execute query
        cur.execute(query, values)

        last = query.strip().upper()
        res = None
        # on a select statement, return the selected objects
        if last.startswith("SELECT"):
            res = cur.fetchall()
            
        # on an INSERT or UPDATE statement, return the product id
        elif last.startswith(("INSERT", "UPDATE", "DELETE")):
            res = cur.fetchone()

        con.commit()
        return res

    finally:
        cur.close()
        con.close()

        print("Closed connection. Executed function")
 
def initialize_db():

    query = """
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        url TEXT UNIQUE NOT NULL,
        price NUMERIC NOT NULL,
        last_checked TIMESTAMP NOT NULL
    );
    """

    con = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='127.0.0.1',
        port=5432
    )

    cur = con.cursor()

    try:
        cur.execute(query)
    finally:
        con.commit()
        cur.close()
        con.close()

        print("Closed connection. Executed function")

        last = query.strip().upper()
        if last.startswith("SELECT"):
            return cur.fetchall()

def add_product (name, url, price):

    query = """
        INSERT INTO products (name, url, price, last_checked) 
        VALUES (%s, %s, %s, NOW())
        RETURNING *
        """
    values = (name, url, price)
    
    return execute(query, values)

def update_price (product_id, new_price):

    query = """
    UPDATE products
    SET price = %s, last_checked = NOW()
    WHERE id = %s
    RETURNING id, price;
    """
    values = (new_price, product_id)

    return execute(query, values)

def get_product(product_id):

    query = """
    SELECT * FROM products
    WHERE id=%s"""
    return execute(query, (product_id,)) 

def get_products(conditions, values=None):

    query = """
    SELECT * from products
    """
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    
    return execute (query, values)

def delete_product(product_id):

    query = """
    DELETE FROM products
    WHERE id = %s
    RETURNING *;
    """

    return execute(query, (product_id,))