from sqlalchemy import Column, String, Integer, Date, Time, Boolean, Identity, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from KeyRequest import KeyRequest
class Room(Base):
    __tablename__ = "rooms"
    num = Column("num", Integer, primary_key=True, nullable=False)
    buildings_name = Column(String(50), ForeignKey('buildings.name'), primary_key=True, nullable=False)
    
    door = relationship("Door")
    employees_list: [KeyRequest] = relationship("KeyRequest", back_populates="room", viewonly=False) 
    def __init__(self, num: Integer, building):
        self.num = num
        self.buildings_name = building.buildings_name
        
    def add_employee(self, employee):
        for next_employee in self.employees_list:
            if next_employee == employee:
                return
        # Create an instance of the junction table class.
        key_request = KeyRequest(employee, self)
        # add that new instance to the list of genres that the Movie keeps.
        employee.rooms_list.append(key_request)
        # add that new instance to the list of movies that this genre keeps.
        self.employees_list.append(key_request)
