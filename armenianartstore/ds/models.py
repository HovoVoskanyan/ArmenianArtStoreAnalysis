#models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Event(Base):
    __tablename__ = "Events"

    EventId = Column(Integer, primary_key=True, autoincrement=True)
    EventName = Column(String(255))

class Project(Base):
    __tablename__ = "Projects"

    project_id = Column(Integer, primary_key=True, index=True)
    project_description = Column(String(255), nullable=False)
    bandits_qty = Column(Integer, nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)

    # Relationship with Bandit
    bandits = relationship("Bandit", back_populates="project")


class Bandit(Base):
    __tablename__ = "Bandits"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("Projects.project_id"), nullable=False)  # Use project_id
    name = Column(String(50), nullable=False)
    alpha = Column(Integer, default=1)
    beta = Column(Integer, default=1)
    n = Column(Integer, default=0)
    updated_date = Column(DateTime, default=datetime.utcnow)

    # Relationship with Project
    project = relationship("Project", back_populates="bandits")


class UserEvent(Base):
    __tablename__ = "User_Events"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("Projects.project_id"))
    bandit_id = Column(Integer, ForeignKey("Bandits.id"))  # Ensure 'bandits' matches the table name
    event_id = Column(Integer, ForeignKey("Events.EventId"))
    event_date = Column(DateTime, default=datetime.utcnow)
