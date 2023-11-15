from playwright.sync_api import Page

from components.categories_elements import CategoryElements
from components.sub_menu_elements import SubMenu
from pages.base_page import BasePage


class Categories(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @staticmethod
    def apple_page(page_apple: SubMenu):
        page_apple.page_apple()

    @staticmethod
    def samsung_page(page_samsung: SubMenu):
        page_samsung.page_samsung()

    @staticmethod
    def xiaomi_page(xiaomi_page: SubMenu):
        xiaomi_page.page_xiaomi()

    @staticmethod
    def sony_page(sony_page: SubMenu):
        sony_page.page_sony()

    @staticmethod
    def realme_page(realme_page: SubMenu):
        realme_page.page_realme()

    @staticmethod
    def blackview_page(blackview_page: SubMenu):
        blackview_page.page_blackview()

    @staticmethod
    def zte_page(zte_page: SubMenu):
        zte_page.page_zte()

    @staticmethod
    def oneplus_page(oneplus_page: SubMenu):
        oneplus_page.page_oneplus()

    @staticmethod
    def google_page(google_page: SubMenu):
        google_page.page_google()

    @staticmethod
    def other_page(other_page: SubMenu):
        other_page.page_other()

    @staticmethod
    def diagonal_checkbox(diagonal_checkbox: CategoryElements):
        diagonal_checkbox.diagonal_checkboxes()

    @staticmethod
    def mobile_phone_filter_apply(filter_applied: CategoryElements):
        filter_applied.mobile_phone_page_filter_applied()

    @staticmethod
    def tablet_filter_apply(filter_applied: CategoryElements):
        filter_applied.tablet_page_filter_applied()

    @staticmethod
    def laptop_filter_apply(filter_applied: CategoryElements):
        filter_applied.laptop_page_filter_applied()

    @staticmethod
    def headphones_filter_apply(filter_applied: CategoryElements):
        filter_applied.headphone_page_filter_applied()

    @staticmethod
    def smartwatch_filter_apply(filter_applied: CategoryElements):
        filter_applied.smartwatch_page_filter_applied()

    @staticmethod
    def constructor_filter_apply(filter_applied: CategoryElements):
        filter_applied.constructor_page_filter_applied()

    @staticmethod
    def photo_filter_apply(filter_applied: CategoryElements):
        filter_applied.photo_page_filter_applied()

    @staticmethod
    def tv_filter_apply(filter_applied: CategoryElements):
        filter_applied.tv_page_filter_applied()

    @staticmethod
    def console_filter_apply(filter_applied: CategoryElements):
        filter_applied.console_page_filter_applied()

    @staticmethod
    def coffee_filter_apply(filter_applied: CategoryElements):
        filter_applied.coffee_page_filter_applied()
