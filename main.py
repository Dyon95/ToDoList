from fastapi import FastAPI, Depends, Query, Path
import models
from db import engine, SessionLocal
import crud
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

description="""
ToDo API will let you add and update tasks and their status.
When creating a task only use the values To Do, Done or Deleted. 
With these values ToDo API is able to get lists of everything that is 
still to be done, already done or deleted. 

WARNING: If you want to access your deleted items please update the status with the value Deleted.
Using the delete_item method will completely remove the task and will no longer be retrievable. 
"""

app = FastAPI(
    title="ToDo API",
    description=description,
    version=1.0
)
    

#define endpoint for creating an item
@app.post("/create_item")
def create_item(description:str, status:str | None = Query(description = "Only use values: To Do, Done or Deleted"), db:Session = Depends(get_db)):
    item = crud.create_item(db=db, description=description, status=status)
    return {"item": item}

@app.get("/get_all")
def get_all(db:Session = Depends(get_db)):
    all_list = crud.get_all (db=db)
    return all_list

#define endpoint for getting to do items
@app.get("/get_todo")
def get_todo(db:Session = Depends(get_db)):
    todo_list = crud.get_todo_items (db=db)
    return todo_list

#define endpoint for getting done items
@app.get("/get_done")
def get_done(db:Session = Depends(get_db)):
    done_list = crud.get_done_items (db=db)
    return done_list

#define endpoint for getting deleted items
@app.get("/get_deleted")
def get_deleted(db:Session = Depends(get_db)):
    deleted_list = crud.get_deleted_items (db=db)
    return deleted_list

#define endpoint for updating description of items 
@app.put("/update_description")
def update_description(id:int, description:str, db:Session = Depends(get_db)):
    item = crud.get_item(db=db, id=id)
    if item:
        updated_desc_item = crud.update_item_description(db=db, id=id, description=description)
        return updated_desc_item
    else:
        return {"error": f"Item with id {id} does not exist."}

#define endpoint for updating status of items
@app.put("/update_status")
def update_status(id:int, status:str | None = Query(description = "Only use values: To Do, Done or Deleted"), db:Session = Depends(get_db)):
    item = crud.get_item(db=db, id=id)
    if item:
        updated_status_item = crud.update_status_item(db=db, id=id, status=status)
        return updated_status_item
    else:
        return {"error": f"Item with id {id} does not exist."}

#define endpoint for completely removing item 
@app.delete("/delete_item")
def delete_item(id:int, db:Session = Depends(get_db)):
    item = crud.get_item(db=db, id=id)
    if item:
        return crud.delete_item(db=db, id=id)
    else:
        return {"error": f"Item with id {id} does not exist."}
