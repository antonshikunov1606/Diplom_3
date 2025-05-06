import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from test_data import URLCollection


class ProfilePageStellar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие страницы История заказов")
    def open_order_history_page(self):
        self.navigate(URLCollection.STELLAR_ORDER_HISTORY)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.find_element(ProfilePageLocators.ORDER_NUMBER).text

    @allure.step('Клик по кнопке "История заказов"')
    def click_button_order_history(self):
        self.click_element(ProfilePageLocators.BUTTON_ORDER_HISTORY)

    @allure.step('Клик по кнопке "Выход"')
    def click_button_logout(self):
        self.click_element(ProfilePageLocators.BUTTON_LOGOUT)

    @allure.step('Ожидание загрузки страницы личного кабинета')
    def wait_for_load_profile_page(self):
        self.wait_for_element(ProfilePageLocators.PANEL_PROFILE)

    @allure.step('Ожидание загрузки истории заказов')
    def wait_for_load_order_history(self):
        self.wait_for_element(ProfilePageLocators.PANEL_ORDER_HISTORY)

    @allure.step('Проверка отображения истории заказов')
    def check_order_history_is_displayed(self):
        return self.element_is_displayed(ProfilePageLocators.PANEL_ORDER_HISTORY)

    @allure.step('Получение номера последнего заказа')
    def get_last_item_text(self):
        last_item_text = self.get_text_of_last_list_item(ProfilePageLocators.LIST_ORDERS)
        return last_item_text
