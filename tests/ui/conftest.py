import pytest
import requests
from faker.proxy import Faker
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from src.utils.helpers import AUTH_HEADERS, BASE_URL, CLICKUP_EMAIL, CLICKUP_PASSWORD


@pytest.fixture
def auth_session():
    session = requests.Session()
    session.headers.update(AUTH_HEADERS)
    return session

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()

fake = Faker()

@pytest.fixture()
def fake_password():
    return fake.password()

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
def data_task():
    return {
            "name": fake.file_name(),
            "description": fake.sentence(nb_words=10),
            "priority": fake.random_int(min=1, max=4)
    }

@pytest.fixture
def task_name():
    return fake.file_name()

@pytest.fixture
def task_id(data_task, auth_session, list_id):
    response = auth_session.post(f"{BASE_URL}/list/{list_id}/task", headers=AUTH_HEADERS, json=data_task)
    assert response.status_code in (200, 201), f"Item creation failed: {response.text}"

@pytest.fixture
def login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login(username=CLICKUP_EMAIL, password=CLICKUP_PASSWORD)