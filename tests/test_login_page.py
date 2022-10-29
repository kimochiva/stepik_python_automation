from pages.login_page import LoginPage
import pytest

login_page_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

def test_login_page_url(browser):
    page = LoginPage(browser, login_page_url)
    page.open()
    page.should_be_login_page()

