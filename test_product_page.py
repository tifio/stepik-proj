import time
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



########################## -----первая реализация тестов на память----- ##########################

# def test_guest_open(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     pageProduct = ProductPage(browser, link)
#     pageProduct.open()
#     pageProduct.should_be_button_add()
#     pageProduct.solve_quiz_and_get_code()
#     pageProduct.should_be_name_book()
#     pageProduct.should_be_cost()
#
#     time.sleep(2)


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


