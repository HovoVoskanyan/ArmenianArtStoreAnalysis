from crud import (
    create_user, get_user, update_user, delete_user,
    create_variant, get_variant, get_all_variants, update_variant, delete_variant,
    create_event, get_event, get_all_events, update_event, delete_event
)

from database import get_db

db = next(get_db())
print("Database session initialized.")

# USERS TABLE
def user_operations():
    """
    Perform CRUD operations for the Users table:
    - Create: Adds a new user with specified device type and user type.
    - Read: Fetches details of a user by user ID.
    - Update: Modifies the device type and user type for an existing user.
    - Delete: Removes a user record by user ID.
    """
    # Create a User
    new_user = create_user(db, device_type="Desktop", user_type="Admin")
    print(f"Created User: {new_user}")

    # Read the User
    read_user = get_user(db, new_user.UserId)
    print(f"Read User: {read_user}")

    # Update the User
    updated_user = update_user(db, new_user.UserId, device_type="Mobile", user_type="User")
    print(f"Updated User: {updated_user}")

    # Delete the User
    deleted_user = delete_user(db, new_user.UserId)
    print(f"Deleted User: {deleted_user}")


# VARIANT TABLE
def variant_operations():
    """
    Perform CRUD operations for the Variants table:
    - Create: Adds a new product variant with a specified name.
    - Read: Fetches details of a variant by variant ID.
    - Read All: Retrieves all variants from the database.
    - Update: Modifies the name of an existing variant.
    - Delete: Removes a variant record by variant ID.
    """
    # Create a Variant
    new_variant = create_variant(db, name="Test Variant")
    print(f"Created Variant: {new_variant}")

    # Read the Variant
    read_variant = get_variant(db, new_variant.VariantId)
    print(f"Read Variant: {read_variant}")

    # Read All Variants
    all_variants = get_all_variants(db)
    print(f"All Variants: {all_variants}")

    # Update the Variant
    updated_variant = update_variant(db, new_variant.VariantId, name="Updated Variant")
    print(f"Updated Variant: {updated_variant}")

    # Delete the Variant
    deleted_variant = delete_variant(db, new_variant.VariantId)
    print(f"Deleted Variant: {deleted_variant}")


# EVENT TABLE
def event_operations():
    """
    Perform CRUD operations for the Events table:
    - Create: Adds a new event with a specified event name.
    - Read: Fetches details of an event by event ID.
    - Read All: Retrieves all events from the database.
    - Update: Modifies the name of an existing event.
    - Delete: Removes an event record by event ID.
    """
    # Create an Event
    new_event = create_event(db, event_name="Test Event")
    print(f"Created Event: {new_event}")

    # Read the Event
    read_event = get_event(db, new_event.EventId)
    print(f"Read Event: {read_event}")

    # Read All Events
    all_events = get_all_events(db)
    print(f"All Events: {all_events}")

    # Update the Event
    updated_event = update_event(db, new_event.EventId, event_name="Updated Event")
    print(f"Updated Event: {updated_event}")

    # Delete the Event
    deleted_event = delete_event(db, new_event.EventId)
    print(f"Deleted Event: {deleted_event}")


# PRODUCT TABLE
def product_operations():
    """
    Perform CRUD operations for the Products table:
    - Create: Adds a new product with details like name, description, price, creation date, and type.
    - Read: Fetches details of a product by product ID.
    - Read All: Retrieves all products from the database.
    - Update: Modifies the details of an existing product.
    - Delete: Removes a product record by product ID.
    """
    from crud import create_product, get_product, get_all_products, update_product, delete_product

    # Create a Product
    new_product = create_product(
        db,
        name="Test Product",
        description="This is a test product.",
        images="test_image.png",
        unit_price=9.99,
        creation_date="2024-11-16",
        author_full_name="Test Author",
        product_type="Test Type"
    )
    print(f"Created Product: {new_product}")

    # Read the Product
    read_product = get_product(db, new_product.ProductId)
    print(f"Read Product: {read_product}")

    # Read All Products
    all_products = get_all_products(db)
    print(f"All Products: {all_products}")

    # Update the Product
    updated_product = update_product(
        db,
        new_product.ProductId,
        name="Updated Product",
        description="Updated description.",
        images="updated_image.png",
        unit_price=19.99,
        creation_date="2024-11-17",
        author_full_name="Updated Author",
        product_type="Updated Type"
    )
    print(f"Updated Product: {updated_product}")

    # Delete the Product
    deleted_product = delete_product(db, new_product.ProductId)
    print(f"Deleted Product: {deleted_product}")


# ORDER TABLE
def order_operations():
    """
    Perform CRUD operations for the Orders table:
    - Create: Adds a new order with details like order date, product ID, user ID, and variant ID.
    - Read: Fetches details of an order by order ID.
    - Read All: Retrieves all orders from the database.
    - Update: Modifies the details of an existing order.
    - Delete: Removes an order record by order ID.
    """
    from crud import create_order, get_order, get_all_orders, update_order, delete_order

    # Create an Order
    new_order = create_order(
        db,
        order_date="2024-11-16",
        product_id=1,
        user_id=1,
        variant_id=1
    )
    print(f"Created Order: {new_order}")

    # Read the Order
    read_order = get_order(db, new_order.OrderId)
    print(f"Read Order: {read_order}")

    # Read All Orders
    all_orders = get_all_orders(db)
    print(f"All Orders: {all_orders}")

    # Update the Order
    updated_order = update_order(
        db,
        new_order.OrderId,
        order_date="2024-11-17",
        product_id=2,
        user_id=2,
        variant_id=2
    )
    print(f"Updated Order: {updated_order}")

    # Delete the Order
    deleted_order = delete_order(db, new_order.OrderId)
    print(f"Deleted Order: {deleted_order}")

