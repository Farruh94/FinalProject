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

    def test_health_page(self, browser, sub_menu: SubMenu):
        health = Categories(browser)
        health.go_to(BASE_URL)
        health.health_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_mono_page(self, browser, sub_menu: SubMenu):
        mono = Categories(browser)
        mono.go_to(BASE_URL)
        mono.mono_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_mouse_page(self, browser, sub_menu: SubMenu):
        mouse = Categories(browser)
        mouse.go_to(BASE_URL)
        mouse.mouse_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_acoustic_page(self, browser, sub_menu: SubMenu):
        acoustic = Categories(browser)
        acoustic.go_to(BASE_URL)
        acoustic.acoustic_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_system_unit_page(self, browser, sub_menu: SubMenu):
        system_unit = Categories(browser)
        system_unit.go_to(BASE_URL)
        system_unit.system_unit_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_ram_page(self, browser, sub_menu: SubMenu):
        ram = Categories(browser)
        ram.go_to(BASE_URL)
        ram.ram_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_rom_page(self, browser, sub_menu: SubMenu):
        rom = Categories(browser)
        rom.go_to(BASE_URL)
        rom.rom_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_microphone_page(self, browser, sub_menu: SubMenu):
        microphone = Categories(browser)
        microphone.go_to(BASE_URL)
        microphone.microphone_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_webcam_page(self, browser, sub_menu: SubMenu):
        webcam = Categories(browser)
        webcam.go_to(BASE_URL)
        webcam.webcam_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_quad_page(self, browser, sub_menu: SubMenu):
        quad = Categories(browser)
        quad.go_to(BASE_URL)
        quad.quad_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_gps_page(self, browser, sub_menu: SubMenu):
        gps = Categories(browser)
        gps.go_to(BASE_URL)
        gps.gps_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_camera_page(self, browser, sub_menu: SubMenu):
        camera = Categories(browser)
        camera.go_to(BASE_URL)
        camera.camera_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_router_page(self, browser, sub_menu: SubMenu):
        router = Categories(browser)
        router.go_to(BASE_URL)
        router.router_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_vacuum_cleaner_page(self, browser, sub_menu: SubMenu):
        vacuum = Categories(browser)
        vacuum.go_to(BASE_URL)
        vacuum.vacuum_cleaner_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_lamp_cleaner_page(self, browser, sub_menu: SubMenu):
        lamp = Categories(browser)
        lamp.go_to(BASE_URL)
        lamp.lamp_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_dryer_page(self, browser, sub_menu: SubMenu):
        dryer = Categories(browser)
        dryer.go_to(BASE_URL)
        dryer.dryer_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_toothbrush_page(self, browser, sub_menu: SubMenu):
        toothbrush = Categories(browser)
        toothbrush.go_to(BASE_URL)
        toothbrush.toothbrush_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_amateur_camera_page(self, browser, sub_menu: SubMenu):
        amateur_camera = Categories(browser)
        amateur_camera.go_to(BASE_URL)
        amateur_camera.amateur_camera_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_pro_camera_page(self, browser, sub_menu: SubMenu):
        pro_camera = Categories(browser)
        pro_camera.go_to(BASE_URL)
        pro_camera.pro_camera_page(sub_menu)

        browser.screenshot(path=f"./screenshot/screenshot{datetime.now()}.png")

    def test_lens_page(self, browser, sub_menu: SubMenu):
        lens = Categories(browser)
        lens.go_to(BASE_URL)
        lens.lens_page(sub_menu)

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
