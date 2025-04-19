# app/init_db.py
from datetime import date
from .database import Base, engine, SessionLocal
from .models import SalesRecord

def init():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(SalesRecord).first():
        print("DB already seeded.")
        db.close()
        return

    mock_data = [
        SalesRecord(region="North", product="Widget A", sales_amount=1200.0, date=date(2024, 3, 10)),
        SalesRecord(region="South", product="Widget B", sales_amount=950.0, date=date(2024, 3, 15)),
        SalesRecord(region="West", product="Widget A", sales_amount=1320.0, date=date(2024, 3, 20)),
        SalesRecord(region="East", product="Widget C", sales_amount=870.0, date=date(2024, 3, 12)),
    ]

    db.add_all(mock_data)
    db.commit()
    db.close()
    print("Mock data seeded.")
