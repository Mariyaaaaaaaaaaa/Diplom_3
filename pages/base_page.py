import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from locators.main_page_locators import MainPageLocators
from locators.orders_page_locators import OrdersPageLocators
from locators.password_recovery_locators import PasswordRecoverLocators
from locators.user_account_locators import UserAccountLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Поиск флюоресцентной булки')
    def find_element_ingredient_bun(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(MainPageLocators.INGREDIENT_BUN))

    @allure.step('Поиск номера заказа')
    def find_element_order_number(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(MainPageLocators.ORDER_NUMBER))

    @allure.step('Поиск статуса заказа в истории')
    def find_element_order_status(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(UserAccountLocators.ORDER_STATUS))

    @allure.step('Поиск заголовка "Лента заказов"')
    def find_element_order_list_title(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(OrdersPageLocators.ORDERS_LIST_TITLE))

    @allure.step('Поиск кнопки "Сохранить"')
    def find_element_save_btn(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(PasswordRecoverLocators.SAVE_BTN))

    @allure.step('Поиск активного поля ввода пароля')
    def find_element_input_password_active(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(PasswordRecoverLocators.INPUT_PASSWORD_ACTIVE))

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Получение текста элемента')
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Получение текста заголовка всплывающего окна "Детали ингредиента"')
    def get_text_of_element_ingredient_popup_title(self):
        return self.driver.find_element(*MainPageLocators.INGREDIENT_POPUP_TITLE).text

    @allure.step('Получение текста кнопки "Войти"')
    def get_text_of_element_enter_btn(self):
        return self.driver.find_element(*UserAccountLocators.ENTER_BTN).text

    @allure.step('Вставить текст {text}')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Клик по видимому элементу')
    def click_to_visible_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).click()

    @allure.step('Проверка отображения элемента на странице')
    def check_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверка отображения всплывающего окна Детали ингредиента на странице')
    def check_element_ingredient_popup(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(MainPageLocators.INGREDIENT_POPUP))
        return self.driver.find_element(*MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Проверка отображения всплывающего окна "Ваш заказ начали готовить"')
    def check_element_order_status_text(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(MainPageLocators.ORDER_STATUS_TEXT))
        return self.driver.find_element(*MainPageLocators.ORDER_STATUS_TEXT)

    @allure.step('Проверка отображения заголовка "Состав" в окне с деталями заказа')
    def check_element_order_structure_title(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(OrdersPageLocators.ORDER_STRUCTURE_TITLE))
        return self.driver.find_element(*OrdersPageLocators.ORDER_STRUCTURE_TITLE)

    @allure.step('Проверка невидимости элемента на странице')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(locator))

    @allure.step('Проверка невидимости всплывающего окна Детали ингредиента на странице')
    def check_invisibility_ingredient_popup(self):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(MainPageLocators.INGREDIENT_POPUP))

    @allure.step('Ожидание видимости элемента на странице')
    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание видимости заголовка "Лента заказов" на странице')
    def wait_visibility_element_orders_list_title(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(OrdersPageLocators.ORDERS_LIST_TITLE))

    @allure.step('Ожидание видимости заголовка "Соберите бургер" на странице')
    def wait_visibility_element_burger_construction_title(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(MainPageLocators.BURGER_CONSTRUCTOR_TITLE))

    @allure.step('Ожидание видимости "Все текущие заказы готовы" на странице')
    def wait_visibility_element_all_order_ready(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(OrdersPageLocators.ALL_ORDERS_READY))

    @allure.step('Ожидание видимости номера заказа в работе на странице')
    def wait_visibility_element_order_in_work(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(OrdersPageLocators.ORDER_IN_WORK))

    @allure.step('Ожидание видимости профиля пользователя на странице')
    def wait_visibility_element_profile_btn(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(UserAccountLocators.PROFILE_BTN))

    @allure.step('Ожидание видимости кнопки "Войти" на странице')
    def wait_visibility_element_enter_btn(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(UserAccountLocators.ENTER_BTN))

    @allure.step('Ожидание невидимости элемента на странице')
    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Открыть страницу')
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step('Ожидание открытия новой вкладки')
    def wait_open_new_tab(self, index):
        WebDriverWait(self.driver, 15).until(EC.number_of_windows_to_be(index))

    @allure.step('Ожидание открытия страницы {url}')
    def wait_open_page(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(url))

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, locator_from, locator_to):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator_from))
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator_to))
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)

    @allure.step('Перемещение до элемента и клик по нему')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()
