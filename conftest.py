import pytest
from playwright.sync_api import Page, sync_playwright

from components.basket_elements import BasketElements
from components.main_page_elements import MainPageElements
from components.sidebar import SideBar
from pages.centr_svyazi import CentrSvyazi


# from pages.centr_svyazi_main import CentrSvyaziMain


@pytest.fixture(scope="function")
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        context = chromium.new_context(viewport={"width": 1920, "height": 1080})
        yield context.new_page()


# @pytest.fixture(scope="function")
# def centr_svyazi_main(chromium_page: Page) -> CentrSvyaziMain:
#     return CentrSvyaziMain(chromium_page)


# @pytest.fixture(scope="function")
# def centr_svyazi_logo(chromium_page: Page) -> CentrSvyazi:
#     return CentrSvyazi(chromium_page)


# @pytest.fixture(scope="function")
# def catalog(chromium_page: Page) -> SideBar:
#     return SideBar(chromium_page)


# @pytest.fixture(scope="function")
# def menu(chromium_page: Page) -> SideBar:
#     return SideBar(chromium_page)


# @pytest.fixture(scope="function")
# def mobile_phone(chromium_page: Page) -> CentrSvyazi:
#     return CentrSvyazi(chromium_page)


@pytest.fixture(scope="function")
def sidebar_elems(chromium_page: Page) -> SideBar:
    return SideBar(chromium_page)


@pytest.fixture(scope="function")
def mobile_hover(chromium_page: Page) -> SideBar:
    return SideBar(chromium_page)


@pytest.fixture(scope="function")
def check_addresses(chromium_page: Page) -> MainPageElements:
    return MainPageElements(chromium_page)


@pytest.fixture(scope="function")
def check_social_media(chromium_page: Page) -> MainPageElements:
    return MainPageElements(chromium_page)


@pytest.fixture(scope="function")
def check_logo(chromium_page: Page) -> MainPageElements:
    return MainPageElements(chromium_page)


@pytest.fixture(scope="function")
def empty_basket(chromium_page: Page) -> BasketElements:
    return BasketElements(chromium_page)


@pytest.fixture(scope="function")
def not_empty(chromium_page: Page) -> BasketElements:
    return BasketElements(chromium_page)


@pytest.fixture(scope="function")
def check_credit(chromium_page: Page) -> MainPageElements:
    return MainPageElements(chromium_page)


@pytest.fixture(scope="function")
def check_trade_in(chromium_page: Page) -> MainPageElements:
    return MainPageElements(chromium_page)


@pytest.fixture(scope="function")
def check_delivery(chromium_page: Page) -> MainPageElements:
    return MainPageElements(chromium_page)
