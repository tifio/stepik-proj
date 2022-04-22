from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    BUTTON_LINK = (By.XPATH, "//form[@id='add_to_basket_form']/button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".product_main>p.price_color")
    SUCCESS_MESSAGE_HIDE = (By.CSS_SELECTOR, "#messages>.alert:first-child")


