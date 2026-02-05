import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    browser.config.driver = driver
    driver.maximize_window()

    yield

    driver.quit()