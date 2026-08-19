from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, get_db, Base
from models import Measurement
from schemas import MeasurementOut

# Δημιουργεί τον πίνακα αν δεν υπάρχει ήδη (ίδιο schema με generate_data.py, μέσω models.py)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="IoT Energy API")


@app.get("/devices/{device_id}/measurements", response_model=List[MeasurementOut])
def get_measurements(device_id: int, db: Session = Depends(get_db)):
    results = (
        db.query(Measurement)
        .filter(Measurement.device_id == device_id)
        .order_by(Measurement.timestamp)
        .all()
    )
    if not results:
        raise HTTPException(status_code=404, detail="Δεν βρέθηκαν μετρήσεις για αυτό το device_id")
    return results
