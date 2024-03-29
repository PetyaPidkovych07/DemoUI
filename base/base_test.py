import pytest


from pages.login_page import LoginPage
from pages.nationalities_page import AdminNationalities
from pages.directory_page import Directory
from pages.pim_reports_page import PimReports
from pages.vacancies_page import Vacancies
from pages.recruitment_candidates_page import Recruitment_Candidate





class BaseTest:



    login_page: LoginPage
    nationalities_page = AdminNationalities
    directory_page = Directory
    pim_reports_page = PimReports
    vacancies_page = Vacancies
    recruitment_candidate_page = Recruitment_Candidate


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver


        request.cls.login_page = LoginPage(driver)
        request.cls.nationalities_page = AdminNationalities(driver)
        request.cls.directory_page = Directory(driver)
        request.cls.pim_reports_page = PimReports(driver)
        request.cls.vacancies_page = Vacancies(driver)
        request.cls.recruitment_candidate_page = Recruitment_Candidate(driver)



