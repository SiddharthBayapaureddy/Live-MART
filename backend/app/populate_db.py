
# Populating Database with random sample objects

from database import (
    create_db_and_tables,
    add_customer,
    add_product,
    create_cart_for_customer,
    add_item_to_cart,
    get_cart_items,
    get_cart_size,
)


# Seed function
def seed():

    # Creating tables
    create_db_and_tables()

    # Adding Sample Customers
    customers_data = [
        {"name": "Peacemaker", "mail": "peacemaker@gmail.com", "hashed_password": "eagly", "delivery_address": "Evergreen", "city": "Washington" , "state": "US" , "pincode" : "696969"},
        {"name": "Vigilante",  "mail": "vigilante@gmail.com",   "hashed_password": "nick", "delivery_address": "Kansas", "city": "Texas" , "state": "US" , "pincode" : "696969"},
        {"name": "Harcout",    "mail": "harcout@gmail.com",      "hashed_password": "toxic", "delivery_address": "New York", "city": "New York" , "state": "US" , "pincode" : "696969" },
    ]

    customers = []
    for c in customers_data:
        cust = add_customer(
            name=c["name"],
            mail=c["mail"],
            hashed_password=c["hashed_password"],
            delivery_address=c["delivery_address"],
            city=c["city"],
            state=c["state"],
            pincode=c["pincode"],
            phone_number=c.get("phone_number"),   # Safe way to get the value, and returns None if key does not exist
        )
        print(f"Added customer: id={cust.id} name={cust.name}")
        customers.append(cust)

    # Adding Sample products
    products_data = [
        {"name": "USB-C Cable", "price": 399.0, "stock": 50},
        {"name": "Wireless Mouse", "price": 899.0, "stock": 30},
        {"name": "Mechanical Keyboard", "price": 2999.0, "stock": 10},
        {"name": "Laptop Stand", "price": 799.0, "stock": 15},
        {"name": "Noise Cancelling Headphones", "price": 4999.0, "stock": 8},
    ]

    products = []
    for p in products_data:
        prod = add_product(name=p["name"], price=p["price"], stock=p["stock"])
        print(f"Added product: id={prod.id} name={prod.name} stock={prod.stock}")
        products.append(prod)

    # Adding Shopping Carts
    for idx, cust in enumerate(customers):
        cart = create_cart_for_customer(cust.id)
        print(f"Created cart for customer_id={cust.id} cart_id={cart.id}")

        # add 2 items per user: pick products by index (wrap around)
        prod1 = products[(idx * 2) % len(products)]
        prod2 = products[(idx * 2 + 1) % len(products)]

        item1 = add_item_to_cart(prod1.id, 1, cart.id)  # note: add_item_to_cart(product_id, quantity, cart_id)
        item2 = add_item_to_cart(prod2.id, 2, cart.id)
        print(f"  -> added cart_item {item1.id} (product {prod1.id} qty=1)")
        print(f"  -> added cart_item {item2.id} (product {prod2.id} qty=2)")

        # show cart size
        size = get_cart_size(cart.id)
        print(f"  Cart size now: {size}")

    print("Seeding finished.")

if __name__ == "__main__":
    seed()
