import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC





class Recruitment_Candidate(BasePage):

    PAGE_URL = Links.RECRUITMENT_CANDIDATES

    HINT_ITEM_IN_SEARCH = ("xpath", "//span[text()='Petro  Pidkovych']")
    HINT_ITEM_NO_RECORDS = ("xpath", "//div[text()='No Records Found']")
    CHOOSE_RECRUITMENT_FROM_MENU = ("xpath", "//span[text()='Recruitment']")
    ADD_BTN = ("xpath", "//*[text()=' Add ']")
    CANDIDATE_NAME_INPUT = ("xpath", "//input[@placeholder='Type for hints...']")
    KEYWORDS_INPUT = ("xpath", "//input[@placeholder='Enter comma seperated words...']")
    ERROR_INVALID = ("xpath", "//span[text()='Invalid']")
    TABLE_ROW = ("xpath", "//div[@role='row']//div[contains(text(), 'Petro  Pidkovych')]")
    NO_RECORDS = ("xpath", "//span[text()='No Records Found']")
    SEARCH_BTN = ("xpath", "//button[text()=' Search ']")
    ICON_BUTTON = ("xpath", "(//button[@type='button'][@class='oxd-icon-button'])[2]")
    CANDIDATE_BLOCK = ("xpath", "//form[@class='oxd-form']")
    VACANCY_COLUMN = (
    "xpath", "//div[@class='oxd-table']//div[@class='oxd-table-row oxd-table-row--with-border']/*[2]")
    HIRING_MANAGER_COLUMN = (
    "xpath", "//div[@class='oxd-table']//div[@class='oxd-table-row oxd-table-row--with-border']/*[4]")
    STATUS_COLUMN = ("xpath", "//div[@class='oxd-table']//div[@class='oxd-table-row oxd-table-row--with-border']/*[6]")
    ITEM_QA_LEAD_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Senior QA Lead']")
    ITEM_QA_LEAD2_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='QA Lead']")
    ITEM_QA_LEAD3_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Software Engineer']")
    ITEM_QA_LEAD4_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Sales Representative']")
    ITEM_QA_LEAD5_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='IT Manager']")
    HIRINING_DROPDOWN = ("xpath", "(//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow' ])[3]")
    STATUS_DROPDOWN = ("xpath", "(//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow' ])[4]")
    ITEM_REJECTED_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Rejected']")
    ITEM_QA_LEAD6_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Odis Adalwin']")
    # ????????????///////////////////////////////////////tableeeeeeeeeeeeeeeeeeeeeeeeee
    All_USERS = ("xpath", "//div[@class='oxd-table-body']//div[@role='row']")
    SORT_ICON_VACANCY = ("xpath", "(//div[@class='oxd-table-header-sort'])[1]")
    SORT_CHOOSE_ITEM_VACANCY_AS = ("xpath", "(//span[text()='Ascending'])[1]")
    SORT_CHOOSE_ITEM_VACANCY_DES = ("xpath", "(//span[text()='Descending'])[1]")
    VACANCY_COLUMN = (
    "xpath", "//div[@class='oxd-table']//div[@class='oxd-table-row oxd-table-row--with-border']/*[2]")
    # /////////////////////////////////////////////////////////////////////////
    SORT_ICON_CANDIDATE = ("xpath", "(//div[@class='oxd-table-header-sort'])[2]")
    SORT_CHOOSE_ITEM_CANDIDATE_AS = ("xpath", "(//span[text()='Ascending'])[2]")
    SORT_CHOOSE_ITEM_CANDIDATE_DES = ("xpath", "(//span[text()='Descending'])[2]")
    CANDIDATE_COLUMN = (
    "xpath", "//div[@class='oxd-table']//div[@class='oxd-table-row oxd-table-row--with-border']/*[3]")
    # ?/////////////////////////////////////
    SORT_ICON_HIRING = ("xpath", "(//div[@class='oxd-table-header-sort'])[3]")
    SORT_CHOOSE_ITEM_HIRING_AS = ("xpath", "(//span[text()='Ascending'])[3]")
    SORT_CHOOSE_ITEM_HIRING_DES = ("xpath", "(//span[text()='Descending'])[3]")
    HIRING_COLUMN = ("xpath", "//div[@class='oxd-table']//div[@class='oxd-table-row oxd-table-row--with-border']/*[4]")
    # ?/////////////////////////////////////
    SORT_ICON_DATE = ("xpath", "(//div[@class='oxd-table-header-sort'])[4]")
    SORT_CHOOSE_ITEM_DATE_AS = ("xpath", "(//span[text()='Ascending'])[4]")
    SORT_CHOOSE_ITEM_DATE_DES = ("xpath", "(//span[text()='Descending'])[4]")
    DATE_COLUMN = ("xpath", "//div[@class='oxd-table']//div[@class='oxd-table-row oxd-table-row--with-border']/*[5]")
    # ?/////////////////////////////////////
    SORT_ICON_STATUS = ("xpath", "(//div[@class='oxd-table-header-sort'])[5]")
    SORT_CHOOSE_ITEM_STATUS_AS = ("xpath", "(//span[text()='Ascending'])[5]")
    SORT_CHOOSE_ITEM_STATUS_DES = ("xpath", "(//span[text()='Descending'])[5]")
    STATUS_COLUMN = ("xpath", "//div[@class='oxd-table']//div[@class='oxd-table-row oxd-table-row--with-border']/*[6]")
    # admmmmmmmmmmmmmmminnnnnnnnnn candidateeeeeeeeeeeeeeee bloooooooooooooooooookkkkkkkkkkkkk////
    FIRST_NAME_INPUT = ("xpath", "//input[@placeholder='First Name']")
    LAST_NAME_INPUT = ("xpath", "//input[@placeholder='Last Name']")
    EMAIL_INPUT = ("xpath", "(//input[@placeholder='Type here'])[1]")
    SAVE_BTN = ("xpath", "//*[text()=' Save ']")
    SUCCESSFULLY_SAVED_PUSH_NOTIFICATION = ("xpath", "//p[text()='Successfully Saved']")
    DROPDOWN = ("xpath", "(//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow' ])[1]")
    ERROR_REQUIRED = ("xpath", "//span[text()='Required']")
    # ////////////////////////////////caleendarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
    ICON_FROM_CALENDAR = ("xpath", "//input[@placeholder='From']")
    ICON_TO_CALENDAR = ("xpath", "//input[@placeholder='To']")
    PREVIOUS_BTN_IN_CALENDAR = ("xpath", "//button[@class='oxd-icon-button']//i[@class='oxd-icon bi-chevron-left']")
    NEXT_BTN_IN_CALENDAR = ("xpath", "//div[@class='oxd-calendar-header']//i[@class='oxd-icon bi-chevron-right']")
    CURRENT_MONTH = ("xpath", "//div[@class='oxd-calendar-selector-month-selected']//p")
    CURRENT_YEAR = ("xpath", "(//div//p[@class='oxd-text oxd-text--p'])[2]")
    CHOOSE_DATE = ("xpath", "//div[@class='oxd-calendar-date-wrapper']")
    CANDIDATE_WITH_CALENDAR = ("xpath", "//div[@role='row']//div[contains(text(), 'Charles  Haywire')]")
    CANDIDATE_WITH_JULY = ("xpath", "//div[text()= 'Jennifer  Clinton']")
    PUSH_NOTIFICATION = ("xpath", "//p[text()='No Records Found']")


    def click_on_recruitment_item(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_RECRUITMENT_FROM_MENU)).click()

    def click_on_add_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BTN)).click()

    def type_name_in_the_field(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT)).send_keys("Petro")

    def type__last_name_in_the_field(self):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_INPUT)).send_keys("Pidkovych")

    def click_on_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN)).click()

    def choose_QA_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.ITEM_QA_LEAD_FROM_DROPDOWN)).click()

    def type_email(self):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(
            "test@gmail.com")


    def type_candidate_petr_name(self):
        self.wait.until(EC.element_to_be_clickable(self.CANDIDATE_NAME_INPUT)).send_keys(
            "Petr")

    def type_invalid_name(self):
        self.wait.until(EC.element_to_be_clickable(self.CANDIDATE_NAME_INPUT)).send_keys(
            'dfhjdf')

    def type_invalid_date_keywords_field(self):
        self.wait.until(EC.element_to_be_clickable(self.KEYWORDS_INPUT)).send_keys(
            'dfhjdf')

    def click_on_hint_item(self):
        self.wait.until(EC.element_to_be_clickable(self.HINT_ITEM_IN_SEARCH)).click()

    def click_on_hint_no_records(self):
        self.wait.until(EC.element_to_be_clickable(self.HINT_ITEM_NO_RECORDS)).click()

    def click_on_save_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    def click_on_icon_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ICON_BUTTON)).click()

    def click_on_sort_icon_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_ICON_VACANCY)).click()

    def click_on_search_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
        time.sleep(2)

    def click_on_status_dropdown_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.STATUS_DROPDOWN)).click()

    def click_on_sort_icon_candidate(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_ICON_CANDIDATE)).click()

    def click_on_sort_icon_hiring(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_ICON_HIRING)).click()

    def click_on_icon_from_calendar(self):
        self.wait.until(EC.element_to_be_clickable(self.ICON_FROM_CALENDAR)).click()

    def choose_rejected_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.ITEM_REJECTED_FROM_DROPDOWN)).click()


    def choose_qa_lead_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.ITEM_QA_LEAD2_FROM_DROPDOWN)).click()

    def choose_sales_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.ITEM_QA_LEAD4_FROM_DROPDOWN)).click()


    def choose_it_manager_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.ITEM_QA_LEAD5_FROM_DROPDOWN)).click()

    def choose_software_engineer_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.ITEM_QA_LEAD3_FROM_DROPDOWN)).click()





    def is_added_a_new_candidate(self):
        x = self.wait.until(EC.element_to_be_clickable(self.SUCCESSFULLY_SAVED_PUSH_NOTIFICATION)).text
        assert x == 'Successfully Saved'

    def is_shown_required_error(self):
        x = self.wait.until(EC.element_to_be_clickable(self.ERROR_REQUIRED)).text
        assert x == 'Required'

    def is_found_candidate(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeights);")
        time.sleep(1)
        assert self.wait.until(EC.visibility_of_element_located(self.TABLE_ROW)).is_displayed()


    def is_fond_invalid_name(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ERROR_INVALID)).text
        assert element == 'Invalid'

    def is_fond_no_records_keyword_field(self):
        text = self.wait.until(EC.element_to_be_clickable(self.NO_RECORDS)).text
        assert text == 'No Records Found'

    def is_hidden_block(self):
        assert self.wait.until(EC.invisibility_of_element_located(self.CANDIDATE_BLOCK))


    def are_fonded_qa_lead_when_chosen_from_dropdown(self):
        vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.VACANCY_COLUMN))
        size_list = []
        for size in vacancy_column:
            size_list.append(size.text)
        print(size_list)

        vacancy = ['Vacancy', 'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead',
                   'Senior QA Lead', 'Senior QA Lead',
                   'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead',
                   'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead',
                   'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead',
                   'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead',
                   'Senior QA Lead', 'Senior QA Lead', 'Senior QA Lead']
        print(vacancy)
        assert vacancy == size_list


    def are_fonded_sales_when_chosen_from_dropdown(self):
        vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.VACANCY_COLUMN))
        size_list = []
        for size in vacancy_column:
            size_list.append(size.text)
        print(size_list)

        vacancy = ['Vacancy', 'Sales Representative', 'Sales Representative', 'Sales Representative',
                   'Sales Representative']
        print(vacancy)
        assert vacancy == size_list

    def are_fonded_manager_when_chosen_from_dropdown(self):
        vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.VACANCY_COLUMN))
        size_list = []
        for size in vacancy_column:
            size_list.append(size.text)
        print(size_list)

        vacancy = ['Vacancy', 'Associate IT Manager', 'Associate IT Manager', 'Associate IT Manager',
                   'Associate IT Manager',
                   'Associate IT Manager', 'Associate IT Manager', 'Associate IT Manager', 'Associate IT Manager',
                   'Associate IT Manager',
                   'Associate IT Manager', 'Associate IT Manager', 'Associate IT Manager', 'Associate IT Manager',
                   'Associate IT Manager',
                   'Associate IT Manager', 'Associate IT Manager', 'Associate IT Manager', 'Associate IT Manager',
                   'Associate IT Manager']
        print(vacancy)
        assert vacancy == size_list


    def are_fonded_software_enginner_when_chosen_from_dropdown(self):
        vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.VACANCY_COLUMN))
        size_list = []
        for size in vacancy_column:
            size_list.append(size.text)
        print(size_list)

        vacancy = ['Vacancy', 'Software Engineer', 'Software Engineer']
        print(vacancy)
        assert vacancy == size_list

    def are_displayed_rejected_when_chosen_from_dropdown(self):
        vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.STATUS_COLUMN))
        size_list = []
        for size in vacancy_column:
            size_list.append(size.text)
        print(size_list)

        vacancy = ['Status', 'Rejected', 'Rejected', 'Rejected', 'Rejected', 'Rejected']
        print(vacancy)
        assert vacancy == size_list

    def are_sorted_ascending_vacancy_in_table(self):
        action = ActionChains(self.driver)
        element = self.wait.until(EC.element_to_be_clickable(self.SORT_CHOOSE_ITEM_VACANCY_AS))
        action.move_to_element(element).click().perform()
        vacancy = []

        try:

            for i in range(1, 6):
                vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.All_USERS))
                for user in vacancy_column:
                    vacancy.append(user.find_element("xpath",".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)

                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()
        except NoSuchElementException:
            pass

        y = 'Associate IT Manager', 'Senior QA Lead', 'Software Engineer' in vacancy
        print(y)

        print(f"Users: {vacancy}")

    def are_sorted_descending_vacancy_in_table(self):
        action = ActionChains(self.driver)
        element = self.wait.until(EC.element_to_be_clickable(self.SORT_CHOOSE_ITEM_VACANCY_DES))
        action.move_to_element(element).click().perform()
        vacancy = []

        try:

            for i in range(1, 6):
                vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.All_USERS))
                for user in vacancy_column:
                    vacancy.append(user.find_element("xpath",
                                                     ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)

                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()
        except NoSuchElementException:
            pass

        y = 'Software Engineer', 'Senior QA Lead', 'Associate IT Manager' in vacancy
        print(y)

        print(f"Users: {vacancy}")



    def are_sorted_ascending_candidate_in_table(self):
        action = ActionChains(self.driver)
        element = self.wait.until(EC.element_to_be_clickable(self.SORT_CHOOSE_ITEM_CANDIDATE_AS))
        action.move_to_element(element).click().perform()
        candidate = []

        try:

            for i in range(1, 6):
                vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.All_USERS))
                for user in vacancy_column:
                    candidate.append(user.find_element("xpath",
                                                     ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]").text)

                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()
        except NoSuchElementException:
            pass

        y = 'Jennifer Clinton', 'Chris Harris', 'Peter Smith' in candidate
        print(y)

        print(f"Users: {candidate}")



    def are_sorted_descending_candidate_in_table(self):
        action = ActionChains(self.driver)
        element = self.wait.until(EC.element_to_be_clickable(self.SORT_CHOOSE_ITEM_CANDIDATE_DES))
        action.move_to_element(element).click().perform()
        candidate = []

        try:

            for i in range(1, 6):
                vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.All_USERS))
                for user in vacancy_column:
                    candidate.append(user.find_element("xpath",
                                                     ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]").text)

                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()
        except NoSuchElementException:
            pass

        y = 'Martine Tennat', 'Peter Smith', 'Jennifer Clinton' in candidate
        print(y)

        print(f"Users: {candidate}")

    def are_sorted_ascending_hiring_in_table(self):
        action = ActionChains(self.driver)
        element = self.wait.until(EC.element_to_be_clickable(self.SORT_CHOOSE_ITEM_HIRING_AS))
        action.move_to_element(element).click().perform()
        hiring = []

        try:

            for i in range(1, 6):
                vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.All_USERS))
                for user in vacancy_column:
                    hiring.append(user.find_element("xpath",
                                                       ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][4]").text)

                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()
        except NoSuchElementException:
            pass

        y = 'Odis Adalwin', 'Linda Jane Anderson', 'Dominic Chase' in hiring
        print(y)
        print(f"Users: {hiring}")


    def are_sorted_descending_hiring_in_table(self):
        action = ActionChains(self.driver)
        element = self.wait.until(EC.element_to_be_clickable(self.SORT_CHOOSE_ITEM_HIRING_DES))
        action.move_to_element(element).click().perform()
        hiring = []

        try:

            for i in range(1, 6):
                vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.All_USERS))
                for user in vacancy_column:
                    hiring.append(user.find_element("xpath",
                                                       ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][4]").text)

                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()
        except NoSuchElementException:
            pass
        print(f"Users: {hiring}")



    def are_fonded_valid_date_via_calendar(self, year="2022", month="July", day="15"):
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text


            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(self.ICON_TO_CALENDAR)).click()

        year = "2022"
        month = "July"
        day = "28"

        time.sleep(5)
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text

            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
        time.sleep(2)
        vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.VACANCY_COLUMN))
        size_list = []
        for size in vacancy_column:
            size_list.append(size.text)

        y = ['Vacancy', 'Sales Representative']
        print(y)
        assert y == size_list



    def are_fonded_july_2022_via_calendar(self, year="2022", month="July", day="12"):
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text


            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(self.ICON_TO_CALENDAR)).click()

        year = "2022"
        month = "July"
        day = "14"

        time.sleep(5)
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text

            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
        time.sleep(2)
        vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.VACANCY_COLUMN))
        size_list = []
        for size in vacancy_column:
            size_list.append(size.text)

        y = ['Vacancy', 'Software Engineer']
        print(y)
        assert y == size_list


    def are_fonded_july_11_via_calendar(self, year = "2022", month = "July", day = "8"):
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text


            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(self.ICON_TO_CALENDAR)).click()

        year = "2022"
        month = "July"
        day = "11"

        time.sleep(5)
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text

            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
        time.sleep(2)
        vacancy_column = self.wait.until(EC.presence_of_all_elements_located(self.VACANCY_COLUMN))
        size_list = []
        for size in vacancy_column:
            size_list.append(size.text)

        vacancy = ['Vacancy', 'Senior Support Specialist', 'Senior QA Lead', 'Sales Representative']
        print(vacancy)
        assert vacancy == size_list



    def are_fonded_invalid_data_via_calendar(self, year = "2018", month = "July", day = "9"):
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text


            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(self.ICON_TO_CALENDAR)).click()

        year = "2019"
        month = "July"
        day = "11"

        time.sleep(5)
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text

            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
        time.sleep(2)
        blur = self.wait.until(EC.presence_of_element_located(self.PUSH_NOTIFICATION)).text
        assert blur == 'No Records Found'




    def are_searched_for_invalid_data_via_calendar(self, year="2018", month="July", day ="9"):
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text


            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        time.sleep(3)

        self.wait.until(EC.element_to_be_clickable(self.ICON_TO_CALENDAR)).click()

        year = "2019"
        month = "July"
        day = "12"

        time.sleep(5)
        while True:
            yr = self.driver.find_element(*self.CURRENT_YEAR).text
            mon = self.driver.find_element(*self.CURRENT_MONTH).text

            if yr == year and mon == month:
                break;
            else:
                self.driver.find_element(*self.PREVIOUS_BTN_IN_CALENDAR).click()
        time.sleep(3)

        dates = self.driver.find_elements(*self.CHOOSE_DATE)
        time.sleep(3)
        for ele in dates:
            if ele.text == day:
                ele.click()
                break
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
        time.sleep(2)
        blur = self.wait.until(EC.presence_of_element_located(self.PUSH_NOTIFICATION)).text
        assert blur == 'No Records Found'



