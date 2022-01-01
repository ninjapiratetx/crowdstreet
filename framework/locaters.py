from selenium.webdriver.common.by import By

class MainPageLocators(object):
    REGISTER_BUTTON = (By.XPATH, '//*[@id="app-header"]/div[2]/div[1]/div[2]/div[3]/a[2]')

class SignupPageLocators(object):
    FIRST_NAME = (By.ID,'firstName')
    LAST_NAME = (By.ID,'lastName')
    EMAIL = (By.ID,'email')
    PASSWORD = (By.ID,'password')
    PASSWORD_CONFIRM = (By.ID,'confirmPassword')
    ACCEPT = (By.ID,'hasAgreedTos')