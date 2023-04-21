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

class Accordion(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    body_dropdown_btn_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    body_dropdown_btn_after_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    accordion_stripe_xpath = (By.XPATH, "//input[contains(@value, 'Add Accordion')]")
    accordion_stripe_heading_label_xpath = (By.XPATH,"//label[contains(@for, 'subform-field-title') and contains(@for, 'edit-field-body-0')]")
    accordion_stripe_heading_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-title') and contains(@id, 'edit-field-body-0')]")
    accordion_header_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'subform-field-title') and contains(@class, 'description') and contains(@id, 'edit-field-body-0')]")
    add_accordion_items_btn = (By.XPATH,"//input[contains(@id,'add-more-button-accordion-items') and contains(@id, 'edit-field-body-0')]")
    accordion_body_iframe_xpath = (By.XPATH, "(//iframe[contains(@title, 'Rich Text Editor, Accordion body field')])[1]")
    second_accordion_body_iframe_xpath = (By.XPATH, "(//iframe[contains(@title, 'Rich Text Editor, Accordion body field')])[2]")
    paragraph_css = (By.CSS_SELECTOR, "p")
    accordion_heading_text = "Sample Heading"
    accordion_title_text = "Sample Title"
    accordion_title_text2 = "Sample Title2"
    accordion_body_text = "Sample Body"
    accordion_body_text2 = "Sample Body2"
    accordion_title_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-accordion-title') and contains(@for, 'edit-field-body-0') and contains(@for, 'subform-field-accordion-item-0')]")
    accordion_title_input_xpath = (By.XPATH,"//input[contains(@id, 'subform-field-accordion-title') and contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-accordion-item-0')]")
    accordion_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'subform-field-accordion-title-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-accordion-item-0')]")
    accordion_body_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-accordion-body') and contains(@for, 'edit-field-body-0') and contains(@for, 'subform-field-accordion-item-0')]")

    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    accordion_stripe_value = "accordion"
    
    
    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def click_body_dropdown(self, body_dropdown_flag):

        if body_dropdown_flag == 0:
            BasePage.press_button(self, self.body_dropdown_btn_first_time_xpath)
        else:
            BasePage.press_button(self, self.body_dropdown_btn_after_first_time_xpath)


    def accordion_stripe(self):

        # BasePage.is_visible(self, self.accordion_xpath )
        # BasePage.select_dropdown_by_value(self, self.accordion_xpath ,'button')
        BasePage.press_button(self, self.accordion_stripe_xpath)


    def accordion_stripe_heading_ele(self,label_loc, input_loc, helper_text, heading_text):

        accordion_stripe_heading_title = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self, input_loc, heading_text)
        accordion_heading_helper_txt = BasePage.get_element_text(self,helper_text)
        return accordion_heading_helper_txt, accordion_stripe_heading_title


    
    def accordion_stripe_title_ele(self,label_loc, input_loc, helper_text,title_text):

        accordion_title = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, title_text)
        accordion_title_helper_txt = BasePage.get_element_text(self,helper_text)
        return accordion_title_helper_txt, accordion_title

    def accordion_body_ele(self,label_loc, iframe_xpath, body_text):

        accordion_body = self.get_element_text(label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css, body_text)
        self.driver.switch_to.default_content()
        return accordion_body

    def add_accordion_items(self,btn_loc):

        BasePage.press_button(self, btn_loc)
        

