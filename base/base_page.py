from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






class BasePage:

    OVERLAY = ("css selector", ".oxd-layout-overlay")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=0.2)


    def open(self):
        self.driver.get(self.PAGE_URL)


    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))



    # 🔒 CI-safe wait: overlay повністю "схований"
    def wait_overlay_gone(self):
        try:
            self.wait.until(
                lambda d: "oxd-overlay--hide"
                in d.find_element(*self.OVERLAY).get_attribute("class")
            )
        except Exception:
            # якщо overlay ще не існує — ок
            pass



# 🔥 CI-safe click (scroll + overlay-aware + JS click)
    def safe_click(self, locator):
        self.wait_overlay_gone()

        el = self.wait.until(EC.presence_of_element_located(locator))

        # важливо для CI / Xvfb
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", el
        )

        self.wait_overlay_gone()

        # JS click — стабільно в CI
        self.driver.execute_script("arguments[0].click();", el)
