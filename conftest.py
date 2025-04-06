import os
import pytest
from selenium import webdriver
from datetime import datetime
from utils.utils import take_screenshot


#Defing the variables used in different modules


def pytest_configure(config):
    """Hook to configure the test report settings."""
    config.option.html_path = f"reports/test_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
    config.option.self_contained_html = True  # Embed assets into the report

def pytest_html_report_title(report):
    """Customize the title of the HTML report."""
    report.title = "Automated SauceDemo Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    """Customize the summary section of the HTML report."""
    prefix.extend(["<p><strong>Test Executed By:</strong> Nikesh(QA Team)</p>"])
    prefix.extend(["<p><strong>Project:</strong> SauceDemo Selenium Automation Suite</p>"])

def pytest_html_results_table_header(cells):
    """Modify the report table header."""
    cells.insert(2, "Description")  # Adding a new column for test descriptions

def pytest_html_results_table_row(report, cells):
    """Modify the report table row."""
    cells.insert(2, report.nodeid)  # Populate the test description column


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialise Webdriver and clean up after test."""
    URL_LOGIN = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL_LOGIN)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    """
    Pytest hook to take screenshots when a test fails
    """
    # Execute the test first.
    outcome = yield
    report = outcome.get_result()
    test_name = report.nodeid.replace("::","_").replace("/",'_').replace('.py','') #Clean up for the test name
    # Check if the test failed
    if report.when == "call" and report.failed:
        # Get the driver
        try:
            driver =item.funcargs.get("driver", None)
            if driver:
                take_screenshot(driver, test_name)

        except Exception as e:
            print(f"Failed to capture the screenshot :{e}") # error message


