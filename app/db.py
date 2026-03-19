import psycopg2
def execute(query, values=None):
    con = psycopg2.connect(
        dbname='price_tracker_db',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )

    cur = con.cursor()

    try:
        cur.execute(query, values)
    finally:
        con.commit()
        cur.close()
        con.close()

        print("Closed connection. Executed function")

        last = query.strip().upper()
        if last.startswith("SELECT"):
            return cur.fetchall()
 
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

    execute(query)

def add_product (name, url, price):

    query = """
        INSERT INTO products (name, url, price, last_checked)
        VALUES (%s, %s, %s, NOW())
        """
    values = (name, url, price)
    
    execute(query, values)
def update_price (product_id, new_price):

    query = """
    UPDATE products
    SET price = %s, last_checked = NOW()
    WHERE id = %s;
    """
    values = (new_price, product_id)

    execute(query, values)

def get_product(id):

    query = """
    SELECT * FROM products
    WHERE id=%s"""
    return execute(query, (id))