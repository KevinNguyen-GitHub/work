from sqlalchemy import Column, String, Integer, Date, Time, Boolean, Identity, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base


class Return(Base):
    __tablename__ = "returns"
    return_date = Column("loss_date", Date, nullable=False)
    key_requests_request_id = Column(Integer, ForeignKey('key_requests.request_id'), primary_key=True, nullable=False)
    loaned_date = Column('loaned_date', Date, nullable=False)

    requests = relationship("KeyRequests", back_populates="returns")

    def __init__(self, return_date: Date, key_request, loaned_date):
        self.return_date = return_date
        self.key_requests_request_id = key_request.key_requests_request_id
        self.loaned_date = loaned_date

    def __str__(self):
        return str("loaned Date: " + str(self.loaned_date) + "/nRequest ID: " + str(self.key_requests_request_id) +
                   "/nReturn Date: " + str(self.return_date))