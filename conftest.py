import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data.urls import Urls
from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    driver.get(Urls.MAIN_PAGE)
    page = MainPage(driver)
    page.accept_cookies()
    return page