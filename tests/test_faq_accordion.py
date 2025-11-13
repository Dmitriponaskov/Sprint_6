import pytest
import allure
from pages.main_page import MainPage
from data.test_data import FAQ_DATA


class TestFAQAccordion:
    @pytest.mark.parametrize("index,expected_text", FAQ_DATA)
    @allure.title("Проверка FAQ: вопрос {index}")
    def test_faq_accordion(self, main_page, index, expected_text):
        main_page.click_faq_question(index)
        assert main_page.is_answer_visible(index)
        actual = main_page.get_answer_text(index)
        assert actual == expected_text