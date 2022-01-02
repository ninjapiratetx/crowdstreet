from selenium.webdriver.common.by import By

class MainPageLocators(object):
    REGISTER_BUTTON = (By.XPATH, '//*[@id="app-header"]/div[2]/div[1]/div[2]/div[3]/a[2]')
    SIGNOUT = (By.CLASS_NAME,'log-in-button')

    
class SignupPageLocators(object):
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    PASSWORD_CONFIRM = (By.ID, 'confirmPassword')
    ACCEPT = (By.ID, 'hasAgreedTos')
    YES = (By.ID, 'accreditedYes')
    CAPTCHA_OBJ = (By.ID, 'recaptcha-anchor-label')
    CAPTCHA_FRAME = (By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")
    CAPTCHA_ID = (By.XPATH, "//span[@id='recaptcha-anchor']")
    REGISTRATION = (By.XPATH, '*//button[@data-testid="submit-button"]')
