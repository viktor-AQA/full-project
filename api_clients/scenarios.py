import pytest
import requests

from api_clients.api_class import ApiClass


class Scenarios:
    def __init__(self, api_client: ApiClass):
        self.api_client = api_client
        self.ids = {}

    def create_task(self, data_task, list_id):
        create_task_data = self.api_client.post_task_create(data_task, list_id)
        task_id = create_task_data.get("id")
        assert task_id is not None, f"ID не найден в ответе на создание: {create_task_data}"

        self.api_client.delete_task(task_id)
        print(f"Task с ID {task_id} успешно создана и удалена.")
        return task_id

    def get_task_by_id(self, task_id):
        get_task_by_id = self.api_client.get_task(task_id)
        task_id = get_task_by_id.get("id")
        assert task_id is not None, "ID не найден в ответе"

        print(f"Task с ID {task_id} найдена.")
        return task_id

    def get_task_with_invalid_id(self, invalid_id):
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            self.api_client.get_task(invalid_id)

        assert exc_info.value.response.status_code in (401, 404), (
            f"Ожидался статус 401 или 404, получен {exc_info.value.response.status_code}"
        )

    def update_task(self, upd_data_task, task_id, data_task):
        before_upd = self.api_client.get_task(task_id)
        assert data_task["name"] == before_upd.get("name")
        assert data_task["description"] == before_upd.get("description")
        assert data_task["priority"] == int(before_upd["priority"]["id"])

        after_upd = self.api_client.put_task_update(task_id, upd_data_task)
        assert upd_data_task["name"] == after_upd.get("name")
        assert upd_data_task["description"] == after_upd.get("description")
        assert upd_data_task["priority"] == int(after_upd["priority"]["id"])

        assert after_upd != before_upd, "Обновления данных не произошло"

    def update_with_empty_data(self, task_id, data_task):
        before_upd = self.api_client.get_task(task_id)
        assert data_task["name"] == before_upd.get("name")
        assert data_task["description"] == before_upd.get("description")
        assert int(data_task["priority"]) == int(before_upd["priority"]["id"])

        upd_data_task = {}
        after_upd = self.api_client.put_task_update(task_id, upd_data_task)

        assert before_upd.get("name") == after_upd.get("name")
        assert before_upd.get("description") == after_upd.get("description")
        assert int(before_upd["priority"]["id"]) == int(after_upd["priority"]["id"])

    def delete_without_id(self):
        task_id = None
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            self.api_client.delete_task(task_id)

        assert exc_info.value.response.status_code in (401, 404), (
            f"Ожидался статус 401 или 404, получен {exc_info.value.response.status_code}")

    def full_flow_create_and_delete_task(self, data_task):
        self.ids['team_id'] = self.api_client.get_teams()
        print(f"Получен team_id: {self.ids['team_id']}")

        # 2. Получаем space_id
        self.ids['space_id'] = self.api_client.get_space(self.ids['team_id'])
        print(f"Получен space_id: {self.ids['space_id']}")

        # 3. Получаем folder_id
        self.ids['folder_id'] = self.api_client.get_folders(self.ids['space_id'])
        print(f"Получен folder_id: {self.ids['folder_id']}")

        # 4. Получаем list_id
        self.ids['list_id'] = self.api_client.get_lists(self.ids['folder_id'])
        print(f"Получен list_id: {self.ids['list_id']}")

        # 5. Создаем задачу
        task = self.api_client.post_task_create(data_task, self.ids['list_id'])
        self.ids['task_id'] = task.get('id')
        print(f"Создана задача с ID: {self.ids['task_id']}")

        # 6. Удаляем задачу
        self.api_client.delete_task(self.ids['task_id'])
        print(f"Задача с ID {self.ids['task_id']} удалена")

        return self.ids
