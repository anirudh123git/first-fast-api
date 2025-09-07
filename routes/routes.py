from fastapi import APIRouter,Depends
from database import sessionlocal
import services.services as myservice
from models import Item
from sqlalchemy.orm import Session
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
router=APIRouter(prefix="/items")
@router.get("/")
def get_items(db:Session=Depends(get_db)):
    return myservice.get_all_items(db)
@router.post("/")
def create(item:Item,db:Session=Depends(get_db)):
   return myservice.create_item(item,db)
@router.put("/")
def update(id:int,item:Item,db:Session=Depends(get_db)):
    return myservice.update_items(id,item,db)
@router.delete("/")
def delete(id:int,db:Session=Depends(get_db)):
    return myservice.update_items(id,db)