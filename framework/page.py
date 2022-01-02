import os
import time
from framework import element
from framework.element import BasePageElement
from framework.locators import MainPageLocators
from framework.locators import SignupPageLocators
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, by, locator, data):
        element = self.driver.find_element(by, locator)
        element.send_keys(data)
    
    def click_on_element(self, by, locator):
        element = self.driver.find_element(by, locator)
        element.click()

class MainPage(BasePage):
    def registration_exists(self):
        try:
            self.driver.find_element(*MainPageLocators.REGISTER_BUTTON)
        except NoSuchElementException:
            return False
        return True

    def click_register_button(self):
        self.click_on_element(*MainPageLocators.REGISTER_BUTTON)
        return SignupPage(self.driver)

    def signout(self):
        self.click_on_element(*MainPageLocators.SIGNOUT)

    def get_signin_text(self):
        time.sleep(5) #I know ugly stuff.  Have to wait for the dom to load changes otherwise it's SIGN IN
        element = self.driver.find_element(*MainPageLocators.SIGNOUT)
        return element.text

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
        self.click_on_element(*SignupPageLocators.ACCEPT)

    def click_on_yes_investor(self):
        self.click_on_element(*SignupPageLocators.YES)

    def click_captcha(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((SignupPageLocators.CAPTCHA_FRAME[0],SignupPageLocators.CAPTCHA_FRAME[1])))
        wait.until(ec.element_to_be_clickable((SignupPageLocators.CAPTCHA_ID[0], SignupPageLocators.CAPTCHA_ID[1]))).click()

    def is_captcha_present(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(ec.presence_of_element_located((SignupPageLocators.CAPTCHA_OBJ[0],SignupPageLocators.CAPTCHA_OBJ[1]))) 
        except NoSuchElementException:
            return False
        return True

    def is_register_active(self):
        wait = WebDriverWait(self.driver, 100)
        self.driver.switch_to.default_content() #Python bug with losing content. 
        time.sleep(5) #Ugly but need to give the button time to switch to enanled.  So messy.
        element = wait.until(ec.presence_of_element_located((SignupPageLocators.REGISTRATION[0],SignupPageLocators.REGISTRATION[1]))) 
        return element.get_property('disabled') 

    def click_register(self):
        self.click_on_element(*SignupPageLocators.REGISTRATION)
        return MainPage(self.driver)