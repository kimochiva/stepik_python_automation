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

@pytest.mark.absent_element
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.absent_element
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.absent_element
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()

@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()