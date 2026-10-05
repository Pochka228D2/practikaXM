from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    # Форма информации (Step One)
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

    # Обзор заказа (Step Two) - альтернативные локаторы
    CHECKOUT_SUMMARY = (By.CLASS_NAME, "checkout_summary_container")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    ITEM_QUANTITIES = (By.CLASS_NAME, "cart_quantity")
    SUBTOTAL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    # Кнопки (Step Two)
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON_STEP_TWO = (By.ID, "cancel")

    # Завершение заказа (Step Three)
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    # Сообщения об ошибках
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    ERROR_CONTAINER = (By.CLASS_NAME, "error-message-container")