from selenium.webdriver.chrome.webdriver import WebDriver

__author__ = 'GiSDeCain'

import pytest


@pytest.fixture(scope='session')
def driver(request):
    driver = WebDriver()
    request.addfinalizer(driver.quit)
    return driver
