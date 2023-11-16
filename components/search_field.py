from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title


class SearchField:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_input = Input(page, locator="//*[@class='search-inp']", name="Поиск по товарам")
        self.search_result = ListItem(page, locator="//*[@class='ajax-result']", name="Results")

    def search_field(self):
        self.search_input.click()
        self.search_input.should_be_visible()

    def find_result(self, search_inp: str, result_number: int) -> None:
        self.search_input.fill(search_inp, validate_value=True)
        self.search_input.should_have_value(search_inp)
        self.search_result.click(result_number=result_number)


