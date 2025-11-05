import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


ORDER_DATA = [
    ("Иван", "Петров", "Ленина 1", "+79991234567", "15.11.2025", "Тест 1"),
    ("Анна", "Сидорова", "Пушкина 10", "+79997654321", "16.11.2025", "Тест 2")
]


class TestOrderFlow:

    @pytest.mark.parametrize("name,surname,address,phone,date,comment", ORDER_DATA)
    def test_order_from_header(self, driver, name, surname, address, phone, date, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_header_order_button()
        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(date, comment)
        order_page.confirm_order()

        assert order_page.is_order_success_visible()

        # Закрываем модалку → переходим на страницу статуса
        order_page.click_view_status_button()

        # Клик по логотипу "Самоката" на странице статуса
        status_page = MainPage(driver)
        status_page.click_scooter_logo()

        # Проверяем возврат на главную
        assert driver.current_url.rstrip() == "https://qa-scooter.praktikum-services.ru/"

    @pytest.mark.parametrize("name,surname,address,phone,date,comment", ORDER_DATA)
    def test_order_from_bottom(self, driver, name, surname, address, phone, date, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_bottom_order_button()
        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(date, comment)
        order_page.confirm_order()

        assert order_page.is_order_success_visible()

        order_page.click_view_status_button()

        status_page = MainPage(driver)
        status_page.click_scooter_logo()
        assert driver.current_url.rstrip() == "https://qa-scooter.praktikum-services.ru/"