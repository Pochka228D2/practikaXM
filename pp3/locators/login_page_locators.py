from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы для страницы логина"""
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")