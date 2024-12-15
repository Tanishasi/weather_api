from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import db_dependency
from app import models, schemas
from app.utils import oauth,hashing

router = APIRouter(
    tags=['Authentication']
)

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: db_dependency):
    hashed_pass = hashing.hash(user.password)  
    user.password = hashed_pass

    db_user = models.User(**user.dict(exclude_unset=True))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.post('/login', response_model=schemas.Token)
def login(db: db_dependency, user_cred: OAuth2PasswordRequestForm = Depends()):
    user = db.query(models.User).filter(models.User.username == user_cred.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid username")
    
    if not hashing.verify(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid password")
    
    access_token = oauth.create_access_token(data={"username": user.username})
    
    # Make sure the returned dictionary matches the Token schema
    return {"access_token": access_token, "token_type": "bearer"}
