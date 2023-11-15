from datetime import datetime

from components.categories_elements import CategoryElements
from components.sub_menu_elements import SubMenu
from main import BASE_URL
from pages.categories import Categories


class TestCategoryPage:

    def test_apple_page(self, browser, sub_menu: SubMenu):
        apple = Categories(browser)
        apple.go_to(BASE_URL)
        apple.apple_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_samsung_page(self, browser, sub_menu: SubMenu):
        samsung = Categories(browser)
        samsung.go_to(BASE_URL)
        samsung.samsung_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_xiaomi_page(self, browser, sub_menu: SubMenu):
        xiaomi = Categories(browser)
        xiaomi.go_to(BASE_URL)
        xiaomi.xiaomi_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_sony_page(self, browser, sub_menu: SubMenu):
        sony = Categories(browser)
        sony.go_to(BASE_URL)
        sony.sony_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_realme_page(self, browser, sub_menu: SubMenu):
        realme = Categories(browser)
        realme.go_to(BASE_URL)
        realme.realme_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_blackview_page(self, browser, sub_menu: SubMenu):
        blackview = Categories(browser)
        blackview.go_to(BASE_URL)
        blackview.blackview_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_zte_page(self, browser, sub_menu: SubMenu):
        zte = Categories(browser)
        zte.go_to(BASE_URL)
        zte.zte_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_oneplus_page(self, browser, sub_menu: SubMenu):
        oneplus = Categories(browser)
        oneplus.go_to(BASE_URL)
        oneplus.oneplus_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_google_page(self, browser, sub_menu: SubMenu):
        google = Categories(browser)
        google.go_to(BASE_URL)
        google.zte_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_other_page(self, browser, sub_menu: SubMenu):
        other = Categories(browser)
        other.go_to(BASE_URL)
        other.oneplus_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_diagonal_checkboxes(self, browser, category_elements: CategoryElements):
        checkbox = Categories(browser)
        checkbox.go_to(BASE_URL)
        checkbox.diagonal_checkbox(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_mobile_filter(self, browser, category_elements: CategoryElements):
        mobile = Categories(browser)
        mobile.go_to(BASE_URL)
        mobile.mobile_phone_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_tablet_filter(self, browser, category_elements: CategoryElements):
        tablet = Categories(browser)
        tablet.go_to(BASE_URL)
        tablet.tablet_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_laptop_filter(self, browser, category_elements: CategoryElements):
        laptop = Categories(browser)
        laptop.go_to(BASE_URL)
        laptop.laptop_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_headphone_filter(self, browser, category_elements: CategoryElements):
        headphone = Categories(browser)
        headphone.go_to(BASE_URL)
        headphone.laptop_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_smartwatch_filter(self, browser, category_elements: CategoryElements):
        smartwatch = Categories(browser)
        smartwatch.go_to(BASE_URL)
        smartwatch.laptop_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_constructor_filter(self, browser, category_elements: CategoryElements):
        constructor = Categories(browser)
        constructor.go_to(BASE_URL)
        constructor.laptop_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_photo_filter(self, browser, category_elements: CategoryElements):
        photo = Categories(browser)
        photo.go_to(BASE_URL)
        photo.laptop_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_tv_filter(self, browser, category_elements: CategoryElements):
        tv = Categories(browser)
        tv.go_to(BASE_URL)
        tv.tv_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_console_filter(self, browser, category_elements: CategoryElements):
        console = Categories(browser)
        console.go_to(BASE_URL)
        console.console_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_coffee_filter(self, browser, category_elements: CategoryElements):
        coffee = Categories(browser)
        coffee.go_to(BASE_URL)
        coffee.console_filter_apply(category_elements)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
