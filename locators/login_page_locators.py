from selenium.webdriver.common.by import By


class LoginPageLocators:
    PANEL_LOGIN = [By.XPATH, './/div[@class="Auth_login__3hAey"]']
    FORM_RECOVER_PASSWORD = [By.XPATH, './/form[@class="Auth_form__3qKeq mb-20"]']
    BUTTON_RECOVER_PASSWORD = [By.XPATH, './/a[text()="Восстановить пароль"]']
    BUTTON_RECOVER = [By.XPATH, './/button[text()="Восстановить"]']
    BUTTON_SAVE = [By.XPATH, './/button[text()="Сохранить"]']
    BUTTON_LOGIN = [By.XPATH, './/button[text()="Войти"]']
    BUTTON_TOGGLE_PASSWORD_VISIBILITY = [By.XPATH, './/div[@class="input__icon input__icon-action"]']
    INPUT_EMAIL_RECOVER_TEXTFIELD = [By.XPATH, './/input[@class="text input__textfield text_type_main-default"]']
    INPUT_PASSWORD_RECOVER_TEXTFIELD = [By.XPATH, './/input[@name="Введите новый пароль"]']
    INPUT_EMAIL = [By.XPATH, './/input[@type="text" and @name="name"]']
    INPUT_PASSWORD = [By.XPATH, './/input[@type="password" and @name="Пароль"]']
    FIELD_WITH_HIDDEN_PASSWORD = [By.XPATH, './/input[@type="password" and @name="Введите новый пароль"]']
    FIELD_WITH_SHOWN_PASSWORD = [By.XPATH, './/input[@type="text" and @name="Введите новый пароль"]']
