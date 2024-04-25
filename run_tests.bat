@echo off
echo Cleaning up old Allure results...
if exist allure-results rmdir /s /q allure-results
mkdir allure-results

echo Running tests and generating Allure results...
pytest --alluredir=allure-results

echo Generating Allure report...
allure generate allure-results --clean -o allure-report

echo Opening Allure report in the default web browser...
start allure-report\index.html

echo Allure report generated and opened in web browser.
pause
