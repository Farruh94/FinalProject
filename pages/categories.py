from playwright.sync_api import Page

from components.categories_elements import CategoryElements
from components.sub_menu_elements import SubMenu
from pages.base_page import BasePage


class Categories(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @staticmethod
    def mobile_phones(submenu: SubMenu):
        submenu.mobile_categories()

    @staticmethod
    def apple_page(submenu: SubMenu):
        submenu.page_apple()

    @staticmethod
    def samsung_page(submenu: SubMenu):
        submenu.page_samsung()

    @staticmethod
    def xiaomi_page(submenu: SubMenu):
        submenu.page_xiaomi()

    @staticmethod
    def sony_page(submenu: SubMenu):
        submenu.page_sony()

    @staticmethod
    def realme_page(submenu: SubMenu):
        submenu.page_realme()

    @staticmethod
    def blackview_page(submenu: SubMenu):
        submenu.page_blackview()

    @staticmethod
    def zte_page(submenu: SubMenu):
        submenu.page_zte()

    @staticmethod
    def oneplus_page(submenu: SubMenu):
        submenu.page_oneplus()

    @staticmethod
    def google_page(submenu: SubMenu):
        submenu.page_google()

    @staticmethod
    def other_page(submenu: SubMenu):
        submenu.page_other_phone()

    @staticmethod
    def health_page(submenu: SubMenu):
        submenu.page_health()

    @staticmethod
    def mono_page(submenu: SubMenu):
        submenu.page_mono()

    @staticmethod
    def mouse_page(submenu: SubMenu):
        submenu.page_mouse()

    @staticmethod
    def acoustic_page(submenu: SubMenu):
        submenu.page_acoustic()

    @staticmethod
    def system_unit_page(submenu: SubMenu):
        submenu.page_system_unit()

    @staticmethod
    def ram_page(submenu: SubMenu):
        submenu.page_ram()

    @staticmethod
    def rom_page(submenu: SubMenu):
        submenu.page_rom()

    @staticmethod
    def microphone_page(submenu: SubMenu):
        submenu.page_microphone()

    @staticmethod
    def webcam_page(submenu: SubMenu):
        submenu.page_webcam()

    @staticmethod
    def quad_page(submenu: SubMenu):
        submenu.page_quad()

    @staticmethod
    def gps_page(submenu: SubMenu):
        submenu.page_gps()

    @staticmethod
    def camera_page(submenu: SubMenu):
        submenu.page_camera()

    @staticmethod
    def router_page(submenu: SubMenu):
        submenu.page_router()

    @staticmethod
    def vacuum_cleaner_page(submenu: SubMenu):
        submenu.page_vacuum_cleaner()

    @staticmethod
    def lamp_page(submenu: SubMenu):
        submenu.page_lamp()

    @staticmethod
    def dryer_page(submenu: SubMenu):
        submenu.page_dryer()

    @staticmethod
    def toothbrush_page(submenu: SubMenu):
        submenu.page_toothbrush()

    @staticmethod
    def amateur_camera_page(submenu: SubMenu):
        submenu.page_amateur_camera()

    @staticmethod
    def pro_camera_page(submenu: SubMenu):
        submenu.page_pro_camera()

    @staticmethod
    def lens_page(submenu: SubMenu):
        submenu.page_lens()

    @staticmethod
    def diagonal_checkbox(category: CategoryElements):
        category.diagonal_checkboxes()

    @staticmethod
    def mobile_phone_filter_apply(category: CategoryElements):
        category.mobile_phone_page_filter_applied()

    @staticmethod
    def tablet_filter_apply(category: CategoryElements):
        category.tablet_page_filter_applied()

    @staticmethod
    def laptop_filter_apply(category: CategoryElements):
        category.laptop_page_filter_applied()

    @staticmethod
    def headphones_filter_apply(category: CategoryElements):
        category.headphone_page_filter_applied()

    @staticmethod
    def smartwatch_filter_apply(category: CategoryElements):
        category.smartwatch_page_filter_applied()

    @staticmethod
    def constructor_filter_apply(category: CategoryElements):
        category.constructor_page_filter_applied()

    @staticmethod
    def photo_filter_apply(category: CategoryElements):
        category.photo_page_filter_applied()

    @staticmethod
    def tv_filter_apply(category: CategoryElements):
        category.tv_page_filter_applied()

    @staticmethod
    def console_filter_apply(category: CategoryElements):
        category.console_page_filter_applied()

    @staticmethod
    def coffee_filter_apply(category: CategoryElements):
        category.coffee_page_filter_applied()
