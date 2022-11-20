from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from Building import Building

class Room(Base):
    __tablename__ = "rooms"
    number = Column("number", Integer, primary_key=True, nullable=False)
    buildings_name = Column(String(50), ForeignKey('buildings.name'), primary_key=True, nullable=False)
    
    door = relationship("Door", back_populates="rooms",  viewonly=False)
    requests = relationship("Requests", back_populates="rooms", viewonly=False)
    buildings = relationship("Buildings", back_populates="rooms", viewonly=False)


    
    def __init__(self, number: Integer, building):
        self.number = number
        self.buildings_name = building.buildings_name
