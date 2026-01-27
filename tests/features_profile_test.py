import time

import allure
import pytest

from base.base_test import BaseTest


class TestProfileFeatures(BaseTest):

    def test_with_valid_crendentional(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_on_submit_button()

# @allure.feature("Nationalities")
# class TestNationalities(BaseTest):

#     @allure.story("Scrape and compare all nationalities in table")
#     @pytest.mark.smoke
#     def test_scraping_all_countries_in_table(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Admin -> Nationalities"):
#             self.nationalities_page.click_on_admin_item()
#             self.nationalities_page.is_opened()
#             self.nationalities_page.choose_on_nationalities_item()
#         with allure.step("Validate nationalities list in table"):
#             self.nationalities_page.compare_all_countries_in_table()


    # @allure.story("Create a new nationality entry: Ukraine")
    # @pytest.mark.smoke
    # def test_add_country(self):
    #     with allure.step("Login to OrangeHRM"):
    #         self.login_page.open()
    #         self.login_page.enter_login()
    #         self.login_page.enter_password()
    #         self.login_page.click_on_submit_button()
    #     with allure.step("Navigate to Admin -> Nationalities"):
    #         self.nationalities_page.click_on_admin_item()
    #         self.nationalities_page.is_opened()
    #         self.nationalities_page.choose_on_nationalities_item()
    #     with allure.step("Add nationality 'Ukraine'"):
    #         self.nationalities_page.click_on_add_item()
    #         self.nationalities_page.type_ukraine()
    #         self.nationalities_page.click_on_save_btn()
    #     with allure.step("Verify nationality saved successfully"):
    #         self.nationalities_page.is_saved_country()


    # @allure.story("Create a new nationality entry")
    # @pytest.mark.smoke
    # def test_add_kyiv(self):
    #     allure.dynamic.title("Add nationality: Kyiv")

    #     with allure.step("Login to OrangeHRM"):
    #         self.login_page.open()
    #         self.login_page.enter_login()
    #         self.login_page.enter_password()
    #         self.login_page.click_on_submit_button()
    #     with allure.step("Navigate to Admin -> Nationalities"):
    #         self.nationalities_page.click_on_admin_item()
    #         self.nationalities_page.is_opened()
    #         self.nationalities_page.choose_on_nationalities_item()
    #     with allure.step("Add nationality 'Kyiv'"):
    #         self.nationalities_page.click_on_add_item()
    #         self.nationalities_page.type_kyiv()
    #         self.nationalities_page.click_on_save_btn()
    #     with allure.step("Verify nationality saved successfully"):
    #         self.nationalities_page.is_saved_country()


    # @allure.story("Delete nationality from table")
    # @pytest.mark.smoke
    # def test_delete_kyiv_from_table(self):
    #     allure.dynamic.title("Delete nationality: Kyiv")

    #     with allure.step("Login to OrangeHRM"):
    #         self.login_page.open()
    #         self.login_page.enter_login()
    #         self.login_page.enter_password()
    #         self.login_page.click_on_submit_button()
    #     with allure.step("Navigate to Admin -> Nationalities"):
    #         self.nationalities_page.click_on_admin_item()
    #         self.nationalities_page.is_opened()
    #         self.nationalities_page.choose_on_nationalities_item()
    #     with allure.step("Select nationality 'Kyiv' from table"):
    #         self.nationalities_page.delete_kyiv_from_table()
    #     with allure.step("Delete selected nationality and confirm"):
    #         self.nationalities_page.click_on_delete_btn()
    #         self.nationalities_page.click_on_yes_confirm()
    #     with allure.step("Verify nationality deleted successfully"):
    #         self.nationalities_page.is_deleted_country()


    # @allure.story("Add new nationality")
    # @pytest.mark.smoke
    # def test_add_porto(self):
    #     allure.dynamic.title("Add nationality: Portu")

    #     with allure.step("Login to OrangeHRM"):
    #         self.login_page.open()
    #         self.login_page.enter_login()
    #         self.login_page.enter_password()
    #         self.login_page.click_on_submit_button()
    #     with allure.step("Navigate to Admin -> Nationalities"):
    #         self.nationalities_page.click_on_admin_item()
    #         self.nationalities_page.is_opened()
    #         self.nationalities_page.choose_on_nationalities_item()
    #     with allure.step("Add nationality 'Portu'"):
    #         self.nationalities_page.click_on_add_item()
    #         self.nationalities_page.type_portu()
    #         self.nationalities_page.click_on_save_btn()
    #     with allure.step("Verify nationality saved successfully"):
    #         self.nationalities_page.is_added_porto()


    # @allure.story("Delete nationality from table")
    # @pytest.mark.smoke
    # def test_delete_porto(self):
    #     allure.dynamic.title("Delete nationality: Portu")

    #     with allure.step("Login to OrangeHRM"):
    #         self.login_page.open()
    #         self.login_page.enter_login()
    #         self.login_page.enter_password()
    #         self.login_page.click_on_submit_button()
    #     with allure.step("Navigate to Admin -> Nationalities"):
    #         self.nationalities_page.click_on_admin_item()
    #         self.nationalities_page.is_opened()
    #         self.nationalities_page.choose_on_nationalities_item()
    #     with allure.step("Delete nationality 'Portu' and validate success notification"):
    #         self.nationalities_page.is_deleted_porto()


    # @allure.story("Validation: nationality already exists")
    # @pytest.mark.smoke
    # def test_country_is_exist(self):
    #     allure.dynamic.title("Validate error when nationality already exists (Ukraine)")

    #     with allure.step("Login to OrangeHRM"):
    #         self.login_page.open()
    #         self.login_page.enter_login()
    #         self.login_page.enter_password()
    #         self.login_page.click_on_submit_button()
    #     with allure.step("Navigate to Admin -> Nationalities"):
    #         self.nationalities_page.click_on_admin_item()
    #         self.nationalities_page.is_opened()
    #         self.nationalities_page.choose_on_nationalities_item()
    #     with allure.step("Try to add nationality 'Ukraine' again"):
    #         self.nationalities_page.click_on_add_item()
    #         self.nationalities_page.type_ukraine()
    #     with allure.step("Verify 'Already exists' validation error is displayed"):
    #         self.nationalities_page.is_showed_error()


    # @allure.story("Validation: empty required fields")
    # @pytest.mark.smoke
    # def test_empty_field(self):
    #     allure.dynamic.title("Validate 'Required' error when Nationality field is empty")

    #     with allure.step("Login to OrangeHRM"):
    #         self.login_page.open()
    #         self.login_page.enter_login()
    #         self.login_page.enter_password()
    #         self.login_page.click_on_submit_button()
    #     with allure.step("Navigate to Admin -> Nationalities"):
    #         self.nationalities_page.click_on_admin_item()
    #         self.nationalities_page.is_opened()
    #         self.nationalities_page.choose_on_nationalities_item()
    #     with allure.step("Try to save empty nationality form"):
    #         self.nationalities_page.click_on_add_item()
    #         self.nationalities_page.click_on_save_btn()
    #     with allure.step("Verify 'Required' validation error is displayed"):
    #         self.nationalities_page.is_empty_error()


    # @allure.story("Edit nationality")
    # @pytest.mark.smoke
    # def test_edit_country(self):
    #     allure.dynamic.title("Edit nationality and verify update notification")

    #     with allure.step("Login to OrangeHRM"):
    #         self.login_page.open()
    #         self.login_page.enter_login()
    #         self.login_page.enter_password()
    #         self.login_page.click_on_submit_button()
    #     with allure.step("Navigate to Admin -> Nationalities"):
    #         self.nationalities_page.click_on_admin_item()
    #         self.nationalities_page.is_opened()
    #         self.nationalities_page.choose_on_nationalities_item()
    #     with allure.step("Edit selected nationality and save changes"):
    #         self.nationalities_page.click_on_edit_btn()
    #         self.nationalities_page.type_data()
    #         self.nationalities_page.click_on_save_btn()
    #     with allure.step("Verify nationality updated successfully"):
    #         self.nationalities_page.is_changed_name()



# @allure.feature("Directory")
# class TestDirectory(BaseTest):




#     @allure.story("Filters: Job Title")
#     @pytest.mark.smoke
#     @pytest.mark.parametrize(
#         "choose_method, assert_method, job_title_name",
#         [
#             ("choose_item_from_dropdown", "is_present_software_in_table", "Software Engineer"),
#             ("choose_hr_from_dropdown", "is_present_hr_in_table", "HR Manager"),
#             ("choose_qa_from_dropdown", "is_present_qa_in_table", "QA Engineer"),
#             ("choose_chief_from_dropdown", "is_present_chief_technical_in_table", "Chief Financial Officer"),
#         ],
#         ids=["Software Engineer", "HR Manager", "QA Engineer", "Chief Financial Officer"]
#     )
#     def test_is_display_employee_after_filters_parametrized(self, choose_method, assert_method, job_title_name):
#         allure.dynamic.title(f"Directory filter by Job Title: {job_title_name}")

#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()

#         with allure.step("Navigate to Directory"):
#             self.directory_page.click_on_directory_item()
#             self.directory_page.is_opened()

#         with allure.step(f"Apply filter Job Title = {job_title_name}"):
#             self.directory_page.click_on_dropdown()
#             getattr(self.directory_page, choose_method)()   # ВИБІР елемента
#             self.directory_page.click_on_search_btn()

#         with allure.step("Validate filtered directory results"):
#             getattr(self.directory_page, assert_method)()        #ПЕРЕВІРКА результатів

#     # def test_is_display_employee_after_filters(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.directory_page.click_on_directory_item()
#     #     self.directory_page.is_opened()
#     #     self.directory_page.click_on_dropdown()
#     #     self.directory_page.choose_item_from_dropdown()
#     #     self.directory_page.click_on_search_btn()
#     #     self.directory_page.is_present_software_in_table()
#     #
#     # def test_is_display_hr_after_filters(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.directory_page.click_on_directory_item()
#     #     self.directory_page.is_opened()
#     #     self.directory_page.click_on_dropdown()
#     #     self.directory_page.choose_hr_from_dropdown()
#     #     self.directory_page.click_on_search_btn()
#     #     self.directory_page.is_present_hr_in_table()
#     #
#     # def test_is_display_qa_after_filters(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.directory_page.click_on_directory_item()
#     #     self.directory_page.is_opened()
#     #     self.directory_page.click_on_dropdown()
#     #     self.directory_page.choose_qa_from_dropdown()
#     #     self.directory_page.click_on_search_btn()
#     #     self.directory_page.is_present_qa_in_table()
#     @allure.story("Validate empty results after applying filter")
#     @pytest.mark.smoke
#     def test_no_records(self):
#         allure.dynamic.title("Directory: No records found for Support Specialist filter")
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Directory"):
#             self.directory_page.click_on_directory_item()
#             self.directory_page.is_opened()
#         with allure.step("Apply Job Title filter = Support Specialist"):
#             self.directory_page.click_on_dropdown()
#             self.directory_page.choose_support_specialist_from_dropdown()
#             self.directory_page.click_on_search_btn()
#         with allure.step("Verify that no records are displayed"):
#             self.directory_page.is_no_records()

#     # def test_is_display_chief_after_filters(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.directory_page.click_on_directory_item()
#     #     self.directory_page.is_opened()
#     #     self.directory_page.click_on_dropdown()
#     #     self.directory_page.choose_chief_from_dropdown()
#     #     self.directory_page.click_on_search_btn()
#     #     self.directory_page.is_present_chief_technical_in_table()


#     # def test_all_locations_are_presented_in_dropdown(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.directory_page.click_on_directory_item()
#     #     self.directory_page.is_opened()
#     #     self.directory_page.click_on_location_dropdown()
#     #     self.directory_page.choose_all_location_from_dropdown()
#     #     self.directory_page.click_on_search_btn()
#     #     self.directory_page.is_displayed_locations__in_dropdown()


#     # def test_each_user_have_email(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.directory_page.click_on_directory_item()
#     #     self.directory_page.is_opened()
#     #     self.directory_page.click_on_dropdown()
#     #     self.directory_page.choose_job_title_from_dropdown()
#     #     self.directory_page.click_on_search_btn()
#     #     self.directory_page.is_each_user_have_email()


# @allure.feature("PIM Reports")
# class TestPimReports(BaseTest):

#     @allure.story("Create new report")
#     @pytest.mark.smoke
#     def test_add_report(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to PIM -> Reports"):
#             self.pim_reports_page.click_on_pim_item()
#             self.pim_reports_page.click_on_report_link()
#         with allure.step("Create a new report with Contact Details field"):
#             self.pim_reports_page.click_on_add_btn()
#             self.pim_reports_page.type_pedro()
#             self.pim_reports_page.click_on_dropdown()
#             self.pim_reports_page.choose_contact_from_dropdown()
#             self.pim_reports_page.click_on_plus_icon()
#             self.pim_reports_page.click_save_btn()
#         with allure.step("Validate report was created"):
#             self.pim_reports_page.is_appeared_new_report()


#     @allure.story("Search existing report 'pedro' by name")
#     @pytest.mark.smoke
#     def test_find_a_new_report(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to PIM -> Reports"):
#             self.pim_reports_page.click_on_pim_item()
#             self.pim_reports_page.click_on_report_link()
#         with allure.step("Search report by autocomplete hint"):
#             self.pim_reports_page.type_ped()
#             self.pim_reports_page.click_on_hint_in_the_field()
#             self.pim_reports_page.click_on_search_btn()
#         with allure.step("Validate that report 'pedro' is found"):
#             self.pim_reports_page.is_appeared_new_report()


#     @allure.story("Search report with invalid name")
#     @pytest.mark.smoke
#     def test_find_invalid_report(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to PIM -> Reports"):
#             self.pim_reports_page.click_on_pim_item()
#             self.pim_reports_page.click_on_report_link()
#         with allure.step("Search report with invalid value"):
#             self.pim_reports_page.type_invalid_date()
#             self.pim_reports_page.click_on_search_btn()
#         with allure.step("Validate validation error 'Invalid' is displayed"):
#             self.pim_reports_page.is_searched_invalid_report()


#     @allure.story("Delete existing report 'pedro'")
#     @pytest.mark.smoke
#     def test_delete_report(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to PIM -> Reports"):
#             self.pim_reports_page.click_on_pim_item()
#             self.pim_reports_page.click_on_report_link()
#         with allure.step("Find report 'pedro' to delete"):
#             self.pim_reports_page.type_ped()
#             self.pim_reports_page.click_on_hint_in_the_field()
#             self.pim_reports_page.click_on_search_btn()
#         with allure.step("Delete found report and confirm deletion"):
#             self.pim_reports_page.click_on_delete_icon()
#             self.pim_reports_page.click_on_yes_confirm()
#         with allure.step("Validate report was deleted successfully"):
#             self.pim_reports_page.is_successfully_deleted_report()
#     #
#     # def test_sort_ascending_name(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.pim_reports_page.click_on_pim_item()
#     #     self.pim_reports_page.click_on_report_link()
#     #     self.pim_reports_page.click_on_sort_icon()
#     #     self.pim_reports_page.is_sorted_ascending_name()
#     #
#     # def test_sort_descending_name(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.pim_reports_page.click_on_pim_item()
#     #     self.pim_reports_page.click_on_report_link()
#     #     self.pim_reports_page.click_on_sort_icon()
#     #     self.pim_reports_page.is_sorted_descending_name()


#     @allure.story("User can hide filter panel on Reports page")
#     @pytest.mark.smoke
#     def test_hide_block(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to PIM -> Reports"):
#             self.pim_reports_page.click_on_pim_item()
#             self.pim_reports_page.click_on_report_link()
#         with allure.step("Hide filter block by clicking icon"):
#             self.pim_reports_page.click_on_icon_btn()
#         with allure.step("Validate filter block is hidden"):
#             self.pim_reports_page.is_hidden_block()


#         @allure.story("Sort reports by name in ascending and descending order")
#         @pytest.mark.smoke
#         @pytest.mark.parametrize(
#             "assert_method",
#             [
#                 "is_sorted_ascending_name",                 # тут ми викликаємо метод а тести асерити вже виконуються в пейдж обджект де описані
#                 "is_sorted_descending_name"
#             ]
#         )
#         def test_sort_reports_by_name(self, assert_method):
#             # --- КРОК 1. ЛОГІН ---
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()

#             # --- КРОК 2. НАВІГАЦІЯ ДО СТОРІНКИ ---
#             self.pim_reports_page.click_on_pim_item()
#             self.pim_reports_page.click_on_report_link()

#             # --- КРОК 3. ВИКЛИК МЕТОДУ З PAGEOBJECT ЧЕРЕЗ ІМ'Я ---
#             # Тут assert_method — це рядок:
#             # "is_sorted_ascending_name" або "is_sorted_descending_name"

#             # getattr бере з об'єкта self.pim_reports_page метод з таким ім'ям
#             # і викликає його як звичайну функцію
#             getattr(self.pim_reports_page, assert_method)()

# @allure.feature("Vacancies")
# class TestVacancies(BaseTest):


#     @allure.story("Add new vacancy")
#     @pytest.mark.smoke
#     def test_add_vacancy_QA(self):
#         allure.dynamic.title("Add new vacancy with Job Title: QA Lead")
#         # --- GIVEN ---
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         # --- WHEN ---
#         with allure.step("Navigate to Recruitment -> Vacancies"):
#             self.vacancies_page.click_on_recruitment_item()
#             self.vacancies_page.click_on_vacancies_item()
#         with allure.step("Open Add Vacancy form"):
#             self.vacancies_page.click_on_add_btn()
#         with allure.step("Fill vacancy form with name and Job Title = QA Lead"):
#             self.vacancies_page.type_petro_in_the_field()
#             self.vacancies_page.click_on_dropdown()
#             self.vacancies_page.choose_QA_from_dropdown()
#             self.vacancies_page.type_odis()
#             self.vacancies_page.click_on_hint()
#         with allure.step("Save new vacancy"):
#             self.vacancies_page.click_on_save_btn()
#         # --- THEN ---
#         with allure.step("Verify new vacancy is displayed in vacancies table"):
#             self.vacancies_page.click_on_vacancies_item()
#             self.vacancies_page.is_added_new_vacancy()

#     @allure.story("Validation: vacancy already exists")
#     @pytest.mark.smoke
#     def test_vacancy_existed(self):
#         # --- GIVEN ---
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         # --- WHEN ---
#         with allure.step("Navigate to Recruitment -> Vacancies"):
#             self.vacancies_page.click_on_recruitment_item()
#             self.vacancies_page.click_on_vacancies_item()
#         with allure.step("Open Add Vacancy form"):
#             self.vacancies_page.click_on_add_btn()
#         with allure.step("Enter existing vacancy name"):
#             self.vacancies_page.type_petro_in_the_field()
#         with allure.step("Verify 'Already exists' validation error is displayed"):
#             self.vacancies_page.is_already_existed_position()


#     @allure.story("Validation: empty required fields")
#     @pytest.mark.smoke
#     def test_show_error_when_empty_field(self):
#         # --- GIVEN ---
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         # --- WHEN ---
#         with allure.step("Navigate to Recruitment -> Vacancies"):
#             self.vacancies_page.click_on_recruitment_item()
#             self.vacancies_page.click_on_vacancies_item()
#         with allure.step("Open Add Vacancy form"):
#             self.vacancies_page.click_on_add_btn()
#         with allure.step("Try to save empty vacancy form"):
#             self.vacancies_page.click_on_save_btn()
#         # --- THEN ---
#         with allure.step("Verify 'Required' validation error is displayed"):
#             self.vacancies_page.is_shown_error_when_empty_field()

#     # def test_display_engineer_in_table_after_chosen_dropdown(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.vacancies_page.click_on_recruitment_item()
#     #     self.vacancies_page.click_on_vacancies_item()
#     #     self.vacancies_page.click_on_dropdown()
#     #     self.vacancies_page.choose_engineer_from_dropdown()
#     #     self.vacancies_page.click_on_search_btn()
#     #     self.vacancies_page.is_displayed_engineer_in_table()


#     @allure.story("Vacancies filtering by Job Title")
#     @pytest.mark.smoke
#     @pytest.mark.parametrize(
#         "choose_method, expected_titles",
#         [
#             # 1) Engineer
#             ("choose_engineer_from_dropdown", ["Software Engineer"]),

#             # 2) Sales
#             ("choose_sales_from_dropdown", ["Sales Representative"]),
#         ],
#         ids=["engineer", "sales"]
#     )
#     def test_display_job_title_in_table_after_chosen_dropdown(self, choose_method, expected_titles):
#         allure.dynamic.title(f"Vacancies filter: {expected_titles[0]}")
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Vacancies"):
#             self.vacancies_page.click_on_recruitment_item()
#             self.vacancies_page.click_on_vacancies_item()
#         with allure.step(f"Apply filter Job Title = {expected_titles[0]}"):
#             self.vacancies_page.click_on_dropdown()
#             getattr(self.vacancies_page, choose_method)()
#             self.vacancies_page.click_on_search_btn()
#         with allure.step("Validate filtered table results"):
#             self.vacancies_page.is_displayed_job_titles_in_table(expected_titles)

#         # self.vacancies_page.choose_engineer_from_dropdown()
#         # self.vacancies_page.click_on_search_btn()
#         # self.vacancies_page.is_displayed_engineer_in_table()


#     # def test_display_sales_in_table_after_chosen_dropdown(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.vacancies_page.click_on_recruitment_item()
#     #     self.vacancies_page.click_on_vacancies_item()
#     #     self.vacancies_page.click_on_dropdown()
#     #     self.vacancies_page.choose_sales_from_dropdown()
#     #     self.vacancies_page.click_on_search_btn()
#     #     self.vacancies_page.is_displayed_sales_in_table()
# #
# @allure.feature("Recruitment Candidates")
# class TestRecruitmentCandidate(BaseTest):
#     @allure.story("Create a candidate profile")
#     @pytest.mark.smoke
#     def test_add_new_candidate(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Open Add Candidate form"):
#             self.recruitment_candidate_page.click_on_add_btn()
#         with allure.step("Fill candidate details (First name, Last name, Vacancy, Email)"):
#             self.recruitment_candidate_page.type_name_in_the_field()
#             self.recruitment_candidate_page.type__last_name_in_the_field()
#             self.recruitment_candidate_page.click_on_dropdown()
#             self.recruitment_candidate_page.choose_QA_from_dropdown()
#             self.recruitment_candidate_page.type_email()
#         with allure.step("Save candidate and verify success notification"):
#             self.recruitment_candidate_page.click_on_save_btn()
#             self.recruitment_candidate_page.is_added_a_new_candidate()

#     @allure.story("Validate required fields on candidate creation")
#     @pytest.mark.smoke
#     def test_shown_error_when_empty_fields(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Open Add Candidate form and attempt to save empty form"):
#             self.recruitment_candidate_page.click_on_add_btn()
#             self.recruitment_candidate_page.click_on_save_btn()
#         with allure.step("Verify 'Required' validation error is displayed"):
#             self.recruitment_candidate_page.is_shown_required_error()
#     @allure.story("Search candidates using autocomplete")
#     @pytest.mark.smoke
#     def test_found_candidate(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Search candidate by name using autocomplete hint"):
#             self.recruitment_candidate_page.type_candidate_petr_name()
#             self.recruitment_candidate_page.click_on_hint_item()
#             self.recruitment_candidate_page.click_on_search_btn()
#         with allure.step("Verify candidate is present in results table"):
#             self.recruitment_candidate_page.is_found_candidate()
#     @allure.story("Search validation for invalid candidate name input")
#     @pytest.mark.smoke
#     def test_found_invalid_data(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Enter invalid candidate name and validate UI error"):
#             self.recruitment_candidate_page.type_invalid_name()
#             self.recruitment_candidate_page.click_on_hint_no_records()
#             self.recruitment_candidate_page.is_fond_invalid_name()

#     @allure.story("Search candidates - no records scenario")
#     @pytest.mark.smoke
#     def test_found_no_records(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Search using invalid keywords"):
#             self.recruitment_candidate_page.type_invalid_date_keywords_field()
#             self.recruitment_candidate_page.click_on_search_btn()
#         with allure.step("Verify 'No Records Found' is displayed"):
#             self.recruitment_candidate_page.is_fond_no_records_keyword_field()
#     @allure.story("UI controls - filter panel visibility")
#     @pytest.mark.smoke
#     def test_hidden_block(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Verify candidate filter block is hidden"):
#             self.recruitment_candidate_page.is_hidden_block()

#     @allure.story("Filter candidates by vacancy")
#     @pytest.mark.smoke
#     def test_found_only_qa_lead_after_chosen_from_dropdown(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Filter by Vacancy = Senior QA Lead"):
#             self.recruitment_candidate_page.click_on_dropdown()
#             self.recruitment_candidate_page.choose_qa_lead_from_dropdown()
#             self.recruitment_candidate_page.click_on_search_btn()
#         with allure.step("Verify results contain only 'Senior QA Lead' vacancies"):
#             self.recruitment_candidate_page.are_fonded_qa_lead_when_chosen_from_dropdown()

#     @allure.story("Filter candidates by vacancy")
#     @pytest.mark.smoke
#     def test_found_only_sales_after_chosen_from_dropdown(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Filter by Vacancy = Sales Representative"):
#             self.recruitment_candidate_page.click_on_dropdown()
#             self.recruitment_candidate_page.choose_sales_from_dropdown()
#             self.recruitment_candidate_page.click_on_search_btn()
#         with allure.step("Verify results contain only 'Sales Representative' vacancies"):
#             self.recruitment_candidate_page.are_fonded_sales_when_chosen_from_dropdown()

#     @allure.story("Filter candidates by vacancy")
#     @pytest.mark.smoke
#     def test_found_only_manager_chosen_from_dropdown(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Filter by Vacancy = Associate IT Manager"):
#             self.recruitment_candidate_page.click_on_dropdown()
#             self.recruitment_candidate_page.choose_it_manager_from_dropdown()
#             self.recruitment_candidate_page.click_on_search_btn()
#         with allure.step("Verify results contain only 'Associate IT Manager' vacancies"):
#             self.recruitment_candidate_page.are_fonded_manager_when_chosen_from_dropdown()
#     @allure.story("Filter candidates by vacancy")
#     @pytest.mark.smoke
#     def test_found_only_engineer_chosen_from_dropdown(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Filter by Vacancy = Software Engineer"):
#             self.recruitment_candidate_page.click_on_dropdown()
#             self.recruitment_candidate_page.choose_software_engineer_from_dropdown()
#             self.recruitment_candidate_page.click_on_search_btn()
#         with allure.step("Verify results contain only 'Software Engineer' vacancies"):
#             self.recruitment_candidate_page.are_fonded_software_enginner_when_chosen_from_dropdown()
#     @allure.story("Filter candidates by status")
#     @pytest.mark.smoke
#     def test_found_only_rejected_status_chosen_from_dropdown(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Filter by Status = Rejected"):
#             self.recruitment_candidate_page.click_on_status_dropdown_btn()
#             self.recruitment_candidate_page.choose_rejected_from_dropdown()
#             self.recruitment_candidate_page.click_on_search_btn()
#         with allure.step("Verify results contain only status 'Rejected'"):
#             self.recruitment_candidate_page.are_displayed_rejected_when_chosen_from_dropdown()



#     # def test_sorted_ascending_vacancy(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.recruitment_candidate_page.click_on_recruitment_item()
#     #     self.recruitment_candidate_page.is_opened()
#     #     self.recruitment_candidate_page.click_on_sort_icon_btn()
#     #     self.recruitment_candidate_page.are_sorted_ascending_vacancy_in_table()

#     @allure.feature("Recruitment Candidates")
#     @allure.story("Sorting in table")
#     @pytest.mark.smoke
#     @pytest.mark.parametrize(
#     "sort_click_method, assert_method, sort_area, sort_direction",
#     [
#         # Vacancy column
#         ("click_on_sort_icon_btn",      "are_sorted_ascending_vacancy_in_table",   "Vacancy",   "Ascending"),
#         ("click_on_sort_icon_btn",      "are_sorted_descending_vacancy_in_table",  "Vacancy",   "Descending"),

#         # Candidate column
#         ("click_on_sort_icon_candidate","are_sorted_ascending_candidate_in_table", "Candidate", "Ascending"),
#         ("click_on_sort_icon_candidate","are_sorted_descending_candidate_in_table","Candidate", "Descending"),

#         # Hiring Manager column
#         ("click_on_sort_icon_hiring",   "are_sorted_ascending_hiring_in_table",    "Hiring",    "Ascending"),
#         ("click_on_sort_icon_hiring",   "are_sorted_descending_hiring_in_table",   "Hiring",    "Descending"),
#     ]
# )
#     def test_sorting_in_candidates_table(self, sort_click_method, assert_method, sort_area, sort_direction):
#         # --- КРОК 1: Login ---
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()

#         # --- КРОК 2: Open Recruitment page ---
#         with allure.step("Navigate to Recruitment section"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()

#         # --- КРОК 3: Click sort icon ---
#         with allure.step(f"Apply sorting: {sort_area} = {sort_direction}"):
#             getattr(self.recruitment_candidate_page, sort_click_method)()

#         # --- КРОК 4: Validate sorting result (asserts inside Page Object) ---
#         with allure.step(f"Validate sorting result for {sort_area} ({sort_direction})"):
#             getattr(self.recruitment_candidate_page, assert_method)()





#     # def test_sorted_descending_vacancy(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.recruitment_candidate_page.click_on_recruitment_item()
#     #     self.recruitment_candidate_page.is_opened()
#     #     self.recruitment_candidate_page.click_on_sort_icon_btn()
#     #     self.recruitment_candidate_page.are_sorted_descending_vacancy_in_table()
#     #
#     #
#     # def test_sorted_ascending_candidate(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.recruitment_candidate_page.click_on_recruitment_item()
#     #     self.recruitment_candidate_page.is_opened()
#     #     self.recruitment_candidate_page.click_on_sort_icon_candidate()
#     #     self.recruitment_candidate_page.are_sorted_ascending_candidate_in_table()
#     #
#     #
#     # def test_sorted_descending_candidate(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.recruitment_candidate_page.click_on_recruitment_item()
#     #     self.recruitment_candidate_page.is_opened()
#     #     self.recruitment_candidate_page.click_on_sort_icon_candidate()
#     #     self.recruitment_candidate_page.are_sorted_descending_candidate_in_table()
#     #
#     # def test_sorted_ascending_hiring(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.recruitment_candidate_page.click_on_recruitment_item()
#     #     self.recruitment_candidate_page.is_opened()
#     #     self.recruitment_candidate_page.click_on_sort_icon_hiring()
#     #     self.recruitment_candidate_page.are_sorted_ascending_hiring_in_table()
#     #
#     #
#     # def test_sorted_descending_hiring(self):
#     #     self.login_page.open()
#     #     self.login_page.enter_login()
#     #     self.login_page.enter_password()
#     #     self.login_page.click_on_submit_button()
#     #     self.recruitment_candidate_page.click_on_recruitment_item()
#     #     self.recruitment_candidate_page.is_opened()
#     #     self.recruitment_candidate_page.click_on_sort_icon_hiring()
#     #     self.recruitment_candidate_page.are_sorted_descending_hiring_in_table()
#     @allure.story("Search candidates by date range via calendar")
#     @pytest.mark.smoke
#     def test_search_for_valid_data_via_calendar(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Open calendar and search for valid date range"):
#             self.recruitment_candidate_page.click_on_icon_from_calendar()
#             self.recruitment_candidate_page.are_fonded_valid_date_via_calendar()
#     @allure.story("Search candidates by date range via calendar")
#     @pytest.mark.smoke
#     def test_if_search_for_july_in_calendar(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Open calendar and filter for July 2022 range"):
#             self.recruitment_candidate_page.click_on_icon_from_calendar()
#             self.recruitment_candidate_page.are_fonded_july_2022_via_calendar()

#     @allure.story("Search candidates by date range via calendar")
#     @pytest.mark.smoke
#     def test_if_search_for_11_in_calendar(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Open calendar and filter for July 8 -> July 11"):
#             self.recruitment_candidate_page.click_on_icon_from_calendar()
#             self.recruitment_candidate_page.are_fonded_july_11_via_calendar()
#     @allure.story("Search candidates by date range via calendar - negative scenarios")
#     @pytest.mark.smoke
#     def test_if_search_for_invalid_data_via_calendar(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Open calendar and search for invalid date range (expect no records)"):
#             self.recruitment_candidate_page.click_on_icon_from_calendar()
#             self.recruitment_candidate_page.are_fonded_invalid_data_via_calendar()

#     @allure.story("Search candidates by date range via calendar - negative scenarios")
#     @pytest.mark.smoke
#     def test_if_search_for_invalid_record_via_calendar(self):
#         with allure.step("Login to OrangeHRM"):
#             self.login_page.open()
#             self.login_page.enter_login()
#             self.login_page.enter_password()
#             self.login_page.click_on_submit_button()
#         with allure.step("Navigate to Recruitment -> Candidates"):
#             self.recruitment_candidate_page.click_on_recruitment_item()
#             self.recruitment_candidate_page.is_opened()
#         with allure.step("Open calendar and search for invalid date range (expect no records)"):
#             self.recruitment_candidate_page.click_on_icon_from_calendar()
#             self.recruitment_candidate_page.are_searched_for_invalid_data_via_calendar()

# class TestForgotPassword(BaseTest):
#
#     def test_shown_error(self):
#         self.login_page.open()
#         self.forgot_password_page.click_on_forgot_password_link()
#         self.forgot_password_page.is_opened()
#         self.forgot_password_page.click_on_reset_btn()
#         self.forgot_password_page.is_showed_error()
#
#     def test_back_page(self):
#         self.login_page.open()
#         self.forgot_password_page.click_on_forgot_password_link()
#         self.forgot_password_page.is_opened()
#         self.forgot_password_page.click_on_cancel_btn()
#         self.forgot_password_page.is_back_page()
#
#
#     def test_sent_reset_password(self):
#         self.login_page.open()
#         self.forgot_password_page.click_on_forgot_password_link()
#         self.forgot_password_page.is_opened()
#         self.forgot_password_page.type_invalid_email()
#         self.forgot_password_page.click_on_reset_btn()
#         self.forgot_password_page.is_send_reset_password()
#





