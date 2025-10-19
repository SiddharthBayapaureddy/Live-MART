# Defining functions to create tables in backend

from sqlmodel import SQLModel,create_engine , Session , select
# SQLModel - for ORM
# Session - for DB Sessions
# select - for queries

from db_models import Customer , Product , ShoppingCart , ShoppingCartItem


# File Path of our Database
file_path = "sqlite:///./livemart.db"

# Creating a DB Engine
engine = create_engine(file_path , echo=True)  # "echo=True" prints SQL queries to console


# -------------------------------------------------------------------------------------------------------------------------
# Creating Tables
# -------------------------------------------------------------------------------------------------------------------------

def create_db_and_tables():

    # Creating all the tables in the models.py
    SQLModel.metadata.create_all(engine)


#--------------------------------------------------------------------------------------------------------------------------------------------

# Function to make a customer table
def add_customer(name: str , mail: str , hashed_password: str , delivery_address: str = None , 
                 city:str = None , state:str = None , pincode:str = None , phone_number:str = None):
    

     customer = Customer(
        name = name,                     
        mail = mail,                     
        hashed_password = hashed_password, 
        delivery_address = delivery_address, 
        city = city,                       
        state = state,                     
        pincode = pincode,                 
        phone_number = phone_number,      
        no_of_purchases = 0                 # Initial purchases is zero
     )

     # Creating the table
     with Session(engine) as session: # Opening a session to interact with DB
          session.add(customer)
          session.commit()
          session.refresh(customer)
          return customer
     

#--------------------------------------------------------------------------------------------------------------------------------------------

# Function to check if a customer already exists with the given mail
def get_customer_by_email(mail: str):

     with Session(engine) as session:
          cust = session.exec(
               select(Customer).where(Customer.mail == mail)
               ).first()
          return cust 
          # Returns the customer if found, else returns None

#--------------------------------------------------------------------------------------------------------------------------------------------

# Function to make a product item
def add_product(name:str , price:float , stock:int):
     
     product = Product(
          name = name,
          price = price,
          stock = stock
     )

     with Session(engine) as session: 
          session.add(product)
          session.commit()
          session.refresh(product)
          return product
     

#--------------------------------------------------------------------------------------------------------------------------------------------

# Function to add a shopping cart

def create_cart_for_customer(customer_id:int):
     
     cart = ShoppingCart(
          customer_id=customer_id,
    )
     
     with Session(engine) as session:
          session.add(cart)
          session.commit()
          session.refresh(cart)
          return cart
     

# Shopping Cart Function (To Access/Retrieve items from the cart)
def get_cart_items(cart_id:int):
     
     with Session(engine) as session:
        items = session.exec(
            select(ShoppingCartItem).where(ShoppingCartItem.cart_id == cart_id)
        ).all()

        return items
     

# To get cart size
def get_cart_size(cart_id:int):
     
    items = get_cart_items(cart_id)      
    size = 0
    for item in items:
         size += item.quantity

    return size


# Adding an item to a cart
def add_item_to_cart(product_id:int ,quantity:int , cart_id:int):
     
    # Making a ShoppingCartItem instance
    cart_item = ShoppingCartItem(
         product_id = product_id,
         quantity = quantity,
         cart_id = cart_id
    )

    with Session(engine) as session:
        session.add(cart_item)
        session.commit()
        session.refresh(cart_item)
        return cart_item