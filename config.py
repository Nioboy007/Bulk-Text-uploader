import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6916875347:AAEVxR4cO_sIBB6V57ANA92pHKxzw9G3yX0")
    API_ID = int(os.environ.get("API_ID", 10471716))
    API_HASH = os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6883997969")
