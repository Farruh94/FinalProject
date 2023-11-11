from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from components.sidebar import SideBar
from page_factory.button import Button

APPLE = "//*[contains(@href, 'catalog/phones/apple') and contains(., 'Apple')]"
SAMSUNG = "//*[contains(@href, 'catalog/phones/samsung') and contains(., 'Samsung')]"
XIAOMI = "//*[contains(@href, 'catalog/phones/xiaomi') and contains(., 'Xiaomi')]"
SONY = "//*[contains(@href, 'catalog/phones/sony') and contains(., 'Sony')]"
HUAWEI = "//*[contains(@href, 'catalog/phones/huawei') and contains(., 'Huawei')]"
REALME = "//*[contains(@href, 'catalog/phones/realme') and contains(., 'Realme')]"
NUBIA = "//*[contains(@href, 'catalog/phones/nubia') and contains(., 'Nubia')]"
ASUS = "//*[contains(@href, 'catalog/phones/asus') and contains(., 'Asus')]"
BLACKVIEW = "//*[contains(@href, 'catalog/phones/blackview') and contains(., 'Blackview')]"
ZTE = "//*[contains(@href, 'catalog/phones/zte') and contains(., 'zte')]"
ONEPLUS = "//*[contains(@href, 'catalog/phones/oneplus') and contains(., 'OnePlus')]"
GOOGLE = "//*[contains(@href, 'catalog/phones/google') and contains(., 'Google')]"
OTHER = "//*[contains(@href, 'catalog/phones/other') and contains(., 'Другие телефоны')]"


class SubMenu(SideBar):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.apple = Button(page, locator=APPLE, name="Apple")
        self.samsung = Button(page, locator=SAMSUNG, name="Samsung")
        self.xiaomi = Button(page, locator=XIAOMI, name="Xiaomi")
        self.sony = Button(page, locator=SONY, name="Sony")
        self.huawei = Button(page, locator=HUAWEI, name="Huawei")
        self.realme = Button(page, locator=REALME, name="Realme")
        self.nubia = Button(page, locator=NUBIA, name="Nubia")
        self.asus = Button(page, locator=ASUS, name="Asus")
        self.blackview = Button(page, locator=BLACKVIEW, name="Blackview")
        self.zte = Button(page, locator=ZTE, name="zte")
        self.oneplus = Button(page, locator=ONEPLUS, name="OnePlus")
        self.google = Button(page, locator=GOOGLE, name="Google")
        self.other = Button(page, locator=OTHER, name="Другие телефоны")

    def sub_menu_items(self):
        self.apple.should_be_visible()
        self.samsung.should_be_visible()
        self.xiaomi.should_be_visible()
        self.sony.should_be_visible()
        self.realme.should_be_visible()
        self.nubia.should_be_visible()
        self.zte.should_be_visible()
        self.oneplus.should_be_visible()
        self.google.should_be_visible()
        self.other.should_be_visible()

    def apple(self):
        self.mobile_hover()
        self.apple.should_have_text("Apple")
