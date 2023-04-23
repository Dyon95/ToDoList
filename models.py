from sqlalchemy import Column, Integer, String
from db import Base

#table

class Items(Base):
    __tablename__ = "Items"
    id = Column(Integer, primary_key=True)
    description = Column(String(150), nullable=False)
    status = Column(String(100), nullable=False)