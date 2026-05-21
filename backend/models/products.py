from cgi import maxlen
from datetime import datetime,date
from operator import index
from xmlrpc.client import boolean

from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from database import Base

class products(Base):
    __tablename__= "products"
    Id=Column(Integer,primary_key=True,index=True)
    prod_Id=Column(String)
    prod_name =Column(String)
    prod_cost=Column(String)
    prod_disc=Column(String)
    prod_count=Column(String)
    prod_status=Column(String)
    prod_added_at=Column(Date,default=date.today())
