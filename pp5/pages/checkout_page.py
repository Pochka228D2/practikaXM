from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.checkout_page_locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    """Page Object для страницы оформления заказа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CheckoutPageLocators()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Заполнить информацию для оформления заказа"""
        self.input_text(self.locators.FIRST_NAME_FIELD, first_name)
        self.input_text(self.locators.LAST_NAME_FIELD, last_name)
        self.input_text(self.locators.POSTAL_CODE_FIELD, postal_code)
        self.logger.info("Заполнена информация для заказа")

    def continue_to_overview(self):
        """Перейти к обзору заказа"""
        self.click_element(self.locators.CONTINUE_BUTTON)
        self.logger.info("Переход к обзору заказа")

        # Ждем перехода на следующую страницу
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("checkout-step-two")
            )
            return True
        except TimeoutException:
            self.logger.warning("Не удалось перейти на страницу обзора заказа")
            return False

    def get_order_summary(self):
        """Получить сводку заказа с улучшенной обработкой"""
        try:
            # Даем время на загрузку страницы
            import time
            time.sleep(2)

            items = []
            prices = []

            # Пробуем разные варианты локаторов для товаров
            try:
                item_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
                if item_elements:
                    items = [item.text for item in item_elements]
                else:
                    # Пробуем CSS селектор
                    item_elements = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
                    items = [item.text for item in item_elements]
            except Exception as e:
                self.logger.warning(f"Не удалось получить названия товаров: {e}")

            try:
                price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
                if price_elements:
                    prices = [price.text for price in price_elements]
                else:
                    # Пробуем CSS селектор
                    price_elements = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
                    prices = [price.text for price in price_elements]
            except Exception as e:
                self.logger.warning(f"Не удалось получить цены товаров: {e}")

            # Получаем итоговые суммы с разными попытками
            subtotal = self._get_summary_value("summary_subtotal_label")
            tax = self._get_summary_value("summary_tax_label")
            total = self._get_summary_value("summary_total_label")

            result = {
                'items': list(zip(items, prices)) if items and prices else [],
                'subtotal': subtotal,
                'tax': tax,
                'total': total
            }

            self.logger.info(f"Сводка заказа получена: {result}")
            return result

        except Exception as e:
            self.logger.error(f"Ошибка при получении сводки заказа: {e}")
            return {
                'items': [],
                'subtotal': 'Не найдено',
                'tax': 'Не найдено',
                'total': 'Не найдено'
            }

    def _get_summary_value(self, class_name):
        """Вспомогательный метод для получения значений сводки"""
        try:
            element = self.driver.find_element(By.CLASS_NAME, class_name)
            return element.text
        except:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, f".{class_name}")
                return element.text
            except:
                return "Не найдено"

    def finish_order(self):
        """Завершить заказ"""
        self.click_element(self.locators.FINISH_BUTTON)
        self.logger.info("Заказ завершен")

    def is_order_successful(self):
        """Проверить успешность заказа"""
        return self.is_element_displayed(self.locators.SUCCESS_MESSAGE)

    def get_success_message(self):
        """Получить сообщение об успехе"""
        if self.is_order_successful():
            return self.get_element_text(self.locators.SUCCESS_MESSAGE)
        return "Сообщение об успехе не найдено"

    def is_error_message_displayed(self):
        """Проверить отображение ошибки"""
        return self.is_element_displayed(self.locators.ERROR_MESSAGE)

    def get_error_message(self):
        """Получить текст ошибки"""
        if self.is_error_message_displayed():
            return self.get_element_text(self.locators.ERROR_MESSAGE)
        return ""

    def wait_for_url_contains(self, text, timeout=10):
        """Ожидать появления текста в URL"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            return False