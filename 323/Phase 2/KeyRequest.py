from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base


class KeyRequest(Base):
    __tablename__ = "key_requests"
    request_date = Column("request_date", Date, nullable=False)
    #foreign key from employee class
    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True, nullable=False)
    #foreign key from room class
    rooms_num = Column(Integer, ForeignKey('rooms.num'), primary_key=True, nullable=False)
    rooms_buildings_name = Column(Integer, ForeignKey('rooms.buildings_name'), primary_key=True, nullable=False)
    #foreign key from copy_keys class 
    copy_keys_id = Column(Integer, ForeignKey('copy_keys.id'), primary_key=True, nullable=False)
    copy_keys_is_loss = Column(Boolean, ForeignKey('copy_keys.is_loss'), primary_key=True, nullable=False)
    
    #relationship
    
    def __init__ (self, request_date: Date, employee, room, room, copy_key, copy_key):
        self.request_date = request_date
        self.employee_id = employee.employee_id
        self.rooms_num = room.rooms_num
        self.rooms_buildings_name = room.rooms_buildings_name 
        self.copy_keys_id = copy_key.copy_keys_id 
        self.copy_key_is_loss = copy_key.copy_keys_iss_loss
        
        
