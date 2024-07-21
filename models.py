from sqlalchemy import Boolean, Column, Integer, String, DateTime
from .database import Base

class Todo(Base):
    __tablename__ = "to_do"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    due_date = Column(DateTime)
    completed = Column(Boolean)
