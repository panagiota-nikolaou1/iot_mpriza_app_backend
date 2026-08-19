# IoT energy monitoring system - Backend

This repository contains the backend REST API for the IoT energy monitoring system. 

## Architecture & Tech Stack
- **Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Containerization:** Docker & Docker Compose

## Overview
The API serves as the central data hub, exposing endpoints to retrieve chronological energy consumption measurements for smart devices (plugs). The entire environment is containerized for seamless deployment.

## How to Run

Make sure you have Docker and Docker Compose installed on your system. To build and start the database and the API services, run:

docker compose up --build

Once the containers are running, you can access the interactive API documentation (Swagger UI) generated automatically by FastAPI at:
http://localhost:8000/docs
