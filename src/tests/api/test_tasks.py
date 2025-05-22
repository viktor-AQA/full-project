from src.api_clients.api_class import ApiClass
from src.api_clients.scenarios import Scenarios

class TestTasks:

    def test_create_task(self, auth_session, data_task, list_id):
        # Инициализация клиента API
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.create_task(data_task, list_id)

    def test_get_task(self, auth_session, task_id):
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.get_task_by_id(task_id)

    def test_update_task(self, auth_session, upd_data_task, list_id):
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.update_task(upd_data_task, list_id)

    def test_full_flow(self, auth_session, data_task):
        # Инициализация клиента API
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        # Выполнение сценария
        result = scenarios.full_flow_create_and_delete_task(data_task)

