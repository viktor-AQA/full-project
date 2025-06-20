from pages.board_page import BoardPage
from pages.login_page import LoginPage
from src.utils.helpers import CLICKUP_EMAIL, CLICKUP_PASSWORD


def test_success_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.login(username=CLICKUP_EMAIL, password=CLICKUP_PASSWORD)

def test_unsuccessful_login(browser, fake_password):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.not_valid_login(username=CLICKUP_EMAIL, password=fake_password)

def test_create_task(browser, task_name, team_id, get_task_locator):
    page = browser.new_page()
    login_page = LoginPage(page)
    board_page = BoardPage(page, team_id)

    login_page.login(username=CLICKUP_EMAIL, password=CLICKUP_PASSWORD)
    board_page.create_task(task_name, get_task_locator)



