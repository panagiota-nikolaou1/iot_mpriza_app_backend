from datetime import datetime
from pydantic import BaseModel


class MeasurementOut(BaseModel):
    row_id: int
    device_id: int
    value: float
    timestamp: datetime

    class Config:
        from_attributes = True  # pydantic v2: επιτρέπει mapping από SQLAlchemy object
