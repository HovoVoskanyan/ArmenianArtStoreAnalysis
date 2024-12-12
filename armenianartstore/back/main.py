from datetime import datetime

import numpy as np
from loguru import logger

# from ds_service.Thompson_sampling import apply_reward,select_bandit
from Models.Request.RequestsClasses import CreateProjectRequestModel, CreateBanditRequestModel, \
    SubmitBanditChoiseResponseModel
from Models.Response.ResponseClasses import CreateBanditResponseModel, CreateProjectResponseModel, ProjectReport, \
    UserEventResponse, Projects, UserEventResponses, BanditReport, ProjectItem
from Database.models import Project, Bandit, Event, UserEvent
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
        bandits_qty=project.bandits.qt
    )

    project.bandits.name = project.bandits.name.lower()

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

    event1 = Event(
        EventName="Like"
    )

    event2 = Event(
        EventName="Dislike"
    )

    db.add(event1)
    db.add(event2)
    db.commit()

    for i in range(1,project.bandits.qt+1):
        new_bandit = Bandit(
            project_id=new_project.project_id,
            name=f"{project.bandits.name}{i}",
            alpha=1,
            beta=1,
            n=0,
            updated_date=datetime.utcnow()
        )
        logger.info(f'Adding bandit {new_bandit.name} for project {new_project.project_id}')
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

    samples = [np.random.beta(bandit.alpha, bandit.beta) for bandit in bandits]

    # Select the bandit with the highest sample
    chosen_bandit = bandits[np.argmax(samples)]

    return chosen_bandit.name


@app.put("/user/bandit")
async def user_choose_bandit(bandit: SubmitBanditChoiseResponseModel, db: Session = Depends(get_db)):
    """
     endpoint to record did the user chose bandit positively.

    Args:
        bandit_name (str): The name of the bandit.
        db (Session): The database session dependency.
    """

    bandit_db = db.query(Bandit).filter(Bandit.name == bandit.bandit_name and Bandit.project_id == bandit.project_id).first()

    if not bandit_db:
        raise HTTPException(status_code=404, detail="Employee not found")

    if(bandit.chosen):
        liked_event = db.query(Event).filter(Event.EventName == "Dislike").first()
        bandit_db.alpha += 1
        new_event = UserEvent(
            project_id=bandit_db.project_id,
            bandit_id=bandit_db.id,
            event_id=liked_event.EventId,
        )
        db.add(new_event)
    else:
        bandit_db.beta += 1
        disliked_event = db.query(Event).filter(Event.EventName == "Like").first()
        new_event = UserEvent(
            project_id=bandit_db.project_id,
            bandit_id=bandit_db.id,
            event_id=disliked_event.EventId,
        )
        db.add(new_event)


    bandit_db.n +=1

    db.commit()

    return {"msg": "Ok"}


@app.get("/projects", response_model=Projects)
async def get_project(db: Session = Depends(get_db)):
    """
    Retrieve all projects.

    Returns:
        List[Project]: A list of all projects.
    """

    projects = db.query(Project).all()

    res_project = []

    for project in projects:
        res_project.append(ProjectItem(
            project_id=project.project_id,
            project_description = project.project_description,
            bandits_qty = project.bandits_qty,
            start_date = project.start_date
        ))

    return Projects(data=res_project)


@app.get("/project/report/{project_id}", response_model=ProjectReport)
async def get_project_report(project_id:int,db: Session = Depends(get_db)):
    """
    Retrieve a detailed report for a specific project.

    Args:
        project_id (int): The ID of the project.

    Returns:
        ProjectReport: A detailed project report.
    """
    bandits = db.query(Bandit).filter(project_id == Bandit.project_id)

    pr_report = ProjectReport(
        project_id = project_id,
        bandits_report = []
    )

    for bandit in bandits:
        bandit_rep = BanditReport(
            bandit_id= bandit.id,
            bandit_name = bandit.name,
            bandit_opened_qt = bandit.n,
            alpha = bandit.alpha,
            beta = bandit.beta
        )
        pr_report.bandits_report.append(bandit_rep)

    return pr_report