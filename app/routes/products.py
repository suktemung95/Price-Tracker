from fastapi import FastAPI
from db import get_all_products

app = FastAPI()

@app.get("/products")
def get_products():
    return get_all_products()

