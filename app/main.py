from fastapi import Body, FastAPI #Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import model
from .database import engine, SessionLocal, get_db
from .routers import post, users, auth, votes



# sqlalchemy command for creating tables in database
#model.Base.metadata.create_all(bind=engine)

app = FastAPI()

#origins = ["https://www.google.com", "https://www.youtube.com"]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres",
        password="modupe4816", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection was successfull")
        break
    except Exception as error:
        print("connecting to database failed")
        print('Error: ', error)
        time.sleep(2)
"""
my_posts = [
    {"title": "title of posts 1", "content": "content of posts", "id":1},
    {"title":"fav food","content": "I like pazza", "id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/home")
async def root():
    
    return {"message": "welcome to my api"}