from playwright.sync_api import Page

from page_factory.button import Button

MOBILE_PHONES = "//*[span = 'Сотовые телефоны']"
TABLETS = "//*[span = 'Планшеты']"
LAPTOPS = "//*[span = 'Ноутбуки']"
HEADPHONES = "//*[span = 'Наушники']"
SMARTWATCH = "//*[span = 'Умные часы']"
CONSTRUCTORS = "//*[span = 'Конструкторы']"
PHOTO = "//*[span = 'Фототехника']"
TV = "//*[span = 'Телевизоры']"
CONSOLES = "//*[span = 'Приставки и игры']"
COFFEE = "//*[span = 'Кофемашины']"
OTHER = "//*[span = 'Другая электроника']"
ACCESSORIES = "//*[span = 'Аксессуары']"
DISCOUNT = "//*[span = 'Уцененнные товары']"
USED = "//*[span = 'Товары б/у']"


class SideBar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.catalog = Button(page, locator="//*[@class = 'gamburger-home']", name="Каталог")
        self.mobile_phone = Button(page, locator=MOBILE_PHONES, name="Сотовые телефоны")
        self.tablet = Button(page, locator=TABLETS, name="Планшеты")
        self.laptop = Button(page, locator=LAPTOPS, name="Ноутбуки")
        self.headphone = Button(page, locator=HEADPHONES, name="Наушники")
        self.smartwatch = Button(page, locator=SMARTWATCH, name="Умные часы")
        self.constructor = Button(page, locator=CONSTRUCTORS, name="Конструкторы")
        self.photo = Button(page, locator=PHOTO, name="Фототехника")
        self.tv = Button(page, locator=TV, name="Телевизоры")
        self.console = Button(page, locator=CONSOLES, name="Приставки и игры")
        self.coffee = Button(page, locator=COFFEE, name="Кофемашины")
        self.other = Button(page, locator=OTHER, name="Другая электроника")
        self.accessories = Button(page, locator=ACCESSORIES, name="Аксессуары")
        self.discount = Button(page, locator=DISCOUNT, name="Уцененнные товары")
        self.used = Button(page, locator=USED, name="Товары б/у")

    def sidebar_items(self):
        self.mobile_phone.should_be_visible()
        self.tablet.should_be_visible()
        self.laptop.should_be_visible()
        self.headphone.should_be_visible()
        self.smartwatch.should_be_visible()
        self.constructor.should_be_visible()
        self.photo.should_be_visible()
        self.tv.should_be_visible()
        self.console.should_be_visible()
        self.coffee.should_be_visible()
        self.other.should_be_visible()
        self.accessories.should_be_visible()
        self.discount.should_be_visible()
        self.used.should_be_visible()

    def mobile_hover(self):
        self.mobile_phone.hover()
