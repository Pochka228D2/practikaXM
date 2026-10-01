from locators.login_page_locators import LoginPageLocators
from utils.logger import setup_logger


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginPageLocators()
        self.logger = setup_logger()

    def open(self):
        self.logger.info("Открываем страницу логина")
        self.driver.get("https://autotests.alspio.com/")

    def enter_username(self, username):
        self.logger.info(f"Вводим логин: {username}")
        username_field = self.driver.find_element(*self.locators.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        self.logger.info(f"Вводим пароль: {password}")
        password_field = self.driver.find_element(*self.locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        self.logger.info("Нажимаем кнопку Login")
        login_button = self.driver.find_element(*self.locators.LOGIN_BUTTON)
        login_button.click()

    def login(self, username, password):
        self.logger.info(f"Начинаем логин пользователя {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.logger.info("Логин завершен")

    def is_error_message_displayed(self):
        try:
            error_element = self.driver.find_element(*self.locators.ERROR_MESSAGE)
            is_displayed = error_element.is_displayed()
            if is_displayed:
                self.logger.warning("Обнаружено сообщение об ошибке")
            return is_displayed
        except Exception:
            return False

    def get_error_message(self):
        try:
            error_element = self.driver.find_element(*self.locators.ERROR_MESSAGE)
            error_text = error_element.text
            self.logger.info(f"Текст ошибки: {error_text}")
            return error_text
        except Exception:
            return ""