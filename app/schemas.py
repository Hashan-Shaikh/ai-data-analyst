# app/schemas.py
from pydantic import BaseModel
from datetime import date

class SalesRecordCreate(BaseModel):
    region: str
    product: str
    sales_amount: float
    date: date

class SalesRecordResponse(SalesRecordCreate):
    id: int

    class Config:
        orm_mode = True
