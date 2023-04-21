import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException
from datetime import datetime
from Utilities.config import Utilities
import random
from datetime import date
from datetime import datetime, timedelta

class ParagraphLibraryBlockContent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    custom_block_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-paragraph-custom-block') and contains (@for, 'edit-field-body-0')]")
    custom_block_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-paragraph-custom-block') and contains (@id, 'edit-field-body-0')]")
    paragraph_drp_dwn_value = "paragraph_library_block_content"
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    auto_sugg_txt = "paragraph"



    
    def click_paragraph_dropdown(self,input_loc,value):
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):
        BasePage.press_button(self, btn_loc)

    def custom_block_content_ele(self, input_loc, label_loc):

        BasePage.send_keys(self, input_loc, self.auto_sugg_txt)
        self.driver.find_element(*input_loc).clear()
        BasePage.send_keys(self, input_loc, self.auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*self.auto_sugg_css)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt

    


    

    
    

    


    

    

    


    



    

    


