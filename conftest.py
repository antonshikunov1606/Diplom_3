import allure
import pytest
from webdriver_factory import WebDriverFactory

from pages.home_page import HomePageStellar
from pages.login_page import LoginPageStellar


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests on"
    )


@allure.step('Открытие браузера')
@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = WebDriverFactory.get_webdriver(browser_name)
    driver.set_window_size(1280, 820)
    yield driver
    driver.quit()


@allure.step('Открытие главной страницы Stellar')
@pytest.fixture
def open_home_page(driver):
    home_page = HomePageStellar(driver)
    home_page.open_home_page()
    home_page.wait_for_load_home_page()


@allure.step('Открытие страницы Логина')
@pytest.fixture
def open_login_page(driver):
    login_page = LoginPageStellar(driver)
    login_page.open_login_page()
    login_page.wait_for_load_login_page()


@allure.step('Открытие страницы Логина и авторизация')
@pytest.fixture
def open_login_page_and_do_login(driver):
    login_page = LoginPageStellar(driver)
    login_page.open_login_page()
    login_page.wait_for_load_login_page()
    login_page.enter_email_in_login()
    login_page.enter_password_in_login()
    login_page.click_button_login()
    home_page = HomePageStellar(driver)
    home_page.wait_for_load_home_page()


@allure.step('Авторизация и создание заказа')
@pytest.fixture
def login_and_make_an_order(driver):
    login_page = LoginPageStellar(driver)
    login_page.open_login_page()
    login_page.wait_for_load_login_page()
    login_page.enter_email_in_login()
    login_page.enter_password_in_login()
    login_page.click_button_login()
    home_page = HomePageStellar(driver)
    home_page.wait_for_load_home_page()
    home_page.drag_fluorescent_bun_to_up_target()
    home_page.click_button_make_an_order()
    home_page.wait_for_get_id_of_new_order()
    home_page.click_button_close_order_panel()
