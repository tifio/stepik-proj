from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
    BASKET_LINK = (By.LINK_TEXT, "View basket")
    SUCCESS_MESSAGE = (By.ID, "basket_formset")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD1 = (By.ID, "id_registration-password1")
    PASSWORD_FIELD2 = (By.ID, "id_registration-password2")
    BUTTON_REG = (By.XPATH, "//button[contains(text(),'Register')]")

