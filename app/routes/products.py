from fastapi import FastAPI, status
from pydantic import BaseModel
import db

class Product(BaseModel):
    name: str
    url: str
    price: float

class ProductUpdatePrice(BaseModel):
    product_id: int
    price: float

app = FastAPI()
@app.post("/start")
def initalize_db():
    return db.initialize_db()

@app.get("/products")
def get_products():
    return db.get_all_products()

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return db.get_product(product_id)

@app.post("/products", status_code=status.HTTP_201_CREATED)
def post_product(product: Product):
    product = db.add_product(product.name, product.url, product.price)

    # if not product:
    #     raise HTTPException(404, "Product not found")
    
    return product

@app.patch("/products")
def update_price(product: ProductUpdatePrice):
    return db.update_price(product.product_id, product.price)

@app.delete("/products/{product_id}")
def get_product(product_id: int):
    return db.delete_product(product_id)