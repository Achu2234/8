import os

admins = {}
API_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")
ADMIN = os.getenv("ADMIN")
DB_URL = os.getenv("DB_URL")
DB_NAME = os.getenv("DB_NAME")
SUDO_USERS = os.environ.get("SUDO_USERS", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
COMMAND_PREFIXES = os.environ.get("COMMAND_PREFIXES", "")
