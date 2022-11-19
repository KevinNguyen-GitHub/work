from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Door(Base):
    __tablename__ = "doors"
    door_type_name = Column(String(40), ForeignKey('door_type.name'), primary_key=True, nullable=False)
    rooms_num = Column(Integer, ForeignKey('rooms.num'), primary_key=True, nullable=False)
    rooms_buildings_name = Column(String(50), ForeignKey('rooms.buildings_name'), primary_key=True, nullable=False)
    
    #relationship 
    
    def __ini__(self, door_type, room, room):
        self.door_type_name = door_type.door_type_name
        self.rooms_num = room.rooms_num
        self.rooms_buildings_name = room.rooms_buildings_name
