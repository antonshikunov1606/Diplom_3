import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from test_data import URLCollection


class HomePageStellar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие главной страницы Stellar")
    def open_home_page(self):
        self.navigate(URLCollection.STELLAR_HOME_PAGE)

    @allure.step('Ожидание загрузки главной страницы Stellar')
    def wait_for_load_home_page(self):
        self.find_element(HomePageLocators.PANEL_HOME_PAGE)

    @allure.step('Ожидание загрузки окна "Конструктор"')
    def wait_for_load_panel_constructor(self):
        self.find_element(HomePageLocators.PANEL_CONSTRUCTOR)

    @allure.step('Ожидание загрузки окна "Детали ингредиента"')
    def wait_for_load_panel_ingredient_details(self):
        self.find_element(HomePageLocators.PANEL_INGREDIENT_DETAILS)

    @allure.step('Ожидание загрузки идентификатора заказа')
    def wait_for_load_order_id(self):
        self.find_element(HomePageLocators.ORDER_ID)

    @allure.step('Ожидание закрытия модального окна заказа')
    def wait_for_close_modal_panel(self):
        self.wait_for_close_modal_panel(HomePageLocators.MODAL_PANEL)

    @allure.step('Ожидание присвоения ID новому заказу')
    def wait_for_get_id_of_new_order(self):
        self.wait_for_get_id_order(HomePageLocators.ORDER_ID)
        self.wait_for_three_seconds()

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_button_personal_account(self):
        self.find_element(HomePageLocators.BUTTON_PERSONAL_ACCOUNT).click()

    @allure.step('Клик по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.find_element(HomePageLocators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_button_orders_feed(self):
        self.find_element(HomePageLocators.BUTTON_ORDERS_FEED).click()

    @allure.step('Клик по кнопке закрытия "Детали ингредиента"')
    def click_button_close_ingredient_details(self):
        self.find_element(HomePageLocators.BUTTON_CLOSE_INGREDIENT_DETAILS).click()

    @allure.step('Клик по кнопке "Флюоресцентная булка"')
    def click_button_fluorescent_bun(self):
        self.find_element(HomePageLocators.BUTTON_FLUORESCENT_BUN).click()

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_button_make_an_order(self):
        self.find_element(HomePageLocators.BUTTON_MAKE_AN_ORDER).click()

    @allure.step('Клик по кнопке закрытия окна с заказом')
    def click_button_close_order_panel(self):
        self.find_element(HomePageLocators.BUTTON_CLOSE_ORDER_PANEL).click()

    @allure.step('Проверка отображения окна "Детали ингредиента"')
    def check_panel_ingredient_details_is_displayed(self):
        return self.element_is_displayed(HomePageLocators.PANEL_INGREDIENT_DETAILS)

    @allure.step('Проверка что окно "Детали ингредиента" не отображается')
    def check_panel_ingredient_details_is_not_displayed(self):
        return self.element_is_not_displayed(HomePageLocators.PANEL_INGREDIENT_DETAILS)

    @allure.step('Проверка отображения окна "Конструктор"')
    def check_panel_constructor_is_displayed(self):
        return self.element_is_displayed(HomePageLocators.PANEL_CONSTRUCTOR)

    @allure.step('Проверка отображения идентификатора заказа')
    def check_order_id_is_displayed(self):
        return self.element_is_displayed(HomePageLocators.ORDER_ID)

    @allure.step('Проверка отображения каунтера ингредиента "2"')
    def check_ingredient_counter_2_is_displayed(self):
        return self.element_is_displayed(HomePageLocators.INGREDIENT_COUNTER_2)

    @allure.step('Перетаскивание флюоресцентной булки вверх для заказа')
    def drag_fluorescent_bun_to_up_target(self):
        self.drag_and_drop_element(HomePageLocators.BUTTON_FLUORESCENT_BUN, HomePageLocators.SPAN_TO_DRAG_UP)

    @allure.step('Получение ID нового заказа')
    def get_number_of_new_order(self):
        order_number = self.get_text_of_order_counter(HomePageLocators.ORDER_ID)
        return order_number
