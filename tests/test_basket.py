# from datetime import datetime
#
# from components.basket_elements import BasketElements
# from main import BASE_URL, BASKET_URL
# from pages.basket import Basket
#
#
# class TestBasket:
#
#     def test_empty_basket(self, browser, empty_basket: BasketElements):
#         basket = Basket(browser)
#         basket.go_to(BASKET_URL)
#         basket.basket_is_empty(empty_basket)
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_not_empty_basket(self, browser, not_empty: BasketElements):
#         basket = Basket(browser)
#         basket.go_to(BASE_URL)
#
#         basket.basket_with_product(not_empty)
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
