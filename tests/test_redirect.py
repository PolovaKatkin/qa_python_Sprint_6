import allure

from data import Urls
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage


class TestRedirect:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката со старницы заказа')
    def test_open_main_page_when_click_on_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE_URL)
        order_page.click_element(BasePageLocators.SCOOTER_BUTTON)
        order_page.wait_for_load_element(MainPageLocators.PAGE_TITLE)
        assert driver.current_url == Urls.MAIN_PAGE_URL, 'URL не соответствует главной странице'

    @allure.title('Проверка открытия нового окна станицы Дзена по клику на лого Яндекса')
    def test_open_dzen_in_new_window(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE_URL)
        order_page.click_element(BasePageLocators.YANDEX_BUTTON)
        order_page.switch_to_new_window()
        order_page.wait_for_open_page(Urls.DZEN_URL)
        assert driver.current_url == Urls.DZEN_URL, 'URL не соответствует странице Дзена'
