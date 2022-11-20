from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint
from sqlalchemy.orm import relationship

from orm_base import Base
from HookLine import HookLine

class DoorType(Base):
    __tablebname__ = "door_type"
    name = Column('name', String(100), primary_key= True, nullable=False)
    door = relationship("Door")

    def __init__(self, name: String):
        self.name = name


