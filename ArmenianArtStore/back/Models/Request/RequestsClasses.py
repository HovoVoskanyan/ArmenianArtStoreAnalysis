from pydantic import (BaseModel,conint)
from typing import List


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




