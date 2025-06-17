from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
app = FastAPI()

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Welcome to the FastAPI root endpoint!"})

users_db = []
# class User(BaseModel):
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

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

class ChoiceBase(BaseModel):
    choice_text:str
    is_correct:bool

class QuestionBase(BaseModel):
    question_text:str
    choices:List[ChoiceBase]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/questions/{question_id}")
async def read_question(question_id: int):
    result =db.query(models.questions).filter(models.Questions.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Question is not found')
    return result

@app.get("/choices/{question_id}")
async def read_choices(question_id:int):
    result = db.query(models.choices).filter(models.choices.question_id == question_id).all()
    if not result:
        raise HTTPException(status_code=404, detail='Choices is not found')
    return result
    
@app.post("/questions/")
async def create_questions(question: QuestionBase):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question) 
    for choice in question.choices:
        db_choice = models.Choices(choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choice)
    db.commit()


