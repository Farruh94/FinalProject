from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from components.sidebar_elements import SideBar
from page_factory.button import Button
from page_factory.title import Title

# mobile phone categories
APPLE = "//*[contains(@href, 'catalog/phones/apple') and contains(., 'Apple')]"
SAMSUNG = "//*[contains(@href, 'catalog/phones/samsung') and contains(., 'Samsung')]"
XIAOMI = "//*[contains(@href, 'catalog/phones/xiaomi') and contains(., 'Xiaomi')]"
SONY = "//*[contains(@href, 'catalog/phones/sony') and contains(., 'Sony')]"
HUAWEI = "//*[contains(@href, 'catalog/phones/huawei') and contains(., 'Huawei')]"
REALME = "//*[contains(@href, 'catalog/phones/realme') and contains(., 'Realme')]"
ASUS = "//*[contains(@href, 'catalog/phones/asus') and contains(., 'Asus')]"
BLACKVIEW = "//*[contains(@href, 'catalog/phones/blackview') and contains(., 'Blackview')]"
ZTE = "//*[contains(@href, 'catalog/phones/zte') and contains(., 'zte')]"
ONEPLUS = "//*[contains(@href, 'catalog/phones/oneplus') and contains(., 'OnePlus')]"
GOOGLE = "//*[contains(@href, 'catalog/phones/google') and contains(., 'Google')]"
OTHER = "//*[contains(@href, 'catalog/phones/other') and contains(., 'Другие телефоны')]"

# mobile phone categories page
CATEGORY_PAGE = "h1.category-title"


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
        self.asus = Button(page, locator=ASUS, name="Asus")
        self.blackview = Button(page, locator=BLACKVIEW, name="Blackview")
        self.zte = Button(page, locator=ZTE, name="zte")
        self.oneplus = Button(page, locator=ONEPLUS, name="OnePlus")
        self.google = Button(page, locator=GOOGLE, name="Google")
        self.other = Button(page, locator=OTHER, name="Другие телефоны")
        self.page_title = Title(page, locator=CATEGORY_PAGE, name="Product title")

    def sub_menu_items(self):
        self.apple.should_be_visible()
        self.samsung.should_be_visible()
        self.xiaomi.should_be_visible()
        self.sony.should_be_visible()
        self.realme.should_be_visible()
        self.blackview.should_be_visible()
        self.zte.should_be_visible()
        self.oneplus.should_be_visible()
        self.google.should_be_visible()
        self.other.should_be_visible()

    def page_apple(self):
        self.mobile_hover()
        self.apple.click()
        apple_page_title = self.page_title.get_text()
        self.page_title.should_have_text(apple_page_title)

    def page_samsung(self):
        self.mobile_hover()
        self.samsung.click()
        samsung_page_title = self.page_title.get_text()
        self.page_title.should_have_text(samsung_page_title)

    def page_xiaomi(self):
        self.mobile_hover()
        self.xiaomi.click()
        xiaomi_page_title = self.page_title.get_text()
        self.page_title.should_have_text(xiaomi_page_title)

    def page_sony(self):
        self.mobile_hover()
        self.sony.click()
        sony_page_title = self.page_title.get_text()
        self.page_title.should_have_text(sony_page_title)

    def page_realme(self):
        self.mobile_hover()
        self.realme.click()
        realme_page_title = self.page_title.get_text()
        self.page_title.should_have_text(realme_page_title)

    def page_blackview(self):
        self.mobile_hover()
        self.blackview.click()
        blackview_page_title = self.page_title.get_text()
        self.page_title.should_have_text(blackview_page_title)

    def page_zte(self):
        self.mobile_hover()
        self.zte.click()
        zte_page_title = self.page_title.get_text()
        self.page_title.should_have_text(zte_page_title)

    def page_oneplus(self):
        self.mobile_hover()
        self.oneplus.click()
        oneplus_page_title = self.page_title.get_text()
        self.page_title.should_have_text(oneplus_page_title)

    def page_google(self):
        self.mobile_hover()
        self.google.click()
        google_page_title = self.page_title.get_text()
        self.page_title.should_have_text(google_page_title)

    def page_other(self):
        self.mobile_hover()
        self.other.click()
        other_page_title = self.page_title.get_text()
        self.page_title.should_have_text(other_page_title)
