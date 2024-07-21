from sqlalchemy.orm import Session
from . import schema, models, database

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getpage(id: int, db: Session):
    todo_data = db.query(models.Todo).filter(models.Todo.id == id).first()
    return todo_data

def postpage(todo: schema.TodoCreate, db: Session):
    db_todo = models.Todo(
        title=todo.title, 
        description=todo.description, 
        due_date=todo.due_date, 
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def putpage(id: int, todo: schema.TodoUpdate, db: Session):
    db_data = db.query(models.Todo).filter(models.Todo.id == id).first()
    if db_data is None:
        return None
    for key, value in todo.dict().items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)
    return db_data

def deletepage(id: int, db: Session):
    db_todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if db_todo is None:
        return None
    db.delete(db_todo)
    db.commit()
    return db_todo
