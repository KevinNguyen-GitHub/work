from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class HookLine(Base):
    __tablename__ = "hook_lines"
    doors_door_type_name = Column(String(50), ForeignKey('doors.door_type_name'), primary_key=True, nullable=False)
    doors_rooms_num = Column(Intger, ForeignKey('doors.rooms_num'), primary_key=True, nullable=False)
    doors_rooms_buildings_name = Column(String(50), ForeignKey('doors.rooms_buildings_name'), primary_key=True, nullable=False)
    hooks_id = Column(Integer, Foreign('hooks.id'), primary_key=True, nullable=False)
    
    #relationship 
    
    def __init__(self, door, door, door, hook):
        self.doors_door_type_name = door.doors_door_type_name
        self.doors_rooms_num = door.doors_rooms_num
        self.doors_rooms_buildings_name =door.doors_rooms_buildings_name 
        self.hooks_id = hook.hooks_id
