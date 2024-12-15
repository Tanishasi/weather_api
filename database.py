from typing import Annotated
from fastapi import Depends
from pytest import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
URL_DATABASE=os.getenv("DB_URL")
engine=create_engine(URL_DATABASE)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close
db_dependency=Annotated[Session,Depends(get_db)]