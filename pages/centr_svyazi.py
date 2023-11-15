import pytest
from playwright.sync_api import Page

from components.main_page_elements import MainPageElements
from components.search_field import SearchField
from components.sidebar_elements import SideBar
from pages.base_page import BasePage


class CentrSvyazi(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @staticmethod
    def visible_logo(logo: MainPageElements):
        logo.check_that_logo_is_visible()

    @staticmethod
    def visit_mobile(mobile_phone: SideBar):
        mobile_phone.mobile_hover()

    @staticmethod
    def address(check_address: MainPageElements):
        check_address.check_addresses()

    @staticmethod
    def social_media(check_social_network: MainPageElements):
        check_social_network.check_social_media()

    @staticmethod
    def credit(check_credit: MainPageElements):
        check_credit.check_credit()

    @staticmethod
    def trade_in(check_trade_in: MainPageElements):
        check_trade_in.check_trade_in()

    @staticmethod
    def delivery(check_delivery: MainPageElements):
        check_delivery.check_delivery()

    @staticmethod

    def search_1(search_inp, search: SearchField):
        search.search_field()
        search.find_result(result_number=0, search_inp=search_inp)

