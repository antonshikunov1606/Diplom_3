base_url = 'https://stellarburgers.nomoreparties.site'


class URLCollection:
    STELLAR_HOME_PAGE = f'{base_url}/'
    STELLAR_LOGIN_PAGE = f'{base_url}/login'
    STELLAR_PROFILE_PAGE = f'{base_url}/account/profile'
    STELLAR_ORDERS_FEED_PAGE = f'{base_url}/feed'
    STELLAR_ORDER_HISTORY = f'{base_url}/account/order-history'
    STELLAR_FORGOT_PASSWORD_PAGE = f'{base_url}/forgot-password'


class TestData:
    EMAIL_TO_RECOVER = 'test_email@yandex.ru'
    PASSWORD_TO_RECOVER = 'qwerty'


test_data_for_login = {
    "email": "anton_shikunov_19998@yandex.ru",
    "password": "qwerty"
}
