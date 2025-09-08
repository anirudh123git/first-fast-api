from sqlalchemy.orm import Session
from models import ItemCreate, CategoryCreate
from CRUD import crud_category, crud_item

# ---- Category Service Methods ----
def create_category(db: Session, category: CategoryCreate):
    return crud_category.create_category(category, db)

def get_all_categories(db: Session):
    return crud_category.get_all_categories(db)

def get_category_by_id(db: Session, category_id: int):
    return crud_category.get_category_by_id(category_id, db)


# ---- Item Service Methods ----
def create_item(db: Session, item: ItemCreate):
    return crud_item.create_item(item, db)

def get_all_items(db: Session):
    return crud_item.get_all_items(db)

def get_items_with_category(db: Session):
    return crud_item.get_items_with_category(db)

def update_items(id: int, item: ItemCreate, db: Session):
    return crud_item.update_items(id, item, db)

def delete_item(id: int, db: Session):
    return crud_item.delete_item(id, db)
