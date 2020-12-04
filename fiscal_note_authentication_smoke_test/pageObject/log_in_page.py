from fiscal_note_authentication_smoke_test.pageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class LogInPage(BasePage):
    URL = "https://app.fiscalnote.com/"
    LOG_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Log In')]")
    PASSWORD_FIELD = (By.NAME, 'password')
    USERNAME_FIELD = (By.NAME, 'email')
    MAIN_LOG_IN_BUTTON = (By.XPATH, "//button/span[contains(text(), 'Log In')]")
    INVALID_CREDENTIALS_ERROR_MESSAGE = (By.XPATH, "//div[@class='auth0-global-message auth0-global-message-error']//span[contains(text(), 'Wrong email')]")
    PASSWORD_BLANK_ERROR_MESSAGE = (By.XPATH, "//div[@class='auth0-lock-input-block auth0-lock-input-show-password']//span[contains(text(), 'Can')]")
    USERNAME_BLANK_ERROR_MESSAGE = (By.XPATH, "//div[@class='auth0-lock-input-block auth0-lock-input-email auth0-lock-error']//span[contains(text(), 'Can')]")

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.URL)

    def set_username(self, username):
        self.enter_text(self.USERNAME_FIELD, username)

    def set_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_first_log_in_button(self):
        self.driver.find_element(*self.LOG_IN_BUTTON).click()

    def click_main_log_in_button(self):
        self.driver.find_element(*self.MAIN_LOG_IN_BUTTON).click()

    def check_invalid_credentials_error_message_displayed(self):
        self.is_visible(self.INVALID_CREDENTIALS_ERROR_MESSAGE)
        return self.find_element(*self.INVALID_CREDENTIALS_ERROR_MESSAGE).text

    def check_blank_password_error_message_displayed(self):
        return self.is_visible(self.PASSWORD_BLANK_ERROR_MESSAGE)

    def check_blank_username_error_message_displayed(self):
        return self.is_visible(self.USERNAME_BLANK_ERROR_MESSAGE)

    def check_blank_username_and_password_error_message_displayed(self):
        return self.is_visible(self.USERNAME_BLANK_ERROR_MESSAGE) and self.is_visible(self.PASSWORD_BLANK_ERROR_MESSAGE)



