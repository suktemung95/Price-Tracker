import psycopg2
def get_connection():

    conn = psycopg2.connect(
        dbname='price_tracker_db',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )

    cur = conn.cursor()

    return (conn, cur)
def close_connection(conn, cur):

    conn.commit()
    conn.close()
    cur.close()

    print("Closed connection. Executed function")
def add_product (name, url, price, last_checked):

    con, cur = get_connection()

    query = """
        INSERT INTO products (name, url, price, last_checked)
        VALUES (%s, %s, %s, %s)
        """
    values = (name, url, price, last_checked)
    
    cur.execute(query, values)

    close_connection(con, cur)
def update_price (id, new_price):

    con, cur = get_connection()
    cur.execute("""
    UPDATE products
    SET price = %s, last_checked = NOW()
    WHERE id = %s;
    """, (new_price, id))

    close_connection(con, cur)