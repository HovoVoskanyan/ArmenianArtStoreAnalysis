from sqlalchemy.orm import Session
from models import User, Variant, Event, VariantEvent, Product, Order

def create_user(db: Session, device_type: str, user_type: str):
    print("Creating user...")
    db_user = User(DeviceType=device_type, UserType=user_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(f"User created: {db_user}")
    return db_user


def update_user(db: Session, user_id: int, device_type: str, user_type: str):
    db_user = db.query(User).filter(User.UserId == user_id).first()
    if db_user:
        db_user.DeviceType = device_type
        db_user.UserType = user_type
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.UserId == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

###
from sqlalchemy.orm import Session
from models import User, Variant, Event, VariantEvent, Product, Order

# USERS TABLE
def create_user(db: Session, device_type: str, user_type: str):
    db_user = User(DeviceType=device_type, UserType=user_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.UserId == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, device_type: str, user_type: str):
    db_user = db.query(User).filter(User.UserId == user_id).first()
    if db_user:
        db_user.DeviceType = device_type
        db_user.UserType = user_type
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.UserId == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# VARIANTS TABLE
def create_variant(db: Session, name: str):
    db_variant = Variant(Name=name)
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant

def get_variant(db: Session, variant_id: int):
    return db.query(Variant).filter(Variant.VariantId == variant_id).first()

def get_all_variants(db: Session):
    return db.query(Variant).all()

def update_variant(db: Session, variant_id: int, name: str):
    db_variant = db.query(Variant).filter(Variant.VariantId == variant_id).first()
    if db_variant:
        db_variant.Name = name
        db.commit()
        db.refresh(db_variant)
    return db_variant

def delete_variant(db: Session, variant_id: int):
    db_variant = db.query(Variant).filter(Variant.VariantId == variant_id).first()
    if db_variant:
        db.delete(db_variant)
        db.commit()
    return db_variant

# EVENTS TABLE
def create_event(db: Session, event_name: str):
    db_event = Event(EventName=event_name)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.EventId == event_id).first()

def get_all_events(db: Session):
    return db.query(Event).all()

def update_event(db: Session, event_id: int, event_name: str):
    db_event = db.query(Event).filter(Event.EventId == event_id).first()
    if db_event:
        db_event.EventName = event_name
        db.commit()
        db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = db.query(Event).filter(Event.EventId == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event


# PRODUCTS TABLE
def create_product(db: Session, name: str, description: str, images: str, unit_price: float, 
                   creation_date: str, author_full_name: str, product_type: str):
    db_product = Product(
        Name=name,
        Description=description,
        Images=images,
        UnitPrice=unit_price,
        CreationDate=creation_date,
        AuthorFullName=author_full_name,
        Type=product_type
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.ProductId == product_id).first()

def get_all_products(db: Session):
    return db.query(Product).all()

def update_product(db: Session, product_id: int, name: str, description: str, images: str, 
                   unit_price: float, creation_date: str, author_full_name: str, product_type: str):
    db_product = db.query(Product).filter(Product.ProductId == product_id).first()
    if db_product:
        db_product.Name = name
        db_product.Description = description
        db_product.Images = images
        db_product.UnitPrice = unit_price
        db_product.CreationDate = creation_date
        db_product.AuthorFullName = author_full_name
        db_product.Type = product_type
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.ProductId == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# ORDERS TABLE
def create_order(db: Session, order_date: str, product_id: int, user_id: int, variant_id: int):
    db_order = Order(
        OrderDate=order_date,
        ProductId=product_id,
        UserId=user_id,
        VariantId=variant_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.OrderId == order_id).first()

def get_all_orders(db: Session):
    return db.query(Order).all()

def update_order(db: Session, order_id: int, order_date: str, product_id: int, user_id: int, variant_id: int):
    db_order = db.query(Order).filter(Order.OrderId == order_id).first()
    if db_order:
        db_order.OrderDate = order_date
        db_order.ProductId = product_id
        db_order.UserId = user_id
        db_order.VariantId = variant_id
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.OrderId == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
