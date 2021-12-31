from element import BasePageElement
from locators import MainPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def click_register_button(self):
        element = self.driver.find_element(*MainPageLocators.REGISTER_BUTTON)
        element.click()

class SignupPage(BasePage):
       
