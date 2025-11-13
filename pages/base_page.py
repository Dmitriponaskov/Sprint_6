import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввод текста в поле")
    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    @allure.step("Получение атрибута элемента")
    def get_attribute(self, locator, attr_name):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attr_name)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переход по URL")
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ожидание, что URL содержит {text}")
    def wait_for_url_to_contain(self, text):
        self.wait.until(lambda d: text in d.current_url)

    @allure.step("Поиск элементов")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу через JavaScript")
    def js_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)