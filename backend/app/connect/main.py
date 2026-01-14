from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, TypeAdapter
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import Session
# from schemas import *
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()
engine = create_engine("")
Base = declarative_base()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CreateUser(BaseModel): # validation
    FirstName: str
    LastName: str
    User_Role: str
    User_Name: str # Unique 
    User_Password: str

    class Config:
        orm_mode = True

class CreateProject(BaseModel):  # validation
    User_Id: int = Field()
    Project_Name: str = Field()
    Project_Task: str = Field()

    class Config:
        orm_mode = True

class User(Base):
    __tablename__ = "Users"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String)
    LastName = Column(String)
    User_Role = Column(String)
    User_Name = Column(String)
    User_Password = Column(String)
    Create_At = Column(DateTime, nullable=True)
    Deleted_At = Column(DateTime, nullable=True)
 
@app.get("{file_path:path}")

@app.get("/api/data")
def read_data():
    # return ["Hi"]
    return [{"id": 1, "name": "Project A"}, {"id": 2, "name": "Project B"}]

@app.post("/api/CreateUser")
async def add_User(user: CreateUser):
    # new_User = CreateUser(
    #     FirstName=user.FirstName,
    #     LastName=user.LastName,
    #     User_Role=user.User_Role,
    #     User_Name=user.User_Name,
    #     User_Password=user.User_Password,
    # )
    new_User = {
        "FirstName": user.FirstName,
        "LastName": user.LastName,
        "User_Role": user.User_Role,
        "User_Name": user.User_Name,
        "User_Password": user.User_Password,
    }
    with Session(engine) as session:
        try:
            add_User = User(FirstName=user.FirstName, LastName=user.LastName, User_Role=user.User_Role, User_Name=user.User_Name, User_Password=user.User_Password)
            session.add(add_User)
        except:
            session.rollback()
            raise
        else:
            session.commit()
    return {"message": "New user has been added successfully", "Details": add_User}

@app.post("/api/CreateProject")
async def add_Project(project: CreateProject):
    new_Project = {
        "User_Id": project.User_Id,
        "Project_Name": project.Project_Name,
        "Project_Task": project.Project_Task,
    }
    return {"message": "New project has been created successfully", "Details": new_Project}