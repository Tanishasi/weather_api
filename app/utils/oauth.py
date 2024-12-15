from fastapi import FastAPI, HTTPException, Depends,status
from jose import JWTError, jwt
from datetime import datetime,timedelta
from app import schemas
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

load_dotenv()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# payload
def create_access_token(data:dict):
    to_encode = data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    enc_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)    
    return enc_jwt

def verify_access_token(token:str,credentials_exception):
     try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("username")
        if username is None:
            raise credentials_exception
        token_data=schemas.TokenData(username=username)
     except JWTError as e:
        print(e)
        raise credentials_exception
     return token_data
     
def get_current_user(token: str=Depends(oauth2_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    return verify_access_token(token,credentials_exception)

