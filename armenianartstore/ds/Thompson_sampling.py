#Thompson
from pydantic import (BaseModel,conint)
from typing import List, Optional

from datetime import datetime, timezone
from loguru import logger

import sys
import os

# Add the project root directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
import numpy as np
from datetime import datetime
import logging

from models import Project, Bandit, Event, UserEvent
from database import get_db

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from sqlalchemy.orm import Session
from models import Project, Bandit
from database import engine

with Session(engine) as session:
    # Add a new project
    project = Project(
        project_description="Test Project",
        bandits_qty=2,
        start_date=datetime.now(timezone.utc),
    )
    session.add(project)
    session.commit()

    print(f"Added Project: {project.project_id}")


#Reponse models
class CreateBanditResponseModel(BaseModel):
    """
    Response model for a created bandit.

    Attributes:
        id (int): The ID of the bandit.
        project_id (int): The ID of the project the bandit belongs to.
        name (str): The name of the bandit.
        alpha (int): Alpha parameter for the bandit.
        beta (int): Beta parameter for the bandit.
        update_date (datetime): The last updated date of the bandit.
    """
    id: int
    project_id: int
    name: str
    alpha: int
    beta: int
    update_date: datetime

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class CreateProjectResponseModel(BaseModel):
    """
    Response model for a created project.

    Attributes:
        project_id (int): The ID of the project.
        start_date (datetime): The start date of the project.
        project_description (str): The description of the project.
        bandits_qty (int): The number of bandits in the project.
        bandits (List[CreateBanditResponseModel]): List of bandits associated with the project.
    """
    project_id: Optional[int]
    start_date: datetime
    project_description: str
    bandits_qty: int
    bandits: List[CreateBanditResponseModel]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class BanditReport(BaseModel):
    """
    Report model for a bandit.

    Attributes:
        bandit_id (int): The ID of the bandit.
        bandit_name (str): The name of the bandit.
        bandit_opened_qt (int): The quantity of times the bandit was opened.
        alpha (int): Alpha parameter for the bandit.
        beta (int): Beta parameter for the bandit.
    """
    bandit_id: int
    bandit_name: str
    bandit_opened_qt: int
    alpha: int
    beta: int

class ProjectReport(BaseModel):
    """
    Report model for a project.

    Attributes:
        project_id (int): The ID of the project.
        bandits_report (List[BanditReport]): List of bandit reports associated with the project.
    """
    project_id: int
    bandits_report: List[BanditReport]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class UserEventResponse(BaseModel):
    """
    Response model for a user event.

    Attributes:
        bandit_name (str): The name of the bandit associated with the event.
        positive_qt (int): Quantity of positive events.
        negative_qt (int): Quantity of negative events.
    """
    bandit_name: str
    positive_qt: int
    negative_qt: int

class UserEventResponses(BaseModel):
    """
    Response model for a user event.

    Attributes:
        bandit_name (str): The name of the bandit associated with the event.
        positive_qt (int): Quantity of positive events.
        negative_qt (int): Quantity of negative events.
    """
    data: List[UserEventResponse]


class Project(BaseModel):
    """
    Represents a project in the system.

    Attributes:
        project_id (int): The unique identifier for the project.
        project_description (str): A description of the project (maximum 255 characters).
        bandits_qty (int): The quantity of bandits associated with the project.
        start_date (DateTime): The start date of the project.
    """
    project_id: Optional[int] = None
    project_description:str
    bandits_qty : int
    start_date: datetime

class Projects(BaseModel):
    """
    Represents a list of project responses in the system.

    Attributes:
        data (List): Represents the List of projects
    """
    data:List[Project]

#STRUCTURES

class CreateBanditRequestModel(BaseModel):
    """
    Represents the data model for creating a bandit.

    Attributes:
        name (str): The name of the bandit.

    Config:
        from_attributes (bool): Allows initialization of the model from attributes.
        arbitrary_types_allowed (bool): Enables support for arbitrary types within the model.
    """
    name: str

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class CreateProjectRequestModel(BaseModel):
    """
    Represents the data model for creating a project.

    Attributes:
        project_description (str): A description of the project.
        bandits (List[CreateBanditRequestModel]): A list of bandits associated with the project.

    Config:
        from_attributes (bool): Allows initialization of the model from attributes.
        arbitrary_types_allowed (bool): Enables support for arbitrary types within the model.
    """
    project_description: str
    bandits: List[CreateBanditRequestModel]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class SubmitBanditChoiseResponseModel(BaseModel):
    """
    Represents the response model for submitting a bandit choice.

    Attributes:
        bandit_name (str): The name of the bandit.
        chosen (bool): Indicates whether the bandit was chosen.
    """
    bandit_name:str
    chosen:bool


#CREATION
from models import Project as SQLAlchemyProject  # Explicitly use SQLAlchemy model

def create_project_standalone(project_data: CreateProjectRequestModel, db: Session):
    """
    Create a new project along with associated bandits.

    Args:
        project_data (CreateProjectRequestModel): The project details including description and bandits.
        db (Session): The database session.

    Returns:
        CreateProjectResponseModel: Response containing project and associated bandits.
    """
    # Create the new project
    new_project = SQLAlchemyProject(
        project_description=project_data.project_description,
        start_date=datetime.now(timezone.utc),
        bandits_qty=len(project_data.bandits)
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)  # Ensure `project_id` is populated

    # Build the response
    response = CreateProjectResponseModel(
        project_id=new_project.project_id,  # Use `project_id` here
        project_description=new_project.project_description,
        start_date=new_project.start_date,
        bandits_qty=new_project.bandits_qty,
        bandits=[]
    )

    # Add bandits
    for bandit in project_data.bandits:
        new_bandit = Bandit(
            project_id=new_project.project_id,  # Use `project_id` here
            name=bandit.name,
            alpha=1,
            beta=1,
            updated_date=datetime.now(timezone.utc)
        )
        db.add(new_bandit)
        db.commit()
        db.refresh(new_bandit)

        response_bandit = CreateBanditResponseModel(
            id=new_bandit.id,
            project_id=new_bandit.project_id,
            name=new_bandit.name,
            alpha=new_bandit.alpha,
            beta=new_bandit.beta,
            update_date=new_bandit.updated_date
        )
        response.bandits.append(response_bandit)

    return response




def get_champion_bandit_standalone(project_id: int, db: Session):
    """
    Retrieve the champion bandit for a given project.

    Args:
        project_id (int): The ID of the project.
        db (Session): The database session.

    Returns:
        str: Name of the champion bandit.
    """
    bandits = db.query(Bandit).filter(Bandit.project_id == project_id).all()

    if not bandits:
        raise ValueError(f"No bandits found for project ID {project_id}")

    samples = [np.random.beta(bandit.alpha, bandit.beta) for bandit in bandits]

    # Select the bandit with the highest sample
    chosen_bandit = bandits[np.argmax(samples)]

    return chosen_bandit.name


def user_choose_bandit_standalone(bandit_data: SubmitBanditChoiseResponseModel, db: Session):
    bandit_db = db.query(Bandit).filter(Bandit.name == bandit_data.bandit_name).first()

    if not bandit_db:
        raise ValueError("Bandit not found")

    # Check if events exist, and create them if they don't
    liked_event = db.query(Event).filter(Event.EventId == 1).first()
    if not liked_event:
        liked_event = Event(EventId=1, EventName='Liked Event')
        db.add(liked_event)

    disliked_event = db.query(Event).filter(Event.EventId == 2).first()
    if not disliked_event:
        disliked_event = Event(EventId=2, EventName='Disliked Event')
        db.add(disliked_event)

    db.commit()  # Ensure events are saved to the database

    # Record user choice
    if bandit_data.chosen:
        bandit_db.alpha += 1
        new_event = UserEvent(
            project_id=bandit_db.project_id,
            bandit_id=bandit_db.id,
            event_id=liked_event.EventId,
        )
        db.add(new_event)
    else:
        bandit_db.beta += 1
        new_event = UserEvent(
            project_id=bandit_db.project_id,
            bandit_id=bandit_db.id,
            event_id=disliked_event.EventId,
        )
        db.add(new_event)

    bandit_db.n += 1
    db.commit()

    return {"msg": "Done successfully"}

#CODE TEST

# if __name__ == "__main__":
#     db = next(get_db())  # Replace with actual DB session creation logic

#     # Step 1: Create a project with bandits
#     project_request = CreateProjectRequestModel(
#         project_description="Test Project",
#         bandits=[
#             CreateBanditRequestModel(name="Bandit A"),
#             CreateBanditRequestModel(name="Bandit B")
#         ]
#     )
#     project_response = create_project_standalone(project_request, db)
#     print(f"Created Project: {project_response}")

#     # Step 2: Test get_champion_bandit_standalone
#     try:
#         champion_bandit = get_champion_bandit_standalone(project_id=project_response.project_id, db=db)
#         print(f"Champion Bandit: {champion_bandit}")
#     except ValueError as e:
#         print(f"Error finding champion bandit: {e}")

#     # Step 3: Add mock data to Events table (if not populated already)
#     # Check if liked and disliked events exist; otherwise, create them
#     liked_event = db.query(Event).filter(Event.EventName == "Liked Event").first()
#     if not liked_event:
#         liked_event = Event(EventId=1, EventName="Liked Event")
#         db.add(liked_event)
#         db.commit()

#     disliked_event = db.query(Event).filter(Event.EventName == "Disliked Event").first()
#     if not disliked_event:
#         disliked_event = Event(EventId=2, EventName="Disliked Event")
#         db.add(disliked_event)
#         db.commit()

#     # Step 4: Test user_choose_bandit_standalone
#     try:
#         bandit_choice = SubmitBanditChoiseResponseModel(bandit_name="Bandit A", chosen=True)
#         result = user_choose_bandit_standalone(bandit_choice, db)
#         print(f"Bandit Choice Result: {result}")
#     except ValueError as e:
#         print(f"Error choosing bandit: {e}")
