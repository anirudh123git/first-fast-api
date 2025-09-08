from models import CategoryCreate
import db_models
from sqlalchemy.orm import Session

def create_category(category: CategoryCreate, db: Session):
    db_category = db_models.Category(category_name=category.category_name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_all_categories(db: Session):
    return db.query(db_models.Category).all()


def get_category_by_id(category_id: int, db: Session):
    return db.query(db_models.Category).filter(db_models.Category.category_id == category_id).first()
