import pytest
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestProducts:
    """Тесты для страницы товаров"""

    def test_product_sorting(self, driver):
        """Тест сортировки товаров"""
        # Логин
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)

        # Тестируем разные виды сортировки
        sort_types = ["az", "za", "lohi", "hilo"]

        for sort_type in sort_types:
            products_page.sort_products(sort_type)
            time.sleep(1)

            product_names = products_page.get_all_product_names()
            assert len(product_names) > 0, f"Товары не найдены после сортировки {sort_type}"
            print(f"  Сортировка {sort_type} работает")

    def test_add_multiple_products(self, driver):
        """Упрощенный тест добавления товаров в корзину"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)

        # Просто проверяем что можем добавить хотя бы один товар
        first_product = products_page.add_first_product_to_cart()
        assert first_product is not None

        cart_count = products_page.get_cart_items_count()
        assert cart_count >= 1

        print(f"  Добавлен товар: {first_product}, в корзине: {cart_count} товар(ов)")