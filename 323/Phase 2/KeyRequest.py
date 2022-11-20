from sqlalchemy import Column, String, Integer,Date,Time, Boolean, Identity, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
import datetime


class KeyRequest(Base):
    __tablename__ = "key_requests"
    request_date = Column("request_date", Date, nullable=False)
    #foreign key from employee class
    employee_id = Column("emplyee_id",Integer, ForeignKey('employees.id'), primary_key=True, nullable=False)
    #foreign key from room class
    rooms_num = Column("room_nums",Integer, ForeignKey('rooms.num'), primary_key=True, nullable=False)
    rooms_buildings_name = Column('rooms_buildings_name',Integer, ForeignKey('rooms.buildings_name'), primary_key=True, nullable=False)
    #foreign key from copy_keys class 
    copy_keys_id = Column("copy_keys_id",Integer, ForeignKey('copy_keys.id'), primary_key=True, nullable=False)
    copy_keys_is_loss = Column("copy_keys_is_loss",Boolean, ForeignKey('copy_keys.is_loss'), primary_key=True, nullable=False)
    
    #relationship
    employee = relationship("Employee", back_populates= 'rooms_list')
    room = relationship("Room", back_populates='employees_list')
    key = relationship("CopyKey", back_populates='request')
    returnkey = relationship("Return", back_populates='request')
    lost = relationship("Loss", back_populates='request')

    
    def __init__ (self, request_date: Date, employee,  room, copy_key):
        self.request_date = request_date
        self.employee_id = employee.id
        self.number = room.number
        self.rooms_buildings_name = room.buildings_name
        self.copy_keys_id = copy_key.id
        self.copy_key_is_loss = copy_key.is_loss
        
        
