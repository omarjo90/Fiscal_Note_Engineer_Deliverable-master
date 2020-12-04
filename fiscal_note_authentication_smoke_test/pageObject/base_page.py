from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def enter_text(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        except TimeoutError as e:
            print('Error: ' + str(e))

    def is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).is_displayed()

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()