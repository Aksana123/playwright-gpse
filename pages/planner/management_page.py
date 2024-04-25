from playwright.sync_api import Page
from pages.base_page import BasePage
from utils import config
import time
import re


class ManagementPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.username_label = self.page.get_by_label("Username")
        self.password_label = self.page.get_by_label("Remember me")
        self.login_button = self.page.get_by_role("button", name="Log in")
        self.product_filter_button = self.page.get_by_role("button", name="Product(s) ")
        self.total_levis_checkbox = self.page.get_by_label("Total Levi's")
        self.period_filter_button = self.page.get_by_role("button", name="Period(s) ")
        self.select_company_title = self.page.get_by_role("heading", name="Select Company")
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
        self.created_card = self.page.get_by_role("heading", name="Regression Test")
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
        self.updated_volume_card = self.page.get_by_text("2.1%")
        self.successful_optimization_popup = self.page.locator("span").filter(has_text="Scenario has been").locator("a")
        self.successful_optimization_save = (self.page.locator("span").filter(has_text="Changes to the scenario have")
                                             .locator("a"))
        self.save_as_updated_card = self.page.get_by_role("heading", name="Scenario modified based on [")
        self.regular_card = self.page.get_by_role("heading", name="Regression Test", exact=True)
        self.no_scenarios_title = self.page.get_by_role("heading", name="No scenarios have been")
        self.optimizing_scenario_close = (self.page.locator("span").filter(has_text="Optimizing scenario ...")
                                          .locator("a"))
        self.add_driver_button = self.page.get_by_role("button", name="")
        self.add_new_driver_name = self.page.get_by_label("Add new driver").locator("input[type=\"text\"]")
        self.new_driver_kpi_1 = self.page.locator("div").filter(has_text=re.compile(r"^KPI 1ROI$")).get_by_role(
            "textbox")
        self.new_driver_kpi_2 = (self.page.locator("div").filter(has_text=re.compile(r"^KPI 2Cost Per Acquisition$"))
                                 .get_by_role("textbox"))
        self.new_driver_spend = self.page.get_by_label("Add new driver").get_by_role("textbox").nth(3)
        self.new_driver_activity = self.page.get_by_label("Add new driver").get_by_role("textbox").nth(4)
        self.new_driver_add_form_button = self.page.get_by_role("button", name="Add driver")
        self.new_driver_name_card = self.page.get_by_text("Test Automation")
        self.new_driver_spend_card = self.page.get_by_text("$150,000")
        self.new_driver_activity_card = self.page.get_by_text("200,000")
        self.new_driver_roi_card = self.page.locator("h2").filter(has_text="1.50").locator("span")
        self.kpi_dropdown = self.page.locator(".ant-select-arrow").first
        self.kpi_dropdown_kpi_2 = self.page.get_by_role("menuitem", name="KPI 2")
        self.kpi_dropdown_kpi_1 = self.page.get_by_role("menuitem", name="KPI 1")
        self.select_al_driver = self.page.get_by_role("menuitem", name="Add driver from Agile Learning")
        self.select_add_driver_dropdown = self.page.get_by_text("Add driver manually")
        self.select_ecommerce_dropdown = self.page.get_by_text("Ecommerce Sales")
        self.select_manual_entry = self.page.get_by_role("menuitem", name="Manual Entry")
        self.new_al_driver_kpi_1 = (self.page.locator("div").filter(has_text=re.compile(r"^KPI 1Manual EntryROI$"))
                                    .get_by_role("textbox"))
        self.new_al_driver_kpi_2 = (self.page.locator("div").filter(has_text=re.compile(r"^KPI 2Manual EntryCost Per "
                                                                                        r"Acquisition$"))
                                    .get_by_role("textbox"))
        self.new_al_driver_spend = (self.page.locator("form div").filter(has_text="Spend Activity")
                                    .get_by_role("textbox"))
        self.new_al_driver_activity = (self.page.locator("form div").filter(has_text="Spend Activity")
                                       .get_by_role("textbox"))
        self.new_al_driver_name_card = self.page.get_by_text("AL Driver")
        self.new_al_driver_spend_card = self.page.get_by_text("$160,000")
        self.new_al_driver_activity_card = self.page.get_by_text("205,000")
        self.new_al_driver_roi_card = self.page.locator("h2").filter(has_text="1.60").locator("span")
        self.driver_save_popup = self.page.locator("span").filter(has_text="The simulation has run").locator("a")

    def create_scenario(self):
        self.click(self.product_filter_button)
        self.click(self.total_levis_checkbox)
        self.click(self.period_filter_button)
        self.click(self.fy21_checkbox)
        self.click(self.span.nth(1))
        self.click(self.simulation_filter_button)
        self.fill(self.scenario_name, "Regression Test")
        self.click(self.create_scenario_button)
        self.created_card.wait_for(state="visible", timeout=10000)
        pass

    def check_created_card_visible(self):
        return self.created_card.is_visible()
    pass

    def navigate_to_scenario(self):
        self.navigate(config.SCENARIO_PLANNER_PAGE)

    def delete_scenario(self):
        self.click(self.delete_icon.first)
        self.click(self.delete_confirmation)
        time.sleep(3)
        self.click(self.delete_icon.first)
        self.click(self.delete_confirmation)

    def update_scenario(self):
        self.click(self.edit_scenario_button)
        self.fill(self.enter_scenario_name, 'Edited Regression Test')
        self.click(self.update_button)

    def optimize_scenario(self):
        self.click(self.optimization_tab)
        self.fill(self.percentage_input, "105")
        self.click(self.optimize_button)
        time.sleep(3)
        self.click(self.successful_optimization_popup)

    def add_driver(self):
        self.click(self.view_button)
        self.click(self.add_driver_button)
        self.fill(self.add_new_driver_name, "Test Automation")
        self.fill(self.new_driver_kpi_1, "1.5")
        self.fill(self.new_driver_kpi_2, "1.5")
        self.fill(self.new_driver_spend, "150000")
        self.fill(self.new_driver_activity, "200000")
        self.click(self.new_driver_add_form_button)

    def add_al_driver(self):
        self.click(self.add_driver_button)
        self.click(self.select_add_driver_dropdown)
        self.click(self.select_al_driver)
        self.fill(self.add_new_driver_name, "AL Driver")
        self.fill(self.new_al_driver_kpi_1, "1.6")
        self.fill(self.new_al_driver_kpi_2, "1.6")
        self.fill(self.new_al_driver_spend, "160000")
        self.fill(self.new_al_driver_activity, "205000")
        self.click(self.new_driver_add_form_button)

    def save_scenario(self):
        self.double_click(self.save_dropdown)
        time.sleep(3)
        self.scroll_to_top()
        while not self.is_visible(self.save_button):
            self.double_click(self.save_dropdown)
            time.sleep(1)
        self.click(self.save_button)

    def save_as_scenario(self):
        self.double_click(self.save_dropdown)
        while not self.is_visible(self.save_as_button):
            self.double_click(self.save_dropdown)
            time.sleep(1)
        self.click(self.save_as_button)
        self.click(self.save_new_scenario)
        self.click(self.continue_with_new_scenario)

    def go_back_to_scenario_management_page(self):
        time.sleep(2)
        self.navigate(config.SCENARIO_PLANNER_PAGE)
        if self.is_visible(self.successful_optimization_save):
            self.navigate(config.SCENARIO_PLANNER_PAGE)
        if self.page.url == config.SCENARIO_PLANNER_PAGE:
            self.wait_for_visible(self.updated_volume_card)

    def double_click(self, save_dropdown):
        pass
