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

class Reusable(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    content_link_txt = (By.CSS_SELECTOR,'.toolbar-icon-system-admin-content')
    contents_css = (By.CSS_SELECTOR, "ul.admin-list > li > a  > span")
    add_content_css = (By.CSS_SELECTOR, ".action-links > li > a")
    add_content_txt_css = (By.CSS_SELECTOR, "#block-seven-page-title > h1")

    def click_content(self,env):

        self.driver.get(env + "admin/content")
        self.driver.get(env + "admin/content")
        # BasePage.press_button(self, self.content_link_txt)

    def add_content(self):

        BasePage.press_button(self, self.add_content_css)

    def contents(self):
        content_list = []
        contents = self.driver.find_elements(*self.contents_css)

        for content in contents:
            content_list.append(content.text)

        return content_list



