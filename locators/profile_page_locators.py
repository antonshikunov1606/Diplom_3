from selenium.webdriver.common.by import By


class ProfilePageLocators:
    BUTTON_ORDER_HISTORY = [By.XPATH, './/a[text()="История заказов"]']
    BUTTON_LOGOUT = [By.XPATH, './/button[text()="Выход"]']
    PANEL_ORDER_HISTORY = [By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]']
    PANEL_PROFILE = [By.XPATH, './/div[@class="Account_account__vgk_w"]']
    ORDER_NUMBER = [By.XPATH, './/p[@class="text text_type_digits-default"]']
    LIST_ORDERS = [By.XPATH, './/ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]/li']
