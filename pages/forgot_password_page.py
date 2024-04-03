from base.base_page import BasePage
from config.links import Links
from config.data import Login
from selenium.webdriver.support import expected_conditions as EC




class ForgotPasswordPage(BasePage):

    PAGE_URL = Links.RESET_PASSWORD_PAGE

    LINK_FORGOT_PASSWORD = ("xpath", "//p[text()='Forgot your password? ']")
    CANCEL_BTN = ("xpath", "//button[text()=' Cancel ']")
    H5_TEXT = ("xpath", "//h5[text()='Login']")
    RESET_BTN = ("xpath", "//button[text()=' Reset Password ']")
    ERROR_MESSAGE = ("xpath", "//span[text()='Required']")
    USERNAME_INPUT = ("xpath", "//input[@name='username']")
    H6_TEXT = ("xpath", "//h6[text()='Reset Password link sent successfully']")



    def click_on_forgot_password_link(self):
        self.wait.until(EC.element_to_be_clickable(self.LINK_FORGOT_PASSWORD)).click()

    def click_on_reset_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.RESET_BTN)).click()

    def click_on_cancel_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BTN)).click()

    def type_invalid_email(self):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT)).send_keys("fghfghhfghgfhfghffgh")


    def is_showed_error(self):
        error_text = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE)).text
        assert error_text == "Required"

    def is_back_page(self):
        tittle = self.wait.until(EC.presence_of_element_located(self.H5_TEXT)).text
        assert tittle == "Login"

    def is_send_reset_password(self):
        text = self.wait.until(EC.presence_of_element_located(self.H6_TEXT)).text
        assert text == "Reset Password link sent successfully"

