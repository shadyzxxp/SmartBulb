import json
with open('secrets.json') as f:
    secrets = json.load(f)

TELEGRAM_BOT_TOKEN = secrets['TELEGRAM_BOT_TOKEN']
TAPO_EMAIL = "shadyali237@gmail.com"
TAPO_PASSWORD = "pyl5302992"
TAPO_IP = "192.168.0.102"
