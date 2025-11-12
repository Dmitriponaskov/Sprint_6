import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from data.urls import Urls


class MainPage(BasePage):
    # Локаторы
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Button')]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    FAQ_BUTTONS = (By.XPATH, "//div[@class='accordion__button']")
    FAQ_PANELS = (By.XPATH, "//div[@class='accordion__panel']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @allure.step("Нажать кнопку 'Заказать' в шапке")
    def click_header_order_button(self):
        self.click(self.HEADER_ORDER_BUTTON)

    @allure.step("Нажать кнопку 'Заказать' внизу")
    def click_bottom_order_button(self):
        self.click(self.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать логотип 'Самоката'")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Нажать логотип 'Яндекса'")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    @allure.step("Получить href логотипа Яндекса")
    def get_yandex_logo_href(self):
        return self.get_attribute(self.YANDEX_LOGO, "href")

    @allure.step("Нажать на вопрос FAQ {index}")
    def click_faq_question(self, index):
        questions = self.find_elements(self.FAQ_BUTTONS)
        questions[index].click()

    @allure.step("Получить текст ответа {index}")
    def get_answer_text(self, index):
        answers = self.find_elements(self.FAQ_PANELS)
        return answers[index].text

    @allure.step("Проверить, что ответ {index} виден")
    def is_answer_visible(self, index):
        answers = self.find_elements(self.FAQ_PANELS)
        return answers[index].is_displayed()

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click(self.COOKIE_BUTTON)
        except:
            pass