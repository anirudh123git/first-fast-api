from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class Item(Base):
    __tablename__= "myitems"
    item_id=Column(Integer,primary_key=True,index=True)
    item_name=Column(String)