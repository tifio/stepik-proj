from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        assert "/login" in self.url, "trouble in link"
        # реализуйте проверку на корректный url адрес


    def should_be_login_form(self):
        assert self.is_element_present(By.ID, "login_form"), "Login form is not presented"
        # реализуйте проверку, что есть форма логина


    def should_be_register_form(self):
        assert self.is_element_present(By.ID, "register_form"), "Register form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
