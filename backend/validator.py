"""
NEUROVA Platform - Programmatic Guardrail & Safety Validator
Enforces medical claim prohibition, caregiver time ceilings, trigger substitution logic,
missing-field fallbacks, and per-patient preference overrides in code (not just prompt).
"""

import re
from typing import Dict, Any, List, Tuple
from backend.schemas import GeneratedSchedule, PatientIntake

# Prohibited medical/therapeutic claim terms (regex list)
PROHIBITED_CLAIM_PATTERNS = [
    r"\btreat(?:s|ing|ment)?\b",
    r"\bcure(?:s|ing)?\b",
    r"\breverse(?:s|ing)?\b",
    r"\bprevent(?:s|ing|ion)?\b",
    r"\bstop(?:s|ping)?\s+dementia\b",
    r"\bslow(?:s|ing)?\s+dementia\b",
    r"\bdisease-modifying\b",
    r"\bclinical(?:ly)?\s+proven\s+cure\b",
    r"\brevers(?:e|ing)\s+cognitive\s+decline\b",
]


class GuardrailValidator:
    def __init__(self):
        self.prohibited_regex = re.compile("|".join(PROHIBITED_CLAIM_PATTERNS), re.IGNORECASE)

    def validate_schedule(
        self, schedule: GeneratedSchedule, patient_intake: PatientIntake
    ) -> Tuple[bool, List[str], GeneratedSchedule]:
        """
        Validates a generated schedule against all standing guardrails.
        Returns: (is_valid, list_of_violations, cleaned_schedule)
        """
        violations = []
        cleaned_schedule = schedule.model_copy(deep=True)

        # -------------------------------------------------------------------
        # Guardrail 1: Medical Claim Filter
        # -------------------------------------------------------------------
        full_text = f"{schedule.patient_name} {schedule.stage_used} " + " ".join(
            [f"{item.activity} {item.caregiver_note}" for item in schedule.items]
        )
        found_claims = self.prohibited_regex.findall(full_text)
        if found_claims:
            violations.append(
                f"MEDICAL CLAIM VIOLATION: Output contains prohibited claim terms: {set(found_claims)}"
            )

        # -------------------------------------------------------------------
        # Guardrail 2: Caregiver Time Ceiling Check
        # -------------------------------------------------------------------
        total_activity_minutes = sum(item.duration_minutes for item in schedule.items)
        caregiver_hours = patient_intake.caregiver_info.available_hours_per_day or 1.0
        time_ceiling_minutes = int(caregiver_hours * 60)

        cleaned_schedule.total_duration_minutes = total_activity_minutes
        cleaned_schedule.caregiver_time_ceiling_minutes = time_ceiling_minutes

        if total_activity_minutes > time_ceiling_minutes:
            violations.append(
                f"CAREGIVER TIME CEILING VIOLATION: Total activity time ({total_activity_minutes} min) "
                f"exceeds caregiver ceiling ({time_ceiling_minutes} min)."
            )
            # Automatic programmatic fix: truncate/adjust schedule items to respect ceiling
            pruned_items = []
            accumulated = 0
            for item in cleaned_schedule.items:
                if accumulated + item.duration_minutes <= time_ceiling_minutes:
                    pruned_items.append(item)
                    accumulated += item.duration_minutes
                else:
                    remaining = time_ceiling_minutes - accumulated
                    if remaining >= 5:
                        item.duration_minutes = remaining
                        pruned_items.append(item)
                        accumulated += remaining
                    break
            cleaned_schedule.items = pruned_items
            cleaned_schedule.total_duration_minutes = accumulated

        # -------------------------------------------------------------------
        # Guardrail 3: Trigger & Disliked Activity Substitution Check
        # -------------------------------------------------------------------
        known_triggers = [t.lower() for t in patient_intake.behavioral_safety.known_triggers]
        dislikes = [d.lower() for d in patient_intake.personal_cultural.disliked_activities]
        all_restricted = set(known_triggers + dislikes)

        flagged_items = []
        for item in cleaned_schedule.items:
            item_text = f"{item.activity} {item.category} {item.caregiver_note}".lower()
            for r in all_restricted:
                if r and r in item_text:
                    flagged_items.append((item.step_number, r))

        if flagged_items:
            violations.append(
                f"TRIGGER VIOLATION: Schedule contains restricted/disliked items: {flagged_items}"
            )
            # Automatic programmatic fix: substitute flagged items with safe alternatives
            for step_num, trigger_term in flagged_items:
                for item in cleaned_schedule.items:
                    if item.step_number == step_num:
                        item.category = "reminiscence" if "music" in trigger_term else "orientation"
                        item.activity = "Gentle photo review and quiet conversation"
                        item.caregiver_note = f"[SUBSTITUTED] Replaced '{trigger_term}' with quiet photo review."

        # -------------------------------------------------------------------
        # Guardrail 4: Incomplete Intake Fallback Check
        # -------------------------------------------------------------------
        missing_fields = self.detect_missing_fields(patient_intake)
        cleaned_schedule.missing_fields_warning = missing_fields
        if missing_fields:
            if schedule.stage_used != "middle":
                violations.append(
                    f"FALLBACK VIOLATION: Incomplete intake missing {missing_fields} did not default to 'middle' stage priorities."
                )
                cleaned_schedule.stage_used = "middle"

        is_valid = len(violations) == 0
        return is_valid, violations, cleaned_schedule

    def detect_missing_fields(self, patient_intake: PatientIntake) -> List[str]:
        """
        Detects missing essential intake fields to trigger conservative fallback.
        """
        missing = []
        if not patient_intake.basic_info.current_stage:
            missing.append("current_stage")
        if patient_intake.caregiver_info.available_hours_per_day is None:
            missing.append("caregiver_available_hours")
        if not patient_intake.behavioral_safety.known_triggers and patient_intake.behavioral_safety.known_triggers is None:
            missing.append("known_triggers")
        return missing


# Global instance
validator = GuardrailValidator()
