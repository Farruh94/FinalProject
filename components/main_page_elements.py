from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from page_factory.button import Button
from page_factory.link import Link
from page_factory.text import Text
from page_factory.title import Title

LOGO = "//div[@class='logo']"
# addresses
KIROCHNAYA = "//*[@class = 'kirochnaya']"
MOSKOVSKIY = "body > header > div > div.town-address > div.address-info > div:nth-child(2) > div > p"
ENGELSA = "body > header > div > div.town-address > div.address-info > div:nth-child(3) > div > p"

# social_media
TELEGRAM = "//*[contains(@href ,'tg') and contains(@target, 'blank')]"
WHATSAPP = "//*[contains(@href ,'api.whatsapp') and contains(@target, 'blank')]"
VK = "//*[contains(@href ,'vk.com') and contains(@target, 'blank')]"

# service
DELIVERY = ("//div[contains(@class, 'dop-menu')] //a[(contains(@class, 'hide1440')) and (contains(., 'Доставка и "
            "оплата'))]")
CREDIT = "//div[contains(@class, 'dop-menu')] // a[(contains(., 'Кредит'))]"
SERVICE_PAGE = "//*[contains(@class, 'product-title section-main')]"
TRADE_IN = "//div[contains(@class, 'dop-menu')] // a[(contains(., 'Обмен'))]"


class MainPageElements:
    def __init__(self, page: Page):
        self.page = page

        self.logo = Text(page, locator=LOGO, name="Центр Связи")
        self.kirochnaya = Text(page, locator=KIROCHNAYA, name="СПб, ул. Кирочная 18 ")
        self.moskovskiy = Text(page, locator=MOSKOVSKIY, name="Московский пр.64")
        self.engelsa = Text(page, locator=MOSKOVSKIY, name="пр. Энгельса 124 к1  ")
        self.telegram = Button(page, locator=TELEGRAM, name="Telegram")
        self.whatsapp = Button(page, locator=WHATSAPP, name="Whatsapp")
        self.vk = Button(page, locator=VK, name="VK")
        self.delivery = Link(page, locator=DELIVERY, name="Доставка и оплата")
        self.delivery_page = Title(page, locator=SERVICE_PAGE, name="Доставка и оплата")
        self.credit = Link(page, locator=CREDIT, name="Кредит")
        self.credit_page = Title(page, locator=SERVICE_PAGE, name="Кредит")
        self.trade_in = Link(page, locator=TRADE_IN, name="Обмен")
        self.trade_in_page = Title(page, locator=SERVICE_PAGE, name="Обменяй старый телефон или планшет на новый!")

    def check_that_logo_is_visible(self):
        self.logo.should_be_visible()

    def check_addresses(self):
        self.kirochnaya.should_be_visible()
        self.moskovskiy.should_be_visible()
        self.engelsa.should_be_visible()

    def check_social_media(self):
        self.telegram.should_be_visible()
        self.whatsapp.should_be_visible()
        self.vk.should_be_visible()

    def check_delivery(self):
        delivery_text = self.delivery.get_text()

        self.delivery.should_have_text(delivery_text)
        self.delivery.should_be_visible()
        self.delivery.click()

    def check_credit(self):
        self.credit.click()

        self.credit.should_be_visible()
        self.credit.should_have_text("Кредит")
        self.credit_page.should_be_visible()

    def check_trade_in(self):
        self.trade_in.click()
        self.trade_in.should_be_visible()

        self.trade_in.should_have_text("Обмен")
        self.trade_in_page.should_be_visible()
