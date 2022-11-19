from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Emplyoee(Base):
    __tablename__ = "employee"
    name = Column("name", String(40), nullable=False)
    emplyoeeID = Column('employee_id', Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True)
    
def _init_(self, name: String):
    self.name = name
    #don't really need it, it will still include the id anyway (at least it worked for me on the other sql hw)
    #self.employeeID = employeeID 
