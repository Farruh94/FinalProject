from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from components.sidebar_elements import SideBar
from page_factory.button import Button
from page_factory.checkbox import CheckBox
from page_factory.title import Title


class CategoryElements(SideBar):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.brand_checkbox = CheckBox(page, locator="input#brand0.check_filter", name="1st brand")

        self.diagonal_checkbox = CheckBox(page, locator="input#diagonal0.check_filter", name="1st checkbox")
        self.diagonal_checkbox_1 = CheckBox(page, locator="input#diagonal1.check_filter", name="2nd checkbox")
        self.diagonal_checkbox_2 = CheckBox(page, locator="input#diagonal2.check_filter", name="3rd checkbox")

        self.ram_checkbox = CheckBox(page, locator="input#oper0.check_filter", name="1st ram checkbox")
        self.ram_checkbox_1 = CheckBox(page, locator="input#oper1.check_filter", name="2nd ram checkbox")
        self.ram_checkbox_2 = CheckBox(page, locator="input#oper2.check_filter", name="3rd ram checkbox")

        self.rom_checkbox = CheckBox(page, locator="input#all0.check_filter", name="1st rom checkbox")
        self.rom_checkbox_1 = CheckBox(page, locator="input#all1.check_filter", name="2nd rom checkbox")
        self.rom_checkbox_2 = CheckBox(page, locator="input#all2.check_filter", name="3rd rom checkbox")
        self.rom_checkbox_3 = CheckBox(page, locator="input#all3.check_filter", name="4th rom checkbox")
        self.rom_checkbox_4 = CheckBox(page, locator="input#all4.check_filter", name="5th rom checkbox")

        self.sim_checkbox = CheckBox(page, locator="input#sim0.check_filter", name="1st sim checkbox")
        self.sim_checkbox_1 = CheckBox(page, locator="input#sim1.check_filter", name="2nd sim checkbox")

        self.apply_filters = Button(page, locator="input#b_range", name="Применить фильтры")
        self.reset_filters = Button(page, locator="a.reset_filter.button.btn2", name="Сбросить фильтры")
        self.products = Title(page, locator="div.products", name="Товары")

    def diagonal_checkboxes(self):
        self.mobile_phone.click()
        self.diagonal_checkbox.check()
        self.diagonal_checkbox.is_checked()

    def ram_checkboxes(self):
        self.mobile_phone.click()
        self.ram_checkbox.check()
        self.ram_checkbox.is_checked()

    def rom_checkboxes(self):
        self.mobile_phone.click()
        self.rom_checkbox.check()
        self.rom_checkbox.is_checked()

    def mobile_phone_page_filter_applied(self):
        self.mobile_phone.click()
        self.diagonal_checkbox.check()
        self.ram_checkbox.check()
        self.rom_checkbox.check()
        self.apply_filters.click()
        self.products.should_be_visible()

    def tablet_page_filter_applied(self):
        self.tablet.click()
        self.diagonal_checkbox.check()
        self.ram_checkbox.check()
        self.rom_checkbox.check()
        self.apply_filters.click()
        self.products.should_be_visible()

    def laptop_page_filter_applied(self):
        self.laptop.click()
        self.brand_checkbox.check()
        self.brand_checkbox.is_checked()
        self.ram_checkbox.check()
        self.apply_filters.click()
        self.products.should_be_visible()

    def headphone_page_filter_applied(self):
        self.headphone.click()
        self.brand_checkbox.check()
        self.brand_checkbox.is_checked()
        self.apply_filters.click()
        self.products.should_be_visible()

    def smartwatch_page_filter_applied(self):
        self.smartwatch.click()
        self.brand_checkbox.check()
        self.brand_checkbox.is_checked()
        self.apply_filters.click()
        self.products.should_be_visible()

    def constructor_page_filter_applied(self):
        self.constructor.click()
        self.brand_checkbox.check()
        self.brand_checkbox.is_checked()
        self.apply_filters.click()
        self.products.should_be_visible()

    def photo_page_filter_applied(self):
        self.photo.click()
        self.brand_checkbox.check()
        self.brand_checkbox.is_checked()
        self.apply_filters.click()
        self.products.should_be_visible()

    def tv_page_filter_applied(self):
        self.tv.click()
        self.brand_checkbox.check()
        self.brand_checkbox.is_checked()
        self.apply_filters.click()
        self.products.should_be_visible()

    def console_page_filter_applied(self):
        self.console.click()
        self.brand_checkbox.check()
        self.brand_checkbox.is_checked()
        self.apply_filters.click()
        self.products.should_be_visible()

    def coffee_page_filter_applied(self):
        self.coffee.click()
        self.products.should_be_visible()
