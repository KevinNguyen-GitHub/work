from sqlalchemy import Column, Integer, Identity, Float, String, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from HookLine import HookLine


class DoorType(Base):
    __tablename__ = "door_type"
    name = Column("name", String(100), nullable=False, primary_key=True)
    door = relationship("Door", back_populates="door_type", viewonly=False)

    def __init__(self, name: String):
        self.name = name
