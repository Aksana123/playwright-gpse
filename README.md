
# Setup

## Install Dependencies: 

Ensure you have Python installed. Then, install the required dependencies listed in requirements.txt using the following command:

`pip install -r requirements.txt`

## Environment Configuration:

Create a .env file inside your project folder based on the .env.example provided.
Fill in the necessary environment variables.
When created, delete .env.example.

# Project Structure

pages: Contains page objects for different modules such as AMP, Planner, Agile, DI, and a base page.

tests: Holds test files for different modules, including regression tests for the Planner module.

resources: Includes any additional resources needed for testing, such as test data files.

utils: Contains utility modules for configuration management (config.py), logging (logger.py), email notifications (email.py), and other helper functions.

conftest.py: Defines fixtures, hooks, and configuration for Pytest testing framework.

.gitignore: Specifies files and directories to be ignored by version control system.

pytest.ini: Configuration file for Pytest.

.env.example: Example environment file with placeholders for environment variables.

requirements.txt: Lists all Python dependencies and their versions.

README.md: Documentation file providing an overview of the project, setup instructions, and usage guidelines.

run_tests.bat: Batch script to run the tests.

# How to Run Tests

Run in a Terminal:

`cmd.exe /c run_tests.bat`

or:

`pytest tests/your_module/your_test_file`