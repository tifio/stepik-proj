from pages.base_page import BasePage
from pages.locators import MainPageLocators

class ProductPage(BasePage):
    def should_be_button_add(self):
        link = self.browser.find_element(*MainPageLocators.BUTTON_LINK)
        link.click()
