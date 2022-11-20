from sqlalchemy import Column, String, Identity, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
from KeyRequest import KeyRequest


class Employee(Base):
    __tablename__ = "employees"
    name = Column("name", String(40), nullable=False)
    id = Column("id", Integer, Identity(start=1, cycle=True),
                nullable=False, primary_key=True)

    rooms_list: [KeyRequest] = relationship("KeyRequest", back_populates="employee", viewonly=False)
    request = relationship("KeyRequest", back_popultaes="eployess")
    def __init__(self, name: String, id: Integer):
        self.name = name
        self.id = id
        self.rooms_list = []

    def add_room(self, request):
        # make sure this genre is non already on the list.
        for next_room in self.rooms_list:
            if next_room == request:
                print("Request already made previously.")
                return

        # Create an instance of the junction table class for this relationship.
        key_request = KeyRequest(self, request)
        # Update this move to reflect that we have this genre now.
        request.employees_list.append(key_request)
        # Update the genre to reflect this movie.
        self.rooms_list.append(key_request)
