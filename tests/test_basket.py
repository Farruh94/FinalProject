from datetime import datetime

import pytest

from components.basket_elements import BasketElements
from main import BASE_URL, BASKET_URL
from pages.basket import Basket


class TestBasket:

    def test_empty_basket(self, browser, basket_page: BasketElements):
        basket = Basket(browser)
        basket.go_to(BASKET_URL)
        basket.basket_is_empty(basket_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_not_empty_basket(self, browser, basket_page: BasketElements):
        basket = Basket(browser)
        basket.go_to(BASE_URL)

        basket.basket_with_product(basket_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    @pytest.mark.parametrize("phone", ["9999999999"])
    @pytest.mark.parametrize("name", ["Farruh"])
    def test_pickup_form(self, name, phone, browser, basket_page: BasketElements):
        check_user_info = Basket(browser)
        check_user_info.go_to(BASE_URL)
        check_user_info.pickup_order(name=name, phone=phone, pickup=basket_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    @pytest.mark.parametrize("address", ["ул. Восстания 1"])
    @pytest.mark.parametrize("phone", ["9995232145"])
    @pytest.mark.parametrize("name", ["Никита"])
    def test_delivery_form(self, name, phone, address, browser, basket_page: BasketElements):
        check_delivery_form = Basket(browser)
        check_delivery_form.go_to(BASE_URL)
        check_delivery_form.order_delivery(name=name, phone=phone, address=address, delivery=basket_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
