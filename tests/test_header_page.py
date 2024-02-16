import allure

from conftest import driver
from data import Urls
from pages.header_page import HeaderPage


class TestHeaderPage:
    @allure.title('Проверка перехода в "Конструктор"')
    def test_redirect_to_constructor(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_orders_list_btn()
        header_page.wait_visibility_element_orders_list_title()
        header_page.click_constructor_btn()
        current_url = header_page.get_current_url()
        assert current_url == Urls.MAIN_PAGE

    @allure.title('Проверка перехода в Ленту заказов')
    def test_redirect_to_order_list(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_orders_list_btn()
        current_url = header_page.get_current_url()
        assert current_url == Urls.FEED
