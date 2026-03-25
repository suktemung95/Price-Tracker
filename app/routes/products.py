from fastapi import status, HTTPException, APIRouter 
from pydantic import BaseModel
import services.productServices as s
import db

class Product(BaseModel):
    name: str
    url: str
    price: float

class ProductUpdatePrice(BaseModel):
    product_id: int
    price: float

router = APIRouter()

@router.get("/")
def get_products(
    min_price: float = None,
    max_price: float = None,
    name: str = None,
    min_id: int = None,
    max_id: int = None
):
    return s.get_products(min_price, max_price, name, min_id, max_id)

@router.get("/{product_id}")
def get_product(product_id: int):

    product = s.get_product(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", status_code=status.HTTP_201_CREATED)
def post_product(product: Product):
    product = s.add_product(product.name, product.url, product.price)

    if not product:
        raise HTTPException(status_code=400, detail="Failed to create product")
    
    return product

@router.patch("/")
def update_price(product: ProductUpdatePrice):
    updated = s.update_price(product.product_id, product.price)

    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated

@router.delete("/{product_id}")
def delete_product(product_id: int):
    deleted = s.delete_product(product_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")

    return deleted