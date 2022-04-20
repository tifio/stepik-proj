from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import MainPageLocators




class ProductPage(BasePage):
    def should_be_button_add(self):
        link = self.browser.find_element(*MainPageLocators.BUTTON_LINK)
        # link = self.is_element_present(By.XPATH, "//form[@id='add_to_basket_form']/button"), "Button is not presented"
        link.click()







    # def add_button(self):
    #     link = self.browser.find_element(*MainPageLocators.BUTTON_LINK)
    #     link.click()

    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    # def idontknow(self):

    # pass