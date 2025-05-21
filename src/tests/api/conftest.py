import pytest
import requests
from faker import Faker
from requests import post, delete

from src.utils.helpers import CLICKUP_API_KEY, CLICKUP_EMAIL, CLICKUP_PASSWORD, BASE_URL, AUTH_HEADERS, LIST_ID

fake = Faker()

@pytest.fixture
def data_task():
    return {
            "name": fake.file_name(),
            "description": fake.sentence(nb_words=10),
            "priority": fake.random_int(min=1, max=4)
        }

@pytest.fixture
def task_id(data_task):
    response = post(f"{BASE_URL}/v2/list/{LIST_ID}/task", headers=AUTH_HEADERS, json=data_task)
    assert response.status_code in (200, 201), f"Item creation failed: {response.text}"

    task_id = response.json().get("id")
    assert task_id, "Task ID not found in response"

    yield task_id

    delete(f"{BASE_URL}/api/v1/items/{task_id}")


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    response = session.post(f"{BASE_URL}/v2/oauth/token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"

    token = response.json().get("access_token")
    assert token, "No access_token found"

    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session