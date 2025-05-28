from pages.base_page import BasePage



class BoardPage(BasePage):
    def __init__(self, page, team_id):
        super().__init__(page)
        self._endpoint = f'{team_id}/v/b/t/{team_id}'

    ADD_TASK_BUTTON = "[data-test='board-group__create-task-button__Add Task']"
    INPUT_TASK_NAME = "[data-test='quick-create-task-panel__panel-board__input']"
    PRIORITY_LIST = "[data-test='priority-list-priorities']"
    PRIORITY_BUTTON_NORMAL = "[data-test='priorities-list__item-Normal']"
    SAVE_TASK_BUTTON = "[data-test='quick-create-task-panel__panel-board__enter-button']"
    # TASK_NAME = f"[data-test='board-task__ellipsis-menu__{task_name}']"

    def create_task(self, task_name):
        self.navigate_to()
        self.wait_for_selector_and_click(self.ADD_TASK_BUTTON)
        self.assert_element_is_disable(self.SAVE_TASK_BUTTON)
        self.wait_for_selector_and_type(self.INPUT_TASK_NAME, task_name, 20)
        self.assert_element_is_enabled(self.SAVE_TASK_BUTTON)
        self.wait_for_selector_and_click(self.PRIORITY_LIST)
        self.wait_for_selector_and_click(self.PRIORITY_BUTTON_NORMAL)
        self.wait_for_selector_and_click(self.SAVE_TASK_BUTTON)

        test_task = task_id

