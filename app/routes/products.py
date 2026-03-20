from fastapi import FastAPI
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

@app.get("/products")
def get_products():
    return db.get_all_products()

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return db.get_product(product_id)

@app.post("/products")
def post_product(product: Product):
    return db.add_product(product.name, product.url, product.price)

@app.patch("/products")
def update_price(product: ProductUpdatePrice):
    return db.update_price(product.product_id, product.price)