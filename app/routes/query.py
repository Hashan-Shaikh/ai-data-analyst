# app/routes/query.py
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import SalesRecord
from ..schemas import SalesRecordResponse
from ..langchain_agent import agent_executor

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[SalesRecordResponse])
def read_sales(db: Session = Depends(get_db)):
    return db.query(SalesRecord).all()

@router.post("/ask")
async def ask_question(request: Request):
    body = await request.json()
    question = body.get("question")
    print(question)

    if not question:
        return {"error": "No question provided"}

    try:
        result = agent_executor.run(question)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
