from pydantic import BaseModel
from typing import Optional, List

class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    category_id: int
    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    item_name: str
    description: Optional[str] = None
    price: Optional[float] = None
    is_offer: Optional[bool] = None
    category_id: Optional[int] = None


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    item_id: int

    class Config:
        orm_mode = True
