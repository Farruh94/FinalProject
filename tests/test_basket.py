from datetime import datetime

from components.basket_elements import BasketElements
from main import BASE_URL, BASKET_URL
from pages.basket import Basket


class TestBasket:

    def test_empty_basket(self, chromium_page, empty_basket: BasketElements):
        basket = Basket(chromium_page)
        basket.go_to(BASKET_URL)
        basket.basket_is_empty(empty_basket)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_not_empty_basket(self, chromium_page, not_empty: BasketElements):
        basket = Basket(chromium_page)
        basket.go_to(BASE_URL)

        basket.basket_with_product(not_empty)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
