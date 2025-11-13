import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import ORDER_DATA
from data.urls import Urls


class TestOrderFlow:
    @pytest.mark.parametrize("name,surname,address,phone,date,comment", ORDER_DATA)
    @allure.title("Заказ через шапку + проверка открытия новой вкладки при клике на Яндекс")
    def test_order_from_header(self, main_page, name, surname, address, phone, date, comment):
        main_page.click_header_order_button()
        order_page = OrderPage(main_page.driver)
        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(date, comment)
        order_page.confirm_order()

        assert order_page.is_order_success_visible()
        order_page.click_view_status_button()

        # Возврат на главную
        main_page.click_scooter_logo()
        assert main_page.get_current_url().rstrip() == Urls.MAIN_PAGE.rstrip()

        # Переход на Дзен через клик
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        # Ожидаем, что в URL новой вкладки появился dzen.ru и yredirect=true
        main_page.wait_for_url_to_contain('dzen.ru')
        main_page.wait_for_url_to_contain('yredirect=true')

    @pytest.mark.parametrize("name,surname,address,phone,date,comment", ORDER_DATA)
    @allure.title("Заказ через низ страницы")
    def test_order_from_bottom(self, main_page, name, surname, address, phone, date, comment):
        main_page.click_bottom_order_button()
        order_page = OrderPage(main_page.driver)
        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(date, comment)
        order_page.confirm_order()

        assert order_page.is_order_success_visible()
        order_page.click_view_status_button()

        main_page.click_scooter_logo()
        assert main_page.get_current_url().rstrip() == Urls.MAIN_PAGE.rstrip()