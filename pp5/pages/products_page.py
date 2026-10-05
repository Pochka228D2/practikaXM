from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from locators.products_page_locators import ProductsPageLocators


class ProductsPage(BasePage):
    """Page Object для страницы товаров"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductsPageLocators()

    def get_all_product_names(self):
        """Получить названия всех товаров"""
        products = self.find_elements(self.locators.PRODUCT_NAMES)
        return [product.text for product in products]

    def get_all_product_prices(self):
        """Получить цены всех товаров"""
        prices = self.find_elements(self.locators.PRODUCT_PRICES)
        return [float(price.text.replace('$', '')) for price in prices]

    def add_product_to_cart_by_name(self, product_name):
        """Добавить товар в корзину по названию"""
        products = self.find_elements(self.locators.PRODUCT_NAMES)
        for i, product in enumerate(products):
            if product.text == product_name:
                add_buttons = self.find_elements(self.locators.ADD_TO_CART_BUTTONS)
                add_buttons[i].click()
                self.logger.info(f"Добавлен товар в корзину: {product_name}")
                return True
        return False

    def add_first_product_to_cart(self):
        """Добавить первый товар в корзину"""
        add_buttons = self.find_elements(self.locators.ADD_TO_CART_BUTTONS)
        if add_buttons:
            product_name = self.get_all_product_names()[0]
            add_buttons[0].click()
            self.logger.info(f"Добавлен первый товар: {product_name}")
            return product_name
        return None

    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        try:
            badge = self.find_element(self.locators.CART_BADGE, timeout=2)
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        """Перейти в корзину"""
        self.click_element(self.locators.CART_LINK)
        self.logger.info("Переход в корзину")

    def sort_products(self, sort_by="az"):
        """Сортировать товары"""
        sort_options = {
            "az": "az",
            "za": "za",
            "lohi": "lohi",
            "hilo": "hilo"
        }

        if sort_by in sort_options:
            dropdown = Select(self.find_element(self.locators.SORT_DROPDOWN))
            dropdown.select_by_value(sort_options[sort_by])
            self.logger.info(f"Товары отсортированы по: {sort_by}")

    def logout(self):
        """Выйти из системы"""
        self.click_element(self.locators.MENU_BUTTON)
        self.click_element(self.locators.LOGOUT_LINK)
        self.logger.info("Выполнен выход из системы")