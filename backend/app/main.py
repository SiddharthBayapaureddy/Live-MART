# App

# Importing FastAPI
from fastapi import FastAPI , HTTPException , status # HTTPException for exception handling
from sqlmodel import Session, select
from contextlib import asynccontextmanager

from fastapi.concurrency import run_in_threadpool

import hashlib # To hash password, and save in DB safetly 

# Importing custom-built database models and functions
from database import (
    create_db_and_tables,
    add_customer,
    add_product,
    create_cart_for_customer,
    add_item_to_cart,
    get_cart_items,
    get_cart_size,
    get_customer_by_email,

    engine
)

# Importing the SQLModel classes
from db_models import Customer, Product, ShoppingCart, ShoppingCartItem

# Importing the Schemas
from schemas import *

# --------------------------------------------------------------------------------------------------------------------------------------------


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



# -------------------------------------------------------------------------------------------------------------------------------------------------

# Signup Endpoint - POST  ---> Accepts JSON Body (CustomerCreate) and returns CustomerRead
@app.post("/signup/" , response_model=CustomerRead , status_code=status.HTTP_201_CREATED)   # Returns 201 on Success
async def signup(customer : CustomerCreate):

    # Check if email already exists
    exists = get_customer_by_email(customer.mail)

    if exists:
        raise HTTPException(status_code=400 , detail="Email Already Registered")

    # Hashing the password
    hashed_password = hashlib.sha256(customer.password.encode()).hexdigest()

    new_customer = await run_in_threadpool(
        add_customer,
        customer.name,
        customer.mail,
        hashed_password,
        customer.delivery_address,
        customer.city,
        customer.state,
        customer.pincode,
        customer.phone_number
    )

    # If customer not created
    if not new_customer:
        raise HTTPException(status_code=500 , detail="Failed to create Customer. Oops, Try again!")

    # Used Custom Read to serialize response (orm_mode = True)
    return new_customer 

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Login Endpoint - POST ---> Accepts JSON Body
@app.post("/login/")
async def login(req : LoginRequest):

    # Checking if customer exists
    customer = await run_in_threadpool(get_customer_by_email , req.mail)

    if not customer:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Invalid Credentials: Mail not found")
    

    # Checking password
    # Hashing input password and comparing
    hashed_input_pass = hashlib.sha256(req.password.encode()).hexdigest()

    # Password incorrect
    if hashed_input_pass != customer.hashed_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Invalid Credentials: Password not found")
    

    return {"message": "Login successful", "customer_id": customer.id, "name": customer.name}


# -------------------------------------------------------------------------------------------------------------------------------------------------

# Product Details Endpoint - GET ---> Accepts 
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


# -------------------------------------------------------------------------------------------------------------------------------------------------


# Adding Product Endpoint - POST ---> Accepts JSON Body as response
@app.post("/products/add/" , response_model=ProductRead , status_code=status.HTTP_201_CREATED)
async def create_product_endpoint(product : ProductCreate):
    product = await run_in_threadpool(add_product , product.name , product.price , product.stock)

    if not product:
        raise HTTPException(status_code=500 , detail="Failed to create product. Try again! Oops lol")
    
    return product


# -------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------

