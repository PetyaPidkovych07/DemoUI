from base.base_test import BaseTest




class TestProfileFeatures(BaseTest):

    def test_with_valid_crendentional(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.click_on_submit_button()






