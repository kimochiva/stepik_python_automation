from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(MainPage):
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    def should_be_login_page(self):
        self.login_url_is_correct()
        self.should_be_login_form()
        self.should_be_register_form()

    def login_url_is_correct(self):
        current_link = self.browser.current_url
        assert "/login" in  current_link, f"Login is not presented in url, url is:{current_link}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.input_text(LoginPageLocators.REGISTER_FORM_EMAIL, email)
        self.input_text(LoginPageLocators.REGISTER_FORM_PASSWORD, password)
        self.input_text(LoginPageLocators.REGISTER_FORM_PASSWORD_REPEAT, password)
        self.click_on(LoginPageLocators.REGISTER_BUTTON)
