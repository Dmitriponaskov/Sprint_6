import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")

    # Принять куки, если появляются
    try:
        wait = WebDriverWait(driver, 5)
        cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookie_button.click()
    except:
        pass  # Если куки не появились — игнорируем

    yield driver
    driver.quit()