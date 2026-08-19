import random
from datetime import datetime, timedelta

from database import SessionLocal, engine, Base
from models import Measurement

Base.metadata.create_all(bind=engine)

db = SessionLocal()
db.query(Measurement).delete()  # καθαρισμός παλιών δεδομένων

base_time = datetime(2026, 8, 18, 17, 0, 0)
device_ids = [1, 2]

for i in range(50):
    m = Measurement(
        device_id=random.choice(device_ids),
        value=round(random.uniform(0.5, 5.2), 2),
        timestamp=base_time + timedelta(minutes=i * 5),
    )
    db.add(m)

db.commit()
db.close()
print("Επιτυχία! Η βάση γέμισε με εικονικές μετρήσεις.")
