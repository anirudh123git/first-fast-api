from models import ItemCreate
import db_models
from sqlalchemy.orm import Session
def create_item(item:ItemCreate,db:Session):
    db_item=db_models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    return item
def get_all_items(db:Session):
    
    
    db_items=db.query(db_models.Item).all()
    
    return db_items
def update_items(id:int,item:ItemCreate,db:Session):
    db_item=db.query(db_models.Item).filter(db_models.Item.item_id==id).first()
    if(db_item):
        db_item.item_name=item.item_name
        db.commit()
        return "product updated"
    return "Product not Found"
def delete_item(id:int,db:Session):
    db_item=db.query(db_models.Item).filter(db_models.Item.item_id==id).first()
    if(db_item):
        db.delete(db_item)
        db.commit()
        return "Product deleted"
    
    return "No product found"
def get_items_with_category(db: Session):
    results = db.query(db_models.Item, db_models.Category).join(
        db_models.Category, db_models.Item.category_id == db_models.Category.category_id
    ).all()

    return [
        {
            "item_id": item.item_id,
            "item_name": item.item_name,
            "description": item.description,
            "price": item.price,
            "is_offer": item.is_offer,
            "category": {
                "category_id": category.category_id,
                "category_name": category.category_name
            }
        }
        for item, category in results
    ]

