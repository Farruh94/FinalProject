import pytest
from playwright.sync_api import Page, sync_playwright

from components.basket_elements import BasketElements
from components.categories_elements import CategoryElements
from components.main_page_elements import MainPageElements
from components.search_field import SearchField
from components.sidebar_elements import SideBar
from components.sub_menu_elements import SubMenu


def pytest_addoption(parser):
    parser.addoption("--headless", default=True, help="Run browser in headless mode")


@pytest.fixture(scope="session")
def browser(request) -> Page:
    headless = request.config.getoption("--headless")
    if headless == "True":
        headless = True
    elif headless == "False":
        headless = False
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=headless)
        context = chromium.new_context(viewport={"width": 1920, "height": 1080})
        yield context.new_page()
        context.close()


@pytest.fixture(scope="function")
def main_page(browser: Page) -> MainPageElements:
    return MainPageElements(browser)


@pytest.fixture(scope="function")
def sidebar_elems(browser: Page) -> SideBar:
    return SideBar(browser)


@pytest.fixture(scope="function")
def basket_page(browser: Page) -> BasketElements:
    return BasketElements(browser)


@pytest.fixture(scope="function")
def sub_menu(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def category_elements(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def search(browser: Page) -> SearchField:
    return SearchField(browser)
