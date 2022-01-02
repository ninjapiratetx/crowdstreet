import os
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
        #found hack here: https://stackoverflow.com/questions/53917157/find-the-recaptcha-element-and-click-on-it-python-selenium
        WebDriverWait(self.driver, 10).until(ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
