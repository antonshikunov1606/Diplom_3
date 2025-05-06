import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.orders_feed_locators import OrdersFeedLocators
from locators.profile_page_locators import ProfilePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

    def find_order_by_text(self, text, timeout=10):
        locator = (By.XPATH, OrdersFeedLocators.ORDER_NUMBER.format(text))
        return self.find_element(locator, timeout)

    def get_text_of_order_counter(self, locator):
        counter = self.find_element(locator)
        return counter.text

    def get_text_of_new_order(self, locator):
        order_number = self.find_element(locator)
        return order_number.text

    def get_text_of_last_list_item(self, locator):
        elements = self.driver.find_elements(*locator)

        if elements:
            last_element = elements[-1]
            text_element = last_element.find_element(ProfilePageLocators.ORDER_NUMBER)
            return text_element.text
        else:
            raise ValueError("Элементы не найдены.")

    def wait_for_get_id_order(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.driver.find_element(*locator).text != "9999"
        )

    def order_is_displayed(self, text):
        locator = (By.XPATH, OrdersFeedLocators.ORDER_NUMBER.format(text))
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    def element_is_displayed(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    def element_is_not_displayed(self, locator):
        WebDriverWait(self.driver, 20).until_not(EC.visibility_of_element_located(locator))
        return True

    def wait_for_three_seconds(self):
        time.sleep(3)

    def drag_and_drop_element(self, source_locator, target_locator, timeout=10):
        source_element = self.find_element(source_locator, timeout)
        target_element = self.find_element(target_locator, timeout)

        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element)
        actions.move_to_element(target_element)
        actions.release(target_element)
        actions.perform()
