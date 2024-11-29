from datetime import datetime
from loguru import logger
from Models.Request.RequestsClasses import CreateProjectRequestModel,CreateBanditRequestModel
from Models.Response.ResponseClasses import CreateBanditResponseModel,CreateProjectResponseModel
from Database.models import Project, Bandit,Event,UserEvent
from Database.schema import User, UserCreate
from Database.database import get_db

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from typing import Dict
app = FastAPI(title="FastAPI, Docker, and Traefik")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/users/{user_id}", response_model=User)
# async def get_employee(user_id: int ):#db: Session = Depends(get_db)
#     #employee = db.query(EmployeeDB).filter(EmployeeDB.employee_id == employee_id).first()
#     #if employee is None:
#      #   raise HTTPException(status_code=404, detail="Employee not found")
#     return User(
#         UserType = 'poxos',
#         DeviceType = 'Mobile'
#     )
@app.post("/project", response_model=User)
async def create_project(project: CreateProjectRequestModel, db: Session = Depends(get_db)):

    new_project = Project(
        project_description = project.project_description,
        start_date = datetime.utcnow(),
        bandits_qty = len(project.bandits)
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)


    for bandit in project.bandits:
        new_bandit = Bandit(
            project_id=new_project.project_id,
            name = bandit.name,
            alpha =0,
            beta =0,
            n= new_project.bandits_qty,
            updated_date = datetime.utcnow()
        )
        logger.info(f'adding bandit {bandit.name} for {new_project.project_id}')
        db.add(new_bandit)
        db.commit()
        db.refresh(new_bandit)


# @app.put("/users/{user_id}", response_model=User)
# async def update_user(user_id:int):
#
#     return user_id
#
#
# @app.delete("/users/{user_id}")
# async def delete_employee(user_id: int, db: Session = Depends(get_db)):
#
#     return {"message": "User deleted successfully"}