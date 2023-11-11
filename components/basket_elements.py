from time import sleep

from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from page_factory.button import Button
from page_factory.link import Link
from page_factory.text import Text
from page_factory.title import Title

BASKET = "//*[contains(@class, 'button-cart')]"
PRODUCT_CART = "div.slide-product.slick-slide.slick-current.slick-active"
BUTTON_BUY = "a.in-cart.buy.btn-cart-action"
SWITCH_TO_BASKET = "h1.product-title.section-main"
PRODUCT_IN_BASKET = "//*[contains(@class, 'prod-cart-name')]"
EMPTY_BASKET = "//*[contains(@class, 'no-cart')]"
NEXT_PRODUCTS = "//*[contains(@class, 'next slick-arrow')]"


class BasketElements:
    def __init__(self, page: Page):
        self.page = page

        self.basket = Link(page, locator=BASKET, name="Положите товар в корзину")
        self.click_on_product = Button(page, locator=PRODUCT_CART, name="В наличии")
        self.add_to_basket = Button(page, locator=BUTTON_BUY, name="купить")
        self.empty_basket = Title(page, locator=EMPTY_BASKET, name="Корзина пуста")
        self.switch_to_basket = Button(page, locator=SWITCH_TO_BASKET, name="Оформить заказ")
        self.product_in_basket = Text(page, locator=PRODUCT_IN_BASKET, name="Товар в корзине")
        self.next = Button(page, locator=NEXT_PRODUCTS, name="Next")

    def check_that_basket_is_empty(self):
        self.basket.should_have_text(" Положите товар в корзину \n Оформить заказ")
        sleep(2)

    def add_to_cart(self) -> None:
        self.click_on_product.click()
        sleep(1)
        self.add_to_basket.click()
        sleep(1)
        self.switch_to_basket.click()
        self.product_in_basket.should_be_visible()
        text = self.product_in_basket.get_text()
        self.product_in_basket.should_have_text(f'{text}')
