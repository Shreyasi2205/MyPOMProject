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

class AddCallToAction(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    
    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    cta_title_text_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-cta-title') and contains(@for, 'edit-field-body-0')]")
    cta_title_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-cta-title') and contains(@id, 'edit-field-body-0')]")
    cta_helper_text_title_xpath = (By.XPATH, "//div[contains(@id, 'cta-title') and contains(@class, 'description') and contains (@id, 'edit-field-body-0')]")
    cta_desc_label_xpath = (By.XPATH,"//label[contains(@for, 'subform-field-cta-description') and contains(@for, 'edit-field-body-0')]")
    cta_desc_iframe_xpath = (By.XPATH, "(//iframe[contains(@title, 'Rich Text Editor, CTA Description field')])[1]")
    
    cta_desc_news_interior_iframe_xpath=(By.XPATH,"//div[contains(@id,'cke_edit-field-body-0')] /div/div/iframe[@title='Rich Text Editor, CTA Description field']")

    cta_desc_second_iframe_xpath = (By.XPATH, "(//iframe[contains(@title, 'Rich Text Editor, CTA Description field')])[2]")
    paragraph_css = (By.CSS_SELECTOR, "p")
    cta_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-call-text') and contains(@for, 'edit-field-body-0')]")
    cta_label_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-call-text') and contains(@id, 'edit-field-body-0')]")
    cta_label_helper_text_xpath = (By.XPATH, "//div[contains(@id, 'call-text') and contains(@class, 'description') and contains (@id, 'edit-field-body-0')]")
    cta_url_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-url') and contains (@for, 'edit-field-body-0')]")
    cta_url_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-url') and contains (@id, 'edit-field-body-0')]")
    cta_url_open_in_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-link-open-in') and contains (@for, 'edit-field-body-0')]")
    cta_url_open_in_input_xpath = (By.XPATH, "//select[contains(@id, 'subform-field-link-open-in') and contains(@id, 'edit-field-body-0')]")
    cta_title_text = "Sample Title 1"
    cta_title_text_two = "Sample Title 2"
    cta_desc_text = "Sample Description 1"
    cta_desc_text_two = "Sample Description 2"
    cta_label_text = "Sample label 1"
    cta_label_text_two = "Sample label 2"
    url_text  = "https://gmail.com"
    url_open_in_drp_dwn_value = "_self"
    url_open_in_drp_dwn_value_two = "_blank"
    paragraph_dropdown_value = "call_to_action"
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    auto_sugg_txt = "novartis"

    cta_title_actual_text = "Ukraine response"
    cta_desc_actual_text = "Novartis resumes business in Ukraine"
    

    

    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)
        
             
    '''def call_to_action_stripe(self):
        BasePage.press_button(self, self.call_to_action_stripe_xpath)'''

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)
        

    def cta_stripe_title_ele(self,label_loc, input_loc, helper_text,title_text):

        cta_title = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, title_text)
        cta_title_helper_text = BasePage.get_element_text(self,helper_text)
        return cta_title_helper_text, cta_title


    def cta_stripe_desc_ele(self,label_loc, iframe_xpath, body_text):
        cta_body = self.get_element_text(label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css, body_text)
        self.driver.switch_to.default_content()
        return cta_body

    def cta_label_ele(self,label_loc,input_loc,helper_txt,label_text):

        cta_label = self.get_element_text(label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc,label_text )
        cta_label_helper_text = BasePage.get_element_text(self,helper_txt)
        return cta_label_helper_text, cta_label


    def cta_url_ele(self, input_loc, label_loc):

        BasePage.send_keys(self, input_loc, self.auto_sugg_txt)
        self.driver.find_element(*input_loc).clear()
        BasePage.send_keys(self, input_loc, self.auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*self.auto_sugg_css)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        sugg_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        label_txt = BasePage.get_element_text(self, label_loc)
        return sugg_txt, label_txt

    def cta_url_open_in(self,label,url_loc,url_open_in_drp_dwn_value):
        BasePage.select_dropdown_by_value(self, url_loc, url_open_in_drp_dwn_value)
        cta_url_open_in_label = BasePage.get_element_text(self, label)
        return cta_url_open_in_label




    

    

    

    
        



