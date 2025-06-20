import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Dict


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

@dataclass
class ClickUpAPIClient:
    api_key: str
    base_url: str = 'https://api.clickup.com/api/v2'

    @property
    def auth_headers(self) -> Dict[str, str]:
        return {
            "Authorization": self.api_key,
            "Accept": "application/json"
        }

    @property
    def auth_headers_upd(self) -> Dict[str, str]:
        return {
            **self.auth_headers,
            "Content-type":"application/json"
        }

config = ClickUpAPIClient(api_key=CLICKUP_API_KEY)

AUTH_HEADERS = config.auth_headers
AUTH_HEADERS_UPD = config.auth_headers_upd
BASE_URL = config.base_url

