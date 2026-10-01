import pytest
import time
from pages.login_page import LoginPage


class TestParametrizedLogin:
    """Тесты с параметризацией"""

    @pytest.mark.parametrize("username, password, expected_result", [
        ("standard_user", "secret_sauce", "success"),
        ("locked_out_user", "secret_sauce", "error"),
        ("problem_user", "secret_sauce", "success")
    ])
    def test_login_with_different_users(self, driver, username, password, expected_result):
        """Тест логина с разными пользователями"""
        print(f"\nТестируем пользователя: {username}")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)

        if expected_result == "success":
            assert "/inventory.html" in driver.current_url
            print(f"Успешный логин: {username}")
        else:
            assert login_page.is_error_message_displayed()
            error_text = login_page.get_error_message()
            print(f"Ошибка получена: {error_text}")

        time.sleep(1)

    @pytest.mark.parametrize("username, password, expected_error", [
        ("invalid_user", "wrong_password", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required")
    ])
    def test_invalid_credentials(self, driver, username, password, expected_error):
        """Тест невалидных credentials"""
        print(f"\nТестируем невалидные данные: '{username}' / '{password}'")
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)

        assert login_page.is_error_message_displayed()
        error_text = login_page.get_error_message()
        assert expected_error in error_text
        print(f"Получена ожидаемая ошибка: {error_text}")

        time.sleep(1)