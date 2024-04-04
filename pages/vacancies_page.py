import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC





class Vacancies(BasePage):

    PAGE_URL = Links.RECRUITMENT_VACANCIES

    CHOOSE_RECRUITMENT_FROM_MENU = ("xpath", "//span[text()='Recruitment']")
    VACANCIES_LINK = ("xpath", "//a[text()='Vacancies']")
    ADD_BTN = ("xpath", "//button[text()=' Add ']")
    ITEM_VACANCY_FROM_TABLE = (
    "xpath", "//div[@class='oxd-table-body']//div[@role='row']//*[contains(text(), 'Petro')]")
    ITEM_VACANCY_SOFTWARE_ENGINEER_FROM_Table = (
    "xpath", "//div[@class='oxd-table-body']//div[@role='row']//*[contains(text(), 'Roman')]")
    ITEM_VACANCY_SOFTWARE_ARCHITECT_FROM_TABLE = (
    "xpath", "//div[@class='oxd-table-body']//div[@role='row']//*[contains(text(), 'Taras')]")
    ITEM_VACANCY_SOFTWARE_CONTENT_FROM_TABLE = (
        "xpath", "//div[@class='oxd-table-body']//div[@role='row']//*[contains(text(), 'Vika')]")
    # addddddddddddddddddddd vacancyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    Vacancy_Name_Input = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    HIRING_INPUT = ("xpath", "//input[@placeholder='Type for hints...']")
    HINT_TO_HIRING = ("xpath", "//span[text()='Odis  Adalwin']")
    DROPDOWN_JOB_TITTLE = ("xpath", "(//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow' ])[1]")
    DROPDOWN_SELECT_ITEM_FROM_JOB_TITTLE = ("xpath", "//div[@role='listbox']//span[text()='QA Lead']")
    DROPDOWN_SELECT_ITEM_FROM_SOFT_TITTLE = ("xpath", "//div[@role='listbox']//span[text()='Software Engineer']")
    DROPDOWN_SELECT_ITEM_FROM_ARCHITECT_TITTLE = ("xpath", "//div[@role='listbox']//span[text()='Software Architect']")
    DROPDOWN_SELECT_ITEM_FROM_CONTENT_TITTLE = ("xpath", "//div[@role='listbox']//span[text()='Content Specialist']")
    DROPDOWN_SELECT_ITEM_FROM_SALES_TITTLE = ("xpath", "//div[@role='listbox']//span[text()='Sales Representative']")
    SAVE_BTN = ("xpath", "//button[text()=' Save ']")
    ERROR_REQUIRED = ("xpath", "//span[text()='Required']")
    ERROR_ALREADY_EXISTS = ("xpath", "//span[text()='Already exists']")
    PUSH_NOTIFICATION = ("xpath", "//p[text()='Successfully Saved']")
    All_USERS = ("xpath", "//div[@class='oxd-table-body']//div[@role='row']")
    SEARCH_BTN = ("xpath", "//button[text()=' Search ']")
    JOB_TITTLE_COLUMN = ("xpath", ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]")
    # block /////////////////////////////////////////////////////////vacanciesssssssssssssss
    ICON_BUTTON = ("xpath", "(//button[@type='button'][@class='oxd-icon-button'])[2]")
    BLOCK_EMPLOYEE_INFORMATION = ("xpath", "//div[@class='oxd-grid-4 orangehrm-full-width-grid']")


    def click_on_recruitment_item(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_RECRUITMENT_FROM_MENU)).click()

    def click_on_vacancies_item(self):
        self.wait.until(EC.element_to_be_clickable(self.VACANCIES_LINK)).click()

    def click_on_add_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BTN)).click()

    def type_petro_in_the_field(self):
        self.wait.until(EC.element_to_be_clickable(self.Vacancy_Name_Input)).send_keys('Petro')

    def click_on_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_JOB_TITTLE)).click()

    def choose_QA_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_JOB_TITTLE)).click()

    def choose_engineer_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_SOFT_TITTLE)).click()

    def choose_sales_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_SALES_TITTLE)).click()

    def type_odis(self):
        self.wait.until(EC.element_to_be_clickable(self.HIRING_INPUT)).send_keys('Odis')

    def click_on_hint(self):
        self.wait.until(EC.element_to_be_clickable(self.HINT_TO_HIRING)).click()

    def click_on_save_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()
        time.sleep(2)

    def click_on_search_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()


    def is_added_new_vacancy(self):
        self.wait.until(EC.element_to_be_clickable(self.VACANCIES_LINK)).click()
        x = self.wait.until(EC.visibility_of_element_located(self.ITEM_VACANCY_FROM_TABLE)).text
        assert x == 'Petro'

    def is_already_existed_position(self):
        text_already = self.wait.until(EC.visibility_of_element_located(self.ERROR_ALREADY_EXISTS)).text
        assert text_already == 'Already exists'

    def is_shown_error_when_empty_field(self):
        text_error = self.wait.until(EC.visibility_of_element_located(self.ERROR_REQUIRED)).text
        assert text_error == 'Required'

    def is_displayed_engineer_in_table(self):
        time.sleep(2)
        vacancy = []
        job_title = []

        try:


            for i in range(1, 6):
                vacancy_column = self.wait.until(EC.visibility_of_all_elements_located(self.All_USERS))
                for user in vacancy_column:
                    vacancy.append(user.find_element("xpath", ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)
                    job_title.append(user.find_element("xpath",".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]").text)

                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()
        except NoSuchElementException:
            pass

        list = ["Software Engineer"]
        print(list)

        print(f"Users: {vacancy}")
        print(f"Job Title: {job_title}")

        assert len(job_title) == 1
        assert list == job_title


    def is_displayed_sales_in_table(self):
        time.sleep(2)
        vacancy = []
        job_title = []

        try:


            for i in range(1, 6):
                vacancy_column = self.wait.until(EC.visibility_of_all_elements_located(self.All_USERS))
                for user in vacancy_column:
                    vacancy.append(user.find_element("xpath", ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)
                    job_title.append(user.find_element("xpath",".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]").text)

                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()
        except NoSuchElementException:
            pass

        list = ["Sales Representative"]
        print(list)

        print(f"Users: {vacancy}")
        print(f"Job Title: {job_title}")

        assert len(job_title) == 1
        assert list == job_title
