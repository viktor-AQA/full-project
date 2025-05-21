from src.api_clients.api_class import ApiClass
from src.api_clients.scenarios import Scenarios

class TestTasks:

    def test_full_flow(self, data_task):
        # Инициализация клиента API
        api_client = ApiClass()
        scenarios = Scenarios(api_client)

        # Выполнение сценария
        result = scenarios.full_flow_create_and_delete_task(data_task)

