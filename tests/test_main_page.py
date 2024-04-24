import allure
import pytest

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from data import Urls, MainPageData


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', MainPageData.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, driver, index, question, answer):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.scroll_to_element(MainPageLocators.FAQ_LIST)
        main_page.wait_for_load_element(MainPageLocators.FAQ_LIST)
        question_received = main_page.click_on_question(index)
        answer_received = main_page.get_answer(index)
        # проверяем, что текст вопроса соответствует ожидаемому
        assert question_received == question, 'Вопрос на сайте не соответствует ожидаемому или в тексте есть ошибки'
        # проверяем, что текст ответа соответствует ожидаемому
        assert answer_received == answer, 'Ответ на сайте не соответствует ожидаемому или в тексте есть ошибки'

    @allure.title('Проверка кнопок "Заказать на Главной странице')
    @allure.description('Проверяем, что по клику на кнопку Заказать на Главной странице'
                        'открывается страница заказа')
    @pytest.mark.parametrize('locator', [MainPageLocators.HEADER_ORDER_BUTTON, MainPageLocators.FOOTER_ORDER_BUTTON])
    def test_order_button(self, driver, locator):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.scroll_to_element(locator)
        main_page.wait_for_load_element(locator)
        main_page.click_element(locator)
        main_page.wait_for_load_element(OrderPageLocators.FORM1_TITLE)
        assert driver.current_url == Urls.ORDER_PAGE_URL, 'URL не соответствует странице заказа'
