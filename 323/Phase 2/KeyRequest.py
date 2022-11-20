from sqlalchemy import Column, String, Integer, Date, Time, Boolean, Identity, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base


class KeyRequest(Base):
    __tablename__ = "key_requests"
    request_id = Column('request_id', Integer, Identity(start=1, cycle=True),
                        nullable=False, primary_key=True)
    request_date = Column("request_date", Date, nullable=False)
    # foreign key from employee class
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    # foreign key from room class
    rooms_num = Column(Integer, ForeignKey('rooms.num'), nullable=False)
    rooms_buildings_name = Column(Integer, ForeignKey('rooms.buildings_name'), nullable=False)
    # foreign key from copy_keys class
    copy_keys_id = Column(Integer, ForeignKey('copy_keys.id'), nullable=False)
    copy_keys_is_loss = Column(Boolean, ForeignKey('copy_keys.is_loss'), nullable=False)

    # relationship
    employee = relationship("Employee", back_populates='rooms_list')
    room = relationship("Room", back_populates='employees_list')

    def __init__(self, request_date: Date, employee, room, copy_key):
        self.request_date = request_date
        self.employee_id = employee.employee_id
        self.rooms_num = room.rooms_num
        self.rooms_buildings_name = room.rooms_buildings_name
        self.copy_keys_id = copy_key.copy_keys_id
        self.copy_key_is_loss = copy_key.copy_keys_is_loss
