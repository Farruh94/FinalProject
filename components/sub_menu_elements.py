from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from components.sidebar_elements import SideBar
from page_factory.button import Button
from page_factory.title import Title

# mobile phone categories
APPLE = "//*[contains(@href, 'catalog/phones/apple') and contains(., 'Apple')]"
SAMSUNG = "//*[contains(@href, 'catalog/phones/samsung') and contains(., 'Samsung')]"
XIAOMI = "//*[contains(@href, 'catalog/phones/xiaomi') and contains(., 'Xiaomi')]"
SONY = "//*[contains(@href, 'catalog/phones/sony') and contains(., 'Sony')]"
HUAWEI = "//*[contains(@href, 'catalog/phones/huawei') and contains(., 'Huawei')]"
REALME = "//*[contains(@href, 'catalog/phones/realme') and contains(., 'Realme')]"
ASUS = "//*[contains(@href, 'catalog/phones/asus') and contains(., 'Asus')]"
BLACKVIEW = "//*[contains(@href, 'catalog/phones/blackview') and contains(., 'Blackview')]"
ZTE = "//*[contains(@href, 'catalog/phones/zte') and contains(., 'zte')]"
ONEPLUS = "//*[contains(@href, 'catalog/phones/oneplus') and contains(., 'OnePlus')]"
GOOGLE = "//*[contains(@href, 'catalog/phones/google') and contains(., 'Google')]"
OTHER = "//*[contains(@href, 'catalog/phones/other') and contains(., 'Другие телефоны')]"

# Other categories
HEALTH = "//*[contains(@href, 'catalog/others/health')]"
MONO = "//*[contains(@href, 'catalog/others/mono')]"
MOUSE = "//*[contains(@href, 'catalog/others/mouse')]"
ACOUSTIC = "//*[contains(@href, 'catalog/others/acoustic')]"
SYSTEMUNIT = "//*[contains(@href, 'catalog/others/systemunit')]"
RAM = "//*[contains(@href, 'catalog/others/ram')]"
ROM = "//*[contains(@href, 'catalog/others/hdd')]"
MICROPHONE = "//*[contains(@href, 'catalog/others/microphones')]"
WEBCAM = "//*[contains(@href, 'catalog/others/webcameras')]"
QUAD = "//*[contains(@href, 'catalog/others/quadcopters')]"
AUTO = "//*[contains(@href, 'catalog/others/avtoregistrator')]"
GPS = "//*[contains(@href, 'catalog/others/gps')]"
CAMERA = "//*[contains(@href, 'catalog/others/camcord')]"
ROUTER = "//*[contains(@href, 'catalog/others/router')]"
VACUUM_CLEANER = "//*[contains(@href, 'catalog/others/vacuum')]"
LAMP = "//*[contains(@href, 'catalog/others/lamps')]"
DRYER = "//*[contains(@href, 'catalog/others/dryers')]"
TOOTHBRUSH = "//*[contains(@href, 'catalog/others/toothbrushes')]"

# cameras
AMATEUR = "//*[contains(@href, 'catalog/photo/amateur')]"
PRO = "//*[contains(@href, 'catalog/photo/slr')]"
LENS = "//*[contains(@href, 'catalog/photo/lenses')]"

# mobile phone categories page
CATEGORY_PAGE = "h1.category-title"


class SubMenu(SideBar):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.apple = Button(page, locator=APPLE, name="Apple")
        self.samsung = Button(page, locator=SAMSUNG, name="Samsung")
        self.xiaomi = Button(page, locator=XIAOMI, name="Xiaomi")
        self.sony = Button(page, locator=SONY, name="Sony")
        self.huawei = Button(page, locator=HUAWEI, name="Huawei")
        self.realme = Button(page, locator=REALME, name="Realme")
        self.asus = Button(page, locator=ASUS, name="Asus")
        self.blackview = Button(page, locator=BLACKVIEW, name="Blackview")
        self.zte = Button(page, locator=ZTE, name="zte")
        self.oneplus = Button(page, locator=ONEPLUS, name="OnePlus")
        self.google = Button(page, locator=GOOGLE, name="Google")
        self.other_phone = Button(page, locator=OTHER, name="Другие телефоны")
        self.page_title = Title(page, locator=CATEGORY_PAGE, name="Product title")
        self.health = Button(page, locator=HEALTH, name="Здорровье")
        self.mono = Button(page, locator=MONO, name="Моноблоки")
        self.mouse = Button(page, locator=MOUSE, name="Компьютерные мыши")
        self.acoustic = Button(page, locator=ACOUSTIC, name="Акустические системы")
        self.system_unit = Button(page, locator=SYSTEMUNIT, name="Моноблоки")
        self.ram = Button(page, locator=RAM, name="Оперативная память")
        self.rom = Button(page, locator=ROM, name="Память")
        self.microphone = Button(page, locator=MICROPHONE, name="Микрофоны")
        self.webcam = Button(page, locator=WEBCAM, name="Вебкамеры")
        self.quad = Button(page, locator=QUAD, name="Квадрокоптеры")
        self.gps = Button(page, locator=GPS, name="Навигаторы")
        self.camera = Button(page, locator=CAMERA, name="Видеокамеры")
        self.router = Button(page, locator=ROUTER, name="Роутеры")
        self.vacuum_cleaner = Button(page, locator=VACUUM_CLEANER, name="Пылесосы")
        self.lamp = Button(page, locator=LAMP, name="Лампочки")
        self.dryer = Button(page, locator=DRYER, name="Фены")
        self.toothbrush = Button(page, locator=TOOTHBRUSH, name="Зубные щетки")
        self.amateur = Button(page, locator=AMATEUR, name="Беззеркальные")
        self.pro = Button(page, locator=PRO, name="Зеркальные")
        self.lens = Button(page, locator=LENS, name="Оптика")

    def mobile_categories(self):
        self.mobile_cat()
        self.apple.should_be_visible()
        self.samsung.should_be_visible()
        self.xiaomi.should_be_visible()
        self.sony.should_be_visible()
        self.realme.should_be_visible()
        self.blackview.should_be_visible()
        self.zte.should_be_visible()
        self.oneplus.should_be_visible()
        self.google.should_be_visible()
        self.other.should_be_visible()

    def page_apple(self):
        self.mobile_cat()
        self.apple.click()
        apple_page_title = self.page_title.get_text()
        self.page_title.should_have_text(apple_page_title)

    def page_samsung(self):
        self.mobile_cat()
        self.samsung.click()
        samsung_page_title = self.page_title.get_text()
        self.page_title.should_have_text(samsung_page_title)

    def page_xiaomi(self):
        self.mobile_cat()
        self.xiaomi.click()
        xiaomi_page_title = self.page_title.get_text()
        self.page_title.should_have_text(xiaomi_page_title)

    def page_sony(self):
        self.mobile_cat()
        self.sony.click()
        sony_page_title = self.page_title.get_text()
        self.page_title.should_have_text(sony_page_title)

    def page_realme(self):
        self.mobile_cat()
        self.realme.click()
        realme_page_title = self.page_title.get_text()
        self.page_title.should_have_text(realme_page_title)

    def page_blackview(self):
        self.mobile_cat()
        self.blackview.click()
        blackview_page_title = self.page_title.get_text()
        self.page_title.should_have_text(blackview_page_title)

    def page_zte(self):
        self.mobile_cat()
        self.zte.click()
        zte_page_title = self.page_title.get_text()
        self.page_title.should_have_text(zte_page_title)

    def page_oneplus(self):
        self.mobile_cat()
        self.oneplus.click()
        oneplus_page_title = self.page_title.get_text()
        self.page_title.should_have_text(oneplus_page_title)

    def page_google(self):
        self.mobile_cat()
        self.google.click()
        google_page_title = self.page_title.get_text()
        self.page_title.should_have_text(google_page_title)

    def page_other_phone(self):
        self.mobile_cat()
        self.other_phone.click()
        other_page_title = self.page_title.get_text()
        self.page_title.should_have_text(other_page_title)

    def page_health(self):
        self.other_cat()
        self.health.click()
        health_page_title = self.page_title.get_text()
        self.page_title.should_have_text(health_page_title)

    def page_mono(self):
        self.other_cat()
        self.mono.click()
        mono_page_title = self.page_title.get_text()
        self.page_title.should_have_text(mono_page_title)

    def page_mouse(self):
        self.other_cat()
        self.mouse.click()
        mouse_page_title = self.page_title.get_text()
        self.page_title.should_have_text(mouse_page_title)

    def page_acoustic(self):
        self.other_cat()
        self.acoustic.click()
        acoustic_page_title = self.page_title.get_text()
        self.page_title.should_have_text(acoustic_page_title)

    def page_system_unit(self):
        self.other_cat()
        self.system_unit.click()
        system_unit_page_title = self.page_title.get_text()
        self.page_title.should_have_text(system_unit_page_title)

    def page_ram(self):
        self.other_cat()
        self.ram.click()
        ram_page_title = self.page_title.get_text()
        self.page_title.should_have_text(ram_page_title)

    def page_rom(self):
        self.other_cat()
        self.rom.click()
        rom_page_title = self.page_title.get_text()
        self.page_title.should_have_text(rom_page_title)

    def page_microphone(self):
        self.other_cat()
        self.microphone.click()
        microphone_page_title = self.page_title.get_text()
        self.page_title.should_have_text(microphone_page_title)

    def page_webcam(self):
        self.other_cat()
        self.webcam.click()
        webcam_page_title = self.page_title.get_text()
        self.page_title.should_have_text(webcam_page_title)

    def page_quad(self):
        self.other_cat()
        self.quad.click()
        quad_page_title = self.page_title.get_text()
        self.page_title.should_have_text(quad_page_title)

    def page_gps(self):
        self.other_cat()
        self.gps.click()
        gps_page_title = self.page_title.get_text()
        self.page_title.should_have_text(gps_page_title)

    def page_camera(self):
        self.other_cat()
        self.camera.click()
        camera_page_title = self.page_title.get_text()
        self.page_title.should_have_text(camera_page_title)

    def page_router(self):
        self.other_cat()
        self.router.click()
        router_page_title = self.page_title.get_text()
        self.page_title.should_have_text(router_page_title)

    def page_vacuum_cleaner(self):
        self.other_cat()
        self.vacuum_cleaner.click()
        vacuum_cleaner_page_title = self.page_title.get_text()
        self.page_title.should_have_text(vacuum_cleaner_page_title)

    def page_lamp(self):
        self.other_cat()
        self.lamp.click()
        lamp_page_title = self.page_title.get_text()
        self.page_title.should_have_text(lamp_page_title)

    def page_dryer(self):
        self.other_cat()
        self.dryer.click()
        dryer_page_title = self.page_title.get_text()
        self.page_title.should_have_text(dryer_page_title)

    def page_toothbrush(self):
        self.other_cat()
        self.toothbrush.click()
        toothbrush_page_title = self.page_title.get_text()
        self.page_title.should_have_text(toothbrush_page_title)

    def page_amateur_camera(self):
        self.photo_cat()
        self.amateur.click()
        amateur_camera_page_title = self.page_title.get_text()
        self.page_title.should_have_text(amateur_camera_page_title)

    def page_pro_camera(self):
        self.photo_cat()
        self.pro.click()
        pro_camera_page_title = self.page_title.get_text()
        self.page_title.should_have_text(pro_camera_page_title)

    def page_lens(self):
        self.photo_cat()
        self.lens.click()
        lens_page_title = self.page_title.get_text()
        self.page_title.should_have_text(lens_page_title)
