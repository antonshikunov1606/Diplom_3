import allure

from locators.orders_feed_locators import OrdersFeedLocators
from pages.base_page import BasePage


class OrdersFeedPageStellar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки окна "Лента заказов"')
    def wait_for_load_panel_orders_feed(self):
        self.wait_for_element(OrdersFeedLocators.PANEL_ORDERS_FEED)

    @allure.step('Проверка отображения окна "Лента заказов"')
    def check_panel_orders_feed_is_displayed(self):
        return self.element_is_displayed(OrdersFeedLocators.PANEL_ORDERS_FEED)

    @allure.step('Клик по заказу')
    def click_button_order(self):
        self.click_element(OrdersFeedLocators.BUTTON_ORDER)

    @allure.step('Поиск элемента с текстом')
    def find_order_by_number(self, order_number):
        return self.find_order_by_text(order_number)

    @allure.step('Ожидание загрузки информации о заказе')
    def wait_for_load_info_about_an_order(self):
        self.wait_for_element(OrdersFeedLocators.PANEL_INFO_ABOUT_AN_ORDER)

    @allure.step('Ожидание загрузки заказа "В работе"')
    def wait_for_load_order_in_process(self):
        self.wait_for_element(OrdersFeedLocators.ID_ORDER_IN_PROCCESS)

    @allure.step('Проверка отображения информации о заказе')
    def check_info_about_an_order_is_displayed(self):
        return self.element_is_displayed(OrdersFeedLocators.PANEL_INFO_ABOUT_AN_ORDER)

    @allure.step('Проверка отображения заказа в ленте заказов')
    def check_order_in_orders_feed_is_displayed(self, order_number):
        return self.order_is_displayed(order_number)

    @allure.step('Получение счётчика заказов за всё время')
    def get_total_order_counter(self):
        total_orders = self.get_text_of_order_counter(OrdersFeedLocators.TOTAL_ORDER_COUNTER)
        return total_orders

    @allure.step('Получение счётчика заказов за сегодня')
    def get_total_order_counter(self):
        total_orders = self.get_text_of_order_counter(OrdersFeedLocators.TOTAL_ORDER_COUNTER)
        return total_orders

    @allure.step('Получение счётчика заказов за сегодня')
    def get_today_order_counter(self):
        order_number = self.get_text_of_new_order(OrdersFeedLocators.ID_ORDER_IN_PROCCESS)
        return order_number

    @allure.step('Получение ID нового заказа')
    def get_number_of_order_in_process(self):
        order_number = self.get_text_of_order_counter(OrdersFeedLocators.ID_ORDER_IN_PROCCESS)
        return order_number
