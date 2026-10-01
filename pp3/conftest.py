import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def take_screenshot(driver, test_name):
    """Функция для создания скриншотов"""
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"\nСкриншот сохранен: {filename}")


@pytest.fixture
def driver():
    """Фикстура для управления браузером"""
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    except Exception:
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    """Автоматически делает скриншот при падении теста"""
    def fin():
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            test_name = request.node.name
            take_screenshot(driver, f"FAILED_{test_name}")

    request.addfinalizer(fin)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для получения результата выполнения теста"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)