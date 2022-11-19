from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class Return(Base):
    __tablename__ = "returns"
    report_date = Column("report_date", Date, primary_key=True, nullable=False)
    key_requests_employees_id = Column(Integer, ForeignKey('key_requests.employees_id'), primary_key=True, nullable=False)
    key_requests_rooms_num = Column(Integer, ForeignKey('key_requests.rooms_num'), primary_key=True, nullable=False)
    key_requests_copy_keys_id = Column(Integer, ForeignKey('key_requests.copy_keys_id'), primary_key=True, nullable=False)
    key_requests_copy_keys_is_loss = Column(Integer, ForeignKey('key_requests.copy_keys_is_loss'), primary_key=True, nullable=False)
    
    def __init__(self, report_date: Date, key_request, key_request, key_request, key_request):
        self.report_date = report_date
        self.key_requests_employees_id = key_request.key_requests_employees_id
        self.key_requests_rooms_num = key_request.key_requests_rooms_num
        self.key_requests_copy_keys_id = key_request.key_requests_copy_keys_id
        self.key_requests_copy_keys_is_loss = key_request.key_requests_copy_keys_is_loss
