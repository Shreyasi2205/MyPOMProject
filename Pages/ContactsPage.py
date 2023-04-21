import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from Utilities.config import Utilities
import random

class ContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    contacts_href_xpath = (By.XPATH,"//a[contains(@class,'contacts')]")
    contacts_title_css = (By.CSS_SELECTOR,".title")
    first_col_css = (By.CSS_SELECTOR,".first-col")
    last_col_css = (By.CSS_SELECTOR,'.last-col')
    share_btn_css = (By.CSS_SELECTOR, ".addtoany_share")
    print_css = (By.CSS_SELECTOR, "li.print > a")
    save_css = (By.CSS_SELECTOR, "li.pdf > a")
    first_col_data_css = (By.CSS_SELECTOR,".first-col >p")
    last_col_data_css = (By.CSS_SELECTOR,'.last-col >p')
    

    def launch_contactsPage(self):

        self.press_button(self.contacts_href_xpath)


    def share_button(self):

        share_btn_status = self.is_displayed(self.share_btn_css)
        return share_btn_status

    def print_button(self):

        print_btn_status = self.is_displayed(self.print_css)
        return print_btn_status

    def save_button(self):

        save_btn_status = self.is_displayed(self.save_css)
        return save_btn_status

