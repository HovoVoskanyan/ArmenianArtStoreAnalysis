"""
Database Configuration
======================
This module sets up the database connection, ORM base, and session factory for the application.
It uses environment variables to configure the database URL.

Modules:
    sqlalchemy: Used for database operations.
    sqlalchemy.ext.declarative: Used to define ORM models.
    sqlalchemy.orm: Provides session management for database operations.
    dotenv: Loads environment variables from a `.env` file.
    os: Used for accessing environment variables.

Functions:
    get_db(): Provides a database session and ensures proper cleanup.
"""

import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(".env")

# Get the database URL from environment variables
DATABASE_URL = os.environ.get("DATABASE_URL")

# Create the SQLAlchemy engine
engine = sql.create_engine(DATABASE_URL)

# Base class for declarative models
Base = declarative.declarative_base()

# SessionLocal for database operations
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Provides a database session for database operations.

    This function creates a new SQLAlchemy database session (`SessionLocal`) and
    ensures the session is properly closed after use.

    Yields:
        sqlalchemy.orm.Session: An active database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
