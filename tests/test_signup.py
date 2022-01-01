import pytest
import framework.page
from selenium import webdriver

TEST_SERVER = "https://test.crowdstreet.com/"

@pytest.fixture
def chrome_driver(): 
   driver = webdriver.Chrome()
   driver.get(TEST_SERVER)
   yield driver

def test_registration_asked(chrome_driver):
    driver = chrome_driver
    main_page = framework.page.MainPage(driver)
    assert main_page.registration_exists()