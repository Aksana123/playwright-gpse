from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')

    def click(self, selector_or_locator):
        if isinstance(selector_or_locator, str):
            self.page.click(selector_or_locator)
        else:  # Assuming it's a Locator object
            selector_or_locator.click()

    def fill(self, selector_or_locator, value):
        if isinstance(selector_or_locator, str):
            self.page.fill(selector_or_locator, value)
        else:  # It's a Locator object
            selector_or_locator.fill(value)

    def wait_for_visible(self, selector):
        self.page.wait_for_selector(selector, state="visible")

    def is_visible(self, selector) -> bool:
        return self.page.is_visible(selector)

    def scroll_to_top(self):
        self.page.evaluate('window.scrollTo(0, 0)')

    def wait_for_absent(self, selector):
        self.page.wait_for_selector(selector, state="hidden")
