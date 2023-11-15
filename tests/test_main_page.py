from datetime import datetime

import pytest

from components.main_page_elements import MainPageElements
from components.search_field import SearchField
from components.sidebar_elements import SideBar
from main import BASE_URL
from pages.centr_svyazi import CentrSvyazi


class TestMainPage:

    def test_logo(self, browser, check_logo: MainPageElements):
        centr_svyazi = CentrSvyazi(browser)
        centr_svyazi.go_to(BASE_URL)

        centr_svyazi.visible_logo(check_logo)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_address(self, browser, check_addresses: MainPageElements):
        addresses = CentrSvyazi(browser)
        addresses.go_to(BASE_URL)

        addresses.address(check_addresses)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_delivery(self, browser, check_delivery: MainPageElements):
        delivery = CentrSvyazi(browser)
        delivery.go_to(BASE_URL)

        delivery.delivery(check_delivery)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_credit(self, browser, check_credit: MainPageElements):
        credit = CentrSvyazi(browser)
        credit.go_to(BASE_URL)

        credit.credit(check_credit)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_trade_in(self, browser, check_trade_in: MainPageElements):
        trade_in = CentrSvyazi(browser)
        trade_in.go_to(BASE_URL)

        trade_in.trade_in(check_trade_in)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_social_media(self, browser, check_social_media: MainPageElements):
        social_media = CentrSvyazi(browser)
        social_media.go_to(BASE_URL)

        social_media.address(check_social_media)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_services(self, browser, check_social_media: MainPageElements):
        service = CentrSvyazi(browser)
        service.go_to(BASE_URL)
        service.services(check_social_media)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_sidebar_items(self, browser, sidebar_elems: SideBar):
        sidebar = CentrSvyazi(browser)
        sidebar.go_to(BASE_URL)

        sidebar_elems.sidebar_items()
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_catalog(self, browser, mobile_hover: SideBar):
        mobile_catalog = CentrSvyazi(browser)
        mobile_catalog.go_to(BASE_URL)

        mobile_catalog.visit_mobile(mobile_hover)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    @pytest.mark.parametrize('search_inp', ['xiaomi'])
    def test_search(self, search_inp, browser, search: SearchField):
        check_search = CentrSvyazi(browser)
        check_search.go_to(BASE_URL)
        check_search.search_field_check(search_inp=search_inp, search=search)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
