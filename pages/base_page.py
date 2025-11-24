from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class BasePage:
    BASE_URL = "https://vod.film/" 

    def __init__(self, page: Page):
        self.page = page

    def goto(self, path: str = ""):
        url = self.BASE_URL + path
        self.page.goto(url)

    def wait_for(self, selector: str, timeout: int = 10000):
        try:
            return self.page.wait_for_selector(selector, timeout=timeout)
        except PlaywrightTimeoutError:
            raise AssertionError(f"Element nie pojawił się: {selector}")

    def click(self, selector: str):
        self.wait_for(selector)
        self.page.click(selector)

    def type(self, selector: str, value: str):

        self.wait_for(selector)
        self.page.fill(selector, value)

    def get_text(self, selector: str) -> str:
        self.wait_for(selector)
        return self.page.inner_text(selector)

    def get_attribute(self, selector: str, attr: str):
        self.wait_for(selector)
        return self.page.get_attribute(selector, attr)
