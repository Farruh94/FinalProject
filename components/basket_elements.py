from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from page_factory.button import Button
from page_factory.checkbox import CheckBox
from page_factory.input import Input
from page_factory.link import Link
from page_factory.text import Text
from page_factory.title import Title

BASKET = "//*[contains(@class, 'button-cart')]"
PRODUCT_CART = "div.slide-product.slick-slide.slick-current.slick-active"
BUTTON_BUY = "a.in-cart.buy.btn-cart-action"
SWITCH_TO_BASKET = "h1.product-title.section-main"
PRODUCT_IN_BASKET = "//*[contains(@class, 'prod-cart-name')]"
EMPTY_BASKET = "//*[contains(@class, 'no-cart')]"
CART_FORM = "//* [@class='cart-form']"
NAME = "[id=order-name]"
PHONE = "[id=order-phone]"
SHOP_ADDRESS = "[id=ord1]"
PAYMENT = "[id=payment3]"
DELIVERY_SPB = "[id=cart-dspb]"
DELIVERY_ADDRESS = "[id=order-address]"
DELIVERY_TYPE = "[id=ord5]"

class BasketElements:
    def __init__(self, page: Page):
        self.page = page

        self.cart_form = Text(page, locator=CART_FORM, name="Форма")
        self.basket = Link(page, locator=BASKET, name="Положите товар в корзину")
        self.click_on_product = Button(page, locator=PRODUCT_CART, name="В наличии")
        self.add_to_basket = Button(page, locator=BUTTON_BUY, name="купить")
        self.empty_basket = Title(page, locator=EMPTY_BASKET, name="Корзина пуста")
        self.switch_to_basket = Button(page, locator=SWITCH_TO_BASKET, name="Оформить заказ")
        self.product_in_basket = Text(page, locator=PRODUCT_IN_BASKET, name="Товар в корзине")
        self.name_input = Input(page, locator=NAME, name="Ваше имя")
        self.phone_input = Input(page, locator=PHONE, name="Ваш телефон")
        self.shop_address = CheckBox(page, locator=SHOP_ADDRESS, name="Адрес")
        self.payment_type = CheckBox(page, locator=PAYMENT, name="Оплата")
        self.delivery_spb = Button(page, locator=DELIVERY_SPB, name="Доставка по СПб")
        self.delivery_address = Input(page, locator=DELIVERY_ADDRESS, name="Адрес")
        self.delivery_type = CheckBox(page, locator=DELIVERY_TYPE, name="Срочная доставка")

    def check_that_basket_is_empty(self):
        text = self.basket.get_text()

        self.basket.should_have_text(text)

    def add_to_cart(self) -> None:
        self.click_on_product.click()
        self.add_to_basket.click()
        self.switch_to_basket.click()

        self.cart_form.should_be_visible()
        self.product_in_basket.should_be_visible()
        product_text = self.product_in_basket.get_text()
        self.product_in_basket.should_have_text(product_text)

    def pickup_product(self, name: str, phone: str) -> None:

        self.click_on_product.click()
        self.add_to_basket.click()
        self.switch_to_basket.click()
        self.shop_address.check()
        self.payment_type.check()
        self.name_input.fill(name, validate_value=True)
        self.phone_input.fill(phone, validate_value=False)

        self.cart_form.should_be_visible()
        self.shop_address.is_checked()
        self.payment_type.is_checked()
        self.name_input.should_have_value(name)
        self.phone_input.should_be_visible()

    def delivery_product_spb(self, name: str, phone: str, address: str) -> None:

        self.click_on_product.click()
        self.add_to_basket.click()
        self.switch_to_basket.click()
        self.delivery_spb.click()

        self.name_input.fill(name, validate_value=True)
        self.phone_input.fill(phone, validate_value=False)
        self.delivery_address.fill(address, validate=True)
        self.payment_type.check()

        self.delivery_type.is_checked()
        self.payment_type.is_checked()
        self.name_input.should_have_value(name)
        self.phone_input.should_be_visible()
        self.delivery_address.should_have_value(address)




