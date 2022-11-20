from sqlalchemy import Column, String, Integer, ForeignKey, Identity
from sqlalchemy.orm import relationship
from orm_base import Base
from HookLine import HookLine


class Hook(Base):
    __tablename__ = "hooks"
    id = Column('id', Integer, Identity('hook_num', start=1, cycle=True),
                nullable=False, primary_key=True)

    copy_key = relationship("CopyKey", back_populates="hook")

    doors_list: [HookLine] = relationship("HookLine", back_populates="hook", viewonly=False)

    def __init__(self, id: Integer):
        self.id = id
        self.doors_list = []

    def add_door(self, door):
        # make sure this genre is non already on the list.
        for next_door in self.doors_list:
            if next_door == door:
                print("Door aleady added.")
                return
        # Create an instance of the junction table class for this relationship.
        hook_list = HookLine(self, door)
        # Update this move to reflect that we have this genre now.
        door.hooks_list.append(hook_list)
        # Update the genre to reflect this movie.
        self.doors_list.append(hook_list)
