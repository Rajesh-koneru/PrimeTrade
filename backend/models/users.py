from datetime import datetime,date

from sqlalchemy import Column, Integer, String,Date
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password=Column(String)
    create_data=Column(Date,default=date.today())
    role=Column(String)