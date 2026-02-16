import json
from pathlib import Path

PROFILE_PATH = Path("user_profile.json")


def save_profile(user_prefs):
    with open(PROFILE_PATH, "w") as f:
        json.dump(user_prefs, f, indent=2)


def load_profile():
    if PROFILE_PATH.exists():
        with open(PROFILE_PATH) as f:
            return json.load(f)
    return None
