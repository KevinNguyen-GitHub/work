from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Return(Base):
    __tablename__ = "return"
    return_date = Column("loss_date", Date, nullable=False)
    key_requests_request_id = Column(Integer, ForeignKey('key_requests.request_id'), primary_key=True, nullable=False)
    loaned_date = Column('loaned_date', Date, nullable=False)
    
    def __init__(self, return_date: Date, key_request, loaned_date):
        self.return_date = return_date
        self.key_requests_request_id = key_request.key_requests_request_id
        self.loaned_date = loaned_date 
