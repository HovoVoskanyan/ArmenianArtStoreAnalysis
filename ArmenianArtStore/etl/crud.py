"""
CRUD Operations for Database Models
===================================
This module provides CRUD (Create, Read, Update, Delete) operations for the database models:
User, Variant, Event, Product, and Order. It interacts with a database session (`Session`) to perform these operations.

Dependencies:
    - sqlalchemy.orm.Session: For managing database sessions.
    - models: Database models including User, Variant, Event, Product, and Order.
"""

from sqlalchemy.orm import Session
from models import User, Variant, Event, VariantEvent, Product, Order

# USERS TABLE
def create_user(db: Session, device_type: str, user_type: str):
    """
    Creates a new user in the database.

    Args:
        db (Session): The database session.
        device_type (str): The type of device associated with the user.
        user_type (str): The type of user.

    Returns:
        User: The created user object.
    """
    db_user = User(DeviceType=device_type, UserType=user_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    """
    Retrieves a user by ID.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user.

    Returns:
        User: The user object, or None if not found.
    """
    return db.query(User).filter(User.UserId == user_id).first()

def get_all_users(db: Session):
    """
    Retrieves all users.

    Args:
        db (Session): The database session.

    Returns:
        list[User]: A list of all user objects.
    """
    return db.query(User).all()

def update_user(db: Session, user_id: int, device_type: str, user_type: str):
    """
    Updates a user's details.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to update.
        device_type (str): The updated device type.
        user_type (str): The updated user type.

    Returns:
        User: The updated user object, or None if not found.
    """
    db_user = db.query(User).filter(User.UserId == user_id).first()
    if db_user:
        db_user.DeviceType = device_type
        db_user.UserType = user_type
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """
    Deletes a user by ID.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to delete.

    Returns:
        User: The deleted user object, or None if not found.
    """
    db_user = db.query(User).filter(User.UserId == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Similarly, provide documentation for Variants, Events, Products, and Orders.
# Below is one example for `create_variant`:

# VARIANTS TABLE
def create_variant(db: Session, name: str):
    """
    Creates a new variant in the database.

    Args:
        db (Session): The database session.
        name (str): The name of the variant.

    Returns:
        Variant: The created variant object.
    """
    db_variant = Variant(Name=name)
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant
