from sqlalchemy.orm import Session
from models import User, Variant, Event, VariantEvent, Product, Order
from schema import UserCreate, VariantCreate, EventCreate, VariantEventCreate, ProductCreate, OrderCreate

# USERS TABLE
def create_user(db: Session, user: UserCreate):
    db_user = User(DeviceType=user.device_type, UserType=user.user_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_data: UserCreate):
    db_user = db.query(User).filter(User.UserId == user_id).first()
    if db_user:
        db_user.DeviceType = user_data.device_type
        db_user.UserType = user_data.user_type
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
def create_variant(db: Session, variant: VariantCreate):
    db_variant = Variant(Name=variant.name)
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant

def update_variant(db: Session, variant_id: int, variant_data: VariantCreate):
    db_variant = db.query(Variant).filter(Variant.VariantId == variant_id).first()
    if db_variant:
        db_variant.Name = variant_data.name
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
def create_event(db: Session, event: EventCreate):
    db_event = Event(EventName=event.event_name)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def update_event(db: Session, event_id: int, event_data: EventCreate):
    db_event = db.query(Event).filter(Event.EventId == event_id).first()
    if db_event:
        db_event.EventName = event_data.event_name
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
def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        Name=product.name,
        Description=product.description,
        Images=product.images,
        UnitPrice=product.unit_price,
        CreationDate=product.creation_date,
        AuthorFullName=product.author_full_name,
        Type=product.type
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product_data: ProductCreate):
    db_product = db.query(Product).filter(Product.ProductId == product_id).first()
    if db_product:
        db_product.Name = product_data.name
        db_product.Description = product_data.description
        db_product.Images = product_data.images
        db_product.UnitPrice = product_data.unit_price
        db_product.CreationDate = product_data.creation_date
        db_product.AuthorFullName = product_data.author_full_name
        db_product.Type = product_data.type
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
def create_order(db: Session, order: OrderCreate):
    db_order = Order(
        OrderDate=order.order_date,
        ProductId=order.product_id,
        UserId=order.user_id,
        VariantId=order.variant_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order_id: int, order_data: OrderCreate):
    db_order = db.query(Order).filter(Order.OrderId == order_id).first()
    if db_order:
        db_order.OrderDate = order_data.order_date
        db_order.ProductId = order_data.product_id
        db_order.UserId = order_data.user_id
        db_order.VariantId = order_data.variant_id
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.OrderId == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
