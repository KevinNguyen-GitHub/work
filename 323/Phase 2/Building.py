from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base


class Building(Base):
    __tablename__ = "buildings"
    name = Column("name", String(50), nullable=False, primary_key=True)
    room = relationship("Room", back_populates="buldings")

    def __init__(self, name: String):
        self.name = name
