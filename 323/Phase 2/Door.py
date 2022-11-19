from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from HookLine import HookLine
class Door(Base):
    __tablename__ = "doors"
    door_type_name = Column(String(40), ForeignKey('door_type.name'), primary_key=True, nullable=False)
    rooms_num = Column(Integer, ForeignKey('rooms.num'), primary_key=True, nullable=False)
    rooms_buildings_name = Column(String(50), ForeignKey('rooms.buildings_name'), primary_key=True, nullable=False)
    
    #relationship 
    hooks_list : [HookLine] = relationship("HookLine", back_populates="door", viewonly=False)
    
    def __init__(self, door_type, room):
        self.door_type_name = door_type.door_type_name
        self.rooms_num = room.rooms_num
        self.rooms_buildings_name = room.rooms_buildings_name
        self.hooks_list = []

    def add_hook(self, hook):
        for next_hook in self.hooks_list:
            if next_hook == hook:
                return
        # Create an instance of the junction table class.
        hook_list = (hook, self)
        # add that new instance to the list of genres that the Movie keeps.
        hook.doors_list.append(hook_list)
        # add that new instance to the list of movies that this genre keeps.
        self.hooks_list.append(hook_list)
