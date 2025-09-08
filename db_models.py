from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, nullable=False)

    items = relationship("Item", back_populates="category")


class Item(Base):
    __tablename__ = "myitems"

    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    is_offer = Column(Boolean)
    category_id = Column(Integer, ForeignKey("categories.category_id"))

    category = relationship("Category", back_populates="items")
