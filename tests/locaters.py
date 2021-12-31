from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    REGISTER_BUTTON = (By.XPATH, '//*[@id="app-header"]/div[2]/div[1]/div[2]/div[3]/a[2]')