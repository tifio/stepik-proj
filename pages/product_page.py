from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_add(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_LINK)
        link.click()



    def should_be_name_book(self):
        actual_name = self.browser.find_element_by_css_selector("#messages>.alert>.alertinner>strong")
        print(actual_name.text)
        expected_name = self.browser.find_element_by_css_selector(".breadcrumb>li.active")
        print(expected_name.text)
        assert expected_name.text == actual_name.text, "Wrong name a book"


    def should_be_cost(self):
        actual_price = self.browser.find_element_by_css_selector("#messages>.alert:last-child>.alertinner>p>strong")
        print(actual_price.text)
        expected_price = self.browser.find_element_by_css_selector(".product_main>p.price_color")
        print(expected_price.text)
        assert expected_price.text == actual_price.text, "Wrong price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
