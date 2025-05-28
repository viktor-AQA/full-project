from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'login'

    USERNAME_SELECTOR = "input[data-test='login-email-input']"
    PASSWORD_SELECTOR = "input[data-test='login-password-input']"
    LOGIN_BUTTON_SELECTOR = "button[data-test='login-submit']"
    CHECKOUT_CONTAINER = "#app-root"
    ERROR_MESSAGE = "[data-test='form__error']"

    def login(self, username: str, password: str):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.CHECKOUT_CONTAINER)

    def not_valid_login(self, username: str, password: str):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)

        self.assert_text_in_element(self.ERROR_MESSAGE, " Incorrect password for this email. ")

