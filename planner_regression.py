import pytest
from playwright.sync_api import Page
from management_page import ManagementPage
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# This tests depend on each other
@pytest.mark.smoke
def test_create_scenario(page: Page) -> None:
    management_page = ManagementPage(page)
    management_page.navigate_to_scenario()
    management_page.create_scenario()
    logging.info("Scenario Created")


def test_edit_scenario(page: Page) -> None:
    management_page = ManagementPage(page)
    management_page.update_scenario()
    logging.info("Scenario was updated")


def test_add_driver(page: Page) -> None:
    management_page = ManagementPage(page)
    management_page.add_driver()
    logging.info("Driver was added")


def test_add_al_driver(page: Page) -> None:
    management_page = ManagementPage(page)
    management_page.add_al_driver()
    logging.info("AL Driver was added")


@pytest.mark.regression
def test_save_scenario(page: Page) -> None:
    management_page = ManagementPage(page)
    management_page.optimize_scenario()
    management_page.save_scenario()
    management_page.go_back_to_scenario_management_page()
    logging.info("Scenario was saved")


@pytest.mark.regression
def test_copy_scenario(page: Page) -> None:
    management_page = ManagementPage(page)
    management_page.navigate_to_scenario()
    management_page.copy_scenario_button.click()
    logging.info("Scenario was copied")


@pytest.mark.smoke
def test_delete_scenario(page: Page) -> None:
    management_page = ManagementPage(page)
    management_page.delete_scenario()
    logging.info("Scenarios were deleted")

# @pytest.mark.smoke
# def test_save_as_scenario(page: Page) -> None:
#     management_page = ManagementPage(page)
#     management_page.navigate_to_scenario()
#     management_page.create_scenario()
#     management_page.optimize_scenario()
#     management_page.save_as_scenario()
#     page.goto(config.SCENARIO_PLANNER_PAGE)
#     if page.url == config.SCENARIO_PLANNER_PAGE:
#         management_page.save_as_updated_card.wait_for_selector("visible")
#         management_page.regular_card.wait_for_selector("visible")
#     management_page.delete_scenario()
#     logging.info("Scenarios were deleted")
