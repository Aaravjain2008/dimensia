"""
NEUROVA Platform - Data Schemas
Implements patient intake checklist (all 8 sections from patient_info_needed.txt / master_compilation.md Part 7),
routine schedule outputs, game tasks, and daily outcome logging.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Section 1: Basic & Diagnostic Context
# ---------------------------------------------------------------------------
class BasicInfo(BaseModel):
    age: Optional[int] = Field(None, description="Age in years")
    sex: Optional[str] = Field(None, description="Sex or gender identity")
    dementia_type: Optional[str] = Field(
        None, description="Diagnosed dementia type: Alzheimer's, Vascular, Lewy Body, FTD, Mixed, Unknown"
    )
    current_stage: Optional[str] = Field(
        None, description="Stage: early, middle, late, or unknown"
    )
    doctor_notes: Optional[str] = Field(None, description="Doctor notes / functional details")
    comorbidities: List[str] = Field(default_factory=list, description="Diabetes, hypertension, etc.")


# ---------------------------------------------------------------------------
# Section 2: Cognitive & Functional Baseline
# ---------------------------------------------------------------------------
class DomainStrengths(BaseModel):
    memory: str = Field("moderate", description="strong, moderate, weak")
    attention: str = Field("moderate", description="strong, moderate, weak")
    recognition: str = Field("strong", description="strong, moderate, weak")
    language: str = Field("moderate", description="strong, moderate, weak")
    problem_solving: str = Field("weak", description="strong, moderate, weak")


class CognitiveBaseline(BaseModel):
    domain_strengths: DomainStrengths = Field(default_factory=DomainStrengths)
    mmse_moca_score: Optional[str] = Field(None, description="MMSE or MoCA score if available")
    independence_level: str = Field(
        "supervision_needed", description="independent, supervision_needed, fully_dependent"
    )


# ---------------------------------------------------------------------------
# Section 3: Sensory & Physical Constraints
# ---------------------------------------------------------------------------
class SensoryPhysical(BaseModel):
    hearing_status: str = Field("normal", description="normal, needs_loud_slow, hearing_aid")
    vision_status: str = Field("normal", description="normal, needs_large_text, high_contrast")
    mobility_limitations: str = Field("none", description="none, limited_holding, wheelchair, bedbound")
    literacy_level: str = Field("fluent", description="fluent, simple_reading, non_literate")


# ---------------------------------------------------------------------------
# Section 4: Daily Rhythm
# ---------------------------------------------------------------------------
class DailyRhythm(BaseModel):
    wake_time: str = Field("07:00", description="HH:MM format")
    sleep_time: str = Field("21:30", description="HH:MM format")
    nap_habits: str = Field("Afternoon nap 14:00-15:00", description="Nap details")
    meal_times: List[str] = Field(
        default_factory=lambda: ["08:00 (Breakfast)", "13:00 (Lunch)", "20:00 (Dinner)"]
    )
    medication_schedule: List[Dict[str, str]] = Field(
        default_factory=list, description="[{'time': '08:30', 'name': 'Morning Meds'}]"
    )
    sundowning_risk_window: str = Field("16:00-19:00", description="Time window for increased confusion")


# ---------------------------------------------------------------------------
# Section 5: Personal & Cultural Content
# ---------------------------------------------------------------------------
class PersonalCultural(BaseModel):
    family_members: List[str] = Field(default_factory=list, description="Names of close family")
    familiar_places: List[str] = Field(default_factory=list, description="Hometown, landmarks")
    favorite_songs: List[str] = Field(default_factory=list, description="Favorite music/songs")
    favorite_festivals: List[str] = Field(default_factory=list, description="Festivals or holidays")
    favorite_foods: List[str] = Field(default_factory=list, description="Comfort foods")
    preferred_language: str = Field("English", description="Primary language or dialect")
    disliked_activities: List[str] = Field(default_factory=list, description="Activities patient dislikes (e.g. music)")


# ---------------------------------------------------------------------------
# Section 6: Behavioral & Safety Flags
# ---------------------------------------------------------------------------
class BehavioralSafety(BaseModel):
    known_triggers: List[str] = Field(default_factory=list, description="Triggers for agitation or distress")
    wandering_history: bool = Field(False, description="True if history of wandering")
    emergency_contacts: str = Field("", description="Phone numbers/contacts")
    safety_incidents: Optional[str] = Field(None, description="Past falls or safety notes")


# ---------------------------------------------------------------------------
# Section 7: Caregiver Info
# ---------------------------------------------------------------------------
class CaregiverInfo(BaseModel):
    primary_caregiver: str = Field("Family Caregiver", description="Name/relationship")
    available_hours_per_day: Optional[float] = Field(
        1.0, description="Realistic available hours per day (ceiling for routine duration)"
    )
    tech_comfort: str = Field("moderate", description="low, moderate, high")
    perceived_stress_level: str = Field("moderate", description="low, moderate, high")


# ---------------------------------------------------------------------------
# Full Patient Intake Profile (combines Sections 1-7)
# ---------------------------------------------------------------------------
class PatientIntake(BaseModel):
    patient_id: Optional[str] = Field(None, description="Unique patient identifier")
    name: str = Field("Patient Name", description="Full or preferred name")
    basic_info: BasicInfo = Field(default_factory=BasicInfo)
    cognitive_baseline: CognitiveBaseline = Field(default_factory=CognitiveBaseline)
    sensory_physical: SensoryPhysical = Field(default_factory=SensoryPhysical)
    daily_rhythm: DailyRhythm = Field(default_factory=DailyRhythm)
    personal_cultural: PersonalCultural = Field(default_factory=PersonalCultural)
    behavioral_safety: BehavioralSafety = Field(default_factory=BehavioralSafety)
    caregiver_info: CaregiverInfo = Field(default_factory=CaregiverInfo)


# ---------------------------------------------------------------------------
# Section 8: Schedule Output Schemas
# ---------------------------------------------------------------------------
class ScheduleItem(BaseModel):
    step_number: int
    time_or_slot: str
    activity: str
    category: str  # memory, language, orientation, recognition, problem_solving, discussion, reminiscence, physical, meal, rest, medication, safety_check
    duration_minutes: int
    caregiver_note: str


class GeneratedSchedule(BaseModel):
    schedule_id: Optional[str] = None
    patient_id: str
    patient_name: str
    stage_used: str
    total_duration_minutes: int
    caregiver_time_ceiling_minutes: int
    missing_fields_warning: List[str] = Field(default_factory=list)
    items: List[ScheduleItem]
    generated_at: str
    llm_source: str  # 'ollama_llama32' or 'fallback_rule_engine'
    disclaimer: str = (
        "[DERIVED] Routine generated as illustrative support scaffolding. "
        "Requires clinician or experienced caregiver review before use."
    )


# ---------------------------------------------------------------------------
# Activity Outcome Log & Game Schemas
# ---------------------------------------------------------------------------
class ActivityLog(BaseModel):
    log_id: Optional[str] = None
    patient_id: str
    activity_name: str
    category: str
    outcome: str  # 'completed', 'skipped', 'enjoyed', 'agitated'
    notes: Optional[str] = None
    timestamp: str


class GameTask(BaseModel):
    task_id: str
    category: str  # memory, language, orientation, recognition, problem_solving, discussion, reminiscence, physical
    prompt_text: str
    domain_bridge_note: str
    difficulty_level: str  # 'early', 'middle', 'late'
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    media_type: Optional[str] = None
    caregiver_guidance: str


class GameSessionResult(BaseModel):
    session_id: Optional[str] = None
    patient_id: str
    task_id: str
    category: str
    user_response: str
    outcome: str  # 'completed', 'enjoyed', 'agitated', 'skipped'
    single_session_guardrail_applied: bool = True
    timestamp: str
