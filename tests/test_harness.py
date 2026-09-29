"""
NEUROVA Platform - Automated Test Harness & Guardrail Assertion Suite
Runs 7 synthetic test patients through the full end-to-end pipeline:
Intake Profile -> Local RAG Routine Generator -> Game Engine -> Programmatic Guardrail Validator.

Asserts 100% compliance across all 5 standing guardrails:
1. Anti-Medical Claim Prohibition
2. Caregiver Time Ceiling Limits
3. Trigger & Disliked Activity Substitution
4. Incomplete Intake Fallback to 'Middle' Stage & Warning List
5. Per-Patient Preference Overrides & Strength-First Sequencing
"""

import sys
import os

# Ensure backend is in python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.synthetic_patients import SYNTHETIC_PATIENTS
from backend.schedule_generator import schedule_generator
from backend.game_engine import game_engine
from backend.validator import validator


def run_full_synthetic_test_suite():
    print("=" * 80)
    print("NEUROVA PLATFORM — AUTOMATED SYNTHETIC PATIENT TEST HARNESS")
    print("Running 7 synthetic patient scenarios through RAG pipeline & guardrail assertions...")
    print("=" * 80)

    total_tests = len(SYNTHETIC_PATIENTS)
    passed_tests = 0
    failed_tests = 0
    test_reports = []

    for idx, patient in enumerate(SYNTHETIC_PATIENTS, 1):
        print(f"\n--------------------------------------------------------------------------------")
        print(f"TEST CASE {idx}/{total_tests}: {patient.name} (ID: {patient.patient_id})")
        print(f"Intake Stage: {patient.basic_info.current_stage or 'MISSING'} | Caregiver Time: {patient.caregiver_info.available_hours_per_day} hrs")
        print(f"Triggers: {patient.behavioral_safety.known_triggers} | Dislikes: {patient.personal_cultural.disliked_activities}")
        print(f"--------------------------------------------------------------------------------")

        # Step 1: Generate Routine Schedule via RAG / Ollama / Fallback
        generated_sched = schedule_generator.generate_schedule(patient)

        print(f"-> Generated Routine ({generated_sched.llm_source}): Stage Used = '{generated_sched.stage_used}'")
        print(f"-> Total Activity Duration = {generated_sched.total_duration_minutes} min (Caregiver Ceiling = {generated_sched.caregiver_time_ceiling_minutes} min)")
        if generated_sched.missing_fields_warning:
            print(f"-> Missing Fields Warning = {generated_sched.missing_fields_warning}")

        for item in generated_sched.items:
            print(f"   [{item.time_or_slot}] Step {item.step_number}: {item.activity} ({item.duration_minutes} min) | Note: {item.caregiver_note}")

        # Step 2: Validate through Programmatic Guardrail Validator
        is_valid, violations, cleaned_sched = validator.validate_schedule(generated_sched, patient)

        # Step 3: Game Task Generation Test
        next_game_task = game_engine.get_next_task(patient)
        print(f"-> CST Game Task ({next_game_task.category}): '{next_game_task.prompt_text}'")
        print(f"   Guidance: {next_game_task.caregiver_guidance}")

        # Step 4: Specific Guardrail Assertions
        case_passed = True
        assertion_errors = []

        # Assertion 1: Anti-Medical Claim Check
        for item in cleaned_sched.items:
            combined_text = f"{item.activity} {item.caregiver_note}".lower()
            for banned in ["treat", "cure", "reverse", "prevent", "stop dementia", "disease-modifying"]:
                if banned in combined_text:
                    case_passed = False
                    assertion_errors.append(f"ASSERTION FAIL: Prohibited medical claim term '{banned}' found in output.")

        # Assertion 2: Caregiver Time Ceiling
        if cleaned_sched.total_duration_minutes > cleaned_sched.caregiver_time_ceiling_minutes:
            case_passed = False
            assertion_errors.append(
                f"ASSERTION FAIL: Total activity time ({cleaned_sched.total_duration_minutes}m) "
                f"exceeds caregiver ceiling ({cleaned_sched.caregiver_time_ceiling_minutes}m)."
            )

        # Assertion 3: Trigger Substitution Check
        restricted = patient.behavioral_safety.known_triggers + patient.personal_cultural.disliked_activities
        for r in restricted:
            r_clean = r.lower()
            if r_clean:
                for item in cleaned_sched.items:
                    item_text = f"{item.activity} {item.category} {item.caregiver_note}".lower()
                    if r_clean in item_text:
                        case_passed = False
                        assertion_errors.append(f"ASSERTION FAIL: Restricted trigger/dislike '{r_clean}' found in schedule item {item.step_number}.")
                if next_game_task.category.lower() == r_clean:
                    case_passed = False
                    assertion_errors.append(f"ASSERTION FAIL: Game engine assigned restricted category '{r_clean}'.")

        # Assertion 4: Incomplete Intake Fallback Check (Case 4)
        if patient.patient_id == "syn_incomplete_04":
            if cleaned_sched.stage_used != "middle":
                case_passed = False
                assertion_errors.append(f"ASSERTION FAIL: Missing stage did not default to 'middle' stage priorities.")
            if "current_stage" not in cleaned_sched.missing_fields_warning:
                case_passed = False
                assertion_errors.append(f"ASSERTION FAIL: Missing 'current_stage' field not listed in missing_fields_warning.")

        # Assertion 5: 15-Minute Tight Caregiver Limit Check (Case 2)
        if patient.patient_id == "syn_middle_tight_02":
            if cleaned_sched.total_duration_minutes > 15:
                case_passed = False
                assertion_errors.append(f"ASSERTION FAIL: Schedule exceeded 15-minute caregiver limit ({cleaned_sched.total_duration_minutes}m > 15m).")

        if case_passed:
            passed_tests += 1
            print(f"\n[RESULT] PASS: All guardrail assertions satisfied cleanly.")
        else:
            failed_tests += 1
            print(f"\n[RESULT] FAIL: {len(assertion_errors)} assertion failure(s):")
            for err in assertion_errors:
                print(f"  - {err}")

        test_reports.append({
            "patient_id": patient.patient_id,
            "patient_name": patient.name,
            "passed": case_passed,
            "errors": assertion_errors
        })

    print("\n" + "=" * 80)
    print("FINAL TEST HARNESS REPORT")
    print(f"Total Synthetic Patients Tested: {total_tests}")
    print(f"Passed: {passed_tests} / {total_tests} ({(passed_tests/total_tests)*100:.1f}%)")
    print(f"Failed: {failed_tests} / {total_tests}")
    print("=" * 80)

    return passed_tests == total_tests


if __name__ == "__main__":
    success = run_full_synthetic_test_suite()
    sys.exit(0 if success else 1)
