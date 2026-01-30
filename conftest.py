import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    if os.getenv("CI"):
        # Ми у GitHub Actions → використовуємо системний Chrome
        options.binary_location = "/usr/bin/google-chrome"
        driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)
    else:
        # Локально → webdriver_manager сам качає драйвер
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    request.cls.driver = driver
    yield driver
    driver.quit()







# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     options = Options()
#     #options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920,1080")
#
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()


# from webbrowser import Chrome
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
#
#
#
# @pytest.fixture()
# def driver(request):
#     driver = Chrome(ChromeDriverManager().install())
#     request.cls.driver = driver
#     yield driver
#
#
#
#
# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     options = Options()
#     #options.add_argument("--headless")  # важливо для сучасного Chrome
#     options.add_argument("--no-sandbox")
#     #options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--window-size=1920, 1080")
#     # options.add_argument("--disable-gpu")
#     # options.add_argument("--disable-software-rasterizer")
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
#
#
#
#
