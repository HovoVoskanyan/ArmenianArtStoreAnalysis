from pydantic import (BaseModel,conint)
from typing import List


class CreateBanditRequestModel(BaseModel):
    name:str
    class Config:
        from_attributes=True
        arbitrary_types_allowed = True

class CreateProjectRequestModel(BaseModel):

    project_description: str
    bandits: List[CreateBanditRequestModel]

    class Config:
        from_attributes=True
        arbitrary_types_allowed = True




