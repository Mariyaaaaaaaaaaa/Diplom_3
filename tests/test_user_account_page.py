import allure


from conftest import driver, login
from data import Urls
from pages.user_account_page import UserAccountPage
from pages.header_page import HeaderPage


class TestUserAccount:
    @allure.title('Проверка перехода в личный кабинет по кнопке "Личный кабинет" в шапке')
    def test_redirect_to_account_from_header(self, driver, login):
        account_page = UserAccountPage(driver)
        account_page.click_account_btn()
        assert account_page.get_current_url() == Urls.PROFILE_PAGE

    @allure.title('Проверка перехода в раздел История заказов')
    def test_redirect_to_order_history(self, driver, login):
        account_page = UserAccountPage(driver)
        account_page.click_account_btn()
        account_page.click_on_order_list()
        assert account_page.get_current_url() == Urls.ORDERS_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):
        header_page = HeaderPage(driver)
        account_page = UserAccountPage(driver)
        header_page.click_user_account_btn()
        account_page.wait_visibility_element_profile_btn()
        account_page.click_logout_btn()
        account_page.wait_visibility_element_enter_btn()
        btn_text = account_page.get_text_of_element_enter_btn()
        assert btn_text == 'Войти'
