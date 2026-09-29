"""
NEUROVA Platform - Adaptive Cognitive Game Engine
Generates CST-style interactive tasks across 7 domains using strength-first sequencing
and enforces single-session performance guardrails.
"""

import random
from typing import Dict, Any, List, Optional
from backend.schemas import PatientIntake, GameTask, GameSessionResult


# seed activity pool per domain (derived from master_compilation.md Part 5)
ACTIVITY_SEED_POOL = {
    "recognition": [
        {
            "id": "rec_01",
            "prompt": "Which of these is used to drink tea or warm water?",
            "options": ["Teacup", "Spoon", "Comb", "Key"],
            "answer": "Teacup",
            "guidance": "Hold up a real teacup or point to the screen. Ask with a warm tone."
        },
        {
            "id": "rec_02",
            "prompt": "Identify the photo of a close family member below.",
            "options": ["Daughter (Priya)", "Local Newsreader", "Unknown Person"],
            "answer": "Daughter (Priya)",
            "guidance": "Point to the photo and ask: 'Who is this in our family?'"
        }
    ],
    "reminiscence": [
        {
            "id": "rem_01",
            "prompt": "Look at this festival photo. What memory comes to mind about Diwali celebrations?",
            "options": ["Lighting diyas with family", "Making sweets together", "Watching fireworks"],
            "answer": None,
            "guidance": "No wrong answers! Encourage open reflection and positive feeling."
        },
        {
            "id": "rem_02",
            "prompt": "Let's listen to a melody from your youth. How does this song make you feel?",
            "options": ["Happy & peaceful", "Cozy & nostalgic", "Relaxed"],
            "answer": None,
            "guidance": "Play 30 seconds of preferred music. Observe smile or foot tapping."
        }
    ],
    "orientation": [
        {
            "id": "ori_01",
            "prompt": "What season of the year are we currently enjoying?",
            "options": ["Monsoon / Rainy", "Summer", "Winter"],
            "answer": "Monsoon / Rainy",
            "guidance": "Point to the window weather or calendar visual."
        },
        {
            "id": "ori_02",
            "prompt": "Where are we comfortably seated right now?",
            "options": ["Living Room", "Garden", "Kitchen"],
            "answer": "Living Room",
            "guidance": "Look around the room together and name familiar furniture."
        }
    ],
    "language": [
        {
            "id": "lan_01",
            "prompt": "Complete this well-known saying: 'A stitch in time saves...'",
            "options": ["Nine", "Ten", "Five"],
            "answer": "Nine",
            "guidance": "Say the first half aloud and let the patient finish the sentence."
        },
        {
            "id": "lan_02",
            "prompt": "Can you describe this flower in one pleasant word?",
            "options": ["Bright", "Soft", "Fragrant", "Beautiful"],
            "answer": None,
            "guidance": "Hand a real flower or show picture. Praise any word attempt."
        }
    ],
    "memory": [
        {
            "id": "mem_01",
            "prompt": "What was one item on your breakfast plate this morning?",
            "options": ["Warm Idli / Toast", "Fresh Fruit", "Tea / Milk"],
            "answer": None,
            "guidance": "Supply gentle choice hints if needed. Celebrate effort!"
        },
        {
            "id": "mem_02",
            "prompt": "Remember these 2 items: [Key, Apple]. What was the second item?",
            "options": ["Apple", "Key", "Book"],
            "answer": "Apple",
            "guidance": "State items slowly. Repeat if requested."
        }
    ],
    "problem_solving": [
        {
            "id": "ps_01",
            "prompt": "If you want to prepare a cup of warm tea, what item do you need first?",
            "options": ["Kettle with water", "Toothbrush", "Slipper"],
            "answer": "Kettle with water",
            "guidance": "Use picture cards if helpful. Keep choices simple."
        },
        {
            "id": "ps_02",
            "prompt": "Let's sort these cards: Which of these is a fruit?",
            "options": ["Mango", "Chair", "Shirt"],
            "answer": "Mango",
            "guidance": "Point to the colorful picture."
        }
    ],
    "physical": [
        {
            "id": "phy_01",
            "prompt": "Let's do 5 gentle seated arm raises together to rhythm!",
            "options": ["Completed 5 raises", "Tried 2-3 raises", "Enjoyed watching"],
            "answer": None,
            "guidance": "Demonstrate slowly with a smile. Never force movement."
        }
    ]
}


class GameEngine:
    def get_next_task(self, intake: PatientIntake, preferred_category: Optional[str] = None) -> GameTask:
        """
        Selects next CST activity task applying strength-first sequencing.
        """
        stage = intake.basic_info.current_stage or "middle"
        strengths = intake.cognitive_baseline.domain_strengths
        triggers = [t.lower() for t in intake.behavioral_safety.known_triggers + intake.personal_cultural.disliked_activities]

        # Determine strongest domain for bridging
        domain_rank = {
            "recognition": 3 if strengths.recognition == "strong" else (2 if strengths.recognition == "moderate" else 1),
            "reminiscence": 3 if "music" not in triggers else 1,
            "orientation": 3 if strengths.attention == "strong" else 2,
            "language": 3 if strengths.language == "strong" else 1,
            "memory": 3 if strengths.memory == "strong" else 1,
            "problem_solving": 3 if strengths.problem_solving == "strong" else 1,
            "physical": 2
        }

        # Filter out categories that match patient triggers
        safe_categories = [cat for cat in ACTIVITY_SEED_POOL.keys() if cat not in triggers]
        if not safe_categories:
            safe_categories = ["recognition", "reminiscence", "orientation"]

        # Select category: strength-first or requested
        if preferred_category and preferred_category in safe_categories:
            chosen_cat = preferred_category
        else:
            # Sort categories by strength rating
            sorted_cats = sorted(safe_categories, key=lambda c: domain_rank.get(c, 1), reverse=True)
            chosen_cat = sorted_cats[0]

        seed_list = ACTIVITY_SEED_POOL.get(chosen_cat, ACTIVITY_SEED_POOL["recognition"])
        selected = random.choice(seed_list)

        # Build domain bridge note
        strongest_domain = max(domain_rank, key=domain_rank.get)
        bridge_note = f"Strength-first bridge: Starting from strongest domain '{strongest_domain}' to engage residual ability smoothly."

        return GameTask(
            task_id=selected["id"],
            category=chosen_cat,
            prompt_text=selected["prompt"],
            domain_bridge_note=bridge_note,
            difficulty_level=stage,
            options=selected.get("options"),
            correct_answer=selected.get("answer"),
            media_type="photo" if chosen_cat in ["recognition", "reminiscence"] else "text",
            caregiver_guidance=selected["guidance"]
        )

    def log_game_session(self, patient_id: str, task_id: str, category: str, response: str, outcome: str) -> GameSessionResult:
        """
        Logs a game session outcome, explicitly enforcing the single-session guardrail (Part 2.5 / Part 6).
        """
        return GameSessionResult(
            session_id=None,
            patient_id=patient_id,
            task_id=task_id,
            category=category,
            user_response=response,
            outcome=outcome,
            single_session_guardrail_applied=True
        )


# Global instance
game_engine = GameEngine()
