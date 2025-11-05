from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    # === Первая страница: "Для кого самокат" ===
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # === Вторая страница: "Про аренду" ===
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')][1]")
    BLACK_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__')]//button[text()='Заказать']")

    # === Модальное окно подтверждения: "Хотите оформить заказ?" ===
    CONFIRM_MODAL_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]//button[text()='Да']")

    # === Модальное окно успеха: "Заказ оформлен" ===
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]//div[contains(@class, 'Order_ModalHeader__') and contains(text(), 'Заказ оформлен')]")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_first_form(self, name, surname, address, phone):
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

        metro = self.driver.find_element(*self.METRO_INPUT)
        metro.click()
        metro.send_keys("Черкизовская")
        metro.send_keys(Keys.ARROW_DOWN)
        metro.send_keys(Keys.ENTER)

        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_second_form(self, date, comment):
        date_field = self.wait.until(EC.element_to_be_clickable(self.DATE_INPUT))
        date_field.clear()
        date_field.send_keys(date)

        # Закрываем календарь, кликая по заголовку формы
        header = self.driver.find_element(By.XPATH, "//div[contains(@class, 'Order_Header__')]")
        header.click()

        # Выбор срока аренды
        dropdown = self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD_DROPDOWN))
        dropdown.click()
        option = self.wait.until(EC.element_to_be_clickable(self.RENTAL_OPTION))
        option.click()

        self.driver.find_element(*self.BLACK_CHECKBOX).click()
        if comment:
            self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

        self.driver.find_element(*self.ORDER_BUTTON).click()

    def confirm_order(self):
        """Нажимает 'Да' в модальном окне 'Хотите оформить заказ?'"""
        yes_button = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_MODAL_YES_BUTTON))
        yes_button.click()

    def click_view_status_button(self):
        """Закрывает модальное окно 'Заказ оформлен' и переходит на страницу статуса"""
        button = self.wait.until(EC.element_to_be_clickable(self.VIEW_STATUS_BUTTON))
        button.click()

    def is_order_success_visible(self):
        """Проверяет, что появилось окно 'Заказ оформлен'"""
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL_HEADER)).is_displayed()