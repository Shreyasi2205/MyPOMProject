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




class InThisSection(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    in_this_section_xpath = (By.XPATH, "//input[contains(@value, 'In this section')]")
    title_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-body-0-subform-field-title-0')]")
    title_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-body-0-subform-field-title-0')]")
    title_helper_txt_xpath = (By.XPATH, "//div[contains(@id,'edit-field-body-0-subform-field-title-0') and contains(@class, 'desc')]")
    text_copy_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-body-0-subform-field-text-copy-0')]")
    text_copy_input_xapth = (By.XPATH,"//input[contains(@id,'edit-field-body-0-subform-field-text-copy-0')]")
    text_copy_helper_txt_xpath = (By.XPATH, "//div[contains(@id,'edit-field-body-0-subform-field-text-copy-0')and contains(@class, 'description')]")
    video_upload_xpath = (By.XPATH, "//input[contains(@id,'edit-field-body-0-subform-field-document-public') and contains(@id, 'open')]")
    video_dilog_css = (By.CSS_SELECTOR,"div.ui-dialog")
    video_edit_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'edit-button') and contains(@id, 'field-document')]")
    video_remove_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'remove-button') and contains(@id, 'field-document')]")
    video_data_css = (By.XPATH,"(//span[contains(@class,'field-content')]/img)[1]")
    video_submit_xpath = (By.XPATH,"//input[contains(@id,'edit-submit') and not(contains(@id, 'media'))]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@class, 'entity-browser-modal-iframe')]")
    btn_uri_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-button-0-uri') and contains(@for, 'edit-field-body-0') and contains(@for,'subform-field-link-buttons-0')]")
    btn_uri_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-button-0-uri') and contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-link-buttons-0')]")
    btn_link_text_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-button-0-title') and contains(@for, 'edit-field-body-0') and contains(@for,'subform-field-link-buttons-0')]")
    btn_link_text_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-button-0-title') and contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-link-buttons-0')]")
    url_open_in_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-link-open-in') and contains(@for, 'edit-field-body-0')]")
    url_open_in_input_xpath = (By.XPATH, "//select[contains(@id, 'subform-field-link-open-in') and contains(@id, 'edit-field-body-0')]")
    url_open_in_drp_dwn_value = "_self"
    add_btn_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-link-buttons-add-more-add-more-button-button') and contains(@id, 'edit-field-body-0')]")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    auto_sugg_txt = "novartis"
    stripe_value = "in_this_section"
    title_txt = "SAMPLE TITLE"
    text_copy_txt = "SAMPLE TEXT COPY"
    title_txt1 = "Novartis leadership"
    link_text1 = "Board of Directors"
    link_text2 = "Executive Committee"
    link_text3 = "Organizational structure"
    link_text4 = "Quality"
    link_text5 = "Novartis and the EU"

    def click_paragraph_dropdown(self,input_loc,value):
        
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):

        BasePage.press_button(self, btn_loc)


    def title_ele(self, input_loc, label_loc, helper_loc, txt):

        title = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        title_helper_txt = BasePage.get_element_text(self, helper_loc)
        return title_helper_txt, title


    def text_copy_ele(self, input_loc, label_loc, helper_loc, txt):

        text_copy = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        text_copy_helper_txt = BasePage.get_element_text(self, helper_loc)
        return text_copy_helper_txt, text_copy


    def video_upload_icon(self, upload_loc, edit_btn_loc, remove_btn_loc):

        BasePage.press_button(self, upload_loc)
        # BasePage.is_visible(self,self.video_dilog_css)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0 :
            BasePage.press_button(self, self.video_upload_xpath)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        BasePage.press_button(self, self.video_data_css)
        BasePage.press_button(self,self.video_submit_xpath)
        self.driver.switch_to.default_content()
        edit_btn_txt = BasePage.get_elemet_attribute(self, edit_btn_loc, "value")
        remove_btn_txt = BasePage.get_elemet_attribute(self, remove_btn_loc, "value")


        return edit_btn_txt, remove_btn_txt

    def btn_url_ele(self, input_loc, label_loc):

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

    def btn_link_text_ele(self, input_loc, label_loc, txt):

        link_text = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        return link_text

    def url_open_in(self,label,url_loc,url_open_in_drp_dwn_value):
        BasePage.select_dropdown_by_value(self, url_loc, url_open_in_drp_dwn_value)
        cta_url_open_in_label = BasePage.get_element_text(self, label)
        return cta_url_open_in_label

    def add_btn(self,btn_loc):

        BasePage.press_button(self, btn_loc)


