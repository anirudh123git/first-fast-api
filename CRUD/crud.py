from models import Item
import db_models
from sqlalchemy.orm import Session
def create_item(item:Item,db:Session):
    db_item=db_models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    return item
def get_all_items(db:Session):
    
    
    db_items=db.query(db_models.Item).all()
    
    return db_items
def update_items(id:int,item:Item,db:Session):
    db_item=db.query(db_models.Item).filter(db_models.Item.item_id==id).first()
    if(db_item):
        db_item.item_name=item.item_name
        db.commit()
        return "product updated"
    return "Product not Found"
def delete_products(id:int,db:Session):
    db_item=db.query(db_models.Item).filter(db_models.Item.item_id==id).first()
    if(db_item):
        db.delete(db_item)
        db.commit()
        return "Product deleted"
    
    return "No product found"