import json
from pathlib import Path

REQUIREMENTS = json.loads(Path(__file__).with_name("requirements.json").read_text())

SENSITIVE_TERMS = {
    "personal data": ["customer names", "names", "conversation history", "personal"],
    "financial data": ["account information", "account", "payment", "transaction"],
    "HR / employee data": ["employee", "performance records", "hr information", "promotion"],
    "security data": ["security logs", "security alerts", "threat intelligence"],
}

def get_requirements():
    return REQUIREMENTS


def detect_sensitive_data(text):
    lower = text.lower()
    found = {}
    for category, terms in SENSITIVE_TERMS.items():
        hits = [t for t in terms if t in lower]
        if hits:
            found[category] = hits
    return found


def classify_risk_tier(text, sensitive):
    lower = text.lower()
    reasons = []
    affects_people = "HR / employee data" in sensitive and ("promotion" in lower or "decision" in lower)
    automated = "automatically" in lower or "primary input" in lower
    human_review = "review" in lower
    third_party = "third-party" in lower or "third party" in lower

    if affects_people and automated:
        reasons.append("Automated recommendations drive decisions about people (employment).")
        return "High", reasons
    if sensitive and not human_review:
        reasons.append("Sensitive data is processed without a stated human review step.")
        return "High", reasons
    if sensitive:
        reasons.append("Sensitive data is processed: " + ", ".join(sensitive))
    if third_party:
        reasons.append("Uses a third-party AI service.")
    return ("Medium" if reasons else "Low"), reasons