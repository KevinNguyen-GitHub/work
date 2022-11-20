from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

from Room import Room
from DoorType import DoorType
from HookLine import HookLine
class Door(Base):
    __tablename__ = "doors"
    door_type_name = Column('door_type_name',String(40), ForeignKey('door_type.name'), ce)
    rooms_num = Column('rooms_num',Integer, ForeignKey('rooms.num'), nullable=False, primary_key=True)
    rooms_buildings_name = Column(String(50), ForeignKey('rooms.buildings_name'), nullable=False, primary_key=True)
    
    #relationship
    doortype = relationship("DoorType", back_populates="doors", viewonly=False)
    rooms = relationship("Room", back_populates="doors", viewonly=False)

    hooks_list: [HookLine] = relationship("HookLine", back_populates="doors", viewonly=False)
    def __init__(self, door_type, room):
        self.door_type_name = door_type.door_type_name
        self.rooms_num = room.rooms_num
        self.rooms_buildings_name = room.rooms_buildings_name
        self.hooks_list = []

    def add_hook(self, hook):
        for next_hook in self.hooks_list:
            if next_hook == hook:
                print("Hook has already been created at a previous time")
                return
        # Create an instance of the junction table class.
        hook_line = HookLine(hook, self)
        # add that new instance to the list of genres that the Movie keeps.
        hook.add_door(hook_line)
        # add that new instance to the list of movies that this genre keeps.
        self.hooks_list.append(hook_line)
