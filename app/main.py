from fastapi import FastAPI, HTTPException, Depends,status
from pydantic import BaseModel
# from typing import Annotated,List
# import models,schemas
# from utils import hash
from . import models
from database import engine,Base
from app.routers import auth,weather
app=FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(weather.router)