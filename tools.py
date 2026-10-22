import json
from pathlib import Path

REQUIREMENTS = json.loads(Path(__file__).with_name("requirements.json").read_text())

