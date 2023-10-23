import pytest
from playwright.sync_api import Page, sync_playwright

from components.navigation.sidebar import SideBar
from pages.centr_svyazi_main import CentrSvyaziMain
from pages.centr_svyazi import CentrSvyazi


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        context = chromium.new_context(viewport={"width": 1920, "height": 1080})
        yield context.new_page()


@pytest.fixture(scope='function')
def centr_svyazi_main(chromium_page: Page) -> CentrSvyaziMain:
    return CentrSvyaziMain(chromium_page)


@pytest.fixture(scope='function')
def centr_svyazi_logo(chromium_page: Page) -> CentrSvyazi:
    return CentrSvyazi(chromium_page)


@pytest.fixture(scope="function")
def catalog(chromium_page: Page) -> SideBar:
    return SideBar(chromium_page)


@pytest.fixture(scope="function")
def menu(chromium_page: Page) -> SideBar:
    return SideBar(chromium_page)
