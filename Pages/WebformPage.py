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

class WebformPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    english_radio_button_css = (By.CSS_SELECTOR, "#edit-select-language-english")
    location_btn_css = (By.CSS_SELECTOR, "#select2-edit-select-by-location-container")
    location_labels_xpath = (By.XPATH, "//li[contains(@id,'select-by-location')]")
    country_specific_content_css = (By.CSS_SELECTOR,".country-specific-message > ul")
    france_radio_button_css = (By.CSS_SELECTOR,"#edit-select-language-franais")
    eng_title_css = (By.CSS_SELECTOR,".js-form-item-page-markup-en > h1")
    fr_title_css = (By.CSS_SELECTOR,".js-form-item-page-markup-fr > h1")
    image_css = (By.CSS_SELECTOR,".js-form-item-page-markup-en > img")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    search_input_footer_id = (By.ID, 'edit-keys')


    def filter_location(self):

        display_status_list = []
   
        self.press_button(self.location_btn_css)
        location_elements = self.driver.find_elements(self.location_labels_xpath[0], self.location_labels_xpath[1])
        
        for ele in location_elements:

            display_status_list.append(self.is_displayed_ele(ele))
        
        
        return display_status_list


    def location_content(self):

        content_status = False
        self.press_button(self.location_btn_css)
        if len(self.driver.find_elements(*self.location_labels_xpath)) == 0:
            self.press_button(self.location_btn_css)
        # location_elements = self.driver.find_elements(self.location_labels_xpath[0], self.location_labels_xpath[1])
        self.press_button(self.location_labels_xpath)
        # for ele in location_elements:
            # ele.click()
            # self.driver.execute_script("arguments[0].click()", ele)   
        content_status = self.is_displayed(self.country_specific_content_css)
            # break
        

        return content_status



