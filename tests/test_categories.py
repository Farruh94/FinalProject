# from datetime import datetime
#
# from components.categories_elements import CategoryElements
# from components.sub_menu_elements import SubMenu
# from main import BASE_URL
# from pages.categories import Categories
#
#
# class TestCategoryPage:
#
#     def test_apple_page(self, browser, apple_page: SubMenu):
#         apple = Categories(browser)
#         apple.go_to(BASE_URL)
#         apple.apple_page(apple_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_samsung_page(self, browser, samsung_page: SubMenu):
#         samsung = Categories(browser)
#         samsung.go_to(BASE_URL)
#         samsung.samsung_page(samsung_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_xiaomi_page(self, browser, xiaomi_page: SubMenu):
#         xiaomi = Categories(browser)
#         xiaomi.go_to(BASE_URL)
#         xiaomi.xiaomi_page(xiaomi_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_sony_page(self, browser, sony_page: SubMenu):
#         sony = Categories(browser)
#         sony.go_to(BASE_URL)
#         sony.sony_page(sony_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_realme_page(self, browser, realme_page: SubMenu):
#         realme = Categories(browser)
#         realme.go_to(BASE_URL)
#         realme.realme_page(realme_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_blackview_page(self, browser, blackview_page: SubMenu):
#         blackview = Categories(browser)
#         blackview.go_to(BASE_URL)
#         blackview.blackview_page(blackview_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_zte_page(self, browser, zte_page: SubMenu):
#         zte = Categories(browser)
#         zte.go_to(BASE_URL)
#         zte.zte_page(zte_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_oneplus_page(self, browser, oneplus_page: SubMenu):
#         oneplus = Categories(browser)
#         oneplus.go_to(BASE_URL)
#         oneplus.oneplus_page(oneplus_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_google_page(self, browser, google_page: SubMenu):
#         google = Categories(browser)
#         google.go_to(BASE_URL)
#         google.zte_page(google_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_other_page(self, browser, other_page: SubMenu):
#         other = Categories(browser)
#         other.go_to(BASE_URL)
#         other.oneplus_page(other_page)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_diagonal_checkboxes(self, browser, diagonal_checkbox: CategoryElements):
#         checkbox = Categories(browser)
#         checkbox.go_to(BASE_URL)
#         checkbox.diagonal_checkbox(diagonal_checkbox)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_mobile_filter(self, browser, mobile_filter: CategoryElements):
#         mobile = Categories(browser)
#         mobile.go_to(BASE_URL)
#         mobile.mobile_phone_filter_apply(mobile_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_tablet_filter(self, browser, tablet_filter: CategoryElements):
#         tablet = Categories(browser)
#         tablet.go_to(BASE_URL)
#         tablet.tablet_filter_apply(tablet_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_laptop_filter(self, browser, laptop_filter: CategoryElements):
#         laptop = Categories(browser)
#         laptop.go_to(BASE_URL)
#         laptop.laptop_filter_apply(laptop_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_headphone_filter(self, browser, headphone_filter: CategoryElements):
#         headphone = Categories(browser)
#         headphone.go_to(BASE_URL)
#         headphone.laptop_filter_apply(headphone_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_smartwatch_filter(self, browser, smartwatch_filter: CategoryElements):
#         smartwatch = Categories(browser)
#         smartwatch.go_to(BASE_URL)
#         smartwatch.laptop_filter_apply(smartwatch_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_constructor_filter(self, browser, constructor_filter: CategoryElements):
#         constructor = Categories(browser)
#         constructor.go_to(BASE_URL)
#         constructor.laptop_filter_apply(constructor_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_photo_filter(self, browser, photo_filter: CategoryElements):
#         photo = Categories(browser)
#         photo.go_to(BASE_URL)
#         photo.laptop_filter_apply(photo_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_tv_filter(self, browser, tv_filter: CategoryElements):
#         tv = Categories(browser)
#         tv.go_to(BASE_URL)
#         tv.tv_filter_apply(tv_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_console_filter(self, browser, console_filter: CategoryElements):
#         console = Categories(browser)
#         console.go_to(BASE_URL)
#         console.console_filter_apply(console_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
#
#     def test_coffee_filter(self, browser, coffee_filter: CategoryElements):
#         coffee = Categories(browser)
#         coffee.go_to(BASE_URL)
#         coffee.console_filter_apply(coffee_filter)
#
#         browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")
