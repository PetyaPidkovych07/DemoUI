from webbrowser import Chrome

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    driver = Chrome(ChromeDriverManager().install())
    request.cls.driver = driver
    yield driver


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920, 1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver

