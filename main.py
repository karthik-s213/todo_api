from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schema, models, database, crud

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/", response_model=schema.Todo)
async def postpage(todo: schema.TodoCreate, db: Session = Depends(get_db)):
    return crud.postpage(db=db, todo=todo)

@app.get("/", response_model=schema.Todo)
async def getpage(id: int, db: Session = Depends(get_db)):
    todo_data = crud.getpage(db=db, id=id)
    if todo_data is None:
        raise HTTPException(status_code=404, detail="page not found")
    return todo_data

@app.put("/", response_model=schema.Todo)
async def putpage(id: int, todo: schema.TodoUpdate, db: Session = Depends(get_db)):
    db_data = crud.putpage(id=id, todo=todo, db=db)
    if db_data is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return db_data

@app.delete("/", response_model=schema.Todo)
async def deletepage(id: int, db: Session = Depends(get_db)):
    db_todo = crud.deletepage(id=id, db=db)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return db_todo
