from src.utils.helpers import BASE_URL, AUTH_HEADERS, AUTH_HEADERS_UPD


class ApiClass:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = BASE_URL

    def get_teams(self):
        """ возвращает нам teams_id """
        response = self.auth_session.get(f"{self.base_url}/team", headers=AUTH_HEADERS)
        if response.status_code != 200:  # Проверяем успешный статус
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        teams_id = response.json()['teams'][0]['id']
        return teams_id

    def get_space(self, teams_id):
        response = self.auth_session.get(f"{self.base_url}/team/{teams_id}/space", headers=AUTH_HEADERS)
        if response.status_code != 200:  # Проверяем успешный статус
            response.raise_for_status()
        space_id = response.json()['spaces'][0]['id']
        return space_id

    def get_folders(self, space_id):
        response = self.auth_session.get(f"{self.base_url}/space/{space_id}/folder", headers=AUTH_HEADERS)
        if response.status_code != 200:  # Проверяем успешный статус
            response.raise_for_status()
        folders_id = response.json()['folders'][0]['id']
        return folders_id

    def get_lists(self, folders_id):
        response = self.auth_session.get(f"{self.base_url}/folder/{folders_id}/list", headers=AUTH_HEADERS)
        if response.status_code != 200:  # Проверяем успешный статус
            response.raise_for_status()
        lists_id = response.json()['lists'][0]['id']
        return lists_id

    def post_task_create(self, data_task, lists_id):
        response = self.auth_session.post(f"{self.base_url}/list/{lists_id}/task", headers=AUTH_HEADERS, json=data_task)
        if response.status_code != 200:  # Проверяем успешный статус
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def get_task(self, task_id):
        response = self.auth_session.get(f"{self.base_url}/task/{task_id}", headers=AUTH_HEADERS)
        if response.status_code != 200:  # Проверяем успешный статус
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def put_task_update(self, task_id, upd_data_task):
        response = self.auth_session.put(f"{self.base_url}/task/{task_id}", headers=AUTH_HEADERS_UPD, json=upd_data_task)
        if response.status_code != 200:  # Проверяем успешный статус
            response.raise_for_status() # Выбросит HTTPError для плохих статусов
        return response.json()

    def delete_task(self, task_id):
        response = self.auth_session.delete(f"{self.base_url}/task/{task_id}", headers=AUTH_HEADERS)
        if response.status_code == 204:
            return {"status": "success", "message": "Task deleted"}
        response.raise_for_status()
        return response.json()

