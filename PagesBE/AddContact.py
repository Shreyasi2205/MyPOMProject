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
import os

class AddContact(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    add_contact_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-actions-bundle')]")
    add_new_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-actions-ief-add')]")
    contact_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'field-title-0')]")
    second_contact_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-1') and contains(@id, 'field-title-0')]")
    contact_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-0') and contains(@for, 'field-title-0')]")
    second_contact_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-1') and contains(@for, 'field-title-0')]")
    contact_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-0') and contains(@id, 'field-title-0')]")
    second_contact_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-1') and contains(@id, 'field-title-0')]")
    name_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-name-0')]")
    second_name_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-name-0')]")
    name_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-0') and contains(@for, 'field-contacts-stripe-0') and contains(@for, 'subform-field-name-0')]")
    second_name_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-1') and contains(@for, 'field-contacts-stripe-0') and contains(@for, 'subform-field-name-0')]")
    name_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-0') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-name-0')]")
    second_name_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-name-0')]")
    subtitle_textarea_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-field-body-0') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-subtitle-0')]")
    second_subtitle_textarea_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-subtitle-0')]")
    subtitle_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-0') and contains(@for, 'field-contacts-stripe-0') and contains(@for, 'subform-field-subtitle-0')]")
    second_subtitle_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-1') and contains(@for, 'field-contacts-stripe-0') and contains(@for, 'subform-field-subtitle-0')]")
    phone_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-phone-0')]")
    second_phone_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-phone-0')]")
    phone_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-0') and contains(@for, 'field-contacts-stripe-0') and contains(@for, 'subform-field-phone-0')]")
    second_phone_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-1') and contains(@for, 'field-contacts-stripe-0') and contains(@for, 'subform-field-phone-0')]")
    phone_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-0') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-phone-0')]")
    second_phone_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-phone-0')]")
    email_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-email-0')]")
    second_email_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'subform-field-email-0')]")
    email_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-0') and contains(@for, 'field-contacts-stripe-0') and contains(@for, 'subform-field-email-0')]")
    second_email_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-1') and contains(@for, 'field-contacts-stripe-0') and contains(@for, 'subform-field-email-0')]")
    create_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'add-save') and contains(@id, 'body')]")
    image_summary_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-0') and contains(@id, 'contacts-stripe-0') and contains(@id, 'image-wrapper')]/details/summary")
    second_image_summary_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-1') and contains(@id, 'contacts-stripe-0') and contains(@id, 'image-wrapper')]/details/summary")
    select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'contacts-stripe-0') and contains(@id, 'field-image') and contains(@id, 'open-modal')]")
    second_select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-1') and contains(@id, 'contacts-stripe-0') and contains(@id, 'field-image') and contains(@id, 'open-modal')]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    upload_link_txt = (By.LINK_TEXT, "Upload")
    upload_img_xpath = (By.XPATH, "//input[contains(@id, 'edit-input-file')]")
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    img_remove_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'remove-button') and contains(@id, 'field-image')]")
    second_img_remove_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-1') and contains(@id, 'remove-button') and contains(@id, 'field-image')]")
    img_alt_xpath = (By.XPATH, "//input[contains(@id, 'alt')]")
    img_title_xpath = (By.XPATH, "//input[contains(@id, 'title')]")
    img_name_xpath = (By.XPATH, "//input[contains(@id, 'name')]")
    img_alt_label_xpath = (By.XPATH, "//label[contains(@for, 'alt')]")
    img_title_label_xpath = (By.XPATH, "//label[contains(@for, 'title')]")
    img_name_label_xpath = (By.XPATH, "//label[contains(@for, 'name')]")
    social_media_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'social-media-profiles-0')]")
    # second_social_media_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'social-media-profiles-1-subform')]")
    # third_social_media_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-1') and contains(@id, 'field-contacts-stripe-0') and contains(@id, 'social-media-profiles-2-subform')]")
    social_link_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-1-subform-field-contacts-stripe-0') and contains(@id, 'social-media-profiles-0') and contains(@id, 'uri')]")
    social_link_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-1-subform-field-contacts-stripe-0') and contains(@for, 'social-media-profiles-0') and contains(@for, 'uri')]")
    social_link_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-1-subform-field-contacts-stripe-0') and contains(@id, 'social-media-profiles-0') and contains(@id, 'uri')]")
    social_title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-1-subform-field-contacts-stripe-0') and contains(@id, 'social-media-profiles-0') and contains(@id, 'value')]")
    social_title_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-1-subform-field-contacts-stripe-0') and contains(@for, 'social-media-profiles-0') and contains(@for, 'value')]")
    social_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-body-1-subform-field-contacts-stripe-0') and contains(@id, 'social-media-profiles-0') and contains(@id, 'value')]")
    add_more_btn_social_link_xpath = (By.XPATH, "//input[contains(@id, 'add-more-button-social') and contains(@id, 'edit-field-body-1-subform-field-contacts-stripe-0')]")

    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    contacts_stripe_value = "contacts"
    
    twitter_val = "Twitter"
    twitter_link = "https://www.twitter.com/"
    instagram_val = "Instagram"
    instagram_link = "https://www.instagram.com/"
    fb_val = "Facebook"
    facebook_link = "https://www.facebook.com/"
    contact_input_data = "SAMPLE CONTACT FIRST"
    second_contact_input_data = "SAMPLE CONTACT SECOND"
    img_alt_txt = "IMAGE ALT TEXT"
    img_title_txt = "IMAGE TITLE TEXT"
    img_name_txt = "IMAGE NAME TEXT"
    email_input_data = "demo@sample.com"
    second_email_input_data = "second_demo@sample.com"
    phone_input_data = "+918789098789"
    second_phone_input_data = "+918789098785"
    subtitle_data = "SAMPLE SUBTITLE FIRST"
    second_subtitle_data = "SAMPLE SUBTITLE SECOND"
    name_input_data = "SAMPLE CONTACT NAME FIRST"
    second_name_input_data = "SAMPLE CONTACT NAME SECOND"
    

    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def add_contact_ele(self):

        BasePage.is_visible(self, self.add_contact_xpath)
        BasePage.select_dropdown_by_value(self, self.add_contact_xpath[1], "contacts", self.add_contact_xpath[0])
        BasePage.press_button(self, self.add_new_paragraph_btn_xpath)

    def contacts_input_ele(self, input_loc, data, helper_txt_loc, label_loc):

        BasePage.send_keys(self, input_loc, data)
        contact_helper_txt = BasePage.get_element_text(self, helper_txt_loc)
        contact_label = BasePage.get_element_text(self, label_loc)

        return contact_helper_txt, contact_label

    
    def name_input_ele(self, input_loc, data, helper_txt_loc, label_loc):

        BasePage.send_keys(self, input_loc, data)
        name_helper_txt = BasePage.get_element_text(self, helper_txt_loc)
        name_label = BasePage.get_element_text(self, label_loc)

        return name_helper_txt, name_label

    def subtitle_ele(self, textarea_loc, data, label_loc):

        BasePage.press_button(self, textarea_loc)
        BasePage.send_keys(self, textarea_loc, data)
        subtitle_label = BasePage.get_element_text(self, label_loc)

        return subtitle_label

    def phone_ele(self, input_loc, data, helper_txt_loc, label_loc):

        BasePage.send_keys(self, input_loc, data)
        phone_helper_txt = BasePage.get_element_text(self, helper_txt_loc)
        phone_label = BasePage.get_element_text(self, label_loc)

        return phone_helper_txt, phone_label

    def email_ele(self, input_loc, data, label_loc):

        BasePage.send_keys(self, input_loc, data)
        email_label = BasePage.get_element_text(self, label_loc)

        return email_label

    def create_contact(self):

        BasePage.press_button(self, self.create_paragraph_btn_xpath)

    def add_drupal_image_ele(self, img_loc, select_img_loc):

        BasePage.press_button(self, img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        BasePage.is_visible(self, self.first_img_remove_btn_xpath)

    def add_local_image_ele(self, img_loc, select_img_loc):

        BasePage.press_button(self, img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        BasePage.press_button(self, self.upload_link_txt)
        BasePage.send_keys(self, self.upload_img_xpath, os.getcwd() + "//sample_image.jpeg")
        BasePage.send_keys(self, self.img_alt_xpath, self.img_alt_txt)
        alt_label = BasePage.get_element_text(self, self.img_alt_label_xpath)
        BasePage.send_keys(self, self.img_title_xpath, self.img_title_txt)
        title_label = BasePage.get_element_text(self, self.img_title_label_xpath)
        BasePage.send_keys(self, self.img_name_xpath, self.img_name_txt)
        name_label = BasePage.get_element_text(self, self.img_name_label_xpath)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        BasePage.is_visible(self, self.second_img_remove_btn_xpath)

        return alt_label, title_label, name_label

    def social_media_ele(self, select_loc, social_link_input_loc, social_link_label_loc, social_title_input_loc, social_title_label_loc, social_title_helper_loc, social_link_txt, value):

        BasePage.select_dropdown_by_value(self, select_loc, value)
        BasePage.send_keys(self, social_link_input_loc, social_link_txt)
        BasePage.send_keys(self, social_title_input_loc, value)
        social_link_label_txt = BasePage.get_element_text(self, social_link_label_loc)
        social_title_label_txt = BasePage.get_element_text(self, social_title_label_loc)
        social_title_helper_txt = BasePage.get_element_text(self, social_title_helper_loc)

        return social_link_label_txt, social_title_label_txt, social_title_helper_txt

    def add_more_social_icon(self):
        BasePage.press_button(self, self.add_more_btn_social_link_xpath)
        # BasePage.select_dropdown_by_value(self, self.second_social_media_xpath, self.instagram_val)
        # BasePage.press_button(self, self.add_more_btn_social_link_xpath)
        # BasePage.select_dropdown_by_value(self, self.third_social_media_xpath, self.fb_val)
