from sqlalchemy import Column, String, Integer, Date, Time, Boolean, Identity, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Building(Base):
    __tablename__ = "buildings"
    name = Column("name", String, primary_key=True, nullalbe=False)
    room = relationship("Room")
    
    def __init__(self, name: String):
        self.name = name
