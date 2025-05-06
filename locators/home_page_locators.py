from selenium.webdriver.common.by import By


class HomePageLocators:
    PANEL_HOME_PAGE = [By.CLASS_NAME, 'BurgerIngredients_ingredients__1N8v2']
    PANEL_INGREDIENT_DETAILS = [By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]']
    PANEL_CONSTRUCTOR = [By.XPATH, './/div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]']
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH, './/p[text()="Личный Кабинет"]']
    BUTTON_CONSTRUCTOR = [By.XPATH, './/p[text()="Конструктор"]']
    BUTTON_ORDERS_FEED = [By.XPATH, './/p[text()="Лента Заказов"]']
    BUTTON_CLOSE_INGREDIENT_DETAILS = [By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]']
    BUTTON_FLUORESCENT_BUN = [By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]']
    BUTTON_MAKE_AN_ORDER = [By.XPATH, './/button[text()="Оформить заказ"]']
    SPAN_TO_DRAG_UP = [By.XPATH, './/span[text()="Перетяните булочку сюда (верх)"]']
    INGREDIENT_COUNTER_2 = [By.XPATH, './/p[@class="counter_counter__num__3nue1" and text()="2"]']
    ORDER_ID = [By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]']
    BUTTON_CLOSE_ORDER_PANEL = [By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]']
    MODAL_PANEL = [By.XPATH, './/div[@class="Modal_modal_overlay__x2ZCr"]']
