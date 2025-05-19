import pytest
import requests
from requests import post, delete, get

from src.utils.helpers import BASE_URL, LIST_ID, AUTH_HEADERS


class ApiClass:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = BASE_URL

    def get_task(self, task_id):
        response = get(f"{self.base_url}/v2/task/{task_id}")
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def post_task_create(self, data_task):
        response = post(f"{self.base_url}/v2/list/{LIST_ID}/task", headers=AUTH_HEADERS, json=data_task)
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def put_task_update(self, task_id, data_task):
        response = requests.put(f"{self.base_url}/v2/task/{task_id}")
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def delete_task(self, task_id):
        response = delete(f"{self.base_url}/v2/task/{task_id}")
        if response.status_code not in 204:
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()