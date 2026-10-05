from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    """Page Object для страницы корзины"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocators()

    def get_cart_items(self):
        """Получить все товары в корзине"""
        items = self.find_elements(self.locators.CART_ITEMS)
        cart_items = []

        for i, item in enumerate(items):
            name = self.find_elements(self.locators.ITEM_NAMES)[i].text
            price = self.find_elements(self.locators.ITEM_PRICES)[i].text
            quantity = self.find_elements(self.locators.ITEM_QUANTITIES)[i].text

            cart_items.append({
                'name': name,
                'price': price,
                'quantity': quantity
            })

        return cart_items

    def remove_product_by_name(self, product_name):
        """Удалить товар из корзины по названию"""
        items = self.find_elements(self.locators.ITEM_NAMES)
        for i, item in enumerate(items):
            if item.text == product_name:
                remove_buttons = self.find_elements(self.locators.REMOVE_BUTTONS)
                remove_buttons[i].click()
                self.logger.info(f"Удален товар из корзины: {product_name}")
                return True
        return False

    def continue_shopping(self):
        """Продолжить покупки"""
        self.click_element(self.locators.CONTINUE_SHOPPING_BUTTON)
        self.logger.info("Продолжение покупок")

    def proceed_to_checkout(self):
        """Перейти к оформлению заказа"""
        self.click_element(self.locators.CHECKOUT_BUTTON)
        self.logger.info("Переход к оформлению заказа")

    def is_cart_empty(self):
        """Проверить пуста ли корзина"""
        items = self.find_elements(self.locators.CART_ITEMS)
        return len(items) == 0