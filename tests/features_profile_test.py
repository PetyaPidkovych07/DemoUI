from base.base_test import BaseTest




# class TestProfileFeatures(BaseTest):
#
#     def test_with_valid_crendentional(self):
#         self.login_page.open()
#         self.login_page.enter_login()
#         self.login_page.enter_password()
#         self.login_page.click_on_submit_button()

class TestNationalities(BaseTest):

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



    def test_scraping_all_countries_in_table(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_on_submit_button()
        self.nationalities_page.click_on_admin_item()
        self.nationalities_page.is_opened()
        self.nationalities_page.choose_on_nationalities_item()
        self.nationalities_page.compare_all_countries_in_table()













