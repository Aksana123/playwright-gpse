Playwright Python Test Setup

Installation:

Clone the repository:
`git clone <repo>`

Install inside project:
`pip install playwright` - installs Playwright
`playwright install` - installs Playwright browsers
`pip install pytest` - install pytest

Configuration
Ensure that you have configured the following parameters in the config_example.py file. When done, rename to config.py:

BASE_URL: The base URL of the application under test.
USERNAME: The username for logging into the application.
PASSWORD: The password for logging into the application.

Running Tests
To run the tests, execute the following command:

pytest test_file.py

Test File: planner_regression.py
This file contains test cases for scenario management. Tests are categorized into smoke and regression tests. They cover scenario creation, optimization, saving, copying, and deletion.

Page Object File: management_page.py
This file defines the ManagementPage class, which encapsulates the elements and actions related to scenario management as well as login. It provides methods for creating, updating, optimizing, saving, copying, and deleting scenarios.

Fixture File: conftest.py
This file contains a fixture named page, which sets up the Playwright environment, launches a browser, navigates to the login page, logs in with the provided credentials, and yields the page object for test execution. After test execution, it closes the page and the browser.

Logging
Logging is configured using the Python logging module. Logs are displayed with timestamps and levels (INFO, ERROR) to track the test execution flow and any encountered errors.

Notes
Ensure that Playwright dependencies are installed and compatible with your system.
Adjust test parameters and configurations as per your application's requirements.

Let me know if you face any issues.