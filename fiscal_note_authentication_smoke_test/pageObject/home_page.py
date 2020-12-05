from selenium.webdriver.common.action_chains import ActionChains
from fiscal_note_authentication_smoke_test.pageObject.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    WELCOME_MESSAGE = (By.XPATH, '//h1')
    LOG_OUT_option = (By.XPATH, "//div[@class='sidebar-mini__inner']/div[@class='sidebar-footer']//span[contains(text(), 'Log out')]")
    SITE_BAR = (By.XPATH, "//div[@class='ember-view sidebar']")
    ABSOLUTE_XPATH_LOG_OUT = (By.XPATH, "/html/body/div[1]/div[6]/div/div[1]/div/div[4]/div[2]/div[9]/div[1]/div[1]/a/span/i")
    ABSOLUTE_XPATH_LOG_OUT_BUTTON = (By.XPATH, "/html/body/div[1]/div[6]/div/div[1]/div/div[4]/div[2]/div[9]/div[1]/div[3]/div[2]/a/span")

    def __init__(self, driver):
        self.driver = driver

    def check_home_page_displayed(self):
        self.is_visible(self.WELCOME_MESSAGE)
        return 'Welcome, QA Engineer Deliverable' in self.driver.page_source

    def click_log_out_button(self):
        self.click(self.SITE_BAR)
        self.click(self.ABSOLUTE_XPATH_LOG_OUT)
        self.click(self.ABSOLUTE_XPATH_LOG_OUT_BUTTON)
