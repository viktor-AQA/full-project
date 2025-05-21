import pytest
import requests

from src.utils.helpers import BASE_URL,  AUTH_HEADERS


class ApiClass:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = BASE_URL

    def get_team(self):
        """ возвращает нам teams_id """
        response = requests.get(f"{self.base_url}/v2/team")
        if response.status_code not in 204:
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        teams_id = response.json()['teams'][0]['id']
        return teams_id

    def get_space(self, teams_id):
        response = requests.get(f"{self.base_url}/v2/team/{teams_id}/space", headers=AUTH_HEADERS)
        if response.status_code not in 204:
            response.raise_for_status()
        space_id = response.json()['spaces'][0]['id']
        return space_id

    def get_folders(self, space_id):
        response = requests.get(f"{self.base_url}/v2/space/{space_id}/folder", headers=AUTH_HEADERS)
        if response.status_code not in 204:
            response.raise_for_status()
        folders_id = response.json()['folders'][0]['id']
        return folders_id

    def get_lists(self, folders_id):
        response = requests.get(f"{self.base_url}/v2/space/{folders_id}/folder", headers=AUTH_HEADERS)
        if response.status_code not in 204:
            response.raise_for_status()
        lists_id = response.json()['lists'][0]['id']
        return lists_id

    def get_task(self, task_id):
        response = requests.get(f"{self.base_url}/v2/task/{task_id}", headers=AUTH_HEADERS)
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def post_task_create(self, data_task, lists_id):
        response = requests.post(f"{self.base_url}/v2/list/{lists_id}/task", headers=AUTH_HEADERS, json=data_task)
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def put_task_update(self, task_id):
        response = requests.put(f"{self.base_url}/v2/task/{task_id}")
        if response.status_code not in (200, 201):
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def delete_task(self, task_id):
        response = requests.delete(f"{self.base_url}/v2/task/{task_id}")
        if response.status_code not in 204:
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

