
from cProfile import label
from itertools import count
from operator import index
from pickle import TRUE
import time
from tkinter.tix import Select
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
import os
from datetime import date
from datetime import datetime, timedelta

now = datetime.now()

class MediaLibraryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    title_label_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]/parent::div/label")
    title_input_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]")
    title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-title-0') and contains(@class, 'description')]")
    
    authors_title_xapth = (By.XPATH, "//label[contains(@for, 'edit-field-media-authors-0-target-id')]")
    authors_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-authors-0-target-id')]")

    media_category_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-media-category')]")
    media_category_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-category')]")
    media_category_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-category')]/option")

    media_sub_category_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-media-tags')]")
    media_sub_category_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-tags')]")
    media_sub_category_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-tags')]/option")

    media_asset_type_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-media-asset-type')]")
    media_asset_type_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-asset-type')]")
    media_asset_type_select_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-asset-type')]/option")

    media_asset_logo_image_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-media-asset-logo-wrapper')]/details/summary/span")
    media_asset_upload_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-asset-logo-entity-browser-entity-browser-open-modal')]")
    media_asset_logo_remove_btn_xpath =(By.XPATH, "//input[contains(@id, 'edit-field-media-asset-logo') and contains(@id, 'remove')]")

    document_group_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-media-documents-0') and contains(@for, 'subform-field-document-group-0-target-id')]")
    documnet_group_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-documents-0') and contains(@id, 'subform-field-document-group-0-target-id')]")

    document_audience_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-media-documents-0') and contains(@for, 'subform-field-product-doc-audience')]")
    document_audience_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-documents-0') and contains(@id, 'subform-field-product-doc-audience')]")
    document_audience_select_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-documents-0') and contains(@id, 'subform-field-product-doc-audience')]/option")

    download_cta_btn_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-media-documents-0') and contains(@for, 'subform-field-product-document-title-0')]")
    download_cta_btn_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-media-documents-0') and contains(@id,'subform-field-product-document-title-0-value')]")
    download_cta_btn_helper_text_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-media-documents-0') and contains(@id,'subform-field-product-document-title-0') and contains(@class, 'description')]")

    document_url_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-media-documents-0') and contains(@for, 'subform-field-product-document-url-0')]")
    document_url_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-media-documents-0') and contains(@id, 'subform-field-product-document-url-0')]")
    document_url_helper_txt_xpath = (By.XPATH, "//div[contains(@id,'edit-field-media-documents-0') and contains(@id, 'subform-field-product-document-url-0') and contains(@class, 'description')]")

    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    media_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_media_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")

    document_file_image_xpath = (By.XPATH, "//div[contains(@id,'edit-field-media-documents-0-subform-field-document-public-file-wrapper')]/details/summary/span")
    document_file_upload_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-documents-0-subform-field-document-public-file-entity-browser-entity-browser-open-modal')]")
    document_file_img_remove_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-documents-0') and contains(@id,'subform-field-document-public-file-current-items-0') and contains(@id,'remove-button')]")
    document_file_img_edit_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-documents-0') and contains(@id,'subform-field-document-public-file-current-items-0') and contains(@id,'edit-button')]")

    honor_doc_file_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-documents-1-subform-field-product-doc-private-file-0-upload')]")
    description_label_xpath = (By.XPATH,"//label[contains(@for, 'edit-field-media-documents-1') and contains(@for, 'subform-field-product-doc-private-file-0') and contains(@for, 'description')]")
    description_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-documents-1') and contains(@id, 'subform-field-product-doc-private-file-0') and contains(@id, 'description')]")
    description_helper_text = (By.XPATH, "//div[contains(@id, 'edit-field-media-documents-1') and contains(@id, 'subform-field-product-doc-private-file-0') and contains(@class,'description')]")
    description_remove_btn_xpath = (By.XPATH, "//input[contains(@id,'edit-field-media-documents-1') and contains(@id, 'subform-field-product-doc-private-file-0') and contains(@id,'remove-button')]")

    document_type_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-media-documents-0') and contains(@for, 'subform-field-product-document-type-0-value')]")
    document_type_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-media-documents-0') and contains(@id,'subform-field-product-document-type-0-value')]")
    document_type_helper_text = (By.XPATH, "//div[contains(@id,'edit-field-media-documents-0') and contains(@id,'subform-field-product-document-type-0-value') and contains(@class, 'description')]")

    add_another_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-documents-add-more-add-more-button')]")
    paragraph_type_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-media-documents-add-more-add-more-select')]")
    paragraph_type_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-media-documents-add-more-add-more-select')]")

    file_url_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-link-0-uri')]")
    file_url_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-link-0-uri')]")
    file_link_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-link-0-title')]")
    file_link_txt_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-link-0-title')]")
    file_link_txt_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-link--description') and contains(@class, 'description')]")

    language_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-media-language')]")
    language_section_option_xpath = (By.XPATH, "//select[contains(@id,'edit-field-media-language')]/option")
    language_input_xpath = (By.XPATH, "//select[contains(@id,'edit-field-media-language')]")

    add_media_lib_page_xpath = (By.XPATH, "//a[contains(@href, 'custom_media_library')]/span")

    searchable_section_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]")
    searchable_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]/option")
    searchable_section_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-section')]")
    publish_xpath = (By.XPATH, "//select[contains(@id, 'edit-moderation-state')]")
    error_msg_css = (By.CSS_SELECTOR, ".messages--error > div ")
    save_btn_id = (By.CSS_SELECTOR, '[id="edit-submit"]')
    notify_index_id = (By.ID, "edit-index-now")
    success_msg_css = (By.CSS_SELECTOR, ".alert.alert-dismissible")
    yes_button_xpath = (By.XPATH,"//button[text()='Yes']")
    

    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    
    

    media_library_page = "Sample Media Library Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    error_msg_list = ["Searchable in section field is required."]
    author_name = "Don"
    author_name_txt = "Don Gibbons (3246)"
    featured_headline_text = "featured news page"
    auto_sugg_txt = "nov"
    doc_audience_value = "media-public"
    doc_audience_value2 = "media-hcp"
    media_asset_type_value = "Image"
    cta_btn_text = "sample text1"
    cta_btn_text2 = "sample text2"
    doc_url_text= "novartis"
    doc_url_text2= "novartis123"
    doc_type_text = "Media1"
    doc_type_text2 = "Media2"
    link_text = "Read More"
    link_text2 = "View More"
    paragraph_type_value = "product_documents"
    path = "//sample_image.jpeg"
    description_text = "Sample Description"
    
    

  

    def click_media_library_page(self):

        BasePage.press_button(self, self.add_media_lib_page_xpath)

    def title_ele(self, input_loc, title_label_loc, helper_loc, txt):

        title_txt = BasePage.get_element_text(self, title_label_loc)
        BasePage.send_keys(self, input_loc, txt)
        title_chars_limit_txt = BasePage.get_element_text(self, helper_loc)

        return title_txt, title_chars_limit_txt

    def authors_ele(self, input_loc, auto_sugg_loc, author_name, label_loc, input_text):
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, author_name)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        link_uri= BasePage.get_elemet_attribute(self, input_loc, "value")
        if link_uri == author_name:
            self.driver.find_element(*input_loc).clear()
            BasePage.send_keys(self,input_loc,input_text )
        label_txt = BasePage.get_element_text(self,label_loc)
        return label_txt

    def media_category_ele(self, select_loc, option_loc, label_loc):

        total_category = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_category-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        media_category_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, media_category_txt

    def media_sub_category_ele(self, select_loc, option_loc, label_loc):

        total_sub_category = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_sub_category-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        media_sub_category_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, media_sub_category_txt


    def language_section_ele(self):
        label = BasePage.get_element_text(self,self.language_label_xpath)

        total_languages = len(self.driver.find_elements(*self.language_section_option_xpath))
        index_no = random.randint(1,total_languages-1)
        BasePage.select_dropdown_by_index(self, self.language_input_xpath, index_no)
        language_section_val = self.driver.find_elements(*self.language_section_option_xpath)[index_no].text
        return label, language_section_val


    def click_media_asset_type_dropdown(self,input_loc,value,label_loc):
        BasePage.select_dropdown_by_value(self, input_loc, value)
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt

    def media_asset_logo_img_ele(self, img_loc, select_img_loc, remove_btn_loc):

        # Adding Image
        BasePage.press_button(self,img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        images = self.driver.find_elements(*self.img_css)
        random_img_index = random.randint(0, len(images)-1)
        for img in images:
            self.driver.execute_script("arguments[0].click()", images[random_img_index])
            break
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()

        img_remove_btn = BasePage.is_visible(self, remove_btn_loc)
        

        return img_remove_btn

    def honor_doc_file_ele(self,input_loc,path):
        BasePage.send_keys(self, input_loc, os.getcwd() + path)

    def description_ele(self,input_loc, label_loc, helper_txt, input_text, remove_btn_loc):

        desc_label = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, input_text)
        desc_helper_txt = BasePage.get_element_text(self,helper_txt)
        desc_remove_btn = BasePage.is_visible(self, remove_btn_loc)

        return desc_helper_txt, desc_label,desc_remove_btn




    def doc_group_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc, input_text):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        doc_grp_text = BasePage.get_elemet_attribute(self, input_loc, "value")
        if doc_grp_text == auto_sugg_txt:
            self.driver.find_element(*input_loc).clear()
            BasePage.send_keys(self, input_loc, input_text)
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt

    def doc_audience_ele(self, input_loc, label_loc, value):

        BasePage.select_dropdown_by_value(self, input_loc, value)
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt

    
    def cta_btn_txt_ele(self,input_loc, label_loc, helper_txt, title_text):

        cta_title = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, title_text)
        cta_helper_txt = BasePage.get_element_text(self,helper_txt)
        return cta_helper_txt, cta_title

    def doc_url_ele(self,input_loc, label_loc, helper_txt, text):
        label_txt = self.get_element_text(label_loc)
        BasePage.send_keys(self,input_loc, text)
        cta_helper_txt = BasePage.get_element_text(self,helper_txt)
        return cta_helper_txt, label_txt

    def doc_file_img_ele(self, img_loc, select_img_loc,remove_btn_loc,edit_btn_loc):

        # Adding Image
        BasePage.press_button(self,img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.media_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.media_iframe_xpath))
        images = self.driver.find_elements(*self.img_css)
        random_img_index = random.randint(0, len(images)-1)
        for img in images:
            self.driver.execute_script("arguments[0].click()", images[random_img_index])
            break
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        img_remove_btn = BasePage.is_visible(self, remove_btn_loc)
        img_edit_btn = BasePage.is_visible(self,edit_btn_loc)

        return img_remove_btn,img_edit_btn


    def doc_type_ele(self,input_loc, label_loc, helper_txt, text):
        label_txt = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, text)
        cta_helper_txt = BasePage.get_element_text(self,helper_txt)
        return cta_helper_txt, label_txt

    def click_drpdwn_paragraph_type_ele(self,btn_loc, drop_down_value):
        BasePage.press_button(self,btn_loc)
        BasePage.select_dropdown_by_value(self, btn_loc, drop_down_value)

    def add_another_paragraph_btn_ele(self,btn_loc):
        BasePage.press_button(self,btn_loc)

    def file_url_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc, input_text):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        file_text = BasePage.get_elemet_attribute(self, input_loc, "value")
        if file_text == auto_sugg_txt:
            self.driver.find_element(*input_loc).clear()
            BasePage.send_keys(self, input_loc, input_text)
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt

    
    def link_text_ele(self,input_loc, label_loc, helper_text,text):
        label_txt = self.get_element_text(label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, text)
        link_txt_helper_txt = BasePage.get_element_text(self,helper_text)
        return label_txt, link_txt_helper_txt


    def searchable_section_ele(self, select_loc, option_loc, label_loc):

        total_searchable_section = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_searchable_section-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        searchable_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, searchable_txt
        
    def publish_ele(self):

        BasePage.select_dropdown_by_value(self, self.publish_xpath, "published")

    def save_btn_ele(self):

        BasePage.press_button(self, self.save_btn_id)

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


