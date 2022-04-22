import time

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest


@pytest.mark.parametrize('promo_offer', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    pageProduct = ProductPage(browser, link)
    pageProduct.open()
    pageProduct.should_be_button_add()
    pageProduct.solve_quiz_and_get_code()
    pageProduct.should_be_name_book()
    pageProduct.should_be_cost()
    time.sleep(1)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Sucsess messege isnt disappeared'

########################## -----первая реализация тестов на память----- ##########################

# def test_guest_open(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     pageProduct = ProductPage(browser, link)
#     pageProduct.open()
#     # pageProduct.should_not_be_success_message()
#     pageProduct.should_be_button_add()
#     pageProduct.solve_quiz_and_get_code()
#     pageProduct.should_be_name_book()
#     pageProduct.should_be_cost()
#     # pageProduct.should_disappeared()
#
#
#     time.sleep(200)



# @pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", "7", "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     pageProduct = ProductPage(browser, link)
#     pageProduct.open()
#     pageProduct.should_be_button_add()
#     pageProduct.solve_quiz_and_get_code()
#     pageProduct.should_be_name_book()
#     pageProduct.should_be_cost()
#     time.sleep(1)


