import pytest
import requests
from faker.proxy import Faker

from src.utils.helpers import AUTH_HEADERS, BASE_URL


@pytest.fixture
def auth_session():
    session = requests.Session()
    session.headers.update(AUTH_HEADERS)
    return session

@pytest.fixture
def team_id(auth_session):
    """ возвращает нам teams_id """
    response = auth_session.get(f"{BASE_URL}/team", headers=AUTH_HEADERS)
    if response.status_code != 200:  # Проверяем успешный статус
        response.raise_for_status()  # Выбросит HTTPError для плохих статусов
    teams_id = response.json()['teams'][0]['id']
    return teams_id

fake = Faker()

