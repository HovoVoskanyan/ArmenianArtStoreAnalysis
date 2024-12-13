from loguru import logger
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
from pytz import timezone
from database import Base, engine

Base = declarative_base()

def get_yerevan_time():
    """
    Returns the current time in the Yerevan timezone.
    """
    yerevan_tz = timezone('Asia/Yerevan')
    return datetime.now(yerevan_tz)

class Event(Base):
    """
    Represents an event in the system.

    Attributes:
        __tablename__ (str): The name of the database table.
        EventId (int): The unique identifier for the event.
        EventName (str): The name or identifier of the event.
        created_date (DateTime): The timestamp for when the record is created.
    """
    __tablename__ = "Events"
    EventId = Column(Integer, primary_key=True, autoincrement=True)
    EventName = Column(String(255))
    created_date = Column(DateTime, default=get_yerevan_time)

class Project(Base):
    """
    Represents a project in the system.

    Attributes:
        __tablename__ (str): The name of the database table.
        project_id (int): The unique identifier for the project.
        project_description (str): A description of the project.
        bandits_qty (int): The quantity of bandits associated with the project.
        start_date (DateTime): The start date of the project.
        created_date (DateTime): The timestamp for when the record is created.
    """
    __tablename__ = "Projects"
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_description = Column(String(255))
    bandits_qty = Column(Integer)
    created_date = Column(DateTime, default=get_yerevan_time)

class Bandit(Base):
    """
    Represents a bandit in the system.

    Attributes:
        __tablename__ (str): The name of the database table.
        id (int): The unique identifier for the bandit.
        project_id (int): The identifier of the project the bandit belongs to.
        name (str): The name of the bandit.
        alpha (float): The alpha parameter for the bandit.
        beta (float): The beta parameter for the bandit.
        n (int): The count of some metric associated with the bandit.
        updated_date (DateTime): The timestamp for the last update.
        created_date (DateTime): The timestamp for when the record is created.
    """
    __tablename__ = "Bandits"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("Projects.project_id"))
    name = Column(String(255))
    alpha = Column(Float)
    beta = Column(Float)
    n = Column(Integer)
    updated_date = Column(DateTime, default=get_yerevan_time)
    created_date = Column(DateTime, default=get_yerevan_time)

class UserEvent(Base):
    """
    Represents a user event in the system.

    Attributes:
        __tablename__ (str): The name of the database table.
        id (int): The unique identifier for the user event.
        project_id (int): The identifier of the project related to the event.
        bandit_id (int): The identifier of the bandit related to the event.
        event_id (int): The identifier of the event.
        event_date (DateTime): The timestamp of the event occurrence.
        created_date (DateTime): The timestamp for when the record is created.
    """
    __tablename__ = "User_Events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("Projects.project_id"))
    bandit_id = Column(Integer, ForeignKey("Bandits.id"))
    event_id = Column(Integer, ForeignKey("Events.EventId"))
    created_date = Column(DateTime, default=get_yerevan_time)

# Creates all tables
Base.metadata.create_all(engine)
