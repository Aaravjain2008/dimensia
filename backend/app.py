"""
NEUROVA Platform - FastAPI Application Server
Provides REST API endpoints for patient intake management, RAG routine schedule generation,
interactive CST game tasks, programmatic guardrail validation, and caregiver outcome logging.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any, Optional
import os

from backend.schemas import (
    PatientIntake,
    GeneratedSchedule,
    GameTask,
    GameSessionResult,
    ActivityLog,
)
from backend.database import (
    save_patient,
    get_patient,
    list_patients,
    save_schedule,
    get_latest_schedule,
    save_activity_log,
    get_activity_logs,
    save_game_session,
)
from backend.schedule_generator import schedule_generator
from backend.game_engine import game_engine
from backend.validator import validator

app = FastAPI(
    title="NEUROVA Platform API",
    description="Offline-first caregiver-assisted platform for dementia routines & CST games",
    version="1.0.0",
)

# Enable CORS for local web development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Health Check Endpoint
# ---------------------------------------------------------------------------
@app.get("/api/health")
def health_check():
    return {
        "status": "online",
        "platform": "NEUROVA Dementia Support System",
        "offline_mode": True,
        "ollama_model": "llama3.2",
        "disclaimer": "[DERIVED] Illustrative support scaffolding requiring clinical review before use."
    }


# ---------------------------------------------------------------------------
# Patient Intake Management Endpoints
# ---------------------------------------------------------------------------
@app.post("/api/patients", response_model=Dict[str, Any])
def create_or_update_patient(intake: PatientIntake):
    intake_dict = intake.model_dump()
    patient_id = save_patient(intake_dict)
    return {"message": "Patient profile saved successfully", "patient_id": patient_id}


@app.get("/api/patients/{patient_id}")
def get_patient_profile(patient_id: str):
    data = get_patient(patient_id)
    if not data:
        raise HTTPException(status_code=404, detail="Patient profile not found")
    return data


@app.get("/api/patients")
def get_all_patients():
    return list_patients()


# ---------------------------------------------------------------------------
# Schedule Generation Endpoint
# ---------------------------------------------------------------------------
@app.post("/api/schedule/generate", response_model=GeneratedSchedule)
def generate_schedule_endpoint(intake: PatientIntake):
    # Save patient profile
    intake_dict = intake.model_dump()
    patient_id = save_patient(intake_dict)
    intake.patient_id = patient_id

    # Generate validated schedule
    generated = schedule_generator.generate_schedule(intake)
    save_schedule(generated.model_dump())

    return generated


@app.get("/api/schedule/latest/{patient_id}")
def get_latest_schedule_endpoint(patient_id: str):
    sched = get_latest_schedule(patient_id)
    if not sched:
        raise HTTPException(status_code=404, detail="No schedule found for patient")
    return sched


# ---------------------------------------------------------------------------
# Adaptive Cognitive Game Endpoints
# ---------------------------------------------------------------------------
@app.post("/api/game/next-task", response_model=GameTask)
def get_next_game_task(intake: PatientIntake, preferred_category: Optional[str] = None):
    return game_engine.get_next_task(intake, preferred_category=preferred_category)


@app.post("/api/game/submit-result", response_model=Dict[str, Any])
def submit_game_result(result: GameSessionResult):
    session_id = save_game_session(result.model_dump())
    return {
        "message": "Game session logged successfully",
        "session_id": session_id,
        "single_session_guardrail": (
            "Note: Performance on a single session is not treated as a signal of clinical change "
            "or cognitive decline (Part 2.5 / Part 6 guardrail)."
        )
    }


# ---------------------------------------------------------------------------
# Daily Activity Outcome Logging Endpoints
# ---------------------------------------------------------------------------
@app.post("/api/logs")
def log_activity_outcome(log: ActivityLog):
    log_id = save_activity_log(log.model_dump())
    return {"message": "Activity outcome logged successfully", "log_id": log_id}


@app.get("/api/logs/{patient_id}")
def get_patient_logs(patient_id: str):
    return get_activity_logs(patient_id)


# ---------------------------------------------------------------------------
# Static File Mounting (Serves Frontend Web App)
# ---------------------------------------------------------------------------
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")
if os.path.exists(FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
