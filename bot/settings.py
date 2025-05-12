#TELEGRAM_BOT_TOKEN = "8031680167:AAE64rarQhuPQpKQVNUEkMn4gzxmET5_RBM"
import json
with open('secrets.json') as f:
    secrets = json.load(f)

TELEGRAM_BOT_TOKEN = secrets['TELEGRAM_BOT_TOKEN']
TAPO_EMAIL = "shadyali237@gmail.com"
TAPO_PASSWORD = "pyl5302992"
TAPO_IP = "192.168.0.102"
