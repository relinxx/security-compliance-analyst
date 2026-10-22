import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

MAX_CHARS = 3000
INJECTION = re.compile(
    r"ignore (all |any )?(previous|prior|above) instructions|disregard (the|your) (rules|instructions)"
    r"|mark (every|all) (rule|requirement)s? as met|system prompt",
    re.I,
)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"\+?\d[\d\s-]{7,}\d")

def check_input(text):
    if len(text.strip()) < 20:
        return "Please describe the use case in at least one sentence."
    if len(text) > MAX_CHARS:
        return f"The use case is too long (max {MAX_CHARS} characters)."
    if INJECTION.search(text):
        return "Blocked: the text contains instructions aimed at the AI (possible prompt injection)."
    return None


def redact(text):
    return PHONE.sub("[PHONE]", EMAIL.sub("[EMAIL]", text))


def audit_log(text, tier, result, review):
    Path("logs").mkdir(exist_ok=True)
    entry = {
        "time": datetime.now(timezone.utc).isoformat(),
        "input_sha256": hashlib.sha256(text.encode()).hexdigest()[:16],
        "risk_tier": tier,
        "statuses": {r.rule_id: r.status for r in result.results},
        "human_review": review,
    }
    with open("logs/audit.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")