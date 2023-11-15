from datetime import datetime

import pytest

from components.main_page_elements import MainPageElements
from components.search_field import SearchField
from components.sidebar_elements import SideBar
from main import BASE_URL
from pages.centr_svyazi import CentrSvyazi


class TestMainPage:

    def test_logo(self, browser, main_page: MainPageElements):
        centr_svyazi = CentrSvyazi(browser)
        centr_svyazi.go_to(BASE_URL)

        centr_svyazi.visible_logo(main_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_address(self, browser, main_page: MainPageElements):
        addresses = CentrSvyazi(browser)
        addresses.go_to(BASE_URL)

        addresses.address(main_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_delivery(self, browser, main_page: MainPageElements):
        delivery = CentrSvyazi(browser)
        delivery.go_to(BASE_URL)

        delivery.delivery(main_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_credit(self, browser, main_page: MainPageElements):
        credit = CentrSvyazi(browser)
        credit.go_to(BASE_URL)

        credit.credit(main_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_trade_in(self, browser, main_page: MainPageElements):
        trade_in = CentrSvyazi(browser)
        trade_in.go_to(BASE_URL)

        trade_in.trade_in(main_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_social_media(self, browser, main_page: MainPageElements):
        social_media = CentrSvyazi(browser)
        social_media.go_to(BASE_URL)

        social_media.address(main_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_services(self, browser, main_page: MainPageElements):
        service = CentrSvyazi(browser)
        service.go_to(BASE_URL)
        service.services(main_page)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_sidebar_items(self, browser, sidebar_elems: SideBar):
        sidebar = CentrSvyazi(browser)
        sidebar.go_to(BASE_URL)

        sidebar_elems.sidebar_items()
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_catalog(self, browser, side_bar: SideBar):
        mobile_catalog = CentrSvyazi(browser)
        mobile_catalog.go_to(BASE_URL)

        mobile_catalog.visit_mobile(side_bar)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    @pytest.mark.parametrize('search_inp', ['xiaomi'])
    def test_search(self, search_inp, browser, search: SearchField):
        check_search = CentrSvyazi(browser)
        check_search.go_to(BASE_URL)
        check_search.search_field_check(search_inp=search_inp, search=search)
        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
