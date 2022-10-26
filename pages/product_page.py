from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def open(self):
        self.browser.get(self.url)

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def check_basket_product_title(self, expected_title):
        basket_product_title = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_TITLE).text
        assert basket_product_title == expected_title, f"Book name in basket: {basket_product_title}, should be: {expected_title}"

    def check_basket_product_price(self, expected_price):
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_PRICE).text
        assert basket_product_price  == expected_price, f"Book price in basket: {basket_product_price}, should be: {expected_price}"


    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_PRICE), \
            "Success message is presented"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_PRICE),"Success message is not disappeared"


