from playwright.sync_api import Page

from components.modals.search_modal import SearchModal
from page_factory.button import Button
from page_factory.link import Link
from page_factory.text import Text


class SideBar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_modal = SearchModal(page)

        self.catalog = Button(page, locator="//*[@class = 'gamburger-home']", name="Каталог")
        self.menu = Link(page, locator="//*[@class = 'side-menu']", name="Сотовые телефоны")
        self.mobile_phone = Link(page, locator=".//*[span = 'Сотовые телефоны']", name="Сотовые телефоны")
        self.search_button = Button(page, locator="//*[@id='search-block']/form/button", name="Поиск")

    def menu_is_opened(self):
        self.menu.should_be_visible()

    def visit_mobile_phone(self):
        self.mobile_phone.hover()

    def click_catalog(self):
        self.catalog.click()

    def open_search(self):
        self.search_button.should_be_visible()

        self.search_button.hover()
        self.search_button.click()

        self.search_modal.modal_is_opened()
