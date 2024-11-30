from datetime import datetime
from loguru import logger

# from ds_service.Thompson_sampling import apply_reward,select_bandit
from Models.Request.RequestsClasses import CreateProjectRequestModel, CreateBanditRequestModel
from Models.Response.ResponseClasses import CreateBanditResponseModel, CreateProjectResponseModel, ProjectReport, \
    UserEventResponse
from Database.models import Project, Bandit, Event, UserEvent
from Database.schema import User, UserCreate
from Database.database import get_db

from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from typing import Dict, List

app = FastAPI(title="FastAPI, Docker, and Traefik")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/project", response_model=CreateProjectResponseModel)
async def create_project(project: CreateProjectRequestModel, db: Session = Depends(get_db)):
    """
    Create a new project along with associated bandits.

    Args:
        project (CreateProjectRequestModel): The project details including description and bandits.
        db (Session): The database session dependency.

    Returns:
        CreateProjectResponseModel: Response containing project and associated bandits.
    """
    new_project = Project(
        project_description=project.project_description,
        start_date=datetime.utcnow(),
        bandits_qty=len(project.bandits)
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    response = CreateProjectResponseModel(
        project_id=new_project.project_id,
        project_description=new_project.project_description,
        start_date=new_project.start_date,
        bandits_qty=new_project.bandits_qty,
        bandits=[]
    )

    for bandit in project.bandits:
        new_bandit = Bandit(
            project_id=new_project.project_id,
            name=bandit.name,
            alpha=0,
            beta=0,
            n=new_project.bandits_qty,
            updated_date=datetime.utcnow()
        )
        logger.info(f'Adding bandit {bandit.name} for project {new_project.project_id}')
        db.add(new_bandit)
        db.commit()
        db.refresh(new_bandit)

        response_bandit = CreateBanditResponseModel(
            project_id=new_bandit.project_id,
            name=new_bandit.name,
            alpha=new_bandit.alpha,
            beta=new_bandit.beta,
            id=new_bandit.id,
            update_date=new_bandit.updated_date
        )
        response.bandits.append(response_bandit)

    return response

@app.get("/bandit/{project_id}", response_model=str)
async def get_champion_bandit(project_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the champion bandit for a given project.

    Args:
        project_id (int): The ID of the project.
        db (Session): The database session dependency.

    Returns:
        str: Placeholder response for champion bandit.
    """
    bandits = db.query(Bandit).filter(project_id == Bandit.project_id)

    return "TODO"

@app.post("/bandit/{bandit_name}")
async def get_champion_bandit(bandit_name: str, db: Session = Depends(get_db)):
    """
    Placeholder endpoint to get champion bandit by name.

    Args:
        bandit_name (str): The name of the bandit.
        db (Session): The database session dependency.

    Returns:
        str: Placeholder response.
    """
    # bandits = db.query(Bandit).filter(project_id == Bandit.project_id).list()
    # champion = select_bandit(bandits)

    return "nono"

@app.get("projects", response_model=List[Project])
async def get_project():
    """
    Retrieve all projects.

    Returns:
        List[Project]: A list of all projects.
    """
    return ProjectReport()

@app.get("project/report/{project_id}", response_model=ProjectReport)
async def get_project_report():
    """
    Retrieve a detailed report for a specific project.

    Args:
        project_id (int): The ID of the project.

    Returns:
        ProjectReport: A detailed project report.
    """
    return ProjectReport()

@app.get("user/event", response_model=List[UserEventResponse])
async def get_user_event_report():
    """
    Retrieve a report of user events.

    Returns:
        List[UserEventResponse]: A list of user event responses.
    """
    return None
