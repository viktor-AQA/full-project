import pytest
import requests
from faker import Faker
from pydantic import BaseModel

from src.utils.helpers import BASE_URL, AUTH_HEADERS


@pytest.fixture
def auth_session():
    session = requests.Session()
    session.headers.update(AUTH_HEADERS)
    return session

fake = Faker()

class DataTask(BaseModel):
    name: str
    description: str
    priority: int

    @classmethod
    def generate(cls):
        return cls(
            name=fake.name(),
            description=fake.sentence(nb_words=10),
            priority=fake.random_int(min=1, max=4)
        )

@pytest.fixture
def data_task():
    return DataTask.generate().model_dump()

class UpdDataTask(BaseModel):
    name: str
    description: str
    priority: int

    @classmethod
    def generate(cls):
        return cls(
            name=fake.name(),
            description=fake.sentence(nb_words=10),
            priority=fake.random_int(min=1, max=4)
        )

@pytest.fixture
def upd_data_task():
    return UpdDataTask.generate().model_dump()

@pytest.fixture(params=[None, "", "invalid", 123, "NULL"])
def invalid_id(request):
    return request.param

@pytest.fixture
def list_id(auth_session):
    response = auth_session.get(f"{BASE_URL}/team", headers=AUTH_HEADERS)
    teams_id = response.json()['teams'][0]['id']
    response = auth_session.get(f"{BASE_URL}/team/{teams_id}/space", headers=AUTH_HEADERS)
    space_id = response.json()['spaces'][0]['id']
    response = auth_session.get(f"{BASE_URL}/space/{space_id}/folder", headers=AUTH_HEADERS)
    folders_id = response.json()['folders'][0]['id']
    response = auth_session.get(f"{BASE_URL}/folder/{folders_id}/list", headers=AUTH_HEADERS)
    list_id = response.json()['lists'][0]['id']
    return list_id

@pytest.fixture
def task_id(data_task, auth_session, list_id):
    response = auth_session.post(f"{BASE_URL}/list/{list_id}/task", headers=AUTH_HEADERS, json=data_task)
    assert response.status_code in (200, 201), f"Item creation failed: {response.text}"

    task_id = response.json().get("id")
    json_tasks = response.json()
    assert task_id, "Task ID not found in response"

    yield task_id

    auth_session.delete(f"{BASE_URL}/task/{task_id}")
