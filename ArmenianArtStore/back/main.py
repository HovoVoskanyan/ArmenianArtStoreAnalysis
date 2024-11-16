from Database.models import User, Variant,Event,VariantEvent,Product,Order
from Database.schema import User, UserCreate
from Database.database import get_db

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from typing import Dict

app = FastAPI(title="FastAPI, Docker, and Traefik")

@app.get("/users/{user_id}", response_model=User)
async def get_employee(user_id: int ):#db: Session = Depends(get_db)
    #employee = db.query(EmployeeDB).filter(EmployeeDB.employee_id == employee_id).first()
    #if employee is None:
     #   raise HTTPException(status_code=404, detail="Employee not found")
    return User(
        UserType = 'poxos',
        DeviceType = 'Mobile'
    )
@app.post("/users/", response_model=User)
async def create_employee(user: UserCreate, db: Session = Depends(get_db)):

    return User(
        UserType = user.UserType,
        DeviceType = user.DeviceType
    )


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id:int):

    return user_id


@app.delete("/users/{user_id}")
async def delete_employee(user_id: int, db: Session = Depends(get_db)):

    return {"message": "User deleted successfully"}