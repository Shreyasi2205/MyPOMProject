import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from datetime import datetime
from Utilities.config import Utilities
import random
from datetime import date
from datetime import datetime, timedelta
import os

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    cookie_id = (By.ID, "onetrust-accept-btn-handler")


    def login(self):
        
        username= os.environ.get("username")
        password = os.environ.get("password")
        print(username)
        print(password)

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

        self.send_keys((By.ID, "edit-name"), username)
        self.send_keys((By.ID, "edit-pass"), password)
        self.press_button((By.ID, "edit-submit"))