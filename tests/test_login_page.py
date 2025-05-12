import allure
from pages.login_page import LoginPageStellar
from test_data import URLCollection


class TestLoginPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_navigate_to_page_recover_password(self, driver, open_login_page):
        login_page = LoginPageStellar(driver)
        login_page.wait_for_load_login_page()
        login_page.click_button_recover_password()
        login_page.wait_for_load_form_recover_password()
        actual_result = login_page.get_current_url()
        expected_result = URLCollection.STELLAR_FORGOT_PASSWORD_PAGE

        assert actual_result == expected_result, f'Ожидаемый адрес: {actual_result}, но получили: {expected_result}'

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    def test_enter_email_and_click_recover_in_page_recover_password(self, driver, open_login_page):
        login_page = LoginPageStellar(driver)
        login_page.wait_for_load_login_page()
        login_page.click_button_recover_password()
        login_page.wait_for_load_form_recover_password()
        login_page.enter_email_in_recover_textfield()
        login_page.click_button_recover()
        login_page.wait_for_load_button_save()

        assert login_page.check_button_save_is_displayed() is True, 'Кнопка "Сохранить" не отобразилась'

    @allure.title('Проверка клика по кнопке "показать", подсвечивающая пароль')
    def test_show_password_in_page_recover_password(self, driver, open_login_page):
        login_page = LoginPageStellar(driver)
        login_page.wait_for_load_login_page()
        login_page.click_button_recover_password()
        login_page.wait_for_load_form_recover_password()
        login_page.enter_email_in_recover_textfield()
        login_page.click_button_recover()
        login_page.wait_for_load_button_save()
        login_page.enter_password_in_recover_textfield()
        login_page.click_button_toggle_password_visibility()

        assert login_page.check_password_is_displayed() is True, 'Введённый пароль не подсвечивается'
