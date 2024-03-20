from base.base_page import BasePage
from config.links import Links
from config.data import Login
from selenium.webdriver.support import expected_conditions as EC
import time



class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE
    AUTH = Login.login

    USERNAME_INPUT = ("xpath", "//input[@name='username']")
    PASSWORD_INPUT = ("xpath", "//input[@name='password']")
    LOGIN_BTN = ("xpath", "//button[@type='submit']")



    def enter_login(self, username = "Admin"):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT)).send_keys(username)

    def enter_password(self):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys("admin123")

    def click_on_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()
        time.sleep(3)

