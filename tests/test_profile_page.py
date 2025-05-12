import allure
from pages.home_page import HomePageStellar
from pages.profile_page import ProfilePageStellar
from pages.login_page import LoginPageStellar
from test_data import URLCollection


class TestProfile:
    @allure.title('Проверка перехода в "Личный кабинет"')
    def test_navigate_to_profile_page(self, driver, open_login_page_and_do_login):
        home_page = HomePageStellar(driver)
        home_page.click_button_personal_account()
        profile_page = ProfilePageStellar(driver)
        profile_page.wait_for_load_profile_page()
        actual_result = profile_page.get_current_url()
        expected_result = URLCollection.STELLAR_PROFILE_PAGE

        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'

    @allure.title('Проверка перехода в "История заказов"')
    def test_navigate_to_order_history(self, driver, open_login_page_and_do_login):
        home_page = HomePageStellar(driver)
        home_page.click_button_personal_account()
        profile_page = ProfilePageStellar(driver)
        profile_page.wait_for_load_profile_page()
        profile_page.click_button_order_history()
        profile_page.wait_for_load_order_history()

        assert profile_page.check_order_history_is_displayed() is True, 'История заказов не отобразилась'

    @allure.title('Проверка выхода из аккаунта по кнопке "Выход"')
    def test_logout_from_account_by_button_logout(self, driver, open_login_page_and_do_login):
        home_page = HomePageStellar(driver)
        home_page.click_button_personal_account()
        profile_page = ProfilePageStellar(driver)
        profile_page.wait_for_load_profile_page()
        profile_page.click_button_logout()
        login_page = LoginPageStellar(driver)
        login_page.wait_for_load_login_page()
        actual_result = login_page.get_current_url()
        expected_result = URLCollection.STELLAR_LOGIN_PAGE

        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'
        assert login_page.check_login_panel_is_displayed() is True, 'Форма логина не отобразилась'
