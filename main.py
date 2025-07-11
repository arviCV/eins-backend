from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
import model
from database import engine, SessionLocal
from typing import List, Annotated
from sqlalchemy.orm import Session
import auth
from auth import get_current_user


app = FastAPI()
app.include_router(auth.router)

model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return {"User": user}


class ChoiceBase(BaseModel):
    choice_text:str
    is_correct:bool

class QuestionBase(BaseModel):
    question_text:str
    choices:List[ChoiceBase]


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