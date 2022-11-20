from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base


class HookLine(Base):
    __tablename__ = "hook_lines"
    doors_door_type_name = Column('door_type_name', String(50), ForeignKey('doors.door_type_name'), primary_key=True,
                                  nullable=False)
    doors_rooms_num = Column('rooms_num', Integer, ForeignKey('doors.rooms_num'), primary_key=True, nullable=False)
    doors_rooms_buildings_name = Column('building_name', String(50), ForeignKey('doors.rooms_buildings_name'),
                                        primary_key=True, nullable=False)
    hooks_id = Column('hooks_id', Integer, ForeignKey('hooks.id'), primary_key=True, nullable=False)

    # relationship
    hook = relationship("Hook", back_populates='doors_list')
    # movies_list is the name of the list of MovieGenre instances for the parent movie.
    door = relationship("Door", back_populates='hooks_list')

    def __init__(self, door, hook):
        self.doors_door_type_name = door.doors_door_type_name
        self.hooks_id = hook.hooks_id

        self.hook = hook
        self.door = door
