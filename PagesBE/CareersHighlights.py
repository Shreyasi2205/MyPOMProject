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
from selenium.webdriver.support.ui import Select


class CareersHighlights(BasePage):

    def __init__(self, driver):
        super().__init__(driver)



    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    careers_image_xpath = (By.XPATH,"(//summary[contains(@aria-controls,'edit-field-image')])[2]")
    careers_select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'field-image') and contains(@id, 'open-modal')]")
    image_iframe_xpath = (By.XPATH, "(//iframe[contains(@id, 'entity_browser_iframe_image_browser')])[1]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    careers_remove_button_xpath = (By.XPATH,"//input[contains(@id, 'image') and contains(@id, 'remove-button') and contains(@id, 'edit-field-body-0')]")
    careers_title_xpath = (By.XPATH, "//label[contains(@for, 'job-title') and contains(@for, 'edit-field-body-0')]")
    careers_title_input_xpath = (By.XPATH, "//input[contains(@id, 'job-title') and contains(@id, 'edit-field-body-0')]")
    careers_helper_text_title_xpath = (By.XPATH, "//div[contains(@id, 'job-title') and contains(@class, 'description') and contains (@id, 'edit-field-body-0')]")
    number_of_jobs_xpath = (By.XPATH,"//input[contains(@id,'number-of-jobs')]")
    number_of_jobs_label_xpath = (By.XPATH,"//label[contains(@for,'number-of-jobs')]")
    careers_intro_txt_xpath = (By.XPATH, "//label[contains(@for, 'field-quote-text') and contains(@for, 'edit-field-body-0')]")
    careers_intro_txt_input_xpath = (By.XPATH, "//input[contains(@id, 'field-quote-text') and contains(@id, 'edit-field-body-0')]")
    careers_intro_txt_helper_text_xpath = (By.XPATH, "//div[contains(@id, 'field-quote-text') and contains(@class, 'description') and contains (@id, 'edit-field-body-0')]")
    cta_url_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-url') and contains (@for, 'edit-field-body-0')and not(contains(@for,'title'))]")
    cta_url_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-url') and contains (@id, 'edit-field-body-0') and not(contains(@id,'title'))] ")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    link_txt_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-url') and contains (@for, 'edit-field-body-0')and contains(@for,'title')]")
    link_txt_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-url') and contains (@id, 'edit-field-body-0') and contains(@id,'title')] ")
    division_xpath = (By.XPATH,"//label[contains(@for, 'field-division') and contains (@for, 'edit-field-body-0')]")
    division_input_xpath = (By.XPATH,"//select[contains(@id, 'field-division') and contains(@id,'edit-field-body-0')]")
    function_xpath = (By.XPATH,"//label[contains(@for, 'field-function') and contains (@for, 'edit-field-body-0')]")
    function_input_xpath = (By.XPATH,"//select[contains(@id, 'field-function') and contains(@id,'edit-field-body-0')]")
    location_xpath = (By.XPATH,"//label[contains(@for, 'field-location') and contains (@for, 'edit-field-body-0')]")
    location_input_xpath = (By.XPATH,"//select[contains(@id, 'field-location') and contains(@id,'edit-field-body-0')]")
    job_tags_xpath = (By.XPATH,"//label[contains(@for, 'field-job-tags') and contains (@for, 'edit-field-body-0')]")
    job_tags_input_xpath = (By.XPATH,"//select[contains(@id, 'field-job-tags') and contains(@id,'edit-field-body-0')]")
    job_tags_opt_xpath = (By.XPATH,"(//optgroup[@label='Division']/option[@value='4136'])[1]")
    
    

    careers_title_text = "Sample careers title"
    careers_intro_txt_text = "Sample careers intro text"
    cta_auto_sugg_txt = "nov"
    stripe_value = "careers_highlights"
    job_tags_value = "Global Drug Development"
    link_text = "Sample link text"
    division_value = "Global Drug Development"
    function_first_value = "1"
    function_value = "Research & Development"
    location_first_value = "1"
    location_value = "Ireland"


    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)
    

    def add_image(self,quote_img_loc,select_img_loc,img_iframe_loc,img_loc,submit_loc,remove_btn):

        BasePage.press_button(self, quote_img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*img_iframe_loc)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*img_iframe_loc))
        BasePage.press_button(self, img_loc)
        BasePage.press_button(self, submit_loc)
        self.driver.switch_to.default_content()
        BasePage.is_visible(self,remove_btn)
        remove_button = BasePage.get_elemet_attribute(self, remove_btn,'value')

        return remove_button


    def careers_title_ele(self,label_loc, input_loc, helper_text,title_text):

        careers_title = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, title_text)
        careers_title_helper_text = BasePage.get_element_text(self,helper_text)
        return careers_title , careers_title_helper_text


    def click_no_of_jobs(self,label_loc,no_of_jobs_loc):

        no_of_jobs_title = self.get_element_text(label_loc)
        BasePage.press_button(self, no_of_jobs_loc)
        min_value = int(BasePage.get_elemet_attribute(self,no_of_jobs_loc,'min'))
        max_value = int(BasePage.get_elemet_attribute(self,no_of_jobs_loc,'max'))
        num = random.randint(min_value,max_value)
        BasePage.send_keys(self, no_of_jobs_loc, num)

        return no_of_jobs_title , min_value , max_value


    def careers_intro_text_ele(self,label_loc, input_loc, helper_text,intro_txt):

        careers_intro_txt = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, intro_txt)
        careers_intro_txt_helper_text = BasePage.get_element_text(self,helper_text)
        return careers_intro_txt , careers_intro_txt_helper_text


    def cta_url_ele(self, input_loc, label_loc,auto_sugg_loc,auto_sugg_txt):

        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        label_txt = BasePage.get_element_text(self, label_loc)
        return  label_txt


    def careers_link_text_ele(self,label_loc, input_loc,link_txt):

        careers_link_txt = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, link_txt)
        
        return careers_link_txt 


    def division_ele(self, label_loc, dropdown_loc,  dropdown_value ):

        division_txt = self.get_element_text(label_loc)
        BasePage.select_dropdown_by_visible_text(self,dropdown_loc,dropdown_value)

        return division_txt

    
    def function_ele(self,label_loc,input_loc,firstvalue,function_value):

        function_txt = self.get_element_text(label_loc)
        BasePage.select_dropdown_by_index(self,input_loc,firstvalue)
        action = ActionChains(self.driver)
        element = self.driver.find_element(*input_loc)
        element.send_keys(Keys.DOWN)
        d= Select(element)
        count = 0
        for opt in d.options:
            if function_value in opt.text:
                break
            count+=1
        for i in range(count-1):
            element.send_keys(Keys.DOWN)

        return function_txt

    def location_ele(self,label_loc,input_loc,firstvalue,location_value):

       
        location_txt = self.get_element_text(label_loc)
        BasePage.select_dropdown_by_index(self,input_loc,firstvalue)
        action = ActionChains(self.driver)
        element = self.driver.find_element(*input_loc)
        element.send_keys(Keys.DOWN)
        d= Select(element)
        count = 0
        for opt in d.options:
            if  location_value in opt.text:
                break
            count+=1
        for i in range(count-1):
            element.send_keys(Keys.DOWN)

        return location_txt
        
        

    
    def job_tags_ele(self,label_loc,dropdown_loc):

        job_tags_txt = self.get_element_text(label_loc)
        BasePage.press_button(self,dropdown_loc)

        return job_tags_txt

