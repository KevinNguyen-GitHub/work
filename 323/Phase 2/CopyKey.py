from sqlalchemy import Column, String, Integer, Date, Time, Boolean, Identity, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base


class CopyKey(Base):
    __tablename__ = "copy_keys"
    id = Column('id', Integer, Identity(start=1, cycle=True),
                nullable=False, primary_key=True)
    issuedDate = Column("issued_date", Date, nullable=False)
    issuedTime = Column("issued_time", Time, nullable=False)
    hooks_id = Column(Integer, ForeignKey('hooks.id'), nullable=False)
    is_loss = Column("is_loss", Boolean, nullable=False, primary_key=True)

    def __init__(self, issuedDate: Date, issuedTime: Time, hooks_id: Integer, is_loss: Boolean):
        self.id = id
        self.issuedDate = issuedDate
        self.issuedTime = issuedTime
        self.hooks_id = hooks_id
        self.is_loss = is_loss
