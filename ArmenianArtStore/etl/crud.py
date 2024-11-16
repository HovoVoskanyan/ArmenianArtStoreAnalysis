from sqlalchemy.orm import Session
from models import User, Variant, Event, VariantEvent, Product, Order
#from schema import UserCreate, VariantCreate, EventCreate, VariantEventCreate, ProductCreate, OrderCreate

# def create_user(db: Session, device_type: str, user_type: str):
#     db_user = User(DeviceType=device_type, UserType=user_type)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
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

