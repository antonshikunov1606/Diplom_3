import allure
from pages.home_page import HomePageStellar
from pages.orders_feed_page import OrdersFeedPageStellar
from test_data import URLCollection


class TestHomePage:
    @allure.title('Проверка перехода по клику в "Конструктор"')
    def test_navigate_to_panel_constructor(self, driver, open_login_page):
        home_page = HomePageStellar(driver)
        home_page.click_button_constructor()
        home_page.wait_for_load_panel_constructor()

        assert home_page.check_panel_constructor_is_displayed() is True, 'Окно "Конструктор" не отобразилось'

    @allure.title('Проверка перехода по клику в "Лента заказов"')
    def test_navigate_to_panel_orders_feed(self, driver, open_home_page):
        home_page = HomePageStellar(driver)
        home_page.click_button_orders_feed()
        orders_feed_page = OrdersFeedPageStellar(driver)
        orders_feed_page.wait_for_load_panel_orders_feed()
        actual_result = orders_feed_page.get_current_url()
        expected_result = URLCollection.STELLAR_ORDERS_FEED_PAGE

        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'
        assert orders_feed_page.check_panel_orders_feed_is_displayed() is True, 'Окно "Конструктор" не отобразилось'

    @allure.title('Проверка всплывающего окна "Детали ингредиента"')
    def test_open_panel_ingredient_details(self, driver, open_home_page):
        home_page = HomePageStellar(driver)
        home_page.click_button_fluorescent_bun()
        home_page.wait_for_load_panel_ingredient_details()

        assert home_page.check_panel_ingredient_details_is_displayed() is True, \
            'Окно "Детали ингредиента" не отобразилось'

    @allure.title('Проверка закрытия окна "Детали ингредиента"')
    def test_close_panel_ingredient_details(self, driver, open_home_page):
        home_page = HomePageStellar(driver)
        home_page.click_button_fluorescent_bun()
        home_page.wait_for_load_panel_ingredient_details()
        home_page.click_button_close_ingredient_details()
        home_page.wait_for_load_home_page()

        assert home_page.check_panel_ingredient_details_is_not_displayed() is True, \
            'Окно "Детали ингредиента" отображается'

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении его в заказ')
    def test_increase_ingredient_counter_after_adding_it_to_the_order(self, driver, open_home_page):
        home_page = HomePageStellar(driver)
        home_page.drag_fluorescent_bun_to_up_target()

        assert home_page.check_ingredient_counter_2_is_displayed() is True, 'Каунтер до 2 не увеличился'

    @allure.title('Проверка оформления заказа под авторизованным пользователем')
    def test_successful_make_order_by_authorized_user(self, driver, open_login_page_and_do_login):
        home_page = HomePageStellar(driver)
        home_page.drag_fluorescent_bun_to_up_target()
        home_page.click_button_make_an_order()
        home_page.wait_for_load_order_id()

        assert home_page.check_order_id_is_displayed() is True, 'Заказ не оформлен'
