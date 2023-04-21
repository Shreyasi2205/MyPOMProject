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

class InteriorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    novartis_commitment_xpath = (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'commitment')]")
    mega_menu_patient_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/patients') and not(contains(@target,'_self'))]")
    mega_menu_patient_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/patients') and not(contains(@target,'_self'))]//parent::li/p[@class='we-icon']")
    mega_menu_about_arrow_xpath = (By.XPATH, "//li[contains(@class, 'dropdown-menu')]/a[contains(@href, 'about')  and not(contains(@href,'about/'))]//parent::li/p")
    mega_menu_about_xpath = (By.XPATH, "//li[contains(@class, 'dropdown-menu')]/a[contains(@href, '/about') and not(contains(@href,'about/'))]")
    strategy_xpath = (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'/strategy') and not(contains(@href,'strategy/'))]")
    share_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(2)")
    print_save_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(1)")
    anchor_tag_css = (By.CSS_SELECTOR,'a')
    share_btn_css = (By.CSS_SELECTOR, ".addtoany_share")
    print_css = (By.CSS_SELECTOR, "div.content > ul >li.print > a")
    save_css = (By.CSS_SELECTOR, "div.content > ul >li.pdf > a")
    

    def launch_novartis_commitment(self,env_name):

        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_patient_arrow_xpath)
            else:
                self.move_to_element(self.mega_menu_patient_xpath)

            self.press_button(self.novartis_commitment_xpath)
        except:
            menu = Utilities.multi_language[env_name]['patients']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['commitment']
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))


    def launch_strategy(self,env_name):

        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_about_arrow_xpath)
            else:
               self.move_to_element(self.mega_menu_about_xpath)

            self.press_button(self.strategy_xpath)
        except:
            menu = Utilities.multi_language[env_name]['about']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['strategy']
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))


    def print_block_ele(self):       

        print_block = len(self.driver.find_elements(*self.print_css))
        
        return print_block


    def share_block_ele(self):

        share_block = len(self.driver.find_elements(*self.share_btn_css))

        return share_block

    def save_block_ele(self):

        save_block = len(self.driver.find_elements(*self.save_css))

        return save_block

    def print_share_misalignment(self):

        share_block = self.get_elemet_attribute(self.share_block_css, "id")
        print_save_block = self.get_elemet_attribute(self.print_save_block_css, "id")

        return share_block, print_save_block