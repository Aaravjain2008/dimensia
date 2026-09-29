"""
NEUROVA Platform - SQLite Database Layer
Handles offline local storage for patient intake profiles, schedules, daily logs, and game session results.
"""

import sqlite3
import json
import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "neurova.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Patients table (stores intake data as JSON)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        stage TEXT,
        intake_json TEXT NOT NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    );
    """)

    # Schedules table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedules (
        schedule_id TEXT PRIMARY KEY,
        patient_id TEXT NOT NULL,
        schedule_json TEXT NOT NULL,
        generated_at TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients (patient_id)
    );
    """)

    # Daily outcome logs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity_logs (
        log_id TEXT PRIMARY KEY,
        patient_id TEXT NOT NULL,
        activity_name TEXT NOT NULL,
        category TEXT NOT NULL,
        outcome TEXT NOT NULL,
        notes TEXT,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients (patient_id)
    );
    """)

    # Game sessions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS game_sessions (
        session_id TEXT PRIMARY KEY,
        patient_id TEXT NOT NULL,
        task_id TEXT NOT NULL,
        category TEXT NOT NULL,
        user_response TEXT NOT NULL,
        outcome TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients (patient_id)
    );
    """)

    conn.commit()
    conn.close()


def save_patient(patient_data: Dict[str, Any]) -> str:
    conn = get_connection()
    cursor = conn.cursor()

    patient_id = patient_data.get("patient_id") or str(uuid.uuid4())
    patient_data["patient_id"] = patient_id
    name = patient_data.get("name", "Unnamed Patient")
    stage = patient_data.get("basic_info", {}).get("current_stage", "unknown")
    intake_json = json.dumps(patient_data)
    now = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO patients (patient_id, name, stage, intake_json, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(patient_id) DO UPDATE SET
            name=excluded.name,
            stage=excluded.stage,
            intake_json=excluded.intake_json,
            updated_at=excluded.updated_at;
    """, (patient_id, name, stage, intake_json, now, now))

    conn.commit()
    conn.close()
    return patient_id


def get_patient(patient_id: str) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT intake_json FROM patients WHERE patient_id = ?", (patient_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return json.loads(row["intake_json"])
    return None


def list_patients() -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id, name, stage, updated_at, intake_json FROM patients ORDER BY updated_at DESC")
    rows = cursor.fetchall()
    conn.close()
    results = []
    for r in rows:
        data = json.loads(r["intake_json"])
        data["patient_id"] = r["patient_id"]
        results.append(data)
    return results


def save_schedule(schedule_data: Dict[str, Any]) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    schedule_id = schedule_data.get("schedule_id") or str(uuid.uuid4())
    schedule_data["schedule_id"] = schedule_id
    patient_id = schedule_data.get("patient_id", "")
    schedule_json = json.dumps(schedule_data)
    generated_at = schedule_data.get("generated_at", datetime.now().isoformat())

    cursor.execute("""
        INSERT INTO schedules (schedule_id, patient_id, schedule_json, generated_at)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(schedule_id) DO UPDATE SET schedule_json=excluded.schedule_json;
    """, (schedule_id, patient_id, schedule_json, generated_at))

    conn.commit()
    conn.close()
    return schedule_id


def get_latest_schedule(patient_id: str) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT schedule_json FROM schedules WHERE patient_id = ? ORDER BY generated_at DESC LIMIT 1", (patient_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return json.loads(row["schedule_json"])
    return None


def save_activity_log(log_data: Dict[str, Any]) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    log_id = log_data.get("log_id") or str(uuid.uuid4())
    now = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO activity_logs (log_id, patient_id, activity_name, category, outcome, notes, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        log_id,
        log_data.get("patient_id", ""),
        log_data.get("activity_name", ""),
        log_data.get("category", ""),
        log_data.get("outcome", "completed"),
        log_data.get("notes", ""),
        now
    ))
    conn.commit()
    conn.close()
    return log_id


def get_activity_logs(patient_id: str) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activity_logs WHERE patient_id = ? ORDER BY timestamp DESC", (patient_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def save_game_session(session_data: Dict[str, Any]) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    session_id = session_data.get("session_id") or str(uuid.uuid4())
    now = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO game_sessions (session_id, patient_id, task_id, category, user_response, outcome, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        session_id,
        session_data.get("patient_id", ""),
        session_data.get("task_id", ""),
        session_data.get("category", ""),
        session_data.get("user_response", ""),
        session_data.get("outcome", "completed"),
        now
    ))
    conn.commit()
    conn.close()
    return session_id


# Initialize DB automatically when module is imported
init_db()
