import time

from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest


def test_add_item_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_title = page.get_product_title()
    product_price = page.get_product_price()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.check_basket_product_title(product_title)
    page.check_basket_product_price(product_price)
    time.sleep(5)
