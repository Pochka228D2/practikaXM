from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import setup_logger


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = setup_logger()

    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.logger.error(f"Элемент не найден: {locator}")
            raise

    def find_elements(self, locator, timeout=10):
        """Найти несколько элементов с ожиданием"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            self.logger.error(f"Элементы не найдены: {locator}")
            return []

    def click_element(self, locator):
        """Кликнуть на элемент с ожиданием"""
        element = self.find_element(locator)
        element.click()
        self.logger.info(f"Кликнут элемент: {locator}")

    def input_text(self, locator, text):
        """Ввести текст в элемент"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Введен текст '{text}' в элемент: {locator}")

    def get_element_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text

    def is_element_displayed(self, locator, timeout=5):
        """Проверить отображение элемента"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def wait_for_url_contains(self, text, timeout=10):
        """Ожидать появления текста в URL"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            return False