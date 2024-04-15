import pytest
from playwright.sync_api import sync_playwright
import config
import logging
from management_page import ManagementPage


@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Define login function
        def login():
            management_page = ManagementPage(page)
            page.goto(config.BASE_URL)
            logging.info("Navigated to login page")

            management_page.username_label.click()
            management_page.username_label.fill(config.USERNAME)
            logging.info("Entered username")

            management_page.password_label.click()
            management_page.password_label.fill(config.PASSWORD)
            logging.info("Entered password")

            management_page.login_button.click()
            logging.info("Clicked login button")

            page.wait_for_timeout(1000)

        login()

        yield page

        page.close()
        browser.close()
