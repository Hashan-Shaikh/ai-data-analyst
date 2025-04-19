# app/main.py
from fastapi import FastAPI
from app.routes import query
from app.init_db import init

app = FastAPI(title="AI Data Analyst")

@app.on_event("startup")
def startup():
    init()

app.include_router(query.router, prefix="/query")
