from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Chrome browser is launching....")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Firefox browser is launching....")
    else:
        driver = webdriver.Ie()  #This for default browser when you are not mention the browser

    return driver            #it wil open default automattically (default browser your system have)
                                 #like this...pytest -v -s TestCases/test_login.py

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):        # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# It is Hook for Adding Environment info to HTML Report
def pytest_html_results_table_html(report, data):
    if report.when == 'call':
        data.append(("Project Name", "Your Project Name"))
        data.append(("Module Name", "Your Module Name"))
        data.append(("Tester", "Your Tester Name"))

def pytest_html_report_title(report):
    report.title = "Your Custom HTML Report Title"














