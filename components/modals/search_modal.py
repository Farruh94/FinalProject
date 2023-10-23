from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title


class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.empty_results_title = Title(page, locator=".//*[@class='search-inp']", name="Поиск по товарам")
        self.search_input = Input(page, locator=".//*[@class='search-inp']", name=".//*[@class='ajax-result']")


    def modal_is_opened(self):
        self.search_input.should_be_visible()
        self.empty_results_title.should_be_visible()

    def find_result(self, keyword: str, result_number: int) -> None:
        self.search_input.fill(keyword, validate_value=True)
        self.search_result.click(result_number=result_number)
