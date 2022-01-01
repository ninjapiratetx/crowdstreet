import pytest
import os
import framework.page
from framework.random_number import generate_random_number
from selenium import webdriver


TEST_SERVER = "https://test.crowdstreet.com/"
FIRST_NAME = "test"
LAST_NAME = "test"
EMAIL = f"ninjapiratetx+{generate_random_number()}@gmail.com"
PASSWORD = os.environ['PASSWORD']


@pytest.fixture
def chrome_driver(): 
   driver = webdriver.Chrome()
   driver.get(TEST_SERVER)
   yield driver

def test_registration_asked(chrome_driver):
    driver = chrome_driver
    main_page = framework.page.MainPage(driver)
    assert main_page.registration_exists()

def test_signup(chrome_driver):
    driver = chrome_driver
    main_page = framework.page.MainPage(driver)
    signup_page = main_page.click_register_button()
    signup_page.enter_first_name(FIRST_NAME)
    signup_page.enter_last_name(LAST_NAME)
    signup_page.enter_email_address(EMAIL)
    signup_page.enter_password(PASSWORD)
    signup_page.click_on_accept()