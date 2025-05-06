import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from test_data import URLCollection, TestData, test_data_for_login


class LoginPageStellar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие страницы логина")
    def open_login_page(self):
        self.navigate(URLCollection.STELLAR_LOGIN_PAGE)

    @allure.step('Ожидание загрузки страницы Логина')
    def wait_for_load_login_page(self):
        self.wait_for_element(LoginPageLocators.PANEL_LOGIN)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_button_recover_password(self):
        self.click_element(LoginPageLocators.BUTTON_RECOVER_PASSWORD)

    @allure.step('Ожидание загрузки формы восстановления пароля')
    def wait_for_load_form_recover_password(self):
        self.wait_for_element(LoginPageLocators.FORM_RECOVER_PASSWORD)

    @allure.step('Ввод email в поле логина')
    def enter_email_in_login(self):
        self.enter_text(LoginPageLocators.INPUT_EMAIL, test_data_for_login['email'])

    @allure.step('Ввод password в поле логина')
    def enter_password_in_login(self):
        self.enter_text(LoginPageLocators.INPUT_PASSWORD, test_data_for_login['password'])

    @allure.step('Ввод email в поле восстановления пароля')
    def enter_email_in_recover_textfield(self):
        self.enter_text(LoginPageLocators.INPUT_EMAIL_RECOVER_TEXTFIELD, TestData.EMAIL_TO_RECOVER)

    @allure.step('Ввод пароль в поле восстановления пароля')
    def enter_password_in_recover_textfield(self):
        self.enter_text(LoginPageLocators.INPUT_PASSWORD_RECOVER_TEXTFIELD, TestData.PASSWORD_TO_RECOVER)

    @allure.step('Клик по кнопке "Войти"')
    def click_button_login(self):
        self.click_element(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_button_recover(self):
        self.click_element(LoginPageLocators.BUTTON_RECOVER)

    @allure.step('Ожидание загрузки кнопки "Сохранить"')
    def wait_for_load_button_save(self):
        self.wait_for_element(LoginPageLocators.BUTTON_SAVE)

    @allure.step('Проверка отображения формы логина')
    def check_login_panel_is_displayed(self):
        return self.element_is_displayed(LoginPageLocators.PANEL_LOGIN)

    @allure.step('Проверка отображения кнопки "Сохранить"')
    def check_button_save_is_displayed(self):
        return self.element_is_displayed(LoginPageLocators.BUTTON_SAVE)

    @allure.step('Проверка отображения пароля в форме "Восстановление пароля"')
    def check_password_is_displayed(self):
        return self.element_is_displayed(LoginPageLocators.FIELD_WITH_SHOWN_PASSWORD)

    @allure.step('Клик по кнопке "Показать/спрятать пароль"')
    def click_button_toggle_password_visibility(self):
        self.click_element(LoginPageLocators.BUTTON_TOGGLE_PASSWORD_VISIBILITY)
