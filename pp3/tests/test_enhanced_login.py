import pytest
import time
from pages.login_page import LoginPage
from utils.logger import setup_logger


class TestEnhancedLogin:
    """Тесты с улучшенным логированием"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.logger = setup_logger()
        self.logger.info("=" * 50)

    def test_successful_login_with_logs(self, driver):
        """Тест успешного логина с логированием"""
        self.logger.info("Запуск теста: Успешный логин")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert "/inventory.html" in driver.current_url
        self.logger.info("Тест пройден: Логин успешен")
        time.sleep(1)

    def test_error_messages_with_logs(self, driver):
        """Тест ошибок с логированием"""
        self.logger.info("Запуск теста: Проверка ошибок")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        assert login_page.is_error_message_displayed()
        error_text = login_page.get_error_message()
        assert "locked out" in error_text
        self.logger.info("Тест пройден: Ошибка отображается корректно")
        time.sleep(1)

    def test_failed_login_for_screenshot(self, driver):
        """Тест, который упадет (для демонстрации скриншота)"""
        self.logger.info("Запуск теста: Демонстрация скриншота при падении")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("invalid_user", "wrong_password")

        assert "/inventory.html" in driver.current_url, "Этот тест должен упасть"
        time.sleep(1)