from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from KeyRequest import KeyRequest
from Building import Building


class Room(Base):
    __tablename__ = "rooms"
    num = Column("num", Integer, nullable=False, primary_key=True)
    buildings_name = Column(String(50), ForeignKey('buildings.name'), nullable=False, primary_key=True)

    door = relationship("Door", back_populates="rooms", viewonly=False)
    requests = relationship("Requests", back_populates="rooms", viewonly=False)
    buildings = relationship("Buildings", back_populates="rooms", viewonly=False)

    # table_args = (UniqueConstraint('Door', 'Request', 'Building', name='room_uk_01'))
    def __init__(self, num: Integer, building):
        self.num = num
        self.buildings_name = building.buildings_name

    def __str__(self):
        return str("Room number: " + str(self.num) + "  Building Name: " + str(self.buildings_name))

    # def add_employee(self, employee):
    #     for next_employee in self.employees_list:
    #         if next_employee == employee:
    #             return
    #     # Create an instance of the junction table class.
    #     key_request = KeyRequest(employee, self)
    #     # add that new instance to the list of genres that the Movie keeps.
    #     employee.rooms_list.append(key_request)
    #     # add that new instance to the list of movies that this genre keeps.
    #     self.employees_list.append(key_request)
