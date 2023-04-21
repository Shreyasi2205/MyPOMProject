from conftest import driver
import platform
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

class ClinicalTrials(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    add_clinical_trials_xpath = (By.XPATH,"//li[contains(@class, 'clearfix')]/a[contains(@href, 'clinical_trials')]")
    title_label_xpath = (By.XPATH,"//label[contains(@for,'edit-title-0-value')]")
    title_input_xpath = (By.XPATH,"//input[contains(@id,'edit-title-0-value')]")
    title_helper_txt_css = (By.CSS_SELECTOR,"div#edit-title-0-value--description")
    brief_title_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-brief-title-0-value')]")
    brief_title_input_iframe_xpath = (By.XPATH,"//div[contains(@id,'cke_1_contents')]/iframe[contains(@class,'cke_wysiwyg_frame')]")
    official_title_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-official-title-0-value')]")
    official_title_input_iframe_xpath = (By.XPATH,"//div[contains(@id,'cke_2_contents')]/iframe[contains(@class,'cke_wysiwyg_frame')]")
    paragraph_css = (By.CSS_SELECTOR, "p")
    novartis_ref_no_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-org-study-id-0-value')]")
    nov_ref_no_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-org-study-id-0-value')]")
    NCTid_helper_txt_xpath = (By.XPATH,"//div[contains(@id,'edit-field-org-study-id-0-value-counter')]")
    last_update_label_xpath = (By.XPATH,"//div[contains(@id,'edit-field-last-update-post-date-wrapper')]/h4")
    date_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-last-update-post-date-0-value-date')]")
    time_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-last-update-post-date-0-value-time')]")
    study_desc_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-brief-summary-0-value')]")
    study_desc_input_iframe_xpath = (By.XPATH,"//iframe[contains(@title,'Study Description field')]")
    condition_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-condition')]")
    condition_select_xpath = (By.XPATH,"//select[contains(@id,'edit-field-condition')]")
    condition_option_xpath = (By.XPATH,"//select[contains(@id,'edit-field-condition')]/option")
    phase_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-phase')]")
    phase_select_xpath = (By.XPATH,"//select[contains(@id,'edit-field-phase')]")
    phase_option_xpath = (By.XPATH,"//select[contains(@id,'edit-field-phase')]/option")
    start_date_label_xpath = (By.XPATH,"//div[contains(@id,'edit-field-start-date-wrapper')]/h4[contains(@class,'label')]")
    start_date_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-start-date-0-value-date')]")
    start_date_time_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-start-date-0-value-time')]")
    completion_label_xpath = (By.XPATH,"//div[contains(@class,'field--name-field-completion-date')]/h4")
    completion_date_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-completion-date-0-value-date')]")
    completion_date_time_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-completion-date-0-value-time')]")
    primary_completion_date_label_xpath = (By.XPATH,"//div[contains(@id,'edit-field-primary-completion-date-wrapper')]/h4")
    primary_completion_date_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-primary-completion-date-0-value-date')]")
    primary_completion_date_time_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-primary-completion-date-0-value-time')]")
    overall_status_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-overall-status')]")
    overall_status_select_xpath = (By.XPATH,"//select[contains(@id,'edit-field-overall-status')]")
    overall_status_option_xpath = (By.XPATH,"//select[contains(@id,'edit-field-overall-status')]/option")
    minimum_age_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-minimum-age-0-value')]")
    minimum_age_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-minimum-age-0-value')]")
    maximum_age_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-maximum-age-0-value')]")
    maximum_age_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-maximum-age-0-value')]")
    age_list_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-age-list-0-value')]")
    age_list_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-age-list-0-value')]")
    gender_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-clinical-trials-gender')]")
    gender_select_xpath = (By.XPATH,"//select[contains(@id,'edit-field-clinical-trials-gender')]")
    gender_option_xpath = (By.XPATH,"//select[contains(@id,'edit-field-clinical-trials-gender')]/option")
    intervention_type_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-interventions-0') and contains(@for,'field-intervention-type-0-value')]")
    intervention_type_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-interventions-0') and contains(@id,'intervention-type-0-value')]")
    intervention_type_helper_txt_xpath = (By.XPATH,"//div[contains(@id,'edit-field-interventions-0') and contains(@id,'intervention-type-0-value-counter')]")
    intervention_name_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-interventions-0') and contains(@for,'field-intervention-name-0-value')]")
    intervention_name_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-interventions-0') and contains(@id,'intervention-name-0-value')]")
    internvention_name_helper_txt_path = (By.XPATH,"//div[contains(@id,'edit-field-interventions-0') and contains(@id,'field-intervention-name-0-value')]")
    intervention_desc_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-interventions-0') and contains(@for,'intervention-description-0-value')]")
    intervention_desc_input_iframe_xpath = (By.XPATH,"//iframe[contains(@title,'Intervention Description field')]")
    intervention_sec_desc_input_iframe_xpath = (By.XPATH,"//iframe[contains(@title,'Intervention Description field')][1]")
    eligibility_criteria_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-eligibility-criteria-0-value')]")
    eligibility_criteria_input_iframe_xpath = (By.XPATH,"//div[contains(@id,'cke_5_contents')]/iframe[contains(@class,'cke_wysiwyg_frame')]")
    location_facility_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'location-facility-0-value')]")
    location_facility_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'location-facility-0-value')]")
    location_facility_helper_txt_xpath = (By.XPATH,"//div[contains(@id,'edit-field-location-0') and contains(@id,'location-facility-0-value-counter')]")
    location_status_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'location-status-0-value')]")
    location_status_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'location-status-0-value')]")
    location_status_helper_txt_xpath = (By.XPATH,"//div[contains(@id,'edit-field-location-0') and contains(@id,'location-status-0-value-counter')]")
    location_state_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'location-state-0-value')]")
    location_state_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'location-state-0-value')]")
    location_state_helper_txt_xpath = (By.XPATH,"//div[contains(@id,'edit-field-location-0') and contains(@id,'location-state-0-value-counter')]")
    location_city_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'location-city-0-value')]")
    location_city_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'location-city-0-value')]")
    location_city_helper_txt_xpath = (By.XPATH,"//div[contains(@id,'edit-field-location-0') and contains(@id,'location-city-0-value-counter')]")
    location_zip_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'location-zip-0-value')]")
    location_zip_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'location-zip-0-value')]")
    location_zip_helper_txt_xpath = (By.XPATH,"//div[contains(@id,'edit-field-location-0') and contains(@id,'location-zip-0-value-counter')]")
    location_country_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'location-country-0-target-id')]")
    location_country_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'location-country-0-target-id')]")
    loc_contact_name_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'subform-field-contact-name-0-value')]")
    loc_contact_name_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'subform-field-contact-name-0-value')]")
    loc_contact_role_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'subform-field-contact-role-0-value')]")
    loc_contact_role_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'subform-field-contact-role-0-value')]")
    loc_contact_phone_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'subform-field-contact-phone-0-value')]")
    loc_contact_phone_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'subform-field-contact-phone-0-value')]")
    loc_contact_phone_ext_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'subform-field-contact-phone-ext-0-value')]")
    loc_contact_phone_ext_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'subform-field-contact-phone-ext-0-value')]")
    loc_contact_email_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'subform-field-contact-email-0-value')]")
    loc_contact_email_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-location-0') and contains(@id,'subform-field-contact-email-0-value')]")
    loc_contact_type_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-location-0') and contains(@for,'subform-field-contact-type')]")
    loc_contact_type_select_xpath = (By.XPATH,"//select[contains(@id,'edit-field-location-0') and contains(@id,'subform-field-contact-type')]")
    loc_contact_type_option_xpath = (By.XPATH,"//select[contains(@id,'edit-field-location-0') and contains(@id,'subform-field-contact-type')]/option")

    add_interventions_bttn_xpath = (By.XPATH,"//div[contains(@id,'edit-field-interventions-add-more')]")
    add_loc_contact_bttn_xpath = (By.XPATH,"//div[contains(@id,'edit-field-location-0') and contains(@id,'location-contact-add-more')]")

    rank_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-rank-0-value')]")
    rank_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-rank-0-value')]")

    published_checkbox_css = (By.CSS_SELECTOR,"input#edit-status-value")
    published_label_xpath = (By.XPATH,"//label[contains(@for,'edit-status-value')]")
    save_css = (By.CSS_SELECTOR,"input#edit-submit")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    success_msg_css = (By.CSS_SELECTOR, ".alert.alert-dismissible")
    NCTid_url_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-nctid-link-0-uri')]")
    auto_sugg_nctid_url = (By.CSS_SELECTOR,"ul#ui-id-2 > li > a")
    auto_sugg_nctid_txt = "nov"
    NCTid_url_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-nctid-link-0-uri')]")
    NCTid_link_txt_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-nctid-link-0-title')]")
    NCTid_link_txt_input_xpath = (By.XPATH,"//input[contains(@id,'edit-field-nctid-link-0-title')]")



    date = now.strftime("%d/%M/%Y")
    time = now.strftime("%H:%M:%S")

    clinical_trials_title = "Sample Clinical Trials Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    brief_title_txt = "Clinical trials are at the heart of our work to bring innovative medicines to people with a particular disease or condition."
    official_title_txt = "These studies ensure that an investigative medicine is effective and safe, and rely entirely on patients and healthy volunteers. Learn more about clinical trials at Novartis including opportunities to get involved."
    novartis_ref_no = "NOV@0330"
    study_desc_txt = "Clinical trials are at the heart of our work to bring innovative medicines to people with a particular disease or condition. These studies ensure that an investigative medicine is effective and safe, and rely entirely on patients and healthy volunteers."
    minimum_age = 18
    maximum_age = 60
    age_list = "Child"
    internvention_type = "Drugs"
    internvention_name = "Novartis Trials"
    intervention_desc = "Clinical trials are at the heart of our work to bring innovative medicines to people with a particular disease or condition. These studies ensure that an investigative medicine is effective and safe, and rely entirely on patients and healthy volunteers."
    elegibility_criteria_txt = "Novartis Trials eligibility criteria"
    location_facility = "Novartis Labs"
    location_status = "Active"
    location_state = "Telangana"
    location_city = "Hyderabad"
    location_zip = "500084"
    location_country_auto_sugg_txt = "ind"
    contact_name = "XYZ"
    contact_role = "Admin"
    contact_phone = "7080803162"
    contact_email = "XYZ@novartis.com"
    rank = 4
    NCTid_link_txt = "NCT id Link Text"




    def click_clinical_trials_page(self):
        BasePage.press_button(self,self.add_clinical_trials_xpath)
    
    def title_ele(self,input_loc, label_loc, helper_txt_loc, txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.send_keys(self,input_loc,txt)
        helper_txt = BasePage.get_element_text(self,helper_txt_loc)
        return label_txt, helper_txt
    
    def brief_title_ele(self,label_loc, txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.brief_title_input_iframe_xpath))
        BasePage.send_keys(self,self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        return label_txt
    
    def official_title_ele(self,label_loc,txt):
        label_txt = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.official_title_input_iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        return label_txt
    
    def date_input_ele(self, date_loc,time_loc,label_loc):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.do_click(self,date_loc)
        BasePage.send_keys(self,date_loc,self.date)
        BasePage.do_click(self,time_loc)
        BasePage.send_keys(self,time_loc,self.time)
        return label_txt
    
    def novartis_reference_no_ele(self,input_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.send_keys(self,input_loc,txt)
        return label_txt
    
    def study_desc_ele(self,label_loc,txt):
        label_txt = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.study_desc_input_iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        return label_txt
    
    def select_condition_ele(self,select_loc,option_loc,label_loc):
        condition_len = len(self.driver.find_elements(*option_loc))
        act=ActionChains(self.driver)
        random_cond = random.randint(1,condition_len-1)
        for i in range(3):
            opt = BasePage.select_dropdown_by_index(self,select_loc,random_cond)
            act.key_down ( Keys.CONTROL ).click (opt).key_up(Keys.CONTROL).perform ()
            random_cond = random.randint(1,condition_len-1)  
        label_txt = BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def select_phase_ele(self,select_loc, option_loc,label_loc):
        phase_len = len(self.driver.find_elements(*option_loc))
        act=ActionChains(self.driver)
        random_phase = random.randint(1,phase_len-1)
        for i in range(3):
            opt = BasePage.select_dropdown_by_index(self,select_loc,random_phase)
            act.key_down ( Keys.CONTROL ).click (opt).key_up(Keys.CONTROL).perform ()
            random_phase = random.randint(1,phase_len-1)  
        label_txt = BasePage.get_element_text(self,label_loc)
        return label_txt
    
    
    def overall_status_ele(self,select_loc,label_loc):
        BasePage.select_dropdown_by_index(self,select_loc,1)
        label_txt = BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def minimum_age_ele(self,input_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        return label_txt
    
    def maximum_age_ele(self,input_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        return label_txt
    
    def age_limit_ele(self,input_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        return label_txt
    
    def select_gender_ele(self,select_loc,option_loc,label_loc):
        gender_len = len(self.driver.find_elements(*option_loc))
        random_gender = random.randint(1,gender_len-1)
        BasePage.select_dropdown_by_index(self,select_loc,random_gender)
        label_txt = BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def internvention_type_ele(self,input_loc,label_loc,helper_txt_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        helper_txt = BasePage.get_element_text(self,helper_txt_loc)
        return label_txt, helper_txt
    
    def internvention_name_ele(self,input_loc,label_loc,helper_txt_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        helper_txt = BasePage.get_element_text(self,helper_txt_loc)
        return label_txt, helper_txt
    
    
    def intervention_desc_ele(self,iframe_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*iframe_loc))
        BasePage.send_keys(self, self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        return label_txt
    
    def intervention_sec_desc_ele(self,iframe_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(iframe_loc))
        BasePage.send_keys(self, self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        return label_txt
    
    def add_button_ele(self,bttn_loc):
        BasePage.press_button(self,bttn_loc)
    
    def elegibility_criteria_ele(self,label_loc,txt):
        label_txt = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.eligibility_criteria_input_iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        return label_txt
    
    def study_location_ele(self,input_loc,label_loc,helper_txt_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        helper_txt = BasePage.get_element_text(self,helper_txt_loc)
        return label_txt, helper_txt
    
    def study_location_country_ele(self,input_loc,auto_sugg_loc,auto_sugg_txt,label_loc):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,auto_sugg_txt)
        auto_suggestions=self.driver.find_elements(*auto_sugg_loc)
        sugg_len=len(auto_suggestions)
        random_num=random.randint(0,sugg_len-1)
        self.driver.execute_script("arguments[0].click()",auto_suggestions[random_num])
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt
    
    def location_contact_ele(self,input_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        return label_txt
    
    def loc_contact_type_ele(self,select_loc,option_loc,label_loc):
        len_contact_type = len(self.driver.find_elements(*option_loc))
        randon_contact_type = random.randint(1,len_contact_type-1)
        BasePage.select_dropdown_by_index(self,select_loc,randon_contact_type)
        label_txt = BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def rank_ele(self,input_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        return label_txt
    
    def add_NCTid_url_ele(self,input_loc,auto_sugg_loc,auto_sugg_txt,label_loc):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,auto_sugg_txt)
        auto_suggestions=self.driver.find_elements(*auto_sugg_loc)
        sugg_len=len(auto_suggestions)
        random_num=random.randint(0,sugg_len-1)
        self.driver.execute_script("arguments[0].click()",auto_suggestions[random_num])
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt
    
    def add_NCTid_link_txt_ele(self,input_loc,label_loc,txt):
        label_txt = BasePage.get_element_text(self,label_loc)
        BasePage.send_keys(self,input_loc,txt)
        return label_txt
    
    def check_publish_ele(self,check_box_loc,label_loc):
        BasePage.press_button(self,check_box_loc)
        label_txt = BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def click_save_bttn(self):
        BasePage.press_button(self,self.save_css)
    
    def success_msg_ele(self):

        success_msg_txt = BasePage.get_element_text(self, self.success_msg_css)
        return success_msg_txt
    

    

    

