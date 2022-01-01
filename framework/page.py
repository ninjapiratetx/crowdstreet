from element import BasePageElement
from framework.locators import MainPageLocators
from framework.locaters import SignupPageLocators
from default import SignupPageDefault
from selenium.common.exceptions import NoSuchElementException        

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def registration_exists(self):
        try:
            self.driver.find_element(*MainPageLocators.REGISTER_BUTTON)
        except NoSuchElementException:
            return False
        return True

    def click_register_button(self):
        register = self.driver.find_element(*MainPageLocators.REGISTER_BUTTON)
        register.click()
        return SignupPage(*SignupPageDefault.FIRST_NAME)

class SignupPage(BasePage):
    def enter_first_name(self, name):
        first_name = self.driver.find_eleemnt(*SignupPageLocators.FIRST_NAME)
        first_name.send_keys()
    
    def enter_last_name(self, name)  
        pass 
