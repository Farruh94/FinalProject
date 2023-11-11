from datetime import datetime
from time import sleep

from components.main_page_elements import MainPageElements
from components.sidebar import SideBar
from main import BASE_URL
from pages.centr_svyazi import CentrSvyazi


class TestMainPage:

    def test_logo(self, chromium_page, check_logo: MainPageElements):
        centr_svyazi = CentrSvyazi(chromium_page)
        centr_svyazi.go_to(BASE_URL)

        centr_svyazi.visible_logo(check_logo)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_address(self, chromium_page, check_addresses: MainPageElements):
        addresses = CentrSvyazi(chromium_page)
        addresses.go_to(BASE_URL)

        addresses.address(check_addresses)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_delivery(self, chromium_page, check_delivery: MainPageElements):
        delivery = CentrSvyazi(chromium_page)
        delivery.go_to(BASE_URL)

        delivery.delivery(check_delivery)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_credit(self, chromium_page, check_credit: MainPageElements):
        credit = CentrSvyazi(chromium_page)
        credit.go_to(BASE_URL)

        credit.credit(check_credit)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_trade_in(self, chromium_page, check_trade_in: MainPageElements):
        trade_in = CentrSvyazi(chromium_page)
        trade_in.go_to(BASE_URL)

        trade_in.trade_in(check_trade_in)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_social_media(self, chromium_page, check_social_media: MainPageElements):
        social_media = CentrSvyazi(chromium_page)
        social_media.go_to(BASE_URL)

        social_media.address(check_social_media)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_sidebar_items(self, chromium_page, sidebar_elems: SideBar):
        sidebar = CentrSvyazi(chromium_page)
        sidebar.go_to(BASE_URL)

        sidebar_elems.sidebar_items()
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_catalog(self, chromium_page, mobile_hover: SideBar):
        mobile_catalog = CentrSvyazi(chromium_page)
        mobile_catalog.go_to(BASE_URL)

        mobile_catalog.visit_mobile(mobile_hover)
        chromium_page.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
