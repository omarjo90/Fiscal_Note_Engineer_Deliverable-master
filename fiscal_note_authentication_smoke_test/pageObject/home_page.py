from selenium.webdriver.common.action_chains import ActionChains
from fIscal_note_authentication_smoke_test.pageObject.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    WELCOME_MESSAGE = (By.XPATH, '//h1')
    LOG_OUT_option = (By.XPATH, "//div[@class='sidebar-mini__inner']/div[@class='sidebar-footer']//span[contains(text(), 'Log out')]")
    site_bar = (By.XPATH, "//div[@class='ember-view sidebar']")

    def __init__(self, driver):
        self.driver = driver

    def check_home_page_displayed(self):
        self.is_visible(self.WELCOME_MESSAGE)
        return 'Welcome, QA Engineer Deliverable' in self.driver.page_source

    def click_log_out_button(self):
        self.click(self.site_bar)
        time.sleep(5)
        # self.click(self.LOG_OUT_option)



