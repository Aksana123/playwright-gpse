import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pages.planner.management_page import ManagementPage
from utils.config import EnvironmentConfig, ENVIRONMENTS
from utils.email import send_email
import allure
import os
import logging
from utils.logger import setup_logging


setup_logging()
logging.basicConfig(level=logging.INFO, format='[%(levelname)s:%(threadName)s %(asctime)s.%(msecs)03d] %(message)s')


load_dotenv()

DEFAULT_ENVIRONMENT = EnvironmentConfig.USA_STAGE


@pytest.fixture(scope="session")
def environment():
    return DEFAULT_ENVIRONMENT


@pytest.fixture(scope="session")
def config(environment):
    return ENVIRONMENTS[environment]


@pytest.fixture(scope="session")
def base_url(environment):
    return ENVIRONMENTS[environment]["base_url"]


@pytest.fixture(scope="session")
def username(environment):
    return ENVIRONMENTS[environment]["username"]


@pytest.fixture(scope="session")
def password(environment):
    return ENVIRONMENTS[environment]["password"]


@pytest.fixture(scope="session")
def page(base_url, username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        def login():
            management_page = ManagementPage(page)
            page.goto(base_url)
            logging.info(f"Navigated to {base_url}")
            management_page.username_label.click()
            management_page.username_label.fill(username)
            logging.info(f"Filled username: {username}")
            management_page.password_label.click()
            management_page.password_label.fill(password)
            logging.info(f"Filled password: [HIDDEN]")
            management_page.login_button.click()
            page.wait_for_timeout(1000)
            management_page.select_company_title.wait_for(state="visible", timeout=10000)
            logging.info("Logged in successfully.")

        login()
        yield page
        page.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    yield  # Let other hooks execute before this code runs

    total = session.testscollected
    failed = session.testsfailed
    passed = total - failed

    meta_url = os.getenv('META_URL', 'default-meta-url')
    recipients = os.getenv('TEST_EMAIL_RECIPIENTS', 'default@example.com').split(',')
    subject = "Daily Test Report"
    body = f"Total tests: {total}\nPassed: {passed}\nFailed: {failed}"

    send_email(meta_url, recipients, subject, body, DEFAULT_ENVIRONMENT)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        if call.excinfo is not None:
            if call.excinfo.typename != "Skipped":
                logging.error(f"{item.nodeid} FAILED: {call.excinfo.value}")
            else:
                logging.info(f"{item.nodeid} SKIPPED")
        else:
            logging.info(f"{item.nodeid} PASSED")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.outcome != 'passed':
        with allure.step('Add screenshot on failure'):
            allure.attach(item.funcargs['page'].screenshot(), name="Screenshot on Failure",
                          attachment_type=allure.attachment_type.PNG)

    if report.when == 'call':
        if report.failed:
            allure.dynamic.severity(allure.severity_level.CRITICAL)
        elif report.skipped:
            allure.dynamic.severity(allure.severity_level.MINOR)
        else:
            allure.dynamic.severity(allure.severity_level.NORMAL)


@pytest.fixture
def wait_for_selector(page):
    def _wait_for_selector(selector, timeout=30000):
        return page.wait_for_selector(selector, state='attached', timeout=timeout)

    return _wait_for_selector
