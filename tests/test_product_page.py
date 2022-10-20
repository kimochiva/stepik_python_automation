import time

from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5",
                                   "offer6", pytest.param("offer7", marks=pytest.mark.xfail),
                                   "offer8", "offer9", "offer10"])

def test_add_item_to_basket(browser, promo):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=" + promo
    page = ProductPage(browser, link)
    page.open()
    product_title = page.get_product_title()
    product_price = page.get_product_price()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.check_basket_product_title(product_title)
    page.check_basket_product_price(product_price)

