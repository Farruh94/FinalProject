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
    def visit_mobile(sidebar: SideBar):
        sidebar.mobile_cat()

    @staticmethod
    def address(main_page: MainPageElements):
        main_page.check_addresses()

    @staticmethod
    def social_media(main_page: MainPageElements):
        main_page.check_social_media()

    @staticmethod
    def credit(main_page: MainPageElements):
        main_page.check_credit()

    @staticmethod
    def trade_in(main_page: MainPageElements):
        main_page.check_trade_in()

    @staticmethod
    def delivery(main_page: MainPageElements):
        main_page.check_delivery()

    @staticmethod
    def services(main_page: MainPageElements):
        main_page.check_services()

    @staticmethod
    def search_field_check(search_inp, search: SearchField):
        search.search_field()
        search.find_result(result_number=0, search_inp=search_inp)

