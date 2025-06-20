from api_clients.api_class import ApiClass
from api_clients.scenarios import Scenarios
import allure

@allure.feature("Тестирование API создания, редактирования и удаления задач")
class TestTasks:

    @allure.story("Успешное создание задачи")
    def test_create_task(self, auth_session, data_task, list_id):
        # Инициализация клиента API
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.create_task(data_task, list_id)

    @allure.story("Получение созданной задачи")
    def test_get_task(self, auth_session, task_id):
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.get_task_by_id(task_id)

    @allure.story("Попытка получить несуществующую задачу")
    def test_get_invalid_ids(self, auth_session, invalid_id):
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.get_task_with_invalid_id(invalid_id)

    @allure.story("Успешное обновление задачи")
    def test_update_task(self, auth_session, upd_data_task, task_id, data_task):
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.update_task(upd_data_task, task_id, data_task)

    @allure.story("Обновление тела задачи на пустое значение")
    def test_update_with_empty_body(self, auth_session, task_id, data_task):
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.update_with_empty_data(task_id, data_task)

    @allure.story("Попытка выполнить удаление без передачи в запрос id")
    def test_delete_without_id(self, auth_session):
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        scenarios.delete_without_id()

    @allure.story("Полный сценарий задачи от создания до удаления")
    def test_full_flow(self, auth_session, data_task):
        # Инициализация клиента API
        api_client = ApiClass(auth_session)
        scenarios = Scenarios(api_client)

        result = scenarios.full_flow_create_and_delete_task(data_task)
