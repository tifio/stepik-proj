from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        expected_status = self.browser.find_element_by_css_selector("#content_inner>p")
       # print(expected_status.text)
        assert "Your basket is empty. Continue shopping" == expected_status.text, "basket not empty"

    def should_not_be_item_product(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), "item in basket"


