from fastapi import FastAPI, HTTPException,status,APIRouter
from fastapi import FastAPI, Response,status,HTTPException
# import models,schemas
# from models import User,Post
from app.utils.oauth import get_current_user
from sqlalchemy.orm import Session
from database import engine, SessionLocal, get_db
from typing import Annotated,List
from fastapi.params import Depends
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import httpx


router=APIRouter(
    tags=['weather']
)


load_dotenv()

key=os.getenv("api_key")

@router.get("/weather")
def get_weather(latitude:float, longitude:float, username:str= Depends(get_current_user)):
    url=f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={key}"
    response=httpx.get(url)
    if response.status_code!=200:
        raise HTTPException(status_code=401,detail="unable to fetch weather")
    return response.json()