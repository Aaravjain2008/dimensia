"""
NEUROVA Platform - Schedule & Routine Generator
Powers local RAG-grounded daily routine generation via Ollama (llama3.2).
Includes a deterministic fallback rule engine for offline reliability and feeds output into the guardrail validator.
"""

import json
import urllib.request
import urllib.error
from datetime import datetime
from typing import Dict, Any, List, Optional

from backend.schemas import PatientIntake, GeneratedSchedule, ScheduleItem
from backend.rag_engine import rag_engine
from backend.validator import validator

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


SYSTEM_PROMPT_CONTRACT = """You are a dementia-support routine generator. You produce structured daily or session routines that support residual abilities, reduce distress, and stay sustainable for caregivers. You never diagnose, treat, cure, or claim to reverse dementia.

=== CORE DECISION TABLE ===
Early: Independence-preserving scaffolding, habit formation, mild challenge + novelty, external aids.
Middle: Safety structure, calming pacing, short cognitive windows early in day, clear transitions, reduced choice.
Late: Comfort, sensory and relational presence, reduce distress, familiar sensory input.

=== STRENGTH-FIRST SEQUENCING ===
Always begin with the person's strongest remaining domain and use it as a bridge into weaker domains.

=== STANDING HARD RULES ===
- Per-patient intake data always overrides generic defaults.
- If intake is incomplete (e.g. stage unknown), default to conservative 'middle' stage priorities, and list missing fields.
- Never claim to treat, cure, reverse, or stop dementia.
- Keep total activity duration strictly within caregiver available time limit.
- If intake notes any trigger or distress history, do NOT include that activity type; substitute a safe alternative.
- Output ONLY valid JSON matching the requested schema.
"""


class ScheduleGenerator:
    def __init__(self):
        self.ollama_url = OLLAMA_URL
        self.model = MODEL_NAME

    def generate_schedule(self, intake: PatientIntake) -> GeneratedSchedule:
        """
        Generates a personalized daily routine schedule using local Ollama RAG,
        validated by programmatic guardrails.
        """
        intake_dict = intake.model_dump()
        stage = intake.basic_info.current_stage or "middle"
        missing_fields = validator.detect_missing_fields(intake)

        # Retrieve RAG context
        rag_context = rag_engine.get_grounding_context(intake_dict)

        # Try generating via Ollama llama3.2
        raw_schedule = self._call_ollama(intake, rag_context, missing_fields)
        llm_source = "ollama_llama32"

        if not raw_schedule:
            # Fallback to rule-based routine synthesis if Ollama call unavailable or returned invalid output
            raw_schedule = self._generate_fallback(intake, missing_fields)
            llm_source = "fallback_rule_engine"

        raw_schedule.llm_source = llm_source

        # Run programmatic validator
        is_valid, violations, validated_schedule = validator.validate_schedule(raw_schedule, intake)

        return validated_schedule

    def _call_ollama(
        self, intake: PatientIntake, rag_context: str, missing_fields: List[str]
    ) -> Optional[GeneratedSchedule]:
        caregiver_hours = intake.caregiver_info.available_hours_per_day or 1.0
        ceiling_minutes = int(caregiver_hours * 60)
        stage = intake.basic_info.current_stage or "middle"

        user_prompt = f"""
{SYSTEM_PROMPT_CONTRACT}

{rag_context}

=== PATIENT INTAKE PROFILE ===
Name: {intake.name}
Stage: {stage} (Missing fields: {missing_fields})
Caregiver Available Time Limit: {ceiling_minutes} minutes
Strengths: {intake.cognitive_baseline.domain_strengths.model_dump()}
Restricted/Disliked Triggers: {intake.behavioral_safety.known_triggers + intake.personal_cultural.disliked_activities}
Daily Rhythm: Wake {intake.daily_rhythm.wake_time}, Sleep {intake.daily_rhythm.sleep_time}, Sundowning Risk {intake.daily_rhythm.sundowning_risk_window}

Output a JSON object with this exact structure:
{{
  "patient_id": "{intake.patient_id or 'p1'}",
  "patient_name": "{intake.name}",
  "stage_used": "{stage}",
  "total_duration_minutes": 0,
  "caregiver_time_ceiling_minutes": {ceiling_minutes},
  "missing_fields_warning": {json.dumps(missing_fields)},
  "items": [
    {{
      "step_number": 1,
      "time_or_slot": "09:00 AM",
      "activity": "Activity title description",
      "category": "recognition",
      "duration_minutes": 15,
      "caregiver_note": "Caregiver guidance note"
    }}
  ]
}}
Ensure the sum of duration_minutes is <= {ceiling_minutes} minutes. Respond ONLY with valid JSON.
"""

        payload = {
            "model": self.model,
            "prompt": user_prompt,
            "stream": False,
            "format": "json"
        }

        try:
            req = urllib.request.Request(
                self.ollama_url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=25) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                response_text = result.get("response", "")
                parsed = json.loads(response_text)

                items = [ScheduleItem(**item) for item in parsed.get("items", [])]
                total_min = sum(i.duration_minutes for i in items)

                return GeneratedSchedule(
                    schedule_id=None,
                    patient_id=intake.patient_id or "p1",
                    patient_name=intake.name,
                    stage_used=parsed.get("stage_used", stage),
                    total_duration_minutes=total_min,
                    caregiver_time_ceiling_minutes=ceiling_minutes,
                    missing_fields_warning=parsed.get("missing_fields_warning", missing_fields),
                    items=items,
                    generated_at=datetime.now().isoformat(),
                    llm_source="ollama_llama32"
                )
        except Exception as e:
            # Fallback will handle failure
            return None

    def _generate_fallback(self, intake: PatientIntake, missing_fields: List[str]) -> GeneratedSchedule:
        """
        Deterministic rule-based schedule synthesis grounded in master_compilation.md Parts 3 & 4.
        """
        stage = intake.basic_info.current_stage or "middle"
        if not intake.basic_info.current_stage:
            stage = "middle"  # Conservative fallback

        caregiver_hours = intake.caregiver_info.available_hours_per_day or 1.0
        ceiling_minutes = int(caregiver_hours * 60)

        strengths = intake.cognitive_baseline.domain_strengths
        triggers = [t.lower() for t in intake.behavioral_safety.known_triggers + intake.personal_cultural.disliked_activities]

        items: List[ScheduleItem] = []

        if stage == "early":
            # Worked Example A pattern: Memory lead -> Attention bridge -> Light physical/orientation -> Independence close
            items.append(ScheduleItem(
                step_number=1,
                time_or_slot="09:00 AM",
                activity="Morning memory warm-up with photo cue",
                category="memory",
                duration_minutes=10,
                caregiver_note="Ask patient to share two things done this morning. Supply gentle cues."
            ))
            if "music" not in triggers:
                items.append(ScheduleItem(
                    step_number=2,
                    time_or_slot="10:30 AM",
                    activity="Attention & naming exercise with familiar music",
                    category="language",
                    duration_minutes=15,
                    caregiver_note="Play favorite song, ask patient to complete familiar lyrics."
                ))
            else:
                items.append(ScheduleItem(
                    step_number=2,
                    time_or_slot="10:30 AM",
                    activity="Attention & photo sorting exercise",
                    category="recognition",
                    duration_minutes=15,
                    caregiver_note="Match faces of family members to their names on photo cards."
                ))
            items.append(ScheduleItem(
                step_number=3,
                time_or_slot="11:30 AM",
                activity="Light physical walk and calendar orientation",
                category="orientation",
                duration_minutes=15,
                caregiver_note="Walk to calendar together, note current day, season, and weather."
            ))

        elif stage == "late":
            # Worked Example C pattern: Comfort, sensory & relational presence
            items.append(ScheduleItem(
                step_number=1,
                time_or_slot="10:00 AM",
                activity="Gentle sensory texture and quiet presence",
                category="reminiscence",
                duration_minutes=10,
                caregiver_note="Place preferred soft blanket in hands. Sit at eye level with gentle touch."
            ))
            if "music" not in triggers:
                items.append(ScheduleItem(
                    step_number=2,
                    time_or_slot="15:00 PM",
                    activity="Low-volume familiar music relaxation",
                    category="reminiscence",
                    duration_minutes=10,
                    caregiver_note="Play soft preferred melody in quiet room. Watch for settling or fatigue."
                ))
            else:
                items.append(ScheduleItem(
                    step_number=2,
                    time_or_slot="15:00 PM",
                    activity="Calm visual bird watching / garden viewing",
                    category="reminiscence",
                    duration_minutes=10,
                    caregiver_note="Sit together by window looking at green plants or birds. Minimal speech."
                ))

        else:  # Middle stage (default)
            # Worked Example B pattern: Recognition lead -> Reminiscence bridge -> Physical movement -> Safety close
            items.append(ScheduleItem(
                step_number=1,
                time_or_slot="09:30 AM",
                activity="Recognition lead with family photo album",
                category="recognition",
                duration_minutes=15,
                caregiver_note="Look at 4-5 large photos of family or familiar places. Encourage pointing."
            ))
            if "music" not in triggers:
                items.append(ScheduleItem(
                    step_number=2,
                    time_or_slot="11:00 AM",
                    activity="Reminiscence song & seated rhythmic movement",
                    category="physical",
                    duration_minutes=15,
                    caregiver_note="Listen to one familiar track from youth. Seated arm raises or clapping."
                ))
            else:
                items.append(ScheduleItem(
                    step_number=2,
                    time_or_slot="11:00 AM",
                    activity="Tactile object sorting & quiet reminiscence",
                    category="problem_solving",
                    duration_minutes=15,
                    caregiver_note="Sort familiar household items (e.g. tea cups or colorful fabrics). Concrete verbal cues."
                ))
            items.append(ScheduleItem(
                step_number=3,
                time_or_slot="16:00 PM (Pre-sundowning)",
                activity="Calm environment check-in & orientation cue",
                category="orientation",
                duration_minutes=10,
                caregiver_note="Ensure room is well-lit, door locked, fresh water available, bathroom sign visible."
            ))

        # Respect caregiver time ceiling
        accumulated = 0
        pruned_items = []
        for item in items:
            if accumulated + item.duration_minutes <= ceiling_minutes:
                pruned_items.append(item)
                accumulated += item.duration_minutes
            else:
                remaining = ceiling_minutes - accumulated
                if remaining >= 5:
                    item.duration_minutes = remaining
                    pruned_items.append(item)
                    accumulated += remaining
                break

        return GeneratedSchedule(
            schedule_id=None,
            patient_id=intake.patient_id or "p1",
            patient_name=intake.name,
            stage_used=stage,
            total_duration_minutes=accumulated,
            caregiver_time_ceiling_minutes=ceiling_minutes,
            missing_fields_warning=missing_fields,
            items=pruned_items,
            generated_at=datetime.now().isoformat(),
            llm_source="fallback_rule_engine"
        )


# Global instance
schedule_generator = ScheduleGenerator()
