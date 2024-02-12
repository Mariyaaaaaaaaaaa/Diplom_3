import allure

from conftest import driver, create_and_delete_user
from data import Urls
from locators.password_recovery_locators import PasswordRecoverLocators
from pages.user_account_page import UserAccountPage
from pages.password_recovery_page import PasswordRecoverPage
from pages.header_page import HeaderPage


class TestPasswordRecover:
    @allure.title('Проверка перехода по клику на кнопку Восстановить пароль на странице логина')
    def test_click_password_recover_button(self, driver):
        HeaderPage(driver).click_user_account_btn()
        UserAccountPage(driver).click_password_recover_btn()
        PasswordRecoverPage(driver).click_recover_btn()
        assert PasswordRecoverPage(driver).find_element(PasswordRecoverLocators.SAVE_BTN).is_displayed()

    @allure.title('Проверка перехода по кнопке Восстановить после ввода почты')
    def test_enter_email_and_click_recover(self, driver, create_and_delete_user):
        PasswordRecoverPage(driver).open_page(Urls.FORGOT_PASSWORD_PAGE)
        PasswordRecoverPage(driver).set_email_for_recover_password(create_and_delete_user[0]['email'])
        PasswordRecoverPage(driver).click_recover_btn()
        assert PasswordRecoverPage(driver).find_element(PasswordRecoverLocators.SAVE_BTN).is_displayed()

    @allure.title('Проверка активности поля Пароль после клика по иконке Показать/Скрыть')
    def test_active_password_field(self, driver, create_and_delete_user):
        PasswordRecoverPage(driver).open_page(Urls.FORGOT_PASSWORD_PAGE)
        PasswordRecoverPage(driver).set_email_for_recover_password(create_and_delete_user[0]['email'])
        PasswordRecoverPage(driver).click_recover_btn()
        PasswordRecoverPage(driver).find_element(PasswordRecoverLocators.SAVE_BTN)
        PasswordRecoverPage(driver).click_on_show_password_icon()
        assert PasswordRecoverPage(driver).find_element(PasswordRecoverLocators.INPUT_PASSWORD_ACTIVE)
