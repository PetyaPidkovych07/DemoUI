from selenium.common import ElementClickInterceptedException, ElementNotInteractableException, \
    StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






class BasePage:

    OVERLAY_ACTIVE = ("css selector", ".oxd-layout-overlay:not(.oxd-overlay--hide)")
    SPINNER_ACTIVE = ("css selector", ".oxd-loading-spinner-container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=0.2)


    def open(self):
        self.driver.get(self.PAGE_URL)


    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))



    # 🔒 CI-safe wait: overlay повністю "схований"

    def wait_overlay_gone(self):
        # чекаємо, поки активний overlay зникне (або його нема)
        self.wait.until(EC.invisibility_of_element_located(self.OVERLAY_ACTIVE))
        # і поки спінер зникне (на OrangeHRM часто є)
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER_ACTIVE))



# 🔥 CI-safe click (scroll + overlay-aware + JS click)
    def safe_click(self, locator, retries=3):
        last = None

        for _ in range(retries):
            try:
                self.wait_overlay_gone()

                el = self.wait.until(EC.presence_of_element_located(locator))
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", el
                )
                self.wait.until(EC.visibility_of(el))

                self.wait_overlay_gone()

                # 1️⃣ реальний user-like click
                ActionChains(self.driver) \
                    .move_to_element(el) \
                    .pause(0.05) \
                    .click(el) \
                    .perform()
                return

            except (
                    ElementClickInterceptedException,
                    ElementNotInteractableException,
                    StaleElementReferenceException,
                    TimeoutException
            ) as e:
                last = e

                # 2️⃣ fallback — JS click
                try:
                    el = self.wait.until(EC.presence_of_element_located(locator))
                    self.driver.execute_script("arguments[0].click();", el)
                    return
                except Exception as e2:
                    last = e2

        raise last
