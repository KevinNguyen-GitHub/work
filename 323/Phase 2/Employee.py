from sqlalchemy import Column, String, Integer, Date, Time, Boolean, Identity, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from KeyRequest import KeyRequest

class Employee(Base):
    __tablename__ = "employees"
    name = Column("name", String(40), nullable=False)
    id = Column("id", Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True)
                       
    rooms_list: [KeyRequest] = relationship("KeyRequest", back_populates="employee", viewonly=False)
    
def _init_(self, name: String, id: Integer):
    self.name = name
    self.id = id
    self.rooms_list = []

 def add_room(self, room):
        # make sure this genre is non already on the list.
        for next_room in self.rooms_list:
            if next_room == room:
                return
        # Create an instance of the junction table class for this relationship.
        key_request = KeyRequest(self, room)
        # Update this move to reflect that we have this genre now.
        room.employees_list.append(key_request)
        # Update the genre to reflect this movie.
        self.rooms_list.append(key_request)
