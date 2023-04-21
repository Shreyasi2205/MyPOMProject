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

class BiographyTeaser(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    paragraph_dropdown_btn_second_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")    
    add_another_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button') and contains (@value, 'Add another Paragraph')]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    remove_btn_xpath = (By.XPATH, "//input[contains(@value, 'Remove') and contains (@id,'top-links-remove-button') and contains (@name, 'field_body_0_remove') and contains (@id, 'edit-field-body-0')]")
    #biography_teaser_image_css = (By.CSS_SELECTOR,"span.summary")
    biography_teaser_image_css = (By.XPATH, "//div[contains  (@id, 'subform-field-image-wrapper') and contains (@id, 'edit-field-body-0') ]/details/summary")
    image_layout_title_xpath = (By.XPATH, "//label[contains(@for, 'image-layout') and contains(@for, 'edit-field-body-0')]")
    image_layout_input_xpath = (By.XPATH, "//select[contains(@id, 'image-layout') and contains(@id, 'edit-field-body-0')]")
    biography_teaser_image_xpath = (By.XPATH, "//div[contains(@id, 'image-wrapper') and contains (@id, 'edit-field-body-0')]/details/summary")
    biography_teaser_select_image_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-image') and contains(@id, 'open-modal') and contains(@id, 'edit-field-body-0')]")
    name_label_xpath = (By.XPATH,"//label[contains(@for, 'subform-field-bio-name') and contains(@for, 'edit-field-body-0')]")
    name_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-bio-name') and contains(@id, 'edit-field-body-0')]")
    name_helper_text_xpath = (By.XPATH,"//div[contains(@id, 'subform-field-bio-name') and contains(@id, 'edit-field-body-0') and contains(@class,'description')]")
    title_label_xpath = (By.XPATH,"//label[contains(@for, 'subform-field-bio-title') and contains(@for, 'edit-field-body-0')]")
    title_input_xpath = (By.XPATH,"//input[contains(@id, 'subform-field-bio-title') and contains(@id, 'edit-field-body-0')]")
    title_helper_text_xpath = (By.XPATH,"//div[contains(@id, 'subform-field-bio-title') and contains(@id, 'edit-field-body-0') and contains(@class,'description')]")
    desc_label_xpath = (By.XPATH,"//label[contains(@for, 'subform-field-bio-short-description') and contains (@for, 'edit-field-body-0')]")
    desc_input_xpath = (By.XPATH,"//textarea[contains(@id, 'subform-field-bio-short-description') and contains (@id, 'edit-field-body-0')]")
    media_type_label_xpath = (By.XPATH, "//label[contains(@for, 'social-media') and contains (@for, 'edit-field-body-0')]")
    media_type_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-0') and contains (@id, 'subform-field-media-links') and contains (@id, 'social-media')]")
    social_link_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-social-link') and contains (@for, 'edit-field-body-0')]")
    social_link_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-social-link') and contains (@id, 'edit-field-body-0')]")
    social_title_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-social-title') and contains (@for, 'edit-field-body-0')]")
    social_title_input_xpath = (By.XPATH , "//input[contains(@id, 'subform-field-social-title') and contains (@id, 'edit-field-body-0')]")
    social_title_helper_text_xpath = (By.XPATH, "//div[contains(@id, 'subform-field-social-title') and contains(@id, 'edit-field-body-0') and contains(@class,'description')]")
    name_text = "Sample Name"
    name_text2 = "Sample Name2"
    title_text = "Sample Title"
    title_text2 = "Sample Title2"
    body_text = "Sample Body"
    body_text2 = "Sample Body2"
    social_link = "https://gmail.com"
    social_link2 = "https://yahoo.com"
    social_title_text = "Sample Social Text"
    social_title_text2 = "Sample Social Text2"
    paragraph_drp_dwn_value = 'biography'
    image_layout_drp_dwn_value = 'image_left'
    image_layout_drp_dwn_second_value = 'image_right'
    media_type_drp_dwn_value = 'Facebook'
    media_type_drp_dwn_value2 =  'Instagram'


    
    def click_paragraph_dropdown(self,input_loc,value):
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):
        BasePage.press_button(self, btn_loc)

    def add_image_ele(self,label_loc, input_loc, image_frame, img_input, submit_btn, remove_btn_loc):
        # Adding Image
        BasePage.press_button(self,label_loc)
        BasePage.press_button(self, input_loc)
        if len(self.driver.find_elements(*image_frame)) == 0:
            BasePage.press_button(self, input_loc)
        self.driver.switch_to.frame(self.driver.find_element(*image_frame))
        BasePage.press_button(self, img_input)
        BasePage.press_button(self, submit_btn)
        self.driver.switch_to.default_content()
        remove_btn = BasePage.is_visible(self, remove_btn_loc)
        return remove_btn


    def image_layout_dropdown(self, label_loc,input_loc,image_layout_drp_dwn_value):

        image_layout_label = self.get_element_text(label_loc)
        BasePage.select_dropdown_by_value(self, input_loc, image_layout_drp_dwn_value)
        return image_layout_label

    
    def name_ele(self,label_loc, input_loc, helper_text,name_text):

        biography_name = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, name_text)
        biography_name_helper_text = BasePage.get_element_text(self,helper_text)
        return biography_name_helper_text, biography_name

    def title_ele(self,label_loc, input_loc, helper_text,title_text):

        biography_title = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, title_text)
        biography_title_helper_text = BasePage.get_element_text(self,helper_text)
        return biography_title_helper_text, biography_title


    def desc_ele(self,label_loc,input_loc,body_text):
        biography_desc = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, body_text)
        return biography_desc

    def media_type_dropdown(self,label_loc, input_loc,media_type_value):
        biography_media_type_label = self.get_element_text(label_loc)
        BasePage.select_dropdown_by_value(self,input_loc, media_type_value)
        return biography_media_type_label

    def social_link_ele(self,label_loc,input_loc,social_link):
        biography_social_link = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,social_link )
        return biography_social_link

    def social_title_ele(self,label_loc, input_loc, helper_text, social_title_text):
        biography_social_title = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, social_title_text)
        biography_social_title_helper_text = BasePage.get_element_text(self,helper_text)
        return biography_social_title_helper_text,biography_social_title

    



    

    


