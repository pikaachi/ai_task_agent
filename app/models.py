from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql import expression
from app.database import Base  # ✅ Ensure it imports Base from database.py

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True) 
    description = Column(String, nullable=True)  
    category = Column(String, index=True)  # Personal, Work, Study
    priority = Column(String, index=True)  # High, Medium, Low
    completed = Column(Boolean, nullable=False, default=False)  # Default to False
