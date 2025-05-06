import allure
from pages.home_page import HomePageStellar
from pages.orders_feed_page import OrdersFeedPageStellar
from pages.profile_page import ProfilePageStellar


class TestOrdersFeed:
    @allure.title('Проверка открытия информации о заказе по клику на кнопку заказа')
    def test_open_info_about_an_order_by_clicking_on_order(self, driver, open_home_page):
        home_page = HomePageStellar(driver)
        home_page.click_button_orders_feed()
        orders_feed_page = OrdersFeedPageStellar(driver)
        orders_feed_page.wait_for_load_panel_orders_feed()
        orders_feed_page.click_button_order()
        orders_feed_page.wait_for_load_info_about_an_order()

        assert orders_feed_page.check_info_about_an_order_is_displayed() is True, \
            'Информация о заказе не отобразилась'

    @allure.title('Проверка отображения заказа из раздела "История заказов" на странице "Лента заказов"')
    def test_order_display_in_orders_feed_from_order_history(self, driver, login_and_make_an_order):
        home_page = HomePageStellar(driver)
        home_page.click_button_personal_account()
        profile_page = ProfilePageStellar(driver)
        profile_page.wait_for_load_profile_page()
        profile_page.click_button_order_history()
        profile_page.wait_for_load_order_history()
        order_number = profile_page.get_last_item_text()
        home_page = HomePageStellar(driver)
        home_page.click_button_orders_feed()
        orders_feed_page = OrdersFeedPageStellar(driver)
        orders_feed_page.wait_for_load_panel_orders_feed()

        assert orders_feed_page.check_order_in_orders_feed_is_displayed(order_number) is True, 'Заказ не отобразился'

    @allure.title('Проверка увеличение счётчика "Выполнено за всё время" после заказа')
    def test_total_orders_counter_increases_after_new_order(self, driver, open_login_page_and_do_login):
        home_page = HomePageStellar(driver)
        home_page.click_button_orders_feed()
        orders_feed_page = OrdersFeedPageStellar(driver)
        orders_feed_page.wait_for_load_panel_orders_feed()
        order_counter = orders_feed_page.get_total_order_counter()
        home_page = HomePageStellar(driver)
        home_page.click_button_constructor()
        home_page.wait_for_load_panel_constructor()
        home_page.drag_fluorescent_bun_to_up_target()
        home_page.click_button_make_an_order()
        home_page.wait_for_get_id_of_new_order()
        home_page.click_button_close_order_panel()
        home_page.click_button_orders_feed()
        orders_feed_page = OrdersFeedPageStellar(driver)
        orders_feed_page.wait_for_load_panel_orders_feed()
        new_order_counter = orders_feed_page.get_total_order_counter()

        assert new_order_counter > order_counter, \
            'При создании нового заказа счётчик "Выполнено за всё время" не увеличился'

    @allure.title('Проверка увеличение счётчика "Выполнено за сегодня" после заказа')
    def test_today_counter_increases_after_new_order(self, driver, open_login_page_and_do_login):
        home_page = HomePageStellar(driver)
        home_page.click_button_orders_feed()
        orders_feed_page = OrdersFeedPageStellar(driver)
        orders_feed_page.wait_for_load_panel_orders_feed()
        order_counter = orders_feed_page.get_today_order_counter()
        home_page = HomePageStellar(driver)
        home_page.click_button_constructor()
        home_page.wait_for_load_panel_constructor()
        home_page.drag_fluorescent_bun_to_up_target()
        home_page.click_button_make_an_order()
        home_page.wait_for_get_id_of_new_order()
        home_page.click_button_close_order_panel()
        home_page.click_button_orders_feed()
        orders_feed_page = OrdersFeedPageStellar(driver)
        orders_feed_page.wait_for_load_panel_orders_feed()
        new_order_counter = orders_feed_page.get_today_order_counter()

        assert new_order_counter > order_counter, \
            'При создании нового заказа счётчик "Выполнено за сегодня" не увеличился'

    @allure.title('Проверка отображения заказа в "В работе')
    def test_order_in_process_is_displayed(self, driver, open_login_page_and_do_login):
        home_page = HomePageStellar(driver)
        home_page.drag_fluorescent_bun_to_up_target()
        home_page.click_button_make_an_order()
        home_page.wait_for_get_id_of_new_order()
        order_number = home_page.get_number_of_new_order()
        home_page.click_button_close_order_panel()
        home_page.click_button_orders_feed()
        orders_feed_page = OrdersFeedPageStellar(driver)
        orders_feed_page.wait_for_load_panel_orders_feed()
        orders_feed_page.wait_for_load_order_in_process()
        order_number_in_process = orders_feed_page.get_number_of_order_in_process()
        order_number_in_process = order_number_in_process[1:]

        assert order_number == order_number_in_process, \
            'После оформления заказ "В работе" не отобразился'
