from pydantic import BaseModel



class User(BaseModel):
    user_id:int
    DeviceType:str
    UserType:str

class UserCreate(BaseModel):
    DeviceType:str
    UserType:str


