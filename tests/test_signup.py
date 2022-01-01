import pytest
import tests.page
from selenium import webdriver

TEST_SERVER = "https://test.crowdstreet.com/"

@pytest.fixture
def chrome_driver(): 
   driver = webdriver.Chrome()
   self.driver.get(TEST_SERVER)
   yield driver

def test_registration_asked(chrome_driver):
    driver = chrome_driver
    main_page = page.MainPage(driver)
    assert main_page.registration_exists()