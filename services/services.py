from models import Item
import db_models
from sqlalchemy.orm import Session
from CRUD import crud
def create_item(item:Item,db:Session):
    res=crud.create_item(item,db)
    return res

def get_all_items(db:Session):
    
    
    db_items=crud.get_all_items()
    
    return db_items

def update_items(id:int,item:Item,db:Session):
    return crud.update_items(id,item,db)

def delete_products(id:int,db:Session):
    return  crud.delete_products(id,db)
    