from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class KeyRequest(Base):
    __tablename__ = "key_request"
     employee_id = Column(Integer, ForeignKey("employees.employee_id"), primary_key= True, nullable= False)
    room = Column("room", Integer, nullable=False)
    requestDate = Column("request_date", Date, nullable=False)
    
    def __init__ (self, employee, room: Integer, requestDate: Date):
        self.employee_id = employee.employee_id
        self.room = room
        self.requestDate = requestDate
        
        
