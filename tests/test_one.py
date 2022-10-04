import pytest
from selenium.webdriver.common.by import By


class TestMainPage1:
    link = "http://selenium1py.pythonanywhere.com/"

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(self.link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(self.link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(self.link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")
# дока по Skip and xfail: dealing with tests that cannot succeed. https://pytest.org/en/stable/how-to/skipping.html
