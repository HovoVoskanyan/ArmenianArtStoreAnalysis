from datetime import datetime
from typing import List

from pydantic import (BaseModel, conint)

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
    project_id: int
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
