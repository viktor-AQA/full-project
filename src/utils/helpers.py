import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable '{name}' is not set")
    return value

def helpers():
    return None


CLICKUP_API_KEY = get_env_variable("CLICKUP_API_KEY")
CLICKUP_EMAIL = get_env_variable("CLICKUP_EMAIL")
CLICKUP_PASSWORD = get_env_variable("CLICKUP_PASSWORD")
LIST_ID = get_env_variable("LIST_ID")

BASE_URL = 'https://api.clickup.com/api'

AUTH_HEADERS = {
    "Authorization": "CLICKUP_API_KEY",
    "Accept": "application/json"
}

