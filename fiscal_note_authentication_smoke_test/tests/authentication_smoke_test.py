import pytest, os
from selenium.webdriver import Chrome
from fIscal_note_authentication_smoke_test.pageObject.log_in_page import LogInPage
from fIscal_note_authentication_smoke_test.pageObject.home_page import HomePage


chrome_driver = '/Users/omar.guzman/PycharmProjects/UDR_UI/features/chromedriver'
username = os.environ['FISCALNOTEUSERNAME']
password = os.environ['FISCALNOTEPASSWORD']


@pytest.fixture
def browser():
    driver = Chrome(executable_path=chrome_driver)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_log_in_with_valid_credentials(browser):
    log_in_page = LogInPage(browser)
    home_page = HomePage(browser)
    log_in_page.navigate()
    log_in_page.click_first_log_in_button()
    log_in_page.set_username(username)
    log_in_page.set_password(password)
    log_in_page.click_main_log_in_button()
    assert home_page.check_home_page_displayed()
    # home_page.click_log_out_button()
    # time.sleep(5)


def test_error_message_with_invalid_credentials(browser):
    log_in_page = LogInPage(browser)
    log_in_page.navigate()
    log_in_page.click_first_log_in_button()
    log_in_page.set_username(username)
    log_in_page.set_password('wrong_password')
    log_in_page.click_main_log_in_button()
    assert log_in_page.check_invalid_credentials_error_message_displayed() == 'WRONG EMAIL OR PASSWORD.'


def test_password_field_blank_error_message(browser):
    log_in_page = LogInPage(browser)
    log_in_page.navigate()
    log_in_page.click_first_log_in_button()
    log_in_page.set_username(username)
    log_in_page.set_password('')
    log_in_page.click_main_log_in_button()
    assert log_in_page.check_blank_password_error_message_displayed()


def test_username_field_blank_error_message(browser):
    log_in_page = LogInPage(browser)
    log_in_page.navigate()
    log_in_page.click_first_log_in_button()
    log_in_page.set_username('')
    log_in_page.set_password(password)
    log_in_page.click_main_log_in_button()
    assert log_in_page.check_blank_username_error_message_displayed()


def test_username_and_password_field_blank_error_message(browser):
    log_in_page = LogInPage(browser)
    log_in_page.navigate()
    log_in_page.click_first_log_in_button()
    log_in_page.set_username('')
    log_in_page.set_password('')
    log_in_page.click_main_log_in_button()
    assert log_in_page.check_blank_username_and_password_error_message_displayed()



