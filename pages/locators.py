from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_LINK = (By.XPATH, "//form[@id='add_to_basket_form']/button")
