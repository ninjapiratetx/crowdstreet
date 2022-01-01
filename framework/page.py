import os
from framework.element import BasePageElement
from framework.locaters import MainPageLocators
from framework.locaters import SignupPageLocators
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, by, locator, data):
        element = self.driver.find_element(by, locator)
        element.send_keys(data)

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
        return SignupPage(self.driver)

class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        wait = WebDriverWait(driver, 100)
        wait.until(ec.visibility_of_element_located((SignupPageLocators.FIRST_NAME[0],SignupPageLocators.FIRST_NAME[1])))

    def enter_first_name(self, name):
        self.enter_text(*SignupPageLocators.FIRST_NAME, name)
    
    def enter_last_name(self, name):  
        self.enter_text(*SignupPageLocators.LAST_NAME, name)

    def enter_email_address(self, email):
        self.enter_text(*SignupPageLocators.EMAIL, email)

    def enter_password(self, password):
        self.enter_text(*SignupPageLocators.PASSWORD, password)
        self.enter_text(*SignupPageLocators.PASSWORD_CONFIRM, password)

    def click_on_accept(self):
        element = self.driver.find_element(*SignupPageLocators.ACCEPT)
        element.click()