import json
def save_settings(state):
    with open("settings.json", "w") as f:
        json.dump(state, f)
def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None