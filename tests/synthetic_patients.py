"""
NEUROVA Platform - Synthetic Patient Dataset
Contains 7 synthetic test patient scenarios covering various dementia stages,
incomplete data, preference conflicts, distress triggers, caregiver time limits, and sensory constraints.
"""

from backend.schemas import (
    PatientIntake,
    BasicInfo,
    CognitiveBaseline,
    DomainStrengths,
    SensoryPhysical,
    DailyRhythm,
    PersonalCultural,
    BehavioralSafety,
    CaregiverInfo,
)

SYNTHETIC_PATIENTS = [
    # 1. Early-stage, strong memory / weak attention
    PatientIntake(
        patient_id="syn_early_01",
        name="Anand Sharma (Early Stage)",
        basic_info=BasicInfo(
            age=68,
            sex="Male",
            dementia_type="Alzheimer's",
            current_stage="early",
            comorbidities=["Hypertension"]
        ),
        cognitive_baseline=CognitiveBaseline(
            domain_strengths=DomainStrengths(
                memory="strong",
                attention="weak",
                recognition="strong",
                language="strong",
                problem_solving="moderate"
            ),
            independence_level="independent"
        ),
        sensory_physical=SensoryPhysical(hearing_status="normal", vision_status="normal"),
        daily_rhythm=DailyRhythm(wake_time="07:00", sleep_time="22:00", sundowning_risk_window="None"),
        personal_cultural=PersonalCultural(
            family_members=["Sunita (Wife)", "Rohan (Son)"],
            familiar_places=["Guwahati", "Shillong"],
            favorite_songs=["Borgeet melodies", "Classic Oldies"]
        ),
        behavioral_safety=BehavioralSafety(known_triggers=[]),
        caregiver_info=CaregiverInfo(primary_caregiver="Sunita", available_hours_per_day=2.0)
    ),

    # 2. Middle-stage, strong recognition / weak memory, 15-min caregiver limit
    PatientIntake(
        patient_id="syn_middle_tight_02",
        name="Kamla Devi (Middle Stage - 15m limit)",
        basic_info=BasicInfo(
            age=76,
            sex="Female",
            dementia_type="Vascular",
            current_stage="middle",
            comorbidities=["Diabetes"]
        ),
        cognitive_baseline=CognitiveBaseline(
            domain_strengths=DomainStrengths(
                memory="weak",
                attention="weak",
                recognition="strong",
                language="moderate",
                problem_solving="weak"
            ),
            independence_level="supervision_needed"
        ),
        sensory_physical=SensoryPhysical(hearing_status="needs_loud_slow", vision_status="needs_large_text"),
        daily_rhythm=DailyRhythm(wake_time="06:30", sleep_time="21:00", sundowning_risk_window="16:30-19:00"),
        personal_cultural=PersonalCultural(
            family_members=["Rajesh (Son)", "Meera (Daughter-in-law)"],
            favorite_foods=["Khichdi", "Tea"]
        ),
        behavioral_safety=BehavioralSafety(known_triggers=["Loud sudden sounds"]),
        caregiver_info=CaregiverInfo(primary_caregiver="Meera", available_hours_per_day=0.25)  # 15 minutes!
    ),

    # 3. Late-stage, sensory/comfort focus only
    PatientIntake(
        patient_id="syn_late_03",
        name="Biren Roy (Late Stage)",
        basic_info=BasicInfo(
            age=84,
            sex="Male",
            dementia_type="Mixed",
            current_stage="late",
            comorbidities=["Arthritis", "Hypertension"]
        ),
        cognitive_baseline=CognitiveBaseline(
            domain_strengths=DomainStrengths(
                memory="weak",
                attention="weak",
                recognition="weak",
                language="weak",
                problem_solving="weak"
            ),
            independence_level="fully_dependent"
        ),
        sensory_physical=SensoryPhysical(hearing_status="needs_loud_slow", vision_status="normal", mobility_limitations="wheelchair"),
        daily_rhythm=DailyRhythm(wake_time="08:00", sleep_time="20:00", sundowning_risk_window="15:00-18:00"),
        personal_cultural=PersonalCultural(
            family_members=["Anita (Daughter)"],
            favorite_songs=["Soft instrumental flute"]
        ),
        behavioral_safety=BehavioralSafety(known_triggers=["Crowded spaces"]),
        caregiver_info=CaregiverInfo(primary_caregiver="Anita", available_hours_per_day=1.0)
    ),

    # 4. Incomplete intake (Missing stage & missing caregiver availability)
    PatientIntake(
        patient_id="syn_incomplete_04",
        name="Unknown Intake Patient",
        basic_info=BasicInfo(age=72, current_stage=None),  # MISSING STAGE!
        cognitive_baseline=CognitiveBaseline(),
        sensory_physical=SensoryPhysical(),
        daily_rhythm=DailyRhythm(),
        personal_cultural=PersonalCultural(),
        behavioral_safety=BehavioralSafety(),
        caregiver_info=CaregiverInfo(available_hours_per_day=None)  # MISSING TIME LIMIT!
    ),

    # 5. Conflicting preferences (dislikes music)
    PatientIntake(
        patient_id="syn_dislike_music_05",
        name="Pranab Das (Dislikes Music)",
        basic_info=BasicInfo(
            age=71,
            sex="Male",
            dementia_type="Alzheimer's",
            current_stage="middle"
        ),
        cognitive_baseline=CognitiveBaseline(
            domain_strengths=DomainStrengths(recognition="strong", memory="weak")
        ),
        sensory_physical=SensoryPhysical(),
        daily_rhythm=DailyRhythm(),
        personal_cultural=PersonalCultural(
            disliked_activities=["music", "singing", "loud songs"]
        ),
        behavioral_safety=BehavioralSafety(known_triggers=[]),
        caregiver_info=CaregiverInfo(available_hours_per_day=1.0)
    ),

    # 6. Agitation distress trigger for music & physical group exercises
    PatientIntake(
        patient_id="syn_distress_trigger_06",
        name="Maya Sen (Music Distress Trigger)",
        basic_info=BasicInfo(
            age=75,
            sex="Female",
            dementia_type="Lewy Body",
            current_stage="middle"
        ),
        cognitive_baseline=CognitiveBaseline(
            domain_strengths=DomainStrengths(recognition="strong", language="moderate")
        ),
        sensory_physical=SensoryPhysical(),
        daily_rhythm=DailyRhythm(sundowning_risk_window="16:00-18:00"),
        personal_cultural=PersonalCultural(),
        behavioral_safety=BehavioralSafety(
            known_triggers=["music", "group physical", "loud radio"]
        ),
        caregiver_info=CaregiverInfo(available_hours_per_day=1.0)
    ),

    # 7. High sensory & motor constraints (Vision impairment & hand tremor)
    PatientIntake(
        patient_id="syn_sensory_motor_07",
        name="Dipankar Baruah (Vision & Motor Impairment)",
        basic_info=BasicInfo(
            age=80,
            sex="Male",
            dementia_type="Vascular",
            current_stage="middle"
        ),
        cognitive_baseline=CognitiveBaseline(
            domain_strengths=DomainStrengths(recognition="strong", memory="weak")
        ),
        sensory_physical=SensoryPhysical(
            hearing_status="needs_loud_slow",
            vision_status="needs_large_text",
            mobility_limitations="limited_holding"
        ),
        daily_rhythm=DailyRhythm(),
        personal_cultural=PersonalCultural(),
        behavioral_safety=BehavioralSafety(),
        caregiver_info=CaregiverInfo(available_hours_per_day=0.75)
    )
]
