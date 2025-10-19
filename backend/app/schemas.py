# Used for validating and structuring the data my API recieves and returns


# BaseModel for defining request/response schemas
from pydantic import BaseModel , EmailStr   # EmailStr helps validate proper email structure
from typing import Optional


# --------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------------
# Customer Schemas
# -----------------------------

# Scheme for new SignUp Customers
class CustomerCreate(BaseModel):

    name : str
    mail : EmailStr
    password : str
    delivery_address: Optional[str] = None  
    city: Optional[str] = None            
    state: Optional[str] = None           
    pincode: Optional[str] = None         
    phone_number: Optional[str] = None

# --------------------------------------------------------------------------------------------------------------------------------------------

# Scheme for returning Customer Info
class CustomerRead(BaseModel):

    id : int 
    name : str
    mail : EmailStr
    delivery_address: Optional[str] = None  
    city: Optional[str] = None            
    state: Optional[str] = None           
    pincode: Optional[str] = None         
    phone_number: Optional[str] = None
    no_of_purchases : int 
    preferences: Optional[str] = None

    class Config:
        orm_mode = True    # Allows returning SQLModel objects directlty

# --------------------------------------------------------------------------------------------------------------------------------------------

class LoginRequest(BaseModel):
    mail: EmailStr
    password: str

# --------------------------------------------------------------------------------------------------------------------------------------------

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

# --------------------------------------------------------------------------------------------------------------------------------------------

class ProductRead(BaseModel):
    id: int
    name: str
    price: float
    stock: int

    class Config:
        orm_mode = True

# --------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------




# --------------------------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------------------------

# Schema for creating a ShoppingCartItem
class ShoppingCartItemCreate(BaseModel):

    product_id : int
    quantity: int

# --------------------------------------------------------------------------------------------------------------------------------------------

# Schema for reading a ShoppingCartItem
class ShoppingCartItemRead(BaseModel):

    id: int                     
    product_id: int             
    quantity: int
    cart_id: int

    class Config:
        orm_mode = True          

# --------------------------------------------------------------------------------------------------------------------------------------------







# --------------------------------------------------------------------------------------------------------------------------------------------
