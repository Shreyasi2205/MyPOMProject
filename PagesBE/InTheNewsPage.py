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

now = datetime.now()

class InTheNewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    news_page_xpath = (By.XPATH,"//li[contains(@class, 'clearfix')]/a[contains(@href, 'news_page')]")
    
    title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-title')]")
    title_label_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]/parent::div/label")
    
    title_description_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]/parent::div/div")

    add_news_page_xpath = (By.XPATH, "//a[contains(@href, 'external_news')]/span")
    title_chars_limit_txt_xpath = (By.XPATH, "//div[contains(@id, 'value--description') and contains(@id, 'edit-title')]")
    news_page = "Sample News Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    body_dropdown_content_css = (By.CSS_SELECTOR, "ul.dropbutton > li.dropbutton__item > input")
    error_msg_list = ["Header field is required.", "Searchable in section field is required."]
    searchable_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-section')]")
    searchable_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]/option")
    searchable_section_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]")
    iframe_body_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Body field')]")
    body_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-body-0-value')]")
    body_text = "news page"
    paragraph_css = (By.CSS_SELECTOR, "p")
    date_label_xpath = (By.XPATH,"//span[text()='Date']")
    url_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-link-0-uri')]")
    url_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-link-0-uri')]")
    link_text_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-link-0-title')]")
    link_text_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-link-0-title')]")
    link_helper_text_xpath = (By.XPATH, "//*[contains(text(),'This link title field is limited to 255 characters.')]")
    publish_xpath = (By.XPATH, "//select[contains(@id, 'edit-moderation-state')]")
    link_text = "novartis"
    link_text1 = "arctic"
    url_text = "https://www.gmail.com"
    url_text1 = "https://www.yahoo.com"
    add_another_item_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-link-add-more')]")
    language_label_xpath = (By.XPATH, "//label[contains(@for,'edit-langcode-0-value')]")
    language_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-langcode-0-value')]/option")
    language_input_xpath = (By.XPATH, "//select[contains(@id,'edit-langcode-0-value')]")
    save_btn_id = (By.CSS_SELECTOR, '[id="edit-submit"]')
    error_msg_css = (By.CSS_SELECTOR, ".messages__list > li")
    success_msg_css = (By.CSS_SELECTOR, ".alert.alert-dismissible")
    date_picker_xpath = (By.XPATH, "//input[contains(@id,'edit-field-date-0-value-date')]")
    time_field_xpath = (By.XPATH, "//input[contains(@id,'edit-field-date-0-value-time')]")
    date = now.strftime("%d/%M/%Y")
    time = now.strftime("%H:%M:%S")






    


    def click_news_page(self):

        BasePage.press_button(self, self.add_news_page_xpath)

    def title_ele(self):

        title_txt = BasePage.get_element_text(self, self.title_label_xpath)
        BasePage.send_keys(self, self.title_input_xpath, self.news_page)
        
        title_chars_limit_txt = BasePage.get_element_text(self, self.title_chars_limit_txt_xpath)

        return title_txt, title_chars_limit_txt

    
    def body_ele(self,label_loc, iframe_body_xpath, body_text):

        news_page_body = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*iframe_body_xpath))
        BasePage.send_keys(self, self.paragraph_css, body_text)
        self.driver.switch_to.default_content()
        return news_page_body

    def date_ele(self, label_loc, input_field,date):
        date_label = BasePage.get_element_text(self,label_loc)
        BasePage.do_click(self, input_field)
        BasePage.send_keys(self, input_field, date)
        return date_label

    def time_ele(self, label_loc, input_field,time):
        date_label = BasePage.get_element_text(self,label_loc)
        BasePage.do_click(self, input_field)
        BasePage.send_keys(self, input_field, time)
        return date_label



    def url_ele(self, label_loc, input_loc, url_text):
        label_name = BasePage.get_element_text(self, label_loc)
        BasePage.send_keys(self, input_loc, url_text)
        return label_name

    def link_ele(self, label_loc, input_loc, helper_text, link_text):
        label_name = BasePage.get_element_text(self, label_loc)
        guidance_text = BasePage.get_element_text(self, helper_text)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self, input_loc, link_text)
        return label_name , guidance_text

    

    def add_another_item(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def language_section_ele(self):
        label = BasePage.get_element_text(self,self.language_label_xpath)

        total_languages = len(self.driver.find_elements(*self.language_section_option_xpath))
        index_no = random.randint(1,total_languages-1)
        BasePage.select_dropdown_by_index(self, self.language_input_xpath, index_no)
        language_section_val = self.driver.find_elements(*self.language_section_option_xpath)[index_no].text
        return label, language_section_val
    


    def searchable_section_ele(self):
        label = BasePage.get_element_text(self,self.searchable_label_xpath)

        total_searchable_section = len(self.driver.find_elements(*self.searchable_section_option_xpath))

        index_no = random.randint(1,total_searchable_section-1)

        BasePage.select_dropdown_by_index(self, self.searchable_section_xpath, index_no)
        searchable_section_val = self.driver.find_elements(*self.searchable_section_option_xpath)[index_no].text
        return label, searchable_section_val

    

    def publish_ele(self):

        BasePage.select_dropdown_by_value(self, self.publish_xpath, "published")

    def save_btn_ele(self):

        BasePage.press_button(self, self.save_btn_id)
        # BasePage.press_button(self, self.save_btn_id)


    def error_msg_ele(self):

        error_msgs = []
        BasePage.press_button(self, self.save_btn_id)
        error_msg_contents = self.driver.find_elements(*self.error_msg_css)
        for err in error_msg_contents:
            error_msgs.append(err.text)

        return error_msgs


    def success_msg_ele(self):

        success_msg_txt = BasePage.get_element_text(self, self.success_msg_css)
        return success_msg_txt








