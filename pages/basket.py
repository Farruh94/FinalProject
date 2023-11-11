from playwright.sync_api import Page

from components.basket_elements import BasketElements
from pages.base_page import BasePage


class Basket(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @staticmethod
    def basket_is_empty(basket: BasketElements):
        basket.check_that_basket_is_empty()

    @staticmethod
    def basket_with_product(basket: BasketElements):
        basket.add_to_cart()
