import allure

from conftest import driver, login
from pages.orders_page import OrdersPage
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.user_account_page import UserAccountPage


class TestOrderListPage:
    @allure.title('Проверка всплывающего окна с деталями заказа')
    def test_open_order_details_popup(self, driver):
        order_page = OrdersPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_orders_list_btn()
        order_page.click_order()
        assert order_page.check_element_order_structure_title().is_displayed()

    @allure.title('Проверка отображения созданного заказа в Ленте заказов')
    def test_new_order_in_order_list(self, driver, login):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        account_page = UserAccountPage(driver)
        order_page = OrdersPage(driver)
        main_page.make_order_and_get_order_number()
        account_page.click_account_btn()
        account_page.click_on_order_list()
        account_page.find_element_order_status()
        order_number = account_page.get_order_number()
        header_page.click_orders_list_btn()
        order_page.find_element_order_list_title()
        wanted_order = order_page.get_order_in_orderlist(order_number)
        assert wanted_order.is_displayed()

    @allure.title('Проверка изменения счетчика "Выполнено за все время" после создания заказа')
    def test_change_counter_total_orders(self, driver, login):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        orders_page = OrdersPage(driver)
        main_page.find_element_ingredient_bun()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_element_orders_list_title()
        total_number = orders_page.get_total_orders_number()
        header_page.click_constructor_btn()
        main_page.wait_visibility_element_burger_construction_title()
        main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_element_orders_list_title()
        new_total_number = orders_page.get_total_orders_number()
        assert int(new_total_number) == int(total_number) + 1

    @allure.title('Проверка изменения счетчика "Выполнено за сегодня" после создания заказа')
    def test_change_counter_today_orders(self, driver, login):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        order_page = OrdersPage(driver)
        main_page.find_element_ingredient_bun()
        header_page.click_orders_list_btn()
        order_page.wait_visibility_element_orders_list_title()
        today_number = order_page.get_today_orders_number()
        header_page.click_constructor_btn()
        main_page.wait_visibility_element_burger_construction_title()
        main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        order_page.wait_visibility_element_orders_list_title()
        new_number = order_page.get_today_orders_number()
        assert int(new_number) == int(today_number) + 1

    @allure.title('Проверка отображения нового заказа в списке "В работе"')
    def test_new_order_appears_in_work_list(self, driver, login):
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        orders_page = OrdersPage(driver)
        new_order = main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_element_all_order_ready()
        orders_page.wait_visibility_element_order_in_work()
        order_in_work = orders_page.get_order_number_in_work()
        assert new_order in order_in_work
