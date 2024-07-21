from pydantic import BaseModel
from datetime import datetime

class ToDoBase(BaseModel):
    title: str
    description: str
    due_date: datetime
    completed: bool

class TodoCreate(ToDoBase):
    pass

class TodoUpdate(ToDoBase):
    pass

class TodoInDBBase(ToDoBase):
    id: int

    class Config:
        orm_mode = True

class Todo(TodoInDBBase):
    pass
