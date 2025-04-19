# app/models.py
from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class SalesRecord(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    region = Column(String, index=True)
    product = Column(String)
    sales_amount = Column(Float)
    date = Column(Date)
