from datetime import datetime
from pydantic import BaseModel,EmailStr
from typing import Optional

# Schema for signup input 
class UserCreate(BaseModel):
    username: str
    password: str  
# output on signup
class User(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username:Optional[str]=None
    
