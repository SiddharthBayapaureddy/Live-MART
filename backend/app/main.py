# App

# Importing FastAPI
from fastapi import FastAPI , HTTPException  # HTTPException for exception handling
from sqlmodel import Session, select
from contextlib import asynccontextmanager

from fastapi.concurrency import run_in_threadpool

# Importing custom-built database models and functions
from database import (
    create_db_and_tables,
    add_customer,
    add_product,
    create_cart_for_customer,
    add_item_to_cart,
    get_cart_items,
    get_cart_size,

    engine
)

# Importing the SQLModel classes
from db_models import Customer, Product, ShoppingCart, ShoppingCartItem


# -----------------------------
# Building the App
# -----------------------------

# Initializing an FastAPI app instance
app = FastAPI(title="Live MART")



# Creating endpoints

# Root 
@app.get("/")
def root():
    return "Hello Word!"


# Product Details Endpoint
@app.get("/products/info/{product_id}")
async def get_product(product_id: int):
    def _get():
        with Session(engine) as session:
            return session.exec(select(Product).where(Product.id == product_id)).first()

    prod = await run_in_threadpool(_get)

    # If Product ID does not exist
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return prod


# Adding Product Endpoint
@app.post("/products/add/")
async def create_product_endpoint(name:str , price:float , stock: int):
    product = await run_in_threadpool(add_product , name , price , stock)

    if not product:
        raise HTTPException(status_code=500 , detail="Failed to create product. Try again! Oops lol")
    
    return product