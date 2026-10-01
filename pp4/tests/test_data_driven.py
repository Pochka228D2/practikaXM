import pytest
import json
import os
import time
from pages.login_page import LoginPage


def load_test_data():
    """Загрузка тестовых данных из JSON-файла"""
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "test_users.json")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


class TestDataDriven:
    """Data-Driven Тесты"""

    @pytest.fixture
    def test_data(self):
        return load_test_data()

    def test_all_users_from_json(self, driver, test_data):
        """Тест всех пользователей из JSON-файла"""
        users = test_data["users"]

        for user in users:
            print(f"\nТестируем: {user['description']}")

            login_page = LoginPage(driver)
            driver.get("https://autotests.alspio.com/")
            time.sleep(1)

            login_page.login(user["username"], user["password"])
            time.sleep(1)

            current_url = driver.current_url
            print(f"Текущий URL: {current_url}")

            if user["expected_result"] == "success":
                if "/inventory.html" in current_url:
                    print(f"Успех: {user['description']}")
                else:
                    print(f"Ошибка: {user['description']} не авторизовался")
                    print(f"Неожиданный URL для {user['description']}")
            else:
                if "/inventory.html" not in current_url:
                    print(f"Успех: {user['description']} не авторизовался")
                else:
                    print(f"Неожиданный успех для {user['description']}")