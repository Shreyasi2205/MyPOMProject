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

class AddSlideshowCarousel(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    slideshow_carousel_stripe_value = "slideshow_carousel"
    slideshow_carousel_image_xpath = (By.XPATH, "//div[contains(@id, 'subform-field-slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'image-wrapper')]/details/summary")
    slideshow_carousel_select_image_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-image') and contains(@id, 'edit-field-body-0') and contains(@id, 'open-modal')]")
    slideshow_carousel_upload_video_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'field-document') and contains(@id, 'open-modal')]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    video_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_media_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    video_edit_button_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-button') and contains(@id, 'edit-field-body-0') and contains(@id, 'field-document')]")
    video_remove_button_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'remove-button') and contains(@id, 'edit-field-body-0') and contains(@id, 'field-document')]")
    # video_popup_video_url_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-video-embed')]")
    # video_popup_name_xpath = (By.XPATH, "//input[contains(@id, 'edit-name')]")
    # video_popup_revision_log_msg_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-revision-log-message')]")
    # video_popup_url_save_btn_css = (By.CSS_SELECTOR, "div.ui-dialog-buttonset > button")
    img_remove_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0-subform-field-slideshow-stripe-0-subform-field-image')]")

    text_color_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-0') and contains(@id, 'slideshow-stripe-0') and contains(@id, 'text-color')]")
    text_color_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-0') and contains(@for, 'slideshow-stripe-0') and contains(@for, 'text-color')]")
    hero_title_input_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'field-hero-title')]")
    hero_title_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'edit-field-body-0') and contains(@for, 'field-hero-title')]")
    hero_desc_input_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'field-carousel-description')]")
    hero_desc_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'edit-field-body-0') and contains(@for, 'field-carousel-description')]")
    hero_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-hero-title') and contains(@class, 'description')]")
    hero_desc_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'field-carousel-description') and (@class = 'description')]")
    carousel_text_layout_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'carousel-text-layout')]")
    carousel_text_layout_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'edit-field-body-0') and contains(@for, 'carousel-text-layout')]")
    field_header_variations_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'field-header-variations')]")
    field_header_variations_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'edit-field-body-0') and contains(@for, 'field-header-variations')]")
    hero_txt_uri_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'hero-text-link') and contains(@id, 'uri')]")
    hero_txt_uri_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'edit-field-body-0') and contains(@for, 'hero-text-link') and contains(@for, 'uri')]")
    hero_txt_link_txt_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'hero-text-link') and contains(@id, 'title')]")
    hero_txt_link_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'edit-field-body-0') and contains(@for, 'hero-text-link') and contains(@for, 'title')]")
    hero_txt_link_txt_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'edit-field-body-0') and contains(@id, 'hero-text-link') and contains(@id, 'desc') and not(contains(@id, 'uri'))]")
    no_content_checkbox_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0-subform-field-slideshow-stripe-0-subform-field-no-content-box-value')]")
    no_content_checkbox_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-0-subform-field-slideshow-stripe-0-subform-field-no-content-box-value')]")

    add_more_slideshow_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0-subform-field-slideshow-stripe-add-more-add-more-button-slideshow')]")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")

    text_color = ["black", "white"]
    layout = ["Text on left", "Text on right"]
    header_variation = ["large", "small"]
    hero_txt = ["Sample Hero Text 1", "Sample Hero Text 2", "Sample Hero Text 3", "Sample Hero Text 4","Sample Hero Text 5"]
    hero_desc = ["Sample Hero Desc 1", "Sample Hero Desc 2", "Sample Hero Desc 3", "Sample Hero Desc 4", "Sample Hero Desc 5"]
    hero_link_txt = ["Google", "Facebook", "Linkedin"]
    auto_sugg_txt = "novartis"
    hero_text1 = "#NovartisNews"
    hero_text_desc = "Tweets from the Media Relations team"
    link_text = "Follow @NovartisNews"
    hero_text2 = "Diversity & Inclusion"
    link_text2 = "Learn More"
    



    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def no_content_box_ele(self, input_loc, label_loc, flag):

        is_checked_false = BasePage.is_selected(self, input_loc)
        is_checked_true = False
        if flag == 1:
            BasePage.press_button(self, input_loc)
            is_checked_true = BasePage.is_selected(self, input_loc)
        label_txt = BasePage.get_element_text(self, label_loc)

        return is_checked_false, is_checked_true, label_txt

    def hero_txt_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        if len(BasePage.get_elemet_attribute(self, input_loc, "vlaue")) == 0:
            BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)

        return label_txt, helper_txt

    def hero_txt_desc_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc, txt)
        if len(BasePage.get_elemet_attribute(self,input_loc,"value")) == 0:
            BasePage.send_keys(self,input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)

        return label_txt, helper_txt

    def hero_url_ele(self, button_uri_selector, label):

        BasePage.send_keys(self, button_uri_selector, self.auto_sugg_txt)
        self.driver.find_element(*button_uri_selector).clear()
        BasePage.send_keys(self, button_uri_selector, self.auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*self.auto_sugg_css)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        sugg_txt = BasePage.get_elemet_attribute(self, button_uri_selector, "value")
        label_txt = BasePage.get_element_text(self, label)
        return sugg_txt, label_txt

    def hero_link_txt_ele(self, link_txt_loc, label_loc, helper_txt_loc, link_txt):

        BasePage.send_keys(self, link_txt_loc, link_txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)

        return label_txt, helper_txt

    def text_color_ele(self, select_loc, label_loc, value):

        BasePage.select_dropdown_by_value(self, select_loc, value)
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt

    def layout_ele(self, select_loc, label_loc, value):

        BasePage.select_dropdown_by_value(self, select_loc, value)
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt

    def header_variation_ele(self, select_loc, label_loc, value):

        BasePage.select_dropdown_by_value(self, select_loc, value)
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt


    def add_carousel_img_ele(self, carousel_img_loc, select_img_loc, remove_btn_loc):

        BasePage.press_button(self, carousel_img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        remove_btn = BasePage.is_visible(self, remove_btn_loc)

        return remove_btn
        

    def add_carousel_video_ele(self, upload_vdo_loc, edit_btn_loc, remove_btn_loc, flag):

        """
        Pass flag = 1 for removing video and adding again
        """

        BasePage.press_button(self, upload_vdo_loc)
        if len(self.driver.find_elements(*self.video_iframe_xpath)) == 0:
            BasePage.press_button(self, upload_vdo_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.video_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        edit_btn = BasePage.is_visible(self, edit_btn_loc)
        remove_btn = BasePage.is_visible(self, remove_btn_loc)

        # BasePage.press_button(self, edit_btn_loc)
        # if self.driver.find_elements(*self.video_popup_name_xpath):
        #     BasePage.press_button(self, edit_btn_loc)
        # video_name_status = BasePage.is_displayed(self, self.video_popup_name_xpath)
        # video_url_status = BasePage.is_displayed(self, self.video_popup_video_url_xpath)
        # BasePage.press_button(self, self.video_popup_url_save_btn_css)
        if flag == 1:
            BasePage.is_visible(self, remove_btn_loc)
            BasePage.press_button(self, remove_btn_loc)
            BasePage.press_button(self, upload_vdo_loc)
            if len(self.driver.find_elements(*self.video_iframe_xpath)) == 0:
                BasePage.press_button(self, upload_vdo_loc)
            self.driver.switch_to.frame(self.driver.find_element(*self.video_iframe_xpath))
            BasePage.press_button(self, self.img_css)
            BasePage.press_button(self, self.submit_button_iframe_xpath)
            self.driver.switch_to.default_content()
            BasePage.is_visible(self, remove_btn_loc)

        return edit_btn, remove_btn

    def add_more_slideshow_ele(self, input_loc):

        BasePage.press_button(self, input_loc)
