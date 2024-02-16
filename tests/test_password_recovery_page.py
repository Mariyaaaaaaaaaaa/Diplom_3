import allure

from conftest import driver, create_and_delete_user
from data import Urls
from pages.user_account_page import UserAccountPage
from pages.password_recovery_page import PasswordRecoverPage
from pages.header_page import HeaderPage


class TestPasswordRecover:
    @allure.title('Проверка перехода по клику на кнопку Восстановить пароль на странице логина')
    def test_click_password_recover_button(self, driver):
        header_page = HeaderPage(driver)
        account_page = UserAccountPage(driver)
        password_page = PasswordRecoverPage(driver)
        header_page.click_user_account_btn()
        account_page.click_password_recover_btn()
        password_page.click_recover_btn()
        assert password_page.find_element_save_btn().is_displayed()

    @allure.title('Проверка перехода по кнопке Восстановить после ввода почты')
    def test_enter_email_and_click_recover(self, driver, create_and_delete_user):
        password_page = PasswordRecoverPage(driver)
        password_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        password_page.set_email_for_recover_password(create_and_delete_user[0]['email'])
        password_page.click_recover_btn()
        assert password_page.find_element_save_btn().is_displayed()

    @allure.title('Проверка активности поля Пароль после клика по иконке Показать/Скрыть')
    def test_active_password_field(self, driver, create_and_delete_user):
        password_page = PasswordRecoverPage(driver)
        password_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        password_page.set_email_for_recover_password(create_and_delete_user[0]['email'])
        password_page.click_recover_btn()
        password_page.find_element_save_btn()
        password_page.click_on_show_password_icon()
        assert password_page.find_element_input_password_active()
