from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import ItemCreate, ItemResponse, CategoryCreate
from services import services

router = APIRouter()

# ---- Item Endpoints ----

@router.get("/items")
def get_items(db: Session = Depends(get_db)):
    return services.get_all_items(db)

@router.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return services.create_item(db, item)

@router.put("/items")
def update_item(id: int, item: ItemCreate, db: Session = Depends(get_db)):
    return services.update_items(id, item, db)

@router.delete("/items")
def delete_item(id: int, db: Session = Depends(get_db)):
    return services.delete_item(id, db)

@router.get("/items-with-category")
def get_items_with_category(db: Session = Depends(get_db)):
    return services.get_items_with_category(db)


# ---- Category Endpoints ----

@router.post("/categories")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return services.create_category(db, category)

@router.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    return services.get_all_categories(db)
