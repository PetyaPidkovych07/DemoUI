from selenium.common import NoSuchElementException, TimeoutException

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from config.list_nationalities import Nationalities
import time




class AdminNationalities(BasePage):

    PAGE_URL = Links.CHOOSE_ADMIN_ITEM_FROM_MAIN_MENU
    COUNTRIES = Nationalities

    CHOOSE_ADMIN_FROM_MENU = ("xpath", "//span[text()='Admin']")
    NATIONALITIES_BTN = ("xpath", "//a[text()='Nationalities']")
    DELETE_BTN = ("xpath", "(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[1]")
    EDIT_BTN = ("xpath", "(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[2]")
    YES_DELETE_ITEM = ("xpath", "//*[text()=' Yes, Delete ']")
    PUSH_NOTIFICATION_SUCCESS_DELETE = ("xpath", "//p[text()='Successfully Deleted']")
    PUSH_SUCCSESSFULLY_UPDATE = ("xpath", "//p[text()='Successfully Updated']")
    INPUT_CHECKBOX = ("xpath", "//input[@type='checkbox'][@value='7']")

    # adddddddddddddddddddddd national
    ADD_BTN = ("xpath", "//i[@class='oxd-icon bi-plus oxd-button-icon']")
    SAVE_BTN = ("xpath", "//button[@type='submit']")
    ERROR_REQUIRED = ("xpath", "//span[text()='Required']")
    ERROR_EXSITS = ("xpath", "//span[text()='Already exists']")
    INPUT = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    PUSH_NOTIFICATION_SUCCESSS = ("xpath", "//p[text()='Successfully Saved']")
    PUSH_NOTIFICATION_DELETE = ("xpath", "//p[text()='Successfully Deleted']")

    CONTAINER = ("xpath", "//div[@class='orangehrm-container']")
    All_USERS = ("xpath", "//div[@class='oxd-table-body']//div[@role='row']")

    PAGINATION = ("xpath", "//ul[@class='oxd-pagination__ul']//li//button[@type='button']")
    NEXT_BTN = ("xpath", "//button[@type='button']//i[@class='oxd-icon bi-chevron-right']")
    CHECK_BOX = ("xpath", "//input[@value='36']")
    DELETE_SELECTED = ("xpath", "//*[text()=' Delete Selected ']")
    DELETE_ICON = ("xpath", "(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[71]")
    ITEM_FROM_TABLE_WITH_PAGINATION = ("xpath", "//div[@class='oxd-table-card']//div[text()='Ukrainian']/../../div[1]")
    APPEAR_DEL_BTN = ("xpath", "//i[@class= 'oxd-icon bi-trash-fill oxd-button-icon']")


    def click_on_admin_item(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_ADMIN_FROM_MENU)).click()

    def choose_on_nationalities_item(self):
        self.wait.until(EC.element_to_be_clickable(self.NATIONALITIES_BTN)).click()

    def click_on_add_item(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BTN)).click()

    def type_ukraine(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT)).send_keys("Ukraine")

    def click_on_save_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    def is_saved_country(self):
        push_text = self.wait.until(EC.element_to_be_clickable(self.PUSH_NOTIFICATION_SUCCESSS)).text
        assert push_text == 'Successfully Saved'

    def is_showed_error(self):
        text = self.wait.until(EC.visibility_of_element_located(self.ERROR_EXSITS)).text
        assert text == 'Already exists'

    def is_empty_error(self):
        text = self.wait.until(EC.visibility_of_element_located(self.ERROR_REQUIRED)).text
        assert text == 'Required'

    def type_kyiv(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT)).send_keys("Kyiv")

    def type_portu(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT)).send_keys("Portu")


    def delete_kyiv_from_table(self):
        expected_client = "Kyiv"
        xpath_text1 = "//div[@class='oxd-table-card']//div[text()='" + expected_client + "']"
        for i in range(1, 6):
            try:
                if self.driver.find_element("xpath", xpath_text1).is_displayed():
                    self.driver.find_element("xpath", xpath_text1 + "/../../div[1]").click()
                    time.sleep(2)
                    break
            except NoSuchElementException:
                pass
            xpath_text = "(//nav[@role='navigation']//ul[@class='oxd-pagination__ul']//li[" + str(i) + "])"
            time.sleep(2)
            self.driver.find_element("xpath", xpath_text).click()
            time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollDown);")
        time.sleep(5)

    def click_on_delete_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.APPEAR_DEL_BTN)).click()

    def click_on_yes_confirm(self):
        self.wait.until(EC.element_to_be_clickable(self.YES_DELETE_ITEM)).click()

    def is_deleted_country(self):
        text = self.wait.until(EC.visibility_of_element_located(self.PUSH_NOTIFICATION_DELETE)).text
        assert text == "Successfully Deleted"


    def compare_all_countries_in_table(self):
        try:
            tru = self.wait.until(EC.element_to_be_clickable(self.PAGINATION))
            time.sleep(3)
            pages = tru.find_elements("xpath", "//ul[@class='oxd-pagination__ul']//li//button[@type='button']")
            time.sleep(2)
            last_page = int(pages[-2].text)
            print("There is pagination")
        except:
            print("No pagination")


        current_page = 1
        nationalities = []
        test_data = []

        while current_page <= last_page:
            time.sleep(2)
            container = self.wait.until(EC.element_to_be_clickable(self.CONTAINER))
            all_users = self.wait.until(EC.visibility_of_all_elements_located(self.All_USERS))

            for user in all_users:
                nationalities.append(user.find_element("xpath", ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')][2]").text)

            current_page = current_page + 1

            try:
                next_page = self.wait.until(EC.element_to_be_clickable(self.NEXT_BTN))
                next_page.click()
            except TimeoutException:
                pass
        print(f"Nationalities: {nationalities}")

        assert nationalities == Nationalities.NATIONALITIES


















