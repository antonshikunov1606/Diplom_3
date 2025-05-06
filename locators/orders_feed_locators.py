from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    PANEL_ORDERS_FEED = [By.XPATH, './/div[@class="OrderFeed_orderFeed__2RO_j"]']
    BUTTON_ORDER = [By.XPATH, './/a[@class="OrderHistory_link__1iNby"]']
    PANEL_INFO_ABOUT_AN_ORDER = [By.XPATH, './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]']
    TOTAL_ORDER_COUNTER = [By.XPATH, './/div[2]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    TODAY_ORDER_COUNTER = [By.XPATH, './/div[3]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    ID_ORDER_IN_PROCCESS = [By.XPATH, './/div[1]/ul[2]/li[@class="text text_type_digits-default mb-2"]']
    ORDER_NUMBER = [By.XPATH, './/p[@class="text text_type_digits-default" and text()="{}"]']