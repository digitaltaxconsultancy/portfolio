# helpers.py
# Utility functions for end message detection and candidate summary formatting
import json
import os

DATA_FILE = "data/candidates.json"

def save_candidate_data(candidate_data):
    """
    Save anonymized candidate data locally (simulated backend).
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    # 🧩 Anonymize data (no personal info stored)
    anonymized_data = {
        "candidate_id": hash(candidate_data.get("email", "")),
        "experience": candidate_data.get("experience"),
        "tech_stack": candidate_data.get("tech_stack"),
        "responses": candidate_data.get("responses", []),
    }

    # 🧾 Load existing data
    try:
        with open(DATA_FILE, "r") as f:
            all_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        all_data = []

    # ➕ Append new record
    all_data.append(anonymized_data)

    # 💾 Save back
    with open(DATA_FILE, "w") as f:
        json.dump(all_data, f, indent=4)


# List of keywords to detect conversation end
END_KEYWORDS = ["exit", "quit", "bye", "goodbye", "thanks", "thank you", "stop"]


def is_end_message(text: str) -> bool:
    """
    Check if user message contains a conversation-ending keyword.
    Example:
        is_end_message("thanks, bye") -> True
    """
    if not text:
        return False
    t = text.strip().lower()
    for k in END_KEYWORDS:
        if k == t or k in t:
            return True
    return False


def format_candidate_summary(candidate: dict) -> str:
    """
    Format candidate details for display or export.
    Example:
        format_candidate_summary({
            'name': 'John Doe',
            'email': 'john@example.com',
            'years': 5,
            'positions': ['Backend Developer']
        })
    """
    if not candidate:
        return "No candidate data available."

    lines = []
    lines.append(f"Name: {candidate.get('name', '')}")
    lines.append(f"Email: {candidate.get('email', '')}")
    lines.append(f"Phone: {candidate.get('phone', '')}")
    lines.append(f"Years of experience: {candidate.get('years', '')}")
    lines.append(f"Desired positions: {', '.join(candidate.get('positions', []))}")
    lines.append(f"Location: {candidate.get('location', '')}")
    lines.append("Tech stack (raw):")
    lines.append(candidate.get('tech_stack_raw', ''))

    return "\n".join(lines)
