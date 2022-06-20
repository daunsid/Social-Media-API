from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.types import conint
from app.database import Base



class CreatPost(BaseModel):
    title: str
    content: str
    published: bool = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email : str
    password : str

class UserOut(BaseModel):
    id: int
    email: str
    created_at: datetime
    class Config:
        orm_mode = True

class Post(PostBase):
    created_at: datetime
    id: int
    owner_id : int
    votes:int
    owner: UserOut
    
    #rating: Optional[int] = None

    class Config:
        orm_mode = True
    

class PostOut(PostBase):
    Post:Post
    votes:int
    #owner: UserOut
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None

class Votes(BaseModel):
    post_id:int

    dir:conint(le=1)