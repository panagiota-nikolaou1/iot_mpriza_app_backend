from sqlalchemy import Column, Integer, Float, DateTime
from database import Base


class Measurement(Base):
    __tablename__ = "measurements"

    # row_id: μοναδικό primary key ανά εγγραφή (όχι το device id!)
    row_id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, nullable=False, index=True)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
