from playwright.sync_api import Page
import config
import logging
import time


class ManagementPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_label = self.page.get_by_label("Username")
        self.password_label = self.page.get_by_label("Remember me")
        self.login_button = self.page.get_by_role("button", name="Log in")
        self.product_filter_button = self.page.get_by_role("button", name="Product(s) ")
        self.total_levis_checkbox = self.page.get_by_label("Total Levi's")
        self.period_filter_button = self.page.get_by_role("button", name="Period(s) ")
        self.fy21_checkbox = self.page.get_by_label("FY21")
        self.span = self.page.locator("#createForm span")
        self.simulation_filter_button = self.page.get_by_role("menuitem", name="Simulation ").locator("div")
        self.scenario_name = self.page.get_by_placeholder("Enter a name")
        self.create_scenario_button = self.page.get_by_role("button", name="Create scenario")
        self.delete_icon = self.page.get_by_test_id("DeleteOutlineOutlinedIcon")
        self.delete_confirmation = self.page.get_by_role("button", name="Delete Scenario")
        self.copy_scenario_button = self.page.get_by_role("button", name="content_copy")
        self.find_all_scenarios_headings_with_name = page.query_selector_all('h1[role="heading"]')
        self.find_scenario_names = self.page.query_selector_all('div:has-text("Regression TestSimulation")')
        self.edit_scenario_button = self.page.get_by_role("button", name="edit")
        self.enter_scenario_name = self.page.get_by_placeholder("Enter value").nth(1)
        self.update_button = self.page.get_by_role("button", name="Update").nth(1)
        self.edited_card_name = self.page.get_by_role("heading", name="Edited Regression Test")
        self.view_button = self.page.get_by_text("VIEW", exact=True)
        self.optimization_tab = self.page.get_by_text("Optimization", exact=True)
        self.percentage_input = self.page.locator("span").filter(has_text="Percentage %").get_by_role("textbox")
        self.optimize_button = self.page.get_by_role("button", name="")
        self.save_dropdown = self.page.get_by_label("Save changes").get_by_role("button", name="")
        self.save_button = self.page.locator("li.ant-dropdown-menu-item").filter(has_text="Save").locator("span")
        self.save_as_button = self.page.get_by_role("menuitem", name="Save as")
        self.save_new_scenario = self.page.get_by_role("button", name="Save as a new scenario")
        self.continue_with_new_scenario = self.page.get_by_role("button", name="Continue with new scenario (")
        self.scenario_management_button = self.page.get_by_role("button", name=" Scenario management")
        self.updated_volume_card = self.page.get_by_text("2.0%")
        self.successful_optimization_popup = self.page.locator("span").filter(has_text="Scenario has been").locator("a")
        self.successful_optimization_save = (self.page.locator("span").filter(has_text="Changes to the scenario have")
                                             .locator("a"))
        self.save_as_updated_card = self.page.get_by_role("heading", name="Scenario modified based on [")
        self.regular_card = self.page.get_by_role("heading", name="Regression Test", exact=True)
        self.no_scenarios_title = self.page.get_by_role("heading", name="No scenarios have been")
        self.optimizing_scenario_close = (self.page.locator("span").filter(has_text="Optimizing scenario ...")
                                          .locator("a"))

    def create_scenario(self):
        self.product_filter_button.click()
        self.total_levis_checkbox.click()
        self.period_filter_button.click()
        self.fy21_checkbox.click()
        self.span.nth(1).click()
        self.simulation_filter_button.click()
        self.scenario_name.click()
        self.scenario_name.fill("Regression Test")
        self.create_scenario_button.click()

    def navigate_to_scenario(self):
        self.page.goto(config.SCENARIO_PLANNER_PAGE)

    def delete_scenario(self):
        self.delete_icon.first.click()
        self.delete_confirmation.click()
        time.sleep(3)
        self.delete_icon.first.click()
        self.delete_confirmation.click()

        # while True:
        #     delete_icon = self.delete_icon.first
        #     if not delete_icon:
        #         logging.info("No more delete icons found. Exiting loop.")
        #         break
        #     try:
        #         delete_icon.click()
        #         self.delete_confirmation.click()
        #         logging.info("Delete icon clicked.")
        #         time.sleep(0.5)
        #         self.page.wait_for_selector_absent(self.delete_icon)
        #     except Exception as e:
        #         logging.error(f"Error occurred during deletion: {e}")
        #         break

    def update_scenario(self):
        self.edit_scenario_button.click()
        self.enter_scenario_name.click()
        self.enter_scenario_name.fill('Edited Regression Test')
        self.update_button.click()

    def optimize_scenario(self):
        self.view_button.click()
        self.optimization_tab.click()
        self.percentage_input.click()
        self.percentage_input.fill("105")
        self.optimize_button.click()
        self.optimizing_scenario_close.click()
        self.successful_optimization_popup.click()

    def save_scenario(self):
        self.save_dropdown.dblclick()
        self.page.evaluate('window.scrollTo(0, 0)')
        while not self.save_button.is_visible():
            self.save_dropdown.dblclick()
            time.sleep(1)
        self.save_button.click()

    def save_as_scenario(self):
        self.save_dropdown.dblclick()
        self.page.evaluate('window.scrollTo(0, 0)')
        while not self.save_as_button.is_visible():
            self.save_dropdown.dblclick()
            time.sleep(1)
        self.save_as_button.click()
        self.save_new_scenario.click()
        self.continue_with_new_scenario.click()

    def go_back_to_scenario_management_page(self):
        time.sleep(2)
        self.page.goto(config.SCENARIO_PLANNER_PAGE)
        self.page.wait_for_load_state("networkidle")

        if self.successful_optimization_save.is_visible():
            self.page.goto(config.SCENARIO_PLANNER_PAGE)

        if self.page.url == config.SCENARIO_PLANNER_PAGE:
            self.updated_volume_card.wait_for_selector("visible")
