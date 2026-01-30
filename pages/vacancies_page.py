import time

import allure
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

    @allure.step("Click menu item: Recruitment")
    def click_on_recruitment_item(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_RECRUITMENT_FROM_MENU)).click()

    @allure.step("Open page: Vacancies")
    def click_on_vacancies_item(self):
        self.wait.until(EC.element_to_be_clickable(self.VACANCIES_LINK)).click()

    @allure.step("Click button: Add vacancy")
    def click_on_add_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BTN)).click()

    @allure.step("Type vacancy name: 'Petro'")
    def type_petro_in_the_field(self):
        self.wait.until(EC.element_to_be_clickable(self.Vacancy_Name_Input)).send_keys('Petro')

    @allure.step("Open dropdown: Job Title")
    def click_on_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_JOB_TITTLE)).click()

    @allure.step("Select dropdown item: QA Lead")
    def choose_QA_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_JOB_TITTLE)).click()

    @allure.step("Select dropdown item: Software Engineer")
    def choose_engineer_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_SOFT_TITTLE)).click()

    @allure.step("Select dropdown item: Sales Representative")
    def choose_sales_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_SALES_TITTLE)).click()

    @allure.step("Type hiring manager hint: 'Odis'")
    def type_odis(self):
        self.wait.until(EC.element_to_be_clickable(self.HIRING_INPUT)).send_keys('Rahul Patil')

    @allure.step("Click hiring manager hint from list")
    def click_on_hint(self):
        self.wait.until(EC.element_to_be_clickable(self.HINT_TO_HIRING)).click()

    @allure.step("Click button: Save vacancy")
    def click_on_save_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()
        time.sleep(2)

    @allure.step("Click button: Search")
    def click_on_search_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()

    @allure.step("Assert: new vacancy 'Petro' is displayed in table")
    def is_added_new_vacancy(self):
        self.wait.until(EC.element_to_be_clickable(self.VACANCIES_LINK)).click()
        x = self.wait.until(EC.visibility_of_element_located(self.ITEM_VACANCY_FROM_TABLE)).text
        assert x == 'Petro'

    @allure.step("Assert: error 'Already exists' is displayed")
    def is_already_existed_position(self):
        text_already = self.wait.until(EC.visibility_of_element_located(self.ERROR_ALREADY_EXISTS)).text
        assert text_already == 'Already exists'

    @allure.step("Assert: validation error 'Required' is displayed")
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
                    vacancy.append(user.find_element("xpath",
                                                     ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)
                    job_title.append(user.find_element("xpath",
                                                       ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]").text)

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
                    vacancy.append(user.find_element("xpath",
                                                     ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)
                    job_title.append(user.find_element("xpath",
                                                       ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]").text)

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

    @allure.step("Assert: table Job Titles equal expected: {expected_job_titles}")
    def is_displayed_job_titles_in_table(self, expected_job_titles: list, max_pages: int = 5):
        """
        УНІВЕРСАЛЬНА перевірка для таблиці вакансій.
        Працює так само як твої дві функції (engineer/sales), але:
        - приймає очікуваний список job_title
        - читає всі сторінки пагінації (max_pages)
        - збирає job_title з 3-ї колонки
        - робить assert len та assert списків

        expected_job_titles:
            Наприклад ["Software Engineer", "Software Engineer"]
            або ["Sales Representative"]

        max_pages:
            Скільки сторінок пагінації спробувати пройти (у тебе було range(1,6))
        """

        time.sleep(2)  # залишаю як у тебе (але в майбутньому краще замінити на explicit wait)
        vacancy = []
        job_title = []

        try:
            # Проходимо сторінки пагінації (як у тебе було 1..5)
            for i in range(1, max_pages + 1):
                # Беремо всі рядки таблиці
                vacancy_rows = self.wait.until(EC.visibility_of_all_elements_located(self.All_USERS))

                # Зчитуємо колонку Vacancy(2) і Job Title(3) з кожного рядка
                for row in vacancy_rows:
                    vacancy.append(
                        row.find_element(
                            "xpath",
                            ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]"
                        ).text
                    )
                    job_title.append(
                        row.find_element(
                            "xpath",
                            ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]"
                        ).text
                    )

                # Клік на сторінку пагінації.
                # ⚠️ У тебе був li[i]; залишаю той самий підхід
                xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
                time.sleep(2)
                self.driver.find_element("xpath", xpath_text).click()

        except NoSuchElementException:
            # Якщо пагінації менше, ніж max_pages — просто виходимо (як ти робив)
            pass

        # --- ДЕБАГ-ВИВІД (корисно коли тест падає) ---
        print(f"Expected job titles: {expected_job_titles}")
        print(f"Users (vacancy col): {vacancy}")
        print(f"Actual job titles: {job_title}")

        # --- АСЕРТИ: залишаю твою логіку ---
        # 1) Перевіряємо кількість елементів
        assert len(job_title) == len(expected_job_titles), (
            f"Expected {len(expected_job_titles)} rows, but got {len(job_title)}.\n"
            f"Actual titles: {job_title}"
        )

        # 2) Перевіряємо точний список (порядок також важливий)
        assert expected_job_titles == job_title, (
            f"Job titles mismatch.\n"
            f"Expected: {expected_job_titles}\n"
            f"Actual:   {job_title}"
        )


    # def click_on_recruitment_item(self):
    #     self.wait.until(EC.element_to_be_clickable(self.CHOOSE_RECRUITMENT_FROM_MENU)).click()
    #
    # def click_on_vacancies_item(self):
    #     self.wait.until(EC.element_to_be_clickable(self.VACANCIES_LINK)).click()
    #
    # def click_on_add_btn(self):
    #     self.wait.until(EC.element_to_be_clickable(self.ADD_BTN)).click()
    #
    # def type_petro_in_the_field(self):
    #     self.wait.until(EC.element_to_be_clickable(self.Vacancy_Name_Input)).send_keys('Petro')
    #
    # def click_on_dropdown(self):
    #     self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_JOB_TITTLE)).click()
    #
    # def choose_QA_from_dropdown(self):
    #     self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_JOB_TITTLE)).click()
    #
    # def choose_engineer_from_dropdown(self):
    #     self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_SOFT_TITTLE)).click()
    #
    # def choose_sales_from_dropdown(self):
    #     self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_SELECT_ITEM_FROM_SALES_TITTLE)).click()
    #
    # def type_odis(self):
    #     self.wait.until(EC.element_to_be_clickable(self.HIRING_INPUT)).send_keys('Odis')
    #
    # def click_on_hint(self):
    #     self.wait.until(EC.element_to_be_clickable(self.HINT_TO_HIRING)).click()
    #
    # def click_on_save_btn(self):
    #     self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()
    #     time.sleep(2)
    #
    # def click_on_search_btn(self):
    #     self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
    #
    #
    # def is_added_new_vacancy(self):
    #     self.wait.until(EC.element_to_be_clickable(self.VACANCIES_LINK)).click()
    #     x = self.wait.until(EC.visibility_of_element_located(self.ITEM_VACANCY_FROM_TABLE)).text
    #     assert x == 'Petro'
    #
    # def is_already_existed_position(self):
    #     text_already = self.wait.until(EC.visibility_of_element_located(self.ERROR_ALREADY_EXISTS)).text
    #     assert text_already == 'Already exists'
    #
    # def is_shown_error_when_empty_field(self):
    #     text_error = self.wait.until(EC.visibility_of_element_located(self.ERROR_REQUIRED)).text
    #     assert text_error == 'Required'
    #
    # def is_displayed_engineer_in_table(self):
    #     time.sleep(2)
    #     vacancy = []
    #     job_title = []
    #
    #     try:
    #
    #
    #         for i in range(1, 6):
    #             vacancy_column = self.wait.until(EC.visibility_of_all_elements_located(self.All_USERS))
    #             for user in vacancy_column:
    #                 vacancy.append(user.find_element("xpath", ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)
    #                 job_title.append(user.find_element("xpath",".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]").text)
    #
    #             xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
    #             time.sleep(2)
    #             self.driver.find_element("xpath", xpath_text).click()
    #     except NoSuchElementException:
    #         pass
    #
    #     list = ["Software Engineer", "Software Engineer"]
    #     print(list)
    #
    #     print(f"Users: {vacancy}")
    #     print(f"Job Title: {job_title}")
    #
    #     assert len(job_title) == 2
    #     assert list == job_title
    #
    #
    # def is_displayed_sales_in_table(self):
    #     time.sleep(2)
    #     vacancy = []
    #     job_title = []
    #
    #     try:
    #
    #
    #         for i in range(1, 6):
    #             vacancy_column = self.wait.until(EC.visibility_of_all_elements_located(self.All_USERS))
    #             for user in vacancy_column:
    #                 vacancy.append(user.find_element("xpath", ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)
    #                 job_title.append(user.find_element("xpath",".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][3]").text)
    #
    #             xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
    #             time.sleep(2)
    #             self.driver.find_element("xpath", xpath_text).click()
    #     except NoSuchElementException:
    #         pass
    #
    #     list = ["Sales Representative"]
    #     print(list)
    #
    #     print(f"Users: {vacancy}")
    #     print(f"Job Title: {job_title}")
    #
    #     assert len(job_title) == 1
    #     assert list == job_title