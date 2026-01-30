import allure
from selenium.webdriver import ActionChains

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC





class PimReports(BasePage):

    PAGE_URL = Links.PIM_REPORTS
    PAGE_URL = Links.GENERAL_PIM

    PIM_ITEM_FROM_MENU = ("xpath", "//span[text()='PIM']")
    ITEM_LINK = ("xpath", "//a[text()='Reports']")
    ADD_BTN = ("xpath", "//button[text()=' Add ']//i")
    REPORT_NAME_INPUT = ("xpath", "//input[@placeholder='Type here ...']")
    DROPDOWN_FIELD_GROUP = ("xpath", "(//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow' ])[3]")
    CHOOSE_ITEM_FROM_DROPDOWN = ("xpath", "//div[@role='listbox']//span[text()='Contact Details']")
    ICON_PLUS = ("xpath", "(//button[@class='oxd-icon-button orangehrm-report-icon'])[2]")
    SAVE_BTN = ("xpath", "//button[text()=' Save ']")
    TITTLE_H6 = ("xpath", "//h6[text()='pedro']")
    REPORT_NAME_INPUT2 = ("xpath", "//input[@placeholder='Type for hints...']")
    SEARCH_BTN = ("xpath", "//button[text()=' Search ']")
    HINT_FROM_INPUT = ("xpath", "//div[@role='listbox']//span[text()='pedro']")
    TABLE_ROW = ("xpath", "//div[@role='row']//div[contains(text(), 'pedro')]")
    SPAN_ERROR = ("xpath", "//span[text()='Invalid']")
    ICON_BTN = ("xpath", "(//button[@type='button'][@class='oxd-icon-button'])[2]")
    BLOCK_EMPLOYEE_REPORTS = ("xpath", "//div[@class='oxd-table-filter-area']//form")
    ICON_DELETE = ("xpath", "(//i[@class='oxd-icon bi-trash'])[1]")
    YES_DELETE_BTN = ("xpath", "//i[@class='oxd-icon bi-trash oxd-button-icon']")
    PUSH_NOTIFICATION = ("xpath", "//p[text()='Successfully Deleted']")
    # /////////////////////////////////////////////////name
    SORT_ICON_NAME = ("xpath", "(//div[@class='oxd-table-header-sort'])[1]")
    SORT_CHOOSE_ITEM_NAME_AS = ("xpath", "(//span[text()='Ascending'])[1]")
    SORT_CHOOSE_ITEM_NAME_DES = ("xpath", "(//span[text()='Descending'])[1]")
    NAME_COLUMN = ("xpath", "//div[@class='oxd-table-cell oxd-padding-cell'][@style='flex: 1 1 85%;']")

    def is_opened(self):
        self.wait.until(EC.url_contains("/pim/viewEmployeeList"))

    def is_current_page(self):
        self.wait.until(EC.url_contains("/pim/viewDefinedPredefinedReports")
    )



    @allure.step("Click menu: PIM")
    def click_on_pim_item(self):
        self.wait.until(EC.element_to_be_clickable(self.PIM_ITEM_FROM_MENU)).click()

    @allure.step("Open page: Reports")
    def click_on_report_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ITEM_LINK)).click()

    @allure.step("Click button: Add report")
    def click_on_add_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BTN)).click()

    @allure.step("Enter report name: pedro")
    def type_pedro(self):
        self.wait.until(EC.element_to_be_clickable(self.REPORT_NAME_INPUT)).send_keys("pedro")

    @allure.step("Open dropdown: Field Group")
    def click_on_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_FIELD_GROUP)).click()

    @allure.step("Click icon button (open actions/settings)")
    def click_on_icon_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ICON_BTN)).click()

    @allure.step("Select dropdown item: Contact Details")
    def choose_contact_from_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_ITEM_FROM_DROPDOWN)).click()

    @allure.step("Click icon: Plus (add selected field)")
    def click_on_plus_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.ICON_PLUS)).click()

    @allure.step("Click icon: Sort by Name")
    def click_on_sort_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_ICON_NAME)).click()

    @allure.step("Click button: Save report")
    def click_save_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    @allure.step("Click icon: Delete report")
    def click_on_delete_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.ICON_DELETE)).click()

    @allure.step("Confirm deletion: Yes, Delete")
    def click_on_yes_confirm(self):
        self.wait.until(EC.element_to_be_clickable(self.YES_DELETE_BTN)).click()

    @allure.step("Enter invalid search value in report name field")
    def type_invalid_date(self):
        self.wait.until(EC.element_to_be_clickable(self.REPORT_NAME_INPUT2)).send_keys("gdfsghsdfghdsfghdfsg")

    @allure.step("Enter search text: pedr")
    def type_ped(self):
        self.wait.until(EC.element_to_be_clickable(self.REPORT_NAME_INPUT2)).send_keys("pedr")

    @allure.step("Select hint from autocomplete dropdown")
    def click_on_hint_in_the_field(self):
        self.wait.until(EC.element_to_be_clickable(self.HINT_FROM_INPUT)).click()

    @allure.step("Click button: Search")
    def click_on_search_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()

    @allure.step("Assert: searched report is 'pedro' in table")
    def is_searched_report(self):
        x = self.wait.until(EC.visibility_of_element_located(self.TABLE_ROW)).text
        assert x == "pedro"

    @allure.step("Assert: new report title is 'pedro'")
    def is_appeared_new_report(self):
        report = self.wait.until(EC.element_to_be_clickable(self.TITTLE_H6)).text
        assert report == "pedro"

    @allure.step("Assert: validation error 'Invalid' is displayed")
    def is_searched_invalid_report(self):
        x = self.wait.until(EC.visibility_of_element_located(self.SPAN_ERROR)).text
        assert x == "Invalid"

    @allure.step("Assert: report is deleted successfully")
    def is_successfully_deleted_report(self):
        x = self.wait.until(EC.element_to_be_clickable(self.PUSH_NOTIFICATION)).text
        assert x == "Successfully Deleted"

    def is_sorted_ascending_name(self):
        action = ActionChains(self.driver)
        self.wait.until(EC.element_to_be_clickable(self.SORT_ICON_NAME)).click()
        element = self.wait.until(EC.element_to_be_clickable(self.SORT_CHOOSE_ITEM_NAME_AS))
        action.move_to_element(element).click().perform()
        name_column = self.wait.until(EC.visibility_of_all_elements_located(self.NAME_COLUMN))
        size_list = []
        for size in name_column:
            size_list.append(size.text)
        print(size_list)

        y = ['All Employee Sub Unit Hierarchy Report', 'Employee Contact info report', 'Employee Job Details', 'PIM Sample Report']
        print(y)
        assert all([a == b for a, b in zip(size_list, y)])


    def is_sorted_descending_name(self):
        action = ActionChains(self.driver)
        self.wait.until(EC.element_to_be_clickable(self.SORT_ICON_NAME)).click()
        element = self.wait.until(EC.element_to_be_clickable(self.SORT_CHOOSE_ITEM_NAME_DES))
        action.move_to_element(element).click().perform()
        name_column = self.wait.until(EC.visibility_of_all_elements_located(self.NAME_COLUMN))
        size_list = []
        for size in name_column:
            size_list.append(size.text)
        print(size_list)

        y = ['PIM Sample Report', 'Employee Job Details', 'Employee Contact info report','All Employee Sub Unit Hierarchy Report']
        print(y)
        assert all([a == b for a, b in zip(size_list, y)])


    def is_hidden_block(self):
        assert self.wait.until(EC.invisibility_of_element_located(self.BLOCK_EMPLOYEE_REPORTS))









