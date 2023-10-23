from playwright.sync_api import Page


from pages.base_page import BasePage
from page_factory.text import Text


class CentrSvyazi(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.register_button = Text(page, locator=".logo > a:nth-child(1) > p", name="Центр Связи")

    def logo(self, logo: str):
        self.register_button.should_be_visible(logo=logo)
        self.register_button.should_have_text("Центр Связи")
