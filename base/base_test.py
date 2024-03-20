import pytest


from pages.login_page import LoginPage
from pages.nationalities_page import AdminNationalities





class BaseTest:



    login_page: LoginPage
    nationalities_page = AdminNationalities


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver


        request.cls.login_page = LoginPage(driver)
        request.cls.nationalities_page = AdminNationalities(driver)



