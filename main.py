from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Welcome to the FastAPI root endpoint!"})
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage for user data
users_db = []

# Pydantic model to define the structure of user information
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

@app.post("/users/", response_model=User)
def create_user(user: User):
    # Check if user with same ID already exists
    for existing_user in users_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="User ID already exists")
    users_db.append(user)
    return user

@app.get("/users/", response_model=List[User])
def get_all_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

