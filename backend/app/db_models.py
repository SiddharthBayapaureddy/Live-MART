# Database Models

# Here, we define all the database tables, attributes to each

from sqlmodel import SQLModel , Field
from typing import Optional   #To allow fields to be NULL


# --------------------------------------------------------------------------------------------------------------------
# Customer Table Definition
# --------------------------------------------------------------------------------------------------------------------

class Customer(SQLModel , table=True):

    # Customer ID -- Primary key as a unique identifier (Auto-generated)
    id: Optional[int] = Field(default=None , primary_key=True)    # Keeping it optional, so it'll autogenerate

    name: str
    mail: str
    hashed_password: str  # Hashed password for secure authenticaion

    # Address Details
    delivery_address: Optional[str] = None
    city : Optional[str] = None
    state : Optional[str] = None
    pincode: Optional[str] = None

    # Contact Details
    phone_number: Optional[str] = None

    # Additional Details
    no_of_purchases : int = 0
    preferences: Optional[str] = None




# --------------------------------------------------------------------------------------------------------------------
# Product Table Definition
# --------------------------------------------------------------------------------------------------------------------

class Product(SQLModel , table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    
    name: str
    price: float
    stock: int
    



# --------------------------------------------------------------------------------------------------------------------
# Shopping Cart Table Definition
# --------------------------------------------------------------------------------------------------------------------

class ShoppingCart(SQLModel , table=True):

    id: Optional[int] = Field(default=None , primary_key=True)

    # Refers to the Customer using this cart
    customer_id: int = Field(foreign_key="customer.id")



# --------------------------------------------------------------------------------------------------------------------
# Shopping Cart Item Table Definition
# --------------------------------------------------------------------------------------------------------------------

class ShoppingCartItem(SQLModel , table = True):

    id: Optional[int] = Field(default=None , primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    quantity: int

    # Refers to the shopping cart the item belongs to
    cart_id: int = Field(foreign_key="shoppingcart.id")

