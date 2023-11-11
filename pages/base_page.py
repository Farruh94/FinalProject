import allure
from playwright.sync_api import Page, Response


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def go_to(self, url: str) -> Response | None:
        with allure.step(f"Open the '{url}'"):
            return self.page.goto(url, timeout=500000)

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(timeout=50000)
