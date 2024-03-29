from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LINK_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')

class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_MESSAGE_PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages div:first-child strong")
    BASKET_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")

class BasketPageLocators:
    EMPTY_BASKET_INNER_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket-items")




