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

class BiographyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    biography_page_xpath = (By.XPATH, "//li[contains(@class, 'clearfix')]/a[contains(@href, 'biography_page')]")
    title_label_xpath = (By.XPATH,"//label[contains(@for,'edit-title')]")
    title_input_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]")
    title_description_xpath = (By.XPATH,"//div[contains(@id,'edit-title') and contains(@class,'description')]")
    intro_text_label_xpath = (By.XPATH,"//label[contains(@for,'intro-text')]")
    page_main_category_label_xpath = (By.XPATH,"//*[@id='edit-field-category']/parent::div/label")
    page_main_category_xpath = (By.XPATH,"//*[@id='edit-field-category']")
    page_main_sub_category_label_xpath = (By.XPATH,"//*[@id='edit-field-sub-category']/parent::div/label")
    page_maib_sub_category_xpath = (By.XPATH,"//*[@id='edit-field-sub-category']")
    name_label_xpath=(By.XPATH,"//label[contains(@for,'bio-person-name')]")
    name_css = (By.CSS_SELECTOR,"#edit-field-bio-person-name-0-value")
    title2_label_xpath = (By.XPATH,"//label[contains(@for,'bio-person-title')]")
    title2_xpath = (By.CSS_SELECTOR,"#edit-field-bio-person-title-0-value")
    frame_xpath = (By.XPATH,"(//iframe[contains(@title,'Rich Text Editor, Intro text  field')])[1]")
    text_css = (By.CSS_SELECTOR,'body p')
    image_xpath = (By.XPATH,"//details[@id='edit-field-bio-image']/summary")
    select_image_xpath = (By.XPATH,"//input[contains(@id, 'bio-image') and contains(@id, 'open-modal')]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    remove_button_xpath = (By.XPATH,"//input[contains(@id,'remove-button') and contains(@id,'edit-field-bio-image')]")
    language_dropdown_xpath = (By.XPATH,"//select[contains(@id,'edit-lang')]/option[@selected='selected']")
    language_label_xpath = (By.XPATH,"//label[contains(@for,'langcode')]")
    body_stripe_num_xpath = (By.XPATH,"//select[contains(@id,'bio-body')]/option")
    searchable_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]/option")
    searchable_section_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]")
    legend_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Legend field')]")
    paragraph_css = (By.CSS_SELECTOR, "p")
    disclaimer_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Disclaimer field')]")
    searchable_section_label_xpath = (By.XPATH,"//label[contains(@for,'field-section')]")
    legend_label_xpath = (By.XPATH,"//label[contains(@for,'field-legend')]")
    disclaimer_label_xpath = (By.XPATH,"//label[contains(@for,'field-disclaimer')]")

    biography_page_txt = "Sample Biography Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    biography_page_intro_txt = "biographyPage_intro_text"
    biography_page_name_txt = "biographyPage_name"
    biography_page_title2_txt = "biographyPage_title2"
    legend_txt = "SAMPLE LEGEND TEXT"
    disclaimer_txt = "SAMPLE DISCLAIMER TEXT"

    
    def click_biography_page(self):

        BasePage.press_button(self, self.biography_page_xpath)


    def title_ele(self):

        title_txt = BasePage.get_element_text(self, self.title_label_xpath)
        BasePage.send_keys(self, self.title_input_xpath, self.biography_page_txt)
        title_helper_txt = BasePage.get_element_text(self, self.title_description_xpath)

        return title_txt, title_helper_txt



    def intro_text_ele(self):

        self.driver.switch_to.frame(self.driver.find_element(*self.frame_xpath))
        BasePage.press_button(self, self.text_css)
        BasePage.send_keys(self,self.text_css,self.biography_page_intro_txt)
        self.driver.switch_to.default_content()
        intro_label_txt = self.get_element_text(self.intro_text_label_xpath)

        return intro_label_txt


    def name_ele(self):

        name_txt =self.get_element_text(self.name_label_xpath)
        self.send_keys(self.name_css,self.biography_page_name_txt)

        return name_txt


    def title2_ele(self):

        title2_txt = self.get_element_text(self.title2_label_xpath)
        self.send_keys(self.title2_xpath,self.biography_page_title2_txt)

        return title2_txt

    def image_ele(self):

        BasePage.press_button(self,self.image_xpath)
        BasePage.press_button(self, self.select_image_xpath)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, self.select_image_xpath)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        remove_btn_txt  = self.get_elemet_attribute(self.remove_button_xpath,'value')

        return remove_btn_txt


    def language_dropdown_ele(self):

        lang_label = self.get_element_text(self.language_label_xpath)
        default_lang = self.get_element_text(self.language_dropdown_xpath)

        return lang_label, default_lang 


    def stripe_validation(self):

       body_stripe_count = len(self.driver.find_elements(*self.body_stripe_num_xpath))
       
       return body_stripe_count


    def searchable_section_ele(self):

        
        total_searchable_section = len(self.driver.find_elements(*self.searchable_section_option_xpath))
        index_no = random.randint(1,total_searchable_section-1)
        BasePage.select_dropdown_by_index(self, self.searchable_section_xpath, index_no)
        searchable_txt = self.driver.find_elements(*self.searchable_section_option_xpath)[index_no].text
        label_txt = BasePage.get_element_text(self, self.searchable_section_label_xpath)

        return label_txt, searchable_txt


    def legend_ele(self):

        self.driver.switch_to.frame(self.driver.find_element(*self.legend_iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css,self.legend_txt )
        self.driver.switch_to.default_content()
        label_txt = BasePage.get_element_text(self, self.legend_label_xpath)

        return label_txt

    def disclaimer_ele(self):

        self.driver.switch_to.frame(self.driver.find_element(*self.disclaimer_iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css,self.disclaimer_txt )
        self.driver.switch_to.default_content()
        label_txt = BasePage.get_element_text(self, self.disclaimer_label_xpath)

        return label_txt





    
