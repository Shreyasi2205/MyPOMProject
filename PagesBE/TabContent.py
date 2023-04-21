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

class TabContent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    tab_content_xpath = (By.XPATH, "//input[contains(@value, 'Add Tab Content')]")
    tab_title_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-tab-items') and contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-tab-title')]")
    tab_title_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-tab-items') and contains(@for, 'edit-field-body-0') and contains(@for, 'subform-field-tab-title')]")
    tab_title_txt = "SAMPLE TAB TITLE"
    tab_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'subform-field-tab-items') and contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-tab-title') and contains(@class, 'description')]")
    tab_body_iframe_xpath = (By.XPATH, "(//iframe[contains(@title, 'Rich Text Editor, Tab body text content field')])[1]")
    tab_body_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-5-subform-field-tab-items-0') and contains(@for, 'tab-body-text-content-0-value')]")
    paragraph_tag_css = (By.CSS_SELECTOR, "p")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    tab_body_txt = "SAMPLE TAB BODY"
    tab_content_page_txt = "Novartis Facebook Community Guidelines (43276)" 
    tab_content_page_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-tab-items') and contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-content-page')]")
    tab_content_page_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-tab-items') and contains(@for, 'edit-field-body-0') and contains(@for, 'subform-field-content-page')]")
    stripe_value = "tab_content"
    auto_sugg_txt = "nov"

    def click_paragraph_dropdown(self,input_loc,value):
        
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):

        BasePage.press_button(self, btn_loc)

   
    def tab_title_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)
        label_txt = BasePage.get_element_text(self, label_loc)
        return helper_txt, label_txt

    def tab_desc_ele(self, label_loc, iframe_loc, txt):

        label_txt = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*iframe_loc))
        BasePage.press_button(self, self.paragraph_tag_css)
        BasePage.send_keys(self, self.paragraph_tag_css, txt)
        self.driver.switch_to.default_content()

        return label_txt

    def tab_content_page_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc):

        label_txt = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        content_txt = BasePage.get_elemet_attribute(self, input_loc, "value")

        return label_txt, content_txt