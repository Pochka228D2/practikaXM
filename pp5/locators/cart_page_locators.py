from selenium.webdriver.common.by import By


class CartPageLocators:
    # Элементы корзины
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QUANTITIES = (By.CLASS_NAME, "cart_quantity")

    # Кнопки
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button.cart_button")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    # Заголовок
    TITLE = (By.CLASS_NAME, "title")