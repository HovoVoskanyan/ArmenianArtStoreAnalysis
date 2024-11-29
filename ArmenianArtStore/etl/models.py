from loguru import logger


from sqlalchemy import create_engine,Column,Integer,String,Float, DATE, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from database import Base, engine

Base = declarative_base()


class Event(Base):
    __tablename__ = "Events"
    EventId = Column(Integer, primary_key=True, autoincrement=True)
    EventName = Column(Integer)
class Project(Base):
    __tablename__ = "Projects"
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_description = Column(String(255))
    bandits_qty = Column(Integer)
    start_date = Column(DateTime)
class Bandit(Base):
    __tablename__ = "Bandits"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("Projects.project_id"))
    name = Column(String(255))
    alpha = Column(Float)
    beta = Column(Float)
    n = Column(Integer)
    updated_date = Column(DateTime, default=datetime.utcnow)
class UserEvent(Base):
    __tablename__ = "User_Events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("Projects.project_id"))
    bandit_id = Column(Integer, ForeignKey("Bandits.id"))
    event_id = Column(Integer, ForeignKey("Events.EventId"))
    event_date = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)  # Creates all tables
