import time
from pages.product_page import ProductPage
from pages.base_page import BasePage


def test_guest_open(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    pageProduct = ProductPage(browser, link)
    pageProduct.open()
    pageProduct.should_be_button_add()
    pageProduct.solve_quiz_and_get_code()

    # browser.get(link)

    time.sleep(40)
    # pageProduct = ProductPage(browser, link)
    # pageProduct.add_button()


    # page2 = ProductPage(browser, link)
    # page2.add_button()


