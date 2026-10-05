from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    """Page Object для страницы логина"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    def open(self):
        self.driver.get("https://autotests.alspio.com/")
        self.logger.info("Открыта страница логина")

    def enter_username(self, username):
        self.input_text(self.locators.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.input_text(self.locators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.logger.info(f"Выполнен логин пользователя: {username}")

    def is_error_message_displayed(self):
        return self.is_element_displayed(self.locators.ERROR_MESSAGE)

    def get_error_message(self):
        if self.is_error_message_displayed():
            return self.get_element_text(self.locators.ERROR_MESSAGE)
        return ""