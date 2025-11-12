import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class OrderPage(BasePage):
    # Локаторы формы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Order_Header__')]")  # Для закрытия календаря
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')][1]")
    BLACK_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__')]//button[text()='Заказать']")

    # Локаторы модальных окон
    CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]//button[text()='Да']")
    SUCCESS_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__') and contains(text(), 'Заказ оформлен')]")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    @allure.step("Заполнить первую форму")
    def fill_first_form(self, name, surname, address, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)

        metro = self.find_element(self.METRO_INPUT)
        metro.click()
        metro.send_keys("Черкизовская")
        metro.send_keys(Keys.ARROW_DOWN)
        metro.send_keys(Keys.ENTER)

        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму")
    def fill_second_form(self, date, comment):
        date_field = self.find_element(self.DATE_INPUT)
        date_field.clear()
        date_field.send_keys(date)

        # Закрываем календарь кликом по заголовку
        header = self.find_element(self.ORDER_HEADER)
        header.click()

        self.click(self.RENTAL_PERIOD_DROPDOWN)
        self.click(self.RENTAL_OPTION)

        self.click(self.BLACK_CHECKBOX)
        if comment:
            self.send_keys(self.COMMENT_INPUT, comment)

        self.click(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Нажать 'Посмотреть статус'")
    def click_view_status_button(self):
        self.click(self.VIEW_STATUS_BUTTON)

    @allure.step("Проверить, что заказ оформлен")
    def is_order_success_visible(self):
        return self.is_element_visible(self.SUCCESS_HEADER)