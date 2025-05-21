from src.api_clients.api_class import ApiClass


class Scenarios:
    def __init__(self, api_client: ApiClass):
        self.api_client = api_client
        self.ids = {}

    def full_flow_create_and_delete_task(self, data_task):
        self.ids['team_id'] = self.api_client.get_team()
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