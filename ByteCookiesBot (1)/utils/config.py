import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CRYPTOBOT_TOKEN = os.environ.get("CRYPTOBOT_TOKEN")

ADMIN_ID_STR = os.environ.get("ADMIN_ID")
if ADMIN_ID_STR is None:
    raise ValueError("ADMIN_ID is not set in environment variables.")
try:
    ADMIN_ID = int(ADMIN_ID_STR)
except ValueError:
    raise ValueError("ADMIN_ID must be an integer.")
