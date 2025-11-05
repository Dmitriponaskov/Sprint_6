from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Button')]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    FAQ_BUTTONS = (By.XPATH, "//div[@class='accordion__button']")
    FAQ_PANELS = (By.XPATH, "//div[@class='accordion__panel']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_header_order_button(self):
        self.wait.until(EC.element_to_be_clickable(self.HEADER_ORDER_BUTTON)).click()

    def click_bottom_order_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTTOM_ORDER_BUTTON)).click()

    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.SCOOTER_LOGO)).click()

    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO)).click()

    def get_faq_questions(self):
        return self.driver.find_elements(*self.FAQ_BUTTONS)

    def get_faq_answers(self):
        return self.driver.find_elements(*self.FAQ_PANELS)

    def click_faq_question(self, index):
        questions = self.get_faq_questions()
        questions[index].click()

    def is_answer_visible(self, index):
        answers = self.get_faq_answers()
        return answers[index].is_displayed()