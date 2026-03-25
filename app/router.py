from fastapi import FastAPI
from routes import products, scrape
from db import initialize_db

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(scrape.router, prefix="/scrape", tags=["scrape"])

@app.post("/start")
def initalize_db():
    return initialize_db()