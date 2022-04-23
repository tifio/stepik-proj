from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        """Объединяем проверки"""

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка правильного URL страницы логин"""

        assert "/login" in self.url, "trouble in link"

    def should_be_login_form(self):
        """Проверка наличия формы логина"""

        assert self.is_element_present(By.ID, "login_form"), "Login form is not presented"

    def should_be_register_form(self):
        """Проверка наличия формы регистрации"""

        assert self.is_element_present(By.ID, "register_form"), "Register form is not presented"


    def register_new_user(self, email, password):
        """Поиск полей для регистрации нового пользователя, и заполнение их и отправка данных"""

        emailForReg = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        emailForReg.send_keys(email)
        emailForReg = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1)
        emailForReg.send_keys(password)
        emailForReg = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2)
        emailForReg.send_keys(password)
        ButtonReg = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        ButtonReg.click()






