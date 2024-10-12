from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class User(Base):
    __tablename__ = "users"  

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    useremail = Column(String)
    credit_card_number = Column(String)
    created_timestamp = Column(DateTime(timezone=True), server_default=func.now())
