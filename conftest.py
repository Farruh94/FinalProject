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
        chromium = playwright.chromium.launch(headless=False)
        context = chromium.new_context(viewport={"width": 1920, "height": 1080})
        yield context.new_page()


@pytest.fixture(scope="function")
def main_page(browser: Page) -> MainPageElements:
    return MainPageElements(browser)



@pytest.fixture(scope="function")
def sidebar(browser: Page) -> SideBar:
    return SideBar(browser)


@pytest.fixture(scope="function")
def basket(browser: Page) -> BasketElements:
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

###

@pytest.fixture(scope="function")
def check_addresses(browser: Page) -> MainPageElements:
    return MainPageElements(browser)


@pytest.fixture(scope="function")
def check_social_media(browser: Page) -> MainPageElements:
    return MainPageElements(browser)


@pytest.fixture(scope="function")
def check_logo(browser: Page) -> MainPageElements:
    return MainPageElements(browser)


@pytest.fixture(scope="function")
def check_credit(browser: Page) -> MainPageElements:
    return MainPageElements(browser)


@pytest.fixture(scope="function")
def check_trade_in(browser: Page) -> MainPageElements:
    return MainPageElements(browser)


@pytest.fixture(scope="function")
def check_delivery(browser: Page) -> MainPageElements:
    return MainPageElements(browser)


@pytest.fixture(scope="function")
def check_services(browser: Page) -> MainPageElements:
    return MainPageElements(browser)


@pytest.fixture(scope="function")
def sidebar_elems(browser: Page) -> SideBar:
    return SideBar(browser)


@pytest.fixture(scope="function")
def mobile_hover(browser: Page) -> SideBar:
    return SideBar(browser)


@pytest.fixture(scope="function")
def empty_basket(browser: Page) -> BasketElements:
    return BasketElements(browser)


@pytest.fixture(scope="function")
def not_empty(browser: Page) -> BasketElements:
    return BasketElements(browser)


@pytest.fixture(scope="function")
def user_info(browser: Page) -> BasketElements:
    return BasketElements(browser)


@pytest.fixture(scope="function")
def apple_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def samsung_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def xiaomi_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def sony_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def realme_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def blackview_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def zte_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def oneplus_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def google_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def other_page(browser: Page) -> SubMenu:
    return SubMenu(browser)


@pytest.fixture(scope="function")
def diagonal_checkbox(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def mobile_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def tablet_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def laptop_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def headphone_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def smartwatch_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def constructor_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def photo_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def tv_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def console_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def coffee_filter(browser: Page) -> CategoryElements:
    return CategoryElements(browser)


@pytest.fixture(scope="function")
def search(browser: Page) -> SearchField:
    return SearchField(browser)
