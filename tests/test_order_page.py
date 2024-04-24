import allure
import pytest

from data import Urls, OrderPageData
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('data_order', [OrderPageData.DATA_ORDER_1, OrderPageData.DATA_ORDER_2])
    def test_make_an_order(self, driver, data_order):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE_URL)
        order_page.wait_for_load_element(OrderPageLocators.FORM1_TITLE)
        order_page.create_order(data_order)
        order_page.wait_for_load_element(OrderPageLocators.ORDER_COMPLETED)
        assert (OrderPageData.ORDER_CONFIRM_TITLE_TEXT in
                order_page.check_text(OrderPageLocators.ORDER_COMPLETED)), 'Заказ не оформлен'
