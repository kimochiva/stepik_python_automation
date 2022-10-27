from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_text(self):
        basket_inner_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_INNER_TEXT).text
        assert "Your basket is empty." in basket_inner_text, f"Empty basket inner text is: {basket_inner_text}, should be: 'Your basket is empty.'"

    def should_not_be_items_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Items are presented in empty basket"



