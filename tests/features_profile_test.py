from base.base_test import BaseTest


class TestProfileFeatures(BaseTest):

    def test_with_valid_crendentional(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_on_submit_button()
#
#
# class TestNationalities(BaseTest):
#
#     def test_add_country(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.nationalities_page.click_on_admin_item()
#         self.nationalities_page.is_opened()
#         self.nationalities_page.choose_on_nationalities_item()
#         self.nationalities_page.click_on_add_item()
#         self.nationalities_page.type_ukraine()
#         self.nationalities_page.click_on_save_btn()
#         self.nationalities_page.is_saved_country()
#
#     def test_add_kyiv(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.nationalities_page.click_on_admin_item()
#         self.nationalities_page.is_opened()
#         self.nationalities_page.choose_on_nationalities_item()
#         self.nationalities_page.click_on_add_item()
#         self.nationalities_page.type_kyiv()
#         self.nationalities_page.click_on_save_btn()
#         self.nationalities_page.is_saved_country()
#
#     def test_delete_kyiv_from_table(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.nationalities_page.click_on_admin_item()
#         self.nationalities_page.is_opened()
#         self.nationalities_page.choose_on_nationalities_item()
#         self.nationalities_page.delete_kyiv_from_table()
#         self.nationalities_page.click_on_delete_btn()
#         self.nationalities_page.click_on_yes_confirm()
#         self.nationalities_page.is_deleted_country()
#
#     def test_country_is_exist(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.nationalities_page.click_on_admin_item()
#         self.nationalities_page.is_opened()
#         self.nationalities_page.choose_on_nationalities_item()
#         self.nationalities_page.click_on_add_item()
#         self.nationalities_page.type_ukraine()
#         self.nationalities_page.is_showed_error()
#
#     def test_empty_field(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()
#         self.nationalities_page.click_on_admin_item()
#         self.nationalities_page.is_opened()
#         self.nationalities_page.choose_on_nationalities_item()
#         self.nationalities_page.click_on_add_item()
#         self.nationalities_page.click_on_save_btn()
#         self.nationalities_page.is_empty_error()
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

    # def test_add_report(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.pim_reports_page.click_on_pim_item()
    #     self.pim_reports_page.click_on_report_link()
    #     self.pim_reports_page.click_on_add_btn()
    #     self.pim_reports_page.type_pedro()
    #     self.pim_reports_page.click_on_dropdown()
    #     self.pim_reports_page.choose_contact_from_dropdown()
    #     self.pim_reports_page.click_on_plus_icon()
    #     self.pim_reports_page.click_save_btn()
    #     self.pim_reports_page.is_appeared_new_report()
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
    # def test_delete_report(self):
    #     self.login_page.open()
    #     self.login_page.enter_login()
    #     self.login_page.enter_password()
    #     self.login_page.click_on_submit_button()
    #     self.pim_reports_page.click_on_pim_item()
    #     self.pim_reports_page.click_on_report_link()
    #     self.pim_reports_page.type_ped()
    #     self.pim_reports_page.click_on_hint_in_the_field()
    #     self.pim_reports_page.click_on_search_btn()
    #     self.pim_reports_page.click_on_delete_icon()
    #     self.pim_reports_page.click_on_yes_confirm()
    #     self.pim_reports_page.is_successfully_deleted_report()



