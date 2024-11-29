from datetime import datetime
from typing import List

from pydantic import (BaseModel,conint)

class CreateBanditResponseModel(BaseModel):
    id:int
    project_id:int
    name:int
    alpha:float
    beta:float
    update_date: datetime
    class Config:
        from_attributes=True
        arbitrary_types_allowed = True
class CreateProjectResponseModel(BaseModel):

    project_id: str
    start_date: datetime
    project_description:str
    bandit_qty:str
    bandits: List[CreateBanditResponseModel]
    class Config:
        from_attributes=True
        arbitrary_types_allowed = True



