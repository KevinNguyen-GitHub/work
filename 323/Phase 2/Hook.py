from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Hook(Base):
    __tablename__ = "hooks"
    id = Column('id', Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True)
    
    def __init__(self, id: Integer):
        self.id = id
