from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Employee(Base):
    __tablename__ = "employee"
    name = Column("name", String(40), nullable=False)
    employee_id = Column("employee_id", Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True))
    
def _init_(self, name: String):
    self.name = name
