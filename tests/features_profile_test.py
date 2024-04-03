import time

from base.base_test import BaseTest


# class TestProfileFeatures(BaseTest):
#
#     def test_with_valid_crendentional(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#
#
# class TestNationalities(BaseTest):
#
#     def test_scraping_all_countries_in_table(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.nationalities_page.click_on_admin_item()
#         self.nationalities_page.is_opened()
#         self.nationalities_page.choose_on_nationalities_item()
#         self.nationalities_page.compare_all_countries_in_table()

    # def test_add_country(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.nationalities_page.click_on_admin_item()
    #     self.nationalities_page.is_opened()
    #     self.nationalities_page.choose_on_nationalities_item()
    #     self.nationalities_page.click_on_add_item()
    #     self.nationalities_page.type_ukraine()
    #     self.nationalities_page.click_on_save_btn()
    #     self.nationalities_page.is_saved_country()
    #
    # def test_add_kyiv(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.nationalities_page.click_on_admin_item()
    #     self.nationalities_page.is_opened()
    #     self.nationalities_page.choose_on_nationalities_item()
    #     self.nationalities_page.click_on_add_item()
    #     self.nationalities_page.type_kyiv()
    #     self.nationalities_page.click_on_save_btn()
    #     self.nationalities_page.is_saved_country()
    #
    # def test_delete_kyiv_from_table(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.nationalities_page.click_on_admin_item()
    #     self.nationalities_page.is_opened()
    #     self.nationalities_page.choose_on_nationalities_item()
    #     self.nationalities_page.delete_kyiv_from_table()
    #     self.nationalities_page.click_on_delete_btn()
    #     self.nationalities_page.click_on_yes_confirm()
    #     self.nationalities_page.is_deleted_country()
    #
    # def test_country_is_exist(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.nationalities_page.click_on_admin_item()
    #     self.nationalities_page.is_opened()
    #     self.nationalities_page.choose_on_nationalities_item()
    #     self.nationalities_page.click_on_add_item()
    #     self.nationalities_page.type_ukraine()
    #     self.nationalities_page.is_showed_error()
    #
    # def test_empty_field(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.nationalities_page.click_on_admin_item()
    #     self.nationalities_page.is_opened()
    #     self.nationalities_page.choose_on_nationalities_item()
    #     self.nationalities_page.click_on_add_item()
    #     self.nationalities_page.click_on_save_btn()
    #     self.nationalities_page.is_empty_error()


#
#
# class TestDirectory(BaseTest):
#
#     def test_is_display_employee_after_filters(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.directory_page.click_on_directory_item()
#         self.directory_page.is_opened()
#         self.directory_page.click_on_dropdown()
#         self.directory_page.choose_item_from_dropdown()
#         self.directory_page.click_on_search_btn()
#         self.directory_page.is_present_software_in_table()
#
#     def test_is_display_hr_after_filters(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.directory_page.click_on_directory_item()
#         self.directory_page.is_opened()
#         self.directory_page.click_on_dropdown()
#         self.directory_page.choose_hr_from_dropdown()
#         self.directory_page.click_on_search_btn()
#         self.directory_page.is_present_hr_in_table()
#
#     def test_is_display_chief_after_filters(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.directory_page.click_on_directory_item()
#         self.directory_page.is_opened()
#         self.directory_page.click_on_dropdown()
#         self.directory_page.choose_chief_from_dropdown()
#         self.directory_page.click_on_search_btn()
#         self.directory_page.is_present_chief_technical_in_table()
#
#
#     def test_all_locations_are_presented_in_dropdown(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.directory_page.click_on_directory_item()
#         self.directory_page.is_opened()
#         self.directory_page.click_on_location_dropdown()
#         self.directory_page.choose_all_location_from_dropdown()
#         self.directory_page.click_on_search_btn()
#         self.directory_page.is_displayed_locations__in_dropdown()
#
#
#     def test_each_user_have_email(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.directory_page.click_on_directory_item()
#         self.directory_page.is_opened()
#         self.directory_page.click_on_dropdown()
#         self.directory_page.choose_job_title_from_dropdown()
#         self.directory_page.click_on_search_btn()
#         self.directory_page.is_each_user_have_email()
#
#
#
# class TestPimReports(BaseTest):
#
#     def test_add_report(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.pim_reports_page.click_on_pim_item()
#         self.pim_reports_page.click_on_report_link()
#         self.pim_reports_page.click_on_add_btn()
#         self.pim_reports_page.type_pedro()
#         self.pim_reports_page.click_on_dropdown()
#         self.pim_reports_page.choose_contact_from_dropdown()
#         self.pim_reports_page.click_on_plus_icon()
#         self.pim_reports_page.click_save_btn()
#         self.pim_reports_page.is_appeared_new_report()
#
#
#
#     def test_find_a_new_report(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.pim_reports_page.click_on_pim_item()
#         self.pim_reports_page.click_on_report_link()
#         self.pim_reports_page.type_ped()
#         self.pim_reports_page.click_on_hint_in_the_field()
#         self.pim_reports_page.click_on_search_btn()
#         self.pim_reports_page.is_appeared_new_report()
#
#     def test_find_invalid_report(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.pim_reports_page.click_on_pim_item()
#         self.pim_reports_page.click_on_report_link()
#         self.pim_reports_page.type_invalid_date()
#         self.pim_reports_page.click_on_search_btn()
#         self.pim_reports_page.is_searched_invalid_report()
#
#     def test_delete_report(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.pim_reports_page.click_on_pim_item()
#         self.pim_reports_page.click_on_report_link()
#         self.pim_reports_page.type_ped()
#         self.pim_reports_page.click_on_hint_in_the_field()
#         self.pim_reports_page.click_on_search_btn()
#         self.pim_reports_page.click_on_delete_icon()
#         self.pim_reports_page.click_on_yes_confirm()
#         self.pim_reports_page.is_successfully_deleted_report()
#
#     def test_sort_ascending_name(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.pim_reports_page.click_on_pim_item()
#         self.pim_reports_page.click_on_report_link()
#         self.pim_reports_page.click_on_sort_icon()
#         self.pim_reports_page.is_sorted_ascending_name()
#
#     def test_sort_descending_name(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.pim_reports_page.click_on_pim_item()
#         self.pim_reports_page.click_on_report_link()
#         self.pim_reports_page.click_on_sort_icon()
#         self.pim_reports_page.is_sorted_descending_name()
#
#     def test_hide_block(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.pim_reports_page.click_on_pim_item()
#         self.pim_reports_page.click_on_report_link()
#         self.pim_reports_page.click_on_icon_btn()
#         self.pim_reports_page.is_hidden_block()
#
# class TestVacancies(BaseTest):
#
#     def test_add_vacancy_QA(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.vacancies_page.click_on_recruitment_item()
#         self.vacancies_page.click_on_vacancies_item()
#         self.vacancies_page.click_on_add_btn()
#         self.vacancies_page.type_petro_in_the_field()
#         self.vacancies_page.click_on_dropdown()
#         self.vacancies_page.choose_QA_from_dropdown()
#         self.vacancies_page.type_odis()
#         self.vacancies_page.click_on_hint()
#         self.vacancies_page.click_on_save_btn()
#         self.vacancies_page.click_on_vacancies_item()
#         self.vacancies_page.is_added_new_vacancy()
#
#     def test_vacancy_existed(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.vacancies_page.click_on_recruitment_item()
#         self.vacancies_page.click_on_vacancies_item()
#         self.vacancies_page.click_on_add_btn()
#         self.vacancies_page.type_petro_in_the_field()
#         self.vacancies_page.is_already_existed_position()
#
#     def test_show_error_when_empty_field(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.vacancies_page.click_on_recruitment_item()
#         self.vacancies_page.click_on_vacancies_item()
#         self.vacancies_page.click_on_add_btn()
#         self.vacancies_page.click_on_save_btn()
#         self.vacancies_page.is_shown_error_when_empty_field()
#
#     def test_display_engineer_in_table_after_chosen_dropdown(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.vacancies_page.click_on_recruitment_item()
#         self.vacancies_page.click_on_vacancies_item()
#         self.vacancies_page.click_on_dropdown()
#         self.vacancies_page.choose_engineer_from_dropdown()
#         self.vacancies_page.click_on_search_btn()
#         self.vacancies_page.is_displayed_engineer_in_table()
#
#
#     def test_display_sales_in_table_after_chosen_dropdown(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.vacancies_page.click_on_recruitment_item()
#         self.vacancies_page.click_on_vacancies_item()
#         self.vacancies_page.click_on_dropdown()
#         self.vacancies_page.choose_sales_from_dropdown()
#         self.vacancies_page.click_on_search_btn()
#         self.vacancies_page.is_displayed_sales_in_table()


class TestRecruitmentCandidate(BaseTest):

    # def test_add_new_candidate(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_add_btn()
    #     self.recruitment_candidate_page.type_name_in_the_field()
    #     self.recruitment_candidate_page.type__last_name_in_the_field()
    #     self.recruitment_candidate_page.click_on_dropdown()
    #     self.recruitment_candidate_page.choose_QA_from_dropdown()
    #     self.recruitment_candidate_page.type_email()
    #     self.recruitment_candidate_page.click_on_save_btn()
    #     self.recruitment_candidate_page.is_added_a_new_candidate()
    #
    #
    # def test_shown_error_when_empty_fields(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_add_btn()
    #     self.recruitment_candidate_page.click_on_save_btn()
    #     self.recruitment_candidate_page.is_shown_required_error()
    #
    # def test_found_candidate(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.type_candidate_petr_name()
    #     self.recruitment_candidate_page.click_on_hint_item()
    #     self.recruitment_candidate_page.click_on_search_btn()
    #     self.recruitment_candidate_page.is_found_candidate()
    #
    # def test_found_invalid_data(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.type_invalid_name()
    #     self.recruitment_candidate_page.click_on_hint_no_records()
    #     self.recruitment_candidate_page.is_fond_invalid_name()
    #
    # def test_found_no_records(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.type_invalid_date_keywords_field()
    #     self.recruitment_candidate_page.click_on_search_btn()
    #     self.recruitment_candidate_page.is_fond_no_records_keyword_field()
    #
    # def test_hidden_block(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.is_hidden_block()
    #
    # def test_found_only_qa_lead_after_chosen_from_dropdown(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_dropdown()
    #     self.recruitment_candidate_page.choose_qa_lead_from_dropdown()
    #     self.recruitment_candidate_page.click_on_search_btn()
    #     self.recruitment_candidate_page.are_fonded_qa_lead_when_chosen_from_dropdown()
    #
    #
    # def test_found_only_sales_after_chosen_from_dropdown(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_dropdown()
    #     self.recruitment_candidate_page.choose_sales_from_dropdown()
    #     self.recruitment_candidate_page.click_on_search_btn()
    #     self.recruitment_candidate_page.are_fonded_sales_when_chosen_from_dropdown()


    # def test_found_only_manager_chosen_from_dropdown(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_dropdown()
    #     self.recruitment_candidate_page.choose_it_manager_from_dropdown()
    #     self.recruitment_candidate_page.click_on_search_btn()
    #     self.recruitment_candidate_page.are_fonded_manager_when_chosen_from_dropdown()

    # def test_found_only_engineer_chosen_from_dropdown(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_dropdown()
    #     self.recruitment_candidate_page.choose_software_engineer_from_dropdown()
    #     self.recruitment_candidate_page.click_on_search_btn()
    #     self.recruitment_candidate_page.are_fonded_software_enginner_when_chosen_from_dropdown()

    # def test_found_only_rejected_status_chosen_from_dropdown(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_status_dropdown_btn()
    #     self.recruitment_candidate_page.choose_rejected_from_dropdown()
    #     self.recruitment_candidate_page.click_on_search_btn()
    #     self.recruitment_candidate_page.are_displayed_rejected_when_chosen_from_dropdown()

    # def test_sorted_ascending_vacancy(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_sort_icon_btn()
    #     self.recruitment_candidate_page.are_sorted_ascending_vacancy_in_table()

    # def test_sorted_descending_vacancy(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_sort_icon_btn()
    #     self.recruitment_candidate_page.are_sorted_descending_vacancy_in_table()


    # def test_sorted_ascending_candidate(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_sort_icon_candidate()
    #     self.recruitment_candidate_page.are_sorted_ascending_candidate_in_table()


    # def test_sorted_descending_candidate(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_sort_icon_candidate()
    #     self.recruitment_candidate_page.are_sorted_descending_candidate_in_table()

    # def test_sorted_ascending_hiring(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_sort_icon_hiring()
    #     self.recruitment_candidate_page.are_sorted_ascending_hiring_in_table()


    # def test_sorted_descending_hiring(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_sort_icon_hiring()
    #     self.recruitment_candidate_page.are_sorted_descending_hiring_in_table()

    # def test_search_for_valid_data_via_calendar(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_icon_from_calendar()
    #     self.recruitment_candidate_page.are_fonded_valid_date_via_calendar()

    # def test_if_search_for_july_in_calendar(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_icon_from_calendar()
    #     self.recruitment_candidate_page.are_fonded_july_2022_via_calendar()


    # def test_if_search_for_11_in_calendar(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_icon_from_calendar()
    #     self.recruitment_candidate_page.are_fonded_july_11_via_calendar()

    def test_if_search_for_invalid_data_via_calendar(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_on_submit_button()
        self.recruitment_candidate_page.click_on_recruitment_item()
        self.recruitment_candidate_page.is_opened()
        self.recruitment_candidate_page.click_on_icon_from_calendar()
        self.recruitment_candidate_page.are_fonded_invalid_data_via_calendar()

    # def test_if_search_for_invalid_record_via_calendar(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.recruitment_candidate_page.click_on_recruitment_item()
    #     self.recruitment_candidate_page.is_opened()
    #     self.recruitment_candidate_page.click_on_icon_from_calendar()
    #     self.recruitment_candidate_page.are_searched_for_invalid_data_via_calendar()





