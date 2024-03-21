from selenium.webdriver import ActionChains

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time




class Directory(BasePage):

    PAGE_URL = Links.DIRECTORY

    ITEM_DIRECTORY_FROM_MENU = ("xpath", "//span[text()='Directory']")
    NAME_INPUT = ("xpath", "//input[@placeholder='Type for hints...']")
    DROPDOWN_JOB_TITTLE = ("xpath", "(//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow' ])[1]")
    DROPDOWN_SELECT_ITEM_FROM_JOB_TITTLE = ("xpath", "//div[@role='listbox']//span[text()='Software Engineer']")
    DROPDOWN_LOCATION = ("xpath", "(//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow' ])[2]")
    SELECT_ITEM_LOCATION_FORM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Texas R&D']")
    SELECT_ITEM_HR_FORM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='HR Manager']")
    SELECT_ITEM_ACCOUNT_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Account Assistant']")
    SELECT_ITEM_CHIEF_EXECUTIVE_FROM_DROPDOWN = (
    "xpath", "//div[@role='listbox']//span[text()='Chief Executive Officer']")
    SELECT_ITEM_CHIEF_TECHNICAL_FROM_DROPDOWN = (
    "xpath", "//div[@role='listbox']//span[text()='Chief Technical Officer']")
    SELECT_ITEM_CONTENT_SPECIALIST_FROM_DROPDOWN = (
    "xpath", "//div[@role='listbox']//span[text()='Content Specialist']")
    SELECT_ITEM_CONTENT_DATABASE_FROM_DROPDOWN = (
    "xpath", "//div[@role='listbox']//span[text()='Database Administrator']")
    SELECT_ITEM_FINANCE_MANAGER_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Finance Manager']")
    SELECT_ITEM_FINANCE_ANALYST_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Financial Analyst']")
    SELECT_ITEM_SUPPORT_SPESIALIST_FROM_DROPDOWN = (
    "xpath", "//div[@role='listbox']//span[text()='Support Specialist']")
    SELECT_ITEM_CUSTOMER_MANAGER_FROM_DROPDOWN = (
    "xpath", "//div[@role='listbox']//span[text()='Customer Success Manager']")
    SELECT_ITEM_CUSTOMER_ARCHITECT_FROM_DROPDOWN = (
    "xpath", "//div[@role='listbox']//span[text()='Software Architect']")
    SELECT_ITEM_CUSTOMER_CHIEF_FINANCIAL_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Chief Financial Officer']")

    SEARCH_BTN = ("xpath", "//button[text()=' Search ']")
    ALL_BLOCK = ("xpath", "//div[@class='orangehrm-container']/div")
    ALL_BLOCK1 = (
    "xpath", "//div[@class='orangehrm-corporate-directory']//div[@class='oxd-grid-item oxd-grid-item--gutters']")
    ALL = (
    "xpath", "//p[@class= 'oxd-text oxd-text--p orangehrm-directory-card-header --break-words' and contains (.,'')]")
    ALL1 = ("xpath", "//div[@class= 'orangehrm-container']")
    LAST_ITEM = ("xpath",
                 "//div[@class='orangehrm-corporate-directory']//div[@class='oxd-grid-item oxd-grid-item--gutters'][last()]")
    ALL_IMAGES = ("xpath", "//div[contains(@class, 'orangehrm-profile-picture')]")
    NAME_EMPLOYEE_FROM_PROFILE = ("xpath",
                                  "//p[contains(@class, 'oxd-text oxd-text--p orangehrm-directory-card-header --break-words')][contains(text(), '')]")
    HR_MANAGER = ("xpath",
                  "//p[contains(@class, 'oxd-text oxd-text--p orangehrm-directory-card-subtitle --break-words')][contains(text(), '')]")
    LOCATION_EMPLOYEE_FROM_PROFILE = ("xpath",
                                      "//p[contains(@class, 'oxd-text oxd-text--p orangehrm-directory-card-description --break-words')][contains(text(), '')]/following-sibling::p")
    BLYYYYY = ("xpath",
               "//div[@class='oxd-grid-4']//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--white orangehrm-directory-card']")
    ITEM_14 = (
    "xpath", "//div[@class='orangehrm-corporate-directory']//div[@class='oxd-grid-item oxd-grid-item--gutters'][14]")
    ITEM_27 = (
    "xpath", "//div[@class='orangehrm-corporate-directory']//div[@class='oxd-grid-item oxd-grid-item--gutters'][27]")
    ITEM_40 = (
    "xpath", "//div[@class='orangehrm-corporate-directory']//div[@class='oxd-grid-item oxd-grid-item--gutters'][42]")
    EEACH_BLOCK_FROM_TABLE = (
        "xpath", "//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--white orangehrm-directory-card']")
    HINT_FROM_INPUT = ("xpath", "//div[@role='listbox']//span[contains(text(), 'pho')]")
    # Item_name = (By.XPATH, "//p[text()='phone  sdagag']")
    ITEM_NAME2 = ("xpath", "(//div[@class='orangehrm-container']//div/p)[1]")
    ICON_BUTTON = ("xpath", "(//button[@type='button'][@class='oxd-icon-button'])[2]")
    DIRECTORY_INFORMATION_BLOCK = ("xpath", "//div[@class='oxd-table-filter-area']")
    ONE = ("xpath", "(//div[contains(@class, 'orangehrm-profile-picture')])[1]")
    TWO = ("xpath", "(//div[contains(@class, 'orangehrm-profile-picture')])[2]")
    THREE = ("xpath", "(//div[contains(@class, 'orangehrm-profile-picture')])[3]")
    WORK_EMAIL = (
    "xpath", "(//p[contains(@class, 'oxd-text oxd-text--p oxd-text--toast-title')][contains(text(), '')])[2]")
    PUSH_NOTIFICATION_NO_RECORDS = ("xpath", "//p[text()='No Records Found']")


    def click_on_directory_item(self):
        self.wait.until(EC.element_to_be_clickable(self.ITEM_DIRECTORY_FROM_MENU)).click()

    def click_on_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_JOB_TITTLE)).click()

    def click_on_location_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_LOCATION)).click()

    def choose_item_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_JOB_TITTLE)).click()

    def choose_hr_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_ITEM_HR_FORM_DROPDOWN)).click()

    def choose_job_title_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_JOB_TITTLE)).click()

    def choose_chief_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_ITEM_CHIEF_TECHNICAL_FROM_DROPDOWN)).click()

    def choose_all_location_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_ITEM_LOCATION_FORM_DROPDOWN)).click()

    def click_on_search_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()

    def is_present_software_in_table(self):
        results = self.wait.until(EC.visibility_of_all_elements_located(self.NAME_EMPLOYEE_FROM_PROFILE))
        size_list = []

        for size in results:
            size_list.append(size.text)
        print(size_list)

        name_employee = ['Russel Hamilton']
        assert name_employee == size_list

    def is_present_hr_in_table(self):
        results = self.wait.until(EC.visibility_of_all_elements_located(self.HR_MANAGER))
        size_list = []

        for size in results:
            size_list.append(size.text)
        print(size_list)

        name_employee = ['HR Manager']
        assert name_employee == size_list

    def is_present_chief_technical_in_table(self):
        results = self.wait.until(EC.visibility_of_all_elements_located(self.HR_MANAGER))
        size_list = []

        for size in results:
            size_list.append(size.text)
        print(size_list)

        name_employee = ['Chief Technical Officer']
        assert name_employee == size_list


    def is_displayed_locations__in_dropdown(self):
        location = self.wait.until(EC.visibility_of_all_elements_located(self.LOCATION_EMPLOYEE_FROM_PROFILE))
        size_list = []

        for size in location:
            size_list.append(size.text)
        print(size_list)

        location = ['Texas R&D', 'Texas R&D', 'Texas R&D', 'Texas R&D']
        assert location == size_list


    def is_each_user_have_email(self):
        global users_profile
        all_items = self.wait.until(EC.visibility_of_all_elements_located(self.ALL))
        print(all_items)

        action = ActionChains(self.driver)

        for i in all_items:
            action.move_to_element(i).move_by_offset(0, 6).click()
            time.sleep(2)
            action.perform()
            time.sleep(2)
            users_profile = []
            all = self.wait.until(EC.visibility_of_all_elements_located(self.WORK_EMAIL))
            for size in all:
                time.sleep(2)
                users_profile.append(size.text)
            print(f"Show only software employee: {size.text}")

        email = ['russel1@osohrm.com']
        assert email == users_profile




