from sqlalchemy.orm import Session
from models import Items

#function to create a new item
def create_item(db:Session, description, status:str):
    new_item = Items(description=description, status=status)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

#function to retrieve all items
def get_all(db:Session):
    all_items = db.query(Items).all()
    return all_items

#function to retrieve all to do items
def get_todo_items(db:Session):
    todo_items = db.query(Items).filter(Items.status=='To Do').all()
    return todo_items

#function to retrieve all done items
def get_done_items(db:Session):
    done_items = db.query(Items).filter(Items.status=='Done').all()
    return done_items

#function to retrieve all deleted items
def get_deleted_items(db:Session):
    deleted_items = db.query(Items).filter(Items.status=='Deleted').all()
    return deleted_items

#function to retrieve specific item (used in update methods)
def get_item(db:Session, id:int):
    item = db.query(Items).filter(Items.id==id).first()
    return item

#function to update description 
def update_item_description(db:Session, id: int, description: str):
    item = get_item(db=db, id=id)
    item.description = description
    db.commit()
    db.refresh(item)
    return item

#function to update status
def update_status_item(db:Session, id:int, status: str):
    item = get_item(db=db, id=id)
    item.status = status
    db.commit()
    db.refresh(item)
    return item

#function to delete item
def delete_item(db:Session, id:int):
    item = get_item(db=db, id=id)
    db.delete(item)
    db.commit()
