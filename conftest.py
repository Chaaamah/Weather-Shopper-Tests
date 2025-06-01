import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():
    service = Service(ChromeDriverManager().install())
    driver = Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()