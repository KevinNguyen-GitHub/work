from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Room(Base):
    __tablename__ = "rooms"
    num = Column("num", Integer, primary_key=True, nullable=False)
    buildings_name(String(50), ForiegnKey('buildings.name'), primary_key=True, nullable=False)
    
    
    def __init__(self, num: Integer):
        self.num = num
