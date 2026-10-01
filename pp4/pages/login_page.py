from locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginPageLocators()

    def open(self):
        self.driver.get("https://autotests.alspio.com/")

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.locators.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.locators.LOGIN_BUTTON)
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_error_message_displayed(self):
        """Проверить, отображается ли сообщение об ошибке"""
        try:
            error_element = self.driver.find_element(*self.locators.ERROR_MESSAGE)
            return error_element.is_displayed()
        except Exception:
            return False

    def get_error_message(self):
        """Получить текст сообщения об ошибке"""
        try:
            error_element = self.driver.find_element(*self.locators.ERROR_MESSAGE)
            return error_element.text
        except Exception:
            return "Ошибка не найдена"