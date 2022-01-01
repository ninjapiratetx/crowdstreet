import os
from framework.element import BasePageElement
from framework.locaters import MainPageLocators
from framework.locaters import SignupPageLocators
from selenium.common.exceptions import NoSuchElementException        

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, data):
        element = self.driver.find_eleemnt(locator)
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
    def enter_first_name(self, name):
        self.enter_text(*SignupPageLocators.FIRST_NAME, name)
    
    def enter_last_name(self, name):  
        self.enter_texr(*SignupPageLocators.LAST_NAME, name)

    def enter_email_address(self, email) 
        self.enter_texr(*SignupPageLocators.EMAIL, email)

    def enter_password(self, password):
        self.enter_texr(*SignupPageLocators.PASSWORD password)
        self.enter_texr(*SignupPageLocators.PASSWORD_CONFIRM, password)

    def click_on_accept(self):
        element = self.driver.find_eleemnt(*SignupPageLocators.ACCEPT)
        element.click()