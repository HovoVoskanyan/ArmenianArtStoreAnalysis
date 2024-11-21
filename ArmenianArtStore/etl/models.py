from loguru import logger


from sqlalchemy import create_engine,Column,Integer,String,Float, DATE, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship,declarative_base
from datetime import datetime
from database import Base, engine

Base= declarative_base()

class User(Base):
    __tablename__ = "Users"
    UserId = Column(Integer, primary_key=True)
    DeviceType = Column(String(50))
    UserType = Column(String(50))

class Variant(Base):
    __tablename__ = "Variants"
    VariantId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(Integer, default=1)
    alpha = Column(Float, default=1.0)
    beta = Column(Float, default=1.0)

class Event(Base):
    __tablename__ = "Events"
    EventId = Column(Integer, primary_key=True, autoincrement=True)
    EventName = Column(Integer)

class VariantEvent(Base):
    __tablename__ = "VariantEvent"
    Id = Column(Integer, primary_key=True)
    VariantId = Column(Integer, ForeignKey("Variants.VariantId"))
    EventId = Column(Integer, ForeignKey("Events.EventId"))

class Product(Base):
    __tablename__ = "Products"
    ProductId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100))
    Description = Column(String(1000))
    Images = Column(String(1000))
    UnitPrice = Column(Float, nullable=False)
    CreationDate = Column(DateTime, default=datetime.utcnow)
    AuthorFullName = Column(String(255))
    Type = Column(Integer)

class Order(Base):
    __tablename__ = "Orders"
    OrderId = Column(Integer, primary_key=True, autoincrement=True)
    OrderDate = Column(DateTime, default=datetime.utcnow, nullable=False)
    ProductId = Column(Integer, ForeignKey("Products.ProductId"))
    UserId = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    VariantId = Column(Integer, ForeignKey("Variants.VariantId"), nullable=False)


Base.metadata.drop_all(engine)  # Drops all tables
Base.metadata.create_all(engine)  # Creates all tables
