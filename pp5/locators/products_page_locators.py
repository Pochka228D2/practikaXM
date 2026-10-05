from selenium.webdriver.common.by import By


class ProductsPageLocators:
    # Заголовок страницы
    TITLE = (By.CLASS_NAME, "title")

    # Товары
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_DESCRIPTIONS = (By.CLASS_NAME, "inventory_item_desc")

    # Кнопки добавления/удаления
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")

    # Сортировка
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    SORT_OPTIONS = (By.CSS_SELECTOR, "select.product_sort_container option")

    # Корзина
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    # Меню
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")