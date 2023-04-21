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
from datetime import date
from datetime import datetime, timedelta

now = datetime.now()

class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    landing_page_xpath = (By.XPATH,"//li[contains(@class, 'clearfix')]/a[contains(@href, 'landing_page')]")
    title_label_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]/parent::div/label")
    title_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]")
    title_description_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]/parent::div/div")
    
    body_dropdown_content_css = (By.CSS_SELECTOR, "ul.dropbutton > li.dropbutton__item > input")
    error_msg_list = ["Searchable in section field is required."]
    body_content_list = ["Call Out", "Call to Action", "Rich Text Content", "Media Content", "Careers Highlights", "Biography Teaser", "Accordion", "Cards", "Slideshow Carousel", "Big Numbers", "Arctic Iframe", "Image Gallery Slider", "Contacts", "Media Release", "Video Playlist", "Tab Content", "In this section", "Button", "Map Element", "Paragraph Library Block Content", "Supplier Invoice", "Webform", "Image Content"]
    
    add_landing_page_xpath = (By.XPATH, "//a[contains(@href, 'landing_page')]/span")
    title_txt_xpath = (By.XPATH, "//label[contains(@for, 'edit-title')]")
    title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-title')]")
    hide_title_input_xpath = (By.XPATH, "//input[contains(@id, 'hide-title')]")
    hide_title_txt_xpath = (By.XPATH, "//label[contains(@for, 'hide-title')]")
    title_chars_limit_txt_xpath = (By.XPATH, "//div[contains(@id, 'value--description') and contains(@id, 'edit-title')]")
    intro_txt_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-field-intro-text')]")
    intro_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-intro-text')]")
    page_main_category_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-category')]/option")
    page_main_sub_category_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-sub-category')]/option")
    searchable_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]/option")
    page_main_category_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-category')]")
    page_main_category_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-category')]")
    page_main_sub_category_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-sub-category')]")
    page_main_sub_category_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-sub-category')]")
    searchable_section_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]")
    searchable_section_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-section')]")
    legend_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Legend field')]")
    disclaimer_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Disclaimer field')]")
    publish_xpath = (By.XPATH, "//select[contains(@id, 'edit-moderation-state')]")
    error_msg_css = (By.CSS_SELECTOR, ".messages--error > div ")
    save_btn_id = (By.CSS_SELECTOR, '[id="edit-submit"]')
    notify_index_id = (By.ID, "edit-index-now")
    success_msg_css = (By.CSS_SELECTOR, ".alert.alert-dismissible")
    yes_button_xpath = (By.XPATH,"//button[text()='Yes']")
    additional_subcats_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-tags') and contains(@id, 'target-id')]")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    legend_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-legend-0-value')]")
    disclaimer_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-disclaimer-0-value')]")
    add_paragraph_btn_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]/option")

    landing_page = "Sample Landing Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    sample_healthcare_page = "Sample HealthCare Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    intro_txt = "Intro Text"
    auto_sugg_txt = "nov"
    legend_txt = "SAMPLE LEGEND TEXT"
    disclaimer_txt = "SAMPLE DISCLAIMER TEXT"
    hero_title_txt = "SAMPLE HERO TITLE"
    hero_desc_txt =  "SAMPLE HERO DESCRIPTION"
    hero_link_txt = "SAMPLE HERO TXT LINK TXT @#%^&124743"
    additional_sub_cat_txt = "New Scientific Discoveries (576)"

    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    video_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_media_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    paragraph_css = (By.CSS_SELECTOR, "p")
    header_slideshow_carousel_xpath = (By.XPATH, "//div/input[contains(@id, 'slideshow-carousel')]")
    slideshow_carousel_image_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'image-wrapper')]/details/summary")
    slideshow_carousel_image_second_xpath = (By.XPATH, "//div[contains(@id, 'subform-field-slideshow-stripe-1') and contains(@id, 'image-wrapper')]/details/summary")
    slideshow_carousel_select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-entity') and contains(@id, 'open-modal')]")
    slideshow_carousel_select_image_second_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-1') and contains(@id, 'field-image') and contains(@id, 'open-modal')]")
    slideshow_carousel_upload_video_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-document-public-file') and contains(@id, 'open-modal')]")
    video_upload_display_xpath = (By.XPATH, "//article[contains(@data-drupal-selector, 'slideshow')]/div/div/iframe")
    video_edit_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-document-public-file') and contains(@id, 'edit-button')]")
    video_remove_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-document-public-file') and contains(@id, 'remove-button')]")
    video_popup_video_url_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-video-embed')]")
    video_popup_name_xpath = (By.XPATH, "//input[contains(@id, 'edit-name')]")
    video_popup_revision_log_msg_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-revision-log-message')]")
    video_popup_url_alias_xpath = (By.XPATH, "//input[contains(@id, 'edit-path') and contains(@id, 'alias') and contains(@value, 'video')]")
    video_popup_url_save_btn_css = (By.CSS_SELECTOR, "div.ui-dialog-buttonset > button")
    text_color_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@id, 'text-color')]")
    text_color_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@id, 'text-color')]/option")
    text_color_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@for, 'text-color')]")
    hero_title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@id, 'field-hero-title')]")
    hero_title_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@for, 'field-hero-title')]")
    hero_desc_input_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-carousel-description')]")
    hero_desc_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'field-carousel-description')]")
    hero_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-hero-title') and contains(@class, 'description')]")
    hero_desc_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-carousel-description') and (@class = 'description')]")
    # slideshow_category_option_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'subform-field-category')]/option")
    # slideshow_category_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'subform-field-category')]")
    # slideshow_subcategory_option_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'subform-field-subcategory')]/option")
    # slideshow_subcategory_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'subform-field-subcategory')]")
    carousel_text_layout_option_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'carousel-text-layout')]/option")
    carousel_text_layout_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'carousel-text-layout')]")
    carousel_text_layout_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'carousel-text-layout')]")
    field_header_variations_option_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-header-variations')]/option")
    field_header_variations_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-header-variations')]")
    field_header_variations_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'field-header-variations')]")
    hero_txt_uri_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'hero-text-link') and contains(@id, 'uri')]")
    hero_txt_uri_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'hero-text-link') and contains(@for, 'uri')]")
    hero_txt_link_txt_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'hero-text-link') and contains(@id, 'title')]")
    hero_txt_link_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'hero-text-link') and contains(@for, 'title')]")
    hero_txt_link_txt_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'hero-text-link') and contains(@id, 'desc') and not(contains(@id, 'uri'))]")
    add_slideshow_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-add-more-add-more-button-slideshow')]")
    header_carousel_image_xpath = (By.XPATH,"//div[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-wrapper')]/details/summary/span[contains(@class, 'summary')]")
    img_remove_button_xpath = (By.XPATH,"//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-current') and contains(@id, 'remove')]")

    """
    Data related to Investors
    """
    sample_investors_page = "Sample Investors Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    investors_intro_text = "We aim for sustainable performance over time to benefit patients, employees, shareholders and society. Solid financial results and maintaining the trust of society underpin our ability to create value"
    investors_hero_title_txt = "Investors"
    investors_hero_desc_txt =  "Creating value for our company, our shareholders and society"
    investors_hero_link_txt = "Read More"
  

    def click_landing_page(self):

        BasePage.press_button(self, self.add_landing_page_xpath)

    def title_ele(self, input_loc, title_label_loc, hide_title_label_loc, selected_status_loc, helper_loc, txt):

        title_txt = BasePage.get_element_text(self, title_label_loc)
        BasePage.send_keys(self, input_loc, txt)
        hide_title_txt = BasePage.get_element_text(self, hide_title_label_loc)
        selectetd_status = BasePage.is_selected(self, selected_status_loc)
        title_chars_limit_txt = BasePage.get_element_text(self, helper_loc)

        return title_txt, hide_title_txt, selectetd_status, title_chars_limit_txt


    def body_dropdown_ele(self):

        dropdown_contents = self.driver.find_elements(*self.add_paragraph_btn_option_xpath)
        dropdown_contents_list = []
        for content in dropdown_contents:
            dropdown_contents_list.append(content.text)

        return dropdown_contents_list


    def intro_txt_ele(self, input_loc, label_loc, txt):


        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt


    def page_main_category_ele(self, select_loc, option_loc, label_loc):

        total_category = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_category-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        page_main_category_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, page_main_category_txt

    def page_main_sub_category_ele(self, select_loc, option_loc, label_loc):

        total_sub_category = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_sub_category-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        page_main_sub_category_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, page_main_sub_category_txt

    def searchable_section_ele(self, select_loc, option_loc, label_loc):

        total_searchable_section = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_searchable_section-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        searchable_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, searchable_txt


    def legend_ele(self, txt):

        self.driver.switch_to.frame(self.driver.find_element(*self.legend_iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css, txt)
        self.driver.switch_to.default_content()

        label_txt = BasePage.get_element_text(self, self.legend_label_xpath)

        return label_txt


    def disclaimer_ele(self, txt):

        self.driver.switch_to.frame(self.driver.find_element(*self.disclaimer_iframe_xpath))
        BasePage.send_keys(self, self.paragraph_css, txt)
        self.driver.switch_to.default_content()

        label_txt = BasePage.get_element_text(self, self.disclaimer_label_xpath)

        return label_txt

    def header_slideshow_carousel_img_ele(self, img_loc, select_img_loc, remove_btn_loc):

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

    def header_slideshow_carousel_video_ele(self, upload_vdo_loc, edit_btn_loc, remove_btn_loc):
        
        # Upload Video
        BasePage.press_button(self, upload_vdo_loc)
        if len(self.driver.find_elements(*self.video_iframe_xpath)) == 0:
            BasePage.press_button(self, upload_vdo_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.video_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        edit_btn_txt = BasePage.get_elemet_attribute(self, edit_btn_loc, "value")
        remove_btn_txt = BasePage.get_elemet_attribute(self, remove_btn_loc, "value")

        return edit_btn_txt, remove_btn_txt

    def add_more_slideshow_header(self):

        BasePage.press_button(self, self.add_slideshow_xpath)

    def header_slideshow_carousel_remove_video_ele(self):

        BasePage.press_button(self, self.video_remove_button_xpath)
        if len(self.driver.find_elements(*self.video_popup_name_xpath)) == 0:
            BasePage.press_button(self, self.video_remove_button_xpath)
        video_display_status = BasePage.is_displayed(self, self.video_upload_display_xpath)


    def text_color_ele(self, select_loc, option_loc, label_loc):

        text_colors = self.driver.find_elements(*option_loc)
        index_no = random.randint(0,2)
        BasePage.select_dropdown_by_index(self, select_loc , index_no)
        label_txt = BasePage.get_element_text(self, label_loc)
        text_color_val = text_colors[index_no].text

        return text_color_val, label_txt

    def hero_txt_ele(self, input_loc, label_loc, helper_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        print(BasePage.get_elemet_attribute(self, input_loc, "value"))
        if len(BasePage.get_elemet_attribute(self, input_loc, "value")) == 0:
            BasePage.send_keys(self, input_loc, txt)
        hero_title_helper_txt = BasePage.get_element_text(self, helper_loc)
        hero_title_label_txt = BasePage.get_element_text(self, label_loc)
        return hero_title_helper_txt, hero_title_label_txt

    def hero_desc_ele(self, input_loc, label_loc, helper_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        hero_desc_helper_txt = BasePage.get_element_text(self, helper_loc)
        hero_desc_label_txt = BasePage.get_element_text(self, label_loc)
        return hero_desc_helper_txt, hero_desc_label_txt

    def hero_txt_uri_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        hero_txt_uri_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        label_txt = BasePage.get_element_text(self, label_loc)
        return  hero_txt_uri_txt, label_txt

    def hero_txt_link_txt_ele(self, input_loc, label_loc, helper_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        hero_txt_link_txt_helper_txt = BasePage.get_element_text(self, helper_loc)
        hero_txt_link_txt_label_txt = BasePage.get_element_text(self, label_loc)
        return hero_txt_link_txt_helper_txt, hero_txt_link_txt_label_txt

    def carousel_text_layout_ele(self, select_loc, option_loc, label_loc):

        layouts = self.driver.find_elements(*option_loc)
        index_no = random.randint(1,2)

        BasePage.select_dropdown_by_index(self, select_loc , index_no)
        label_txt = BasePage.get_element_text(self, label_loc)
        layout_val = layouts[index_no].text

        return label_txt, layout_val

    def field_header_variation_ele(self, select_loc, option_loc, label_loc):

        field_var = self.driver.find_elements(*option_loc)
        index_no = random.randint(1,2)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        label_txt = BasePage.get_element_text(self, label_loc)
        field_header_var_val = field_var[index_no].text

        return label_txt, field_header_var_val


    def additional_subcats_ele(self, input_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        
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

    def notify_index_ele(self):

        checked_status = False
        checked_status = BasePage.is_selected(self, self.notify_index_id)
        return checked_status

    def success_msg_ele(self):

        success_msg_txt = BasePage.get_element_text(self, self.success_msg_css)
        return success_msg_txt


    # def header_carousel_image(self):

    #     BasePage.press_button(self,self.header_carousel_image_css)
    #     BasePage.press_button(self, self.slideshow_carousel_select_image_xpath)
    #     if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
    #         BasePage.press_button(self, self.slideshow_carousel_select_image_xpath)
    #     self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
    #     BasePage.press_button(self, self.img_css)
    #     BasePage.press_button(self, self.submit_button_iframe_xpath)
    #     self.driver.switch_to.default_content()
    #     remove_btn_txt = BasePage.get_elemet_attribute(self, self.img_remove_button_xpath, "value")

    #     return remove_btn_txt


    # def slideshow_category_ele(self):

    #     total_slideshow_category = len(self.driver.find_elements(*self.slideshow_category_option_xpath))

    #     index_no = random.randint(1,total_slideshow_category-1)

    #     BasePage.select_dropdown_by_index(self, self.slideshow_category_xpath[1], index_no, self.slideshow_category_xpath[0])

    #     slideshow_category_name = self.driver.find_elements(*self.slideshow_category_option_xpath)[index_no].text

    # def slideshow_subcategory_ele(self):

    #     total_slideshow_subcategory = len(self.driver.find_elements(*self.slideshow_subcategory_option_xpath))

    #     index_no = random.randint(1,total_slideshow_subcategory-1)

    #     BasePage.select_dropdown_by_index(self, self.slideshow_subcategory_xpath[1], index_no, self.slideshow_subcategory_xpath[0])

    #     slideshow_subcategory_name = self.driver.find_elements(*self.slideshow_subcategory_option_xpath)[index_no].text


# def header_slideshow_carousel_second_ele(self):

    #     BasePage.press_button(self, self.add_slideshow_xpath)
    #     # if self.driver.find_elements(*self.slideshow_carousel_image_xpath):
    #     #     BasePage.press_button(self, self.header_slideshow_carousel_xpath)

    #     # Adding Image
    #     BasePage.press_button(self, self.slideshow_carousel_image_second_xpath)
    #     BasePage.press_button(self, self.slideshow_carousel_select_image_second_xpath)
    #     if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
    #         BasePage.press_button(self, self.slideshow_carousel_select_image_second_xpath)
    #     self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
    #     BasePage.press_button(self, self.img_css)
    #     BasePage.press_button(self, self.submit_button_iframe_xpath)
    #     self.driver.switch_to.default_content()

    # def header_slideshow_carousel_edit_video_ele(self):

    #     BasePage.press_button(self, self.video_edit_button_xpath)
    #     if self.driver.find_elements(*self.video_popup_name_xpath):
    #         BasePage.press_button(self, self.video_edit_button_xpath)
    #     video_name_status = BasePage.is_displayed(self, self.video_popup_name_xpath)
    #     video_url_status = BasePage.is_displayed(self, self.video_popup_video_url_xpath)
    #     revision_log_status = BasePage.is_displayed(self, self.video_popup_revision_log_msg_xpath)
    #     url_alias_status = BasePage.is_displayed(self, self.video_popup_url_alias_xpath)
    #     BasePage.press_button(self, self.video_popup_url_save_btn_css)

    #     return video_name_status, video_url_status, revision_log_status, url_alias_status





