import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Μέσα σε container: host="db" (όνομα service στο compose network)
# Εκτός container (π.χ. τρέχεις local): host="localhost"
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:password@db:5432/iot_database",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
