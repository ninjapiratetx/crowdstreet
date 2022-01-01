import os
from random_number import generate_random_number

PASSWORD_OS = "PASSWORD"

class SignupPageDefault(object):
    FIRST_NAME = "test"
    LAST_NAME = "test"
    EMAIL = f"ninjapiratetx+{generate_random_number()}@gmail.com"
    PASSWORD = os.environ[PASSWORD_OS]
    SECOND_PASSWORD = os.environ[PASSWORD_OS]

