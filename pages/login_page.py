from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(MainPage):
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    def should_be_login_page(self):
        self.login_url_is_correct()
        self.should_be_login_form()
        self.should_be_register_form()

    def login_url_is_correct(self):
        # реализуйте проверку на корректный url адрес
        current_link = self.browser.current_url
        assert "/login" in  current_link, f"Login is not presented in url, url is:{current_link}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
