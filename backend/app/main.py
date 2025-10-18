# App

# Importing FastAPI
from fastapi import FastAPI , HTTPException  # HTTPException for exception handling
from sqlmodel import Session, select
from contextlib import asynccontextmanager

# Importing custom-built database models and functions
from database import (
    create_db_and_tables,
    add_customer,
    add_product,
    create_cart_for_customer,
    add_item_to_cart,
    get_cart_items,
    get_cart_size
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