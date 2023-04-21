
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

class FeaturedNewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    featured_news_page_xpath = (By.XPATH,"//li[contains(@class, 'clearfix')]/a[contains(@href, 'news')]")
    title_label_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]/parent::div/label")
    title_input_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]")
    title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-title-0') and contains(@class, 'description')]")
    



    language_label_xpath = (By.XPATH, "//label[contains(@for,'edit-langcode-0-value')]")
    language_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-langcode-0-value')]/option")
    language_input_xpath = (By.XPATH, "//select[contains(@id,'edit-langcode-0-value')]")

    date_label_xpath = (By.XPATH,"//span[text()='Date']")
    date_picker_xpath = (By.XPATH, "//input[contains(@id,'edit-field-date-0-value-date')]")
    time_field_xpath = (By.XPATH, "//input[contains(@id,'edit-field-date-0-value-time')]")
    date = now.strftime("%d/%M/%Y")
    time = now.strftime("%H:%M:%S")

    iframe_featured_headline_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Featured Headline / Intro text field')]")
    featured_headline_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-new-intro-text-0-value')]")
    

    paragraph_type_label = (By.XPATH, "//label[contains(@for, 'edit-field-image-news-add-more-add-more-select')]")
    paragraph_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-image-news-add-more-add-more-select')]/option")
    paragraph_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-image-news-add-more-add-more-select')]")
    


    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-image-news-add-more-add-more-button')]")

    error_msg_list = ["Searchable in section field is required."]

    body_paragraph_type_dropdown_xpath = (By.XPATH , "//select[contains(@id, 'edit-field-body-canvas-add-more-add-more-select')]/option")
    body_paragraph_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-canvas-add-more-add-more-select')]")
    body_paragraph_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-body-canvas-add-more-add-more-select')]")
    body_paragraph_type_list = [ "Call to Action", "Rich Text Content", "Media Content", "Careers Highlights",  "Accordion", "Cards", "Slideshow Carousel", "Big Numbers", "Arctic Iframe", "Image Gallery Slider", "Contacts", "Media Release", "Video Playlist", "Tab Content", "In this section", "Button", "Paragraph Library Block Content", "Webform", "Media Library Related Items"]
    body_add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-canvas-add-more-add-more-button')]")

    
    add_featured_news_page_xpath = (By.XPATH, "//a[contains(@href, 'news')]/span")

    right_rail_title_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-right-rail-0') and contains(@for,'subform-field-related-links-title-0-value')]")
    right_rail_title_input_xpath = (By.XPATH, "//input[contains(@id , 'edit-field-right-rail-0') and contains(@id, 'subform-field-related-links-title-0-value')]")
    right_rail_title_helper_text_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-related-links-title-0') and contains(@class, 'description')]")

    right_rail_description_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'subform-field-related-links-desc-0-value')]")
    right_rail_description_input_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-related-links-desc-0-value')]")

    right_rail_image_xpath = (By.XPATH, "//div[contains(@id,'edit-field-right-rail-0') and contains(@id,'subform-field-image-wrapper')]")
    right_rail_select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-image-entity-browser-entity') and contains(@id, 'open-modal')]")
    right_rail_tags_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0')and contains(@for, 'subform-field-subcategory-0-target-id')]")
    right_rail_tags_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-subcategory-0-target-id')]")
    right_rail_img_remove_btn_loc_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id,'subform-field-image-current') and contains(@id, 'remove-button')]")

    link_type_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'subform-field-link-type') and contains(@for, 'subform-field-inner-related-links-0')]")
    link_type_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-link-type') and contains(@id, 'subform-field-inner-related-links-0')]")
    link_type_input_select_xpath = (By.XPATH , "//select[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-link-type') and contains(@id, 'subform-field-inner-related-links-0')]/option")

    link_title_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'subform-field-title-0') and contains(@for, 'subform-field-inner-related-links-0')]")
    link_title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-title-0-value') and contains(@id, 'subform-field-inner-related-links-0')]")
    link_title_helper_text = (By.XPATH, "//div[contains(@id, 'edit-field-right-rail-0-subform-field-inner-related-links-0-subform-field-title-0') and contains(@class, 'description')]")
    
    link_url_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'subform-field-inner-related-links-0') and contains(@for, 'subform-field-url')]")
    link_url_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-inner-related-links-0') and contains(@id, 'subform-field-url-0')]")
    add_inner_related_link_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0-subform-field-inner-related-links-add-more-add-more-button-inner-related-links')]")

    right_rail_paragraph_type_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-add-more-add-more-select')]")
    right_rail_paragraph_type_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-right-rail-add-more-add-more-select')]")
    right_rail_paragraph_type_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-right-rail-add-more-add-more-select')]/option")
    add_another_paragraph_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-add-more-add-more-button')]")


    page_bottom_paragraph_type_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-page-bottom-content-add-more-add-more')]")
    page_bottom_paragraph_type_input_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-page-bottom-content-add-more-add-more')]")
    page_bottom_paragraph_type_select_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-page-bottom-content-add-more-add-more')]/option")
    page_bottom_content_add_paragraph_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-page-bottom-content-add-more-add-more-button')]")
    page_bottom_content_remove_btn_xpath = (By.XPATH, "//input[contains(@id, '//input[contains(@id, 'edit-field-page-bottom-content-0-top-links-remove-button')]")
    page_bottom_content_edit_btn_xpath = (By.XPATH, "//input[contains(@id,'edit-field-page-bottom-content-0-top-links-edit-button')]")
    media_categories_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-page-bottom-content-0') and contains(@for, 'subform-field-media-categories-0')]")
    media_categories_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-page-bottom-content-0') and contains(@id, 'subform-field-media-categories-0')]")
    media_sub_categories_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-page-bottom-content-0') and contains(@for, 'subform-field-media-sub-categories-0')]")
    media_sub_categories_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-page-bottom-content-0') and contains(@id, 'subform-field-media-sub-categories-0')]")

    tags_label_xpath = (By.XPATH, "//table[contains(@id, 'field-tags-values')]/thead")
    tags_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-tags-0-target-id')]")
    draggable_items_xpath = (By.XPATH,"//table[contains(@id,'field-tags-values')]//tr[contains(@class,'draggable')]")
    add_another_item_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-tags-add-more')]")

    news_type_filter_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-news-type-filters-0-target-id')]")
    news_type_filter_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-news-type-filters-0-target-id')]")
    news_type_filters_helper_text_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-news-type-filters-0-target-id') and contains(@class, 'description')]")




    
    searchable_section_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]")
    searchable_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]/option")
    searchable_section_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-section')]")
    legend_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Legend field')]")
    disclaimer_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Disclaimer field')]")
    publish_xpath = (By.XPATH, "//select[contains(@id, 'edit-moderation-state')]")
    error_msg_css = (By.CSS_SELECTOR, ".messages--error > div ")
    save_btn_id = (By.CSS_SELECTOR, '[id="edit-submit"]')
    notify_index_id = (By.ID, "edit-index-now")
    success_msg_css = (By.CSS_SELECTOR, ".alert.alert-dismissible")
    yes_button_xpath = (By.XPATH,"//button[text()='Yes']")
    

    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    legend_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-legend-0-value')]")
    disclaimer_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-disclaimer-0-value')]")
    

    featured_news_page = "Sample Featured News Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    
    featured_headline_text = "featured news page"
    auto_sugg_txt = "nov"
    rail_auto_sugg_txt = "nov"
    auto_sugg_txt2 = "key"
    legend_txt = "SAMPLE LEGEND TEXT OF FEATURED NEWS PAGE"
    disclaimer_txt = "SAMPLE DISCLAIMER TEXT OF FEATURED NEWS PAGE"
    hero_title_txt = "SAMPLE HERO TITLE OF FEATURED NEWS PAGE"
    hero_desc_txt =  "SAMPLE HERO DESCRIPTION OF FEATURED NEWS PAGE"
    hero_link_txt = "SAMPLE HERO TXT LINK TXT @#%^&124743"
    right_rail_title = "Sample Right Rail title"
    right_rail_title2 = "Sample Right Rail title 2"
    right_rail_desc =  "Sample Right Rail Description"
    right_rail_desc2 =  "Sample Right Rail Description 2"
    link_title = "Sample Link Text"
    link_title2 = "Sample Link Text 2"
    link_title3 = "Sample Link Text 3"
    page_bottom_content_paragraph_value = "media_library_related_items"
    link_uri_text = "Novartis Access fact sheet (17796)"
    rail_tag_text = "Innovation"
    new_type_text = "Key Release"
    media_category_text = "Science & Innovation (1886)"
    auto_sugg_txt3 = "act"
    media_sub_category_text = "Fact Sheet (101)"
    
    
    
    

    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    video_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_media_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    paragraph_css = (By.CSS_SELECTOR, "p")
    header_slideshow_carousel_xpath = (By.XPATH, "//div/input[contains(@id, 'slideshow-carousel')]")
    slideshow_carousel_image_xpath = (By.XPATH, "//div[contains(@id, 'image-news-0') and contains(@id, 'image-wrapper')]/details/summary")
    slideshow_carousel_image_second_xpath = (By.XPATH, "//div[contains(@id, 'subform-field-image-news-1') and contains(@id, 'image-wrapper')]/details/summary")
    slideshow_carousel_select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-image-news-0-subform-field-image-entity-browser-entity') and contains(@id, 'open-modal')]")
    slideshow_carousel_select_image_second_xpath = (By.XPATH, "//input[contains(@id, 'image-news-1') and contains(@id, 'field-image') and contains(@id, 'open-modal')]")
    slideshow_carousel_edit_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-image-news-0-top-links-edit-button')]")
    img_remove_button_xpath = (By.XPATH,"//input[contains(@id, 'edit-field-image-news-0-subform-field-image-current') and contains(@id, 'remove')]")
    slideshow_carousel_remove_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-image-news-0-top-links-remove-button')]")
    slideshow_carousel_upload_video_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-image-news-0-subform-field-document-public-file') and contains(@id, 'open-modal')]")
    video_upload_display_xpath = (By.XPATH, "//article[contains(@data-drupal-selector, 'slideshow')]/div/div/iframe")
    video_edit_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-image-news-0-subform-field-document-public-file') and contains(@id, 'edit-button')]")
    video_remove_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-image-news-0-subform-field-document-public-file') and contains(@id, 'remove-button')]")
    video_popup_video_url_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-media-video-embed')]")
    video_popup_name_xpath = (By.XPATH, "//input[contains(@id, 'edit-name')]")
    video_popup_revision_log_msg_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-revision-log-message')]")
    video_popup_url_alias_xpath = (By.XPATH, "//input[contains(@id, 'edit-path') and contains(@id, 'alias') and contains(@value, 'video')]")
    video_popup_url_save_btn_css = (By.CSS_SELECTOR, "div.ui-dialog-buttonset > button")
    text_color_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-image-news-0-subform-field') and contains(@id, 'text-color')]")
    text_color_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-image-news-0-subform-field') and contains(@id, 'text-color')]/option")
    text_color_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-image-news-0-subform-field') and contains(@for, 'text-color')]")
    hero_title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-image-news-0') and contains(@id, 'field-hero-title')]")
    hero_title_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-image-news-0-subform-field') and contains(@for, 'field-hero-title')]")
    hero_desc_input_xpath = (By.XPATH, "//input[contains(@id, 'image-news-0') and contains(@id, 'field-carousel-description')]")
    hero_desc_label_xpath = (By.XPATH, "//label[contains(@for, 'image-news-0') and contains(@for, 'field-carousel-description')]")
    hero_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'image-news-0') and contains(@id, 'field-hero-title') and contains(@class, 'description')]")
    hero_desc_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'image-news-0') and contains(@id, 'field-carousel-description') and (@class = 'description')]")
    # slideshow_category_option_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'subform-field-category')]/option")
    # slideshow_category_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'subform-field-category')]")
    # slideshow_subcategory_option_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'subform-field-subcategory')]/option")
    # slideshow_subcategory_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'subform-field-subcategory')]")
    carousel_text_layout_option_xpath = (By.XPATH, "//select[contains(@id, 'image-news-0') and contains(@id, 'carousel-text-layout')]/option")
    carousel_text_layout_xpath = (By.XPATH, "//select[contains(@id, 'image-news-0') and contains(@id, 'carousel-text-layout')]")
    carousel_text_layout_label_xpath = (By.XPATH, "//label[contains(@for, 'image-news-0') and contains(@for, 'carousel-text-layout')]")
    field_header_variations_option_xpath = (By.XPATH, "//select[contains(@id, 'image-news-0') and contains(@id, 'field-header-variations')]/option")
    field_header_variations_xpath = (By.XPATH, "//select[contains(@id, 'image-news-0') and contains(@id, 'field-header-variations')]")
    field_header_variations_label_xpath = (By.XPATH, "//label[contains(@for, 'image-news-0') and contains(@for, 'field-header-variations')]")
    hero_txt_uri_xpath = (By.XPATH, "//input[contains(@id, 'image-news-0') and contains(@id, 'hero-text-link') and contains(@id, 'uri')]")
    hero_txt_uri_label_xpath = (By.XPATH, "//label[contains(@for, 'image-news-0') and contains(@for, 'hero-text-link') and contains(@for, 'uri')]")
    hero_txt_link_txt_xpath = (By.XPATH, "//input[contains(@id, 'image-news-0') and contains(@id, 'hero-text-link') and contains(@id, 'title')]")
    hero_txt_link_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'image-news-0') and contains(@for, 'hero-text-link') and contains(@for, 'title')]")
    hero_txt_link_txt_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'image-news-0') and contains(@id, 'hero-text-link') and contains(@id, 'desc') and not(contains(@id, 'uri'))]")
    header_carousel_image_xpath = (By.XPATH,"//div[contains(@id, 'edit-field-image-news-0-subform-field-image-wrapper')]/details/summary/span[contains(@class, 'summary')]")
    


    featured_image_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-featured-image')]/details/summary/span")
    featured_image_select_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-featured-image-entity-browser-entity-browser-open-modal')]")
    featured_image_remove_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-featured-image') and contains(@id,'remove-button')]")

    


  

    def click_featured_news_page(self):

        BasePage.press_button(self, self.add_featured_news_page_xpath)

    def title_ele(self, input_loc, title_label_loc, helper_loc, txt):

        title_txt = BasePage.get_element_text(self, title_label_loc)
        BasePage.send_keys(self, input_loc, txt)
        title_chars_limit_txt = BasePage.get_element_text(self, helper_loc)

        return title_txt, title_chars_limit_txt


    def language_section_ele(self):
        label = BasePage.get_element_text(self,self.language_label_xpath)

        total_languages = len(self.driver.find_elements(*self.language_section_option_xpath))
        index_no = random.randint(1,total_languages-1)
        BasePage.select_dropdown_by_index(self, self.language_input_xpath, index_no)
        language_section_val = self.driver.find_elements(*self.language_section_option_xpath)[index_no].text
        return label, language_section_val

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

    def featured_headline_ele(self,label_loc, iframe_featured_headline_xpath, featured_headline_text):

        featured_news_headline = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*iframe_featured_headline_xpath))
        BasePage.send_keys(self, self.paragraph_css, featured_headline_text)
        self.driver.switch_to.default_content()
        return featured_news_headline



    

    def click_featured_image_link(self, img_loc , select_img_loc, remove_btn_loc):
        BasePage.press_button(self,img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        images = self.driver.find_elements(*self.img_css)
        random_img_index = random.randint(0, len(images) - 1)
        for img in images:
            self.driver.execute_script("arguments[0].click()", images[random_img_index])
            break
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()

        img_remove_btn = BasePage.is_visible(self, remove_btn_loc)

        return img_remove_btn

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)


    def body_paragraph_type_dropdown_ele(self):

        dropdown_contents = self.driver.find_elements(*self.body_paragraph_type_dropdown_xpath)
        dropdown_contents_list = []
        for content in dropdown_contents:
            dropdown_contents_list.append(content.text)

        return dropdown_contents_list


    

    def right_rail_title_ele(self, input_loc, label_loc, helper_loc, txt):

        right_rail_title_helper_txt = BasePage.get_element_text(self, helper_loc)
        right_rail_title_label_txt = BasePage.get_element_text(self, label_loc)

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        if len(BasePage.get_elemet_attribute(self, input_loc, "value")) == 0:
            BasePage.send_keys(self, input_loc, txt)

        return right_rail_title_helper_txt, right_rail_title_label_txt


    def right_rail_desc_ele(self, input_loc, label_loc, txt):

        right_rail_desc_label_txt = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        
        return right_rail_desc_label_txt

    def right_rail_img_ele(self, img_loc, select_img_loc, remove_btn_loc):

        # Adding Image
        BasePage.press_button(self,img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        images = self.driver.find_elements(*self.img_css)
        random_img_index = random.randint(0, len(images) - 1)
        for img in images:
            self.driver.execute_script("arguments[0].click()", images[random_img_index])
            break
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()

        img_remove_btn = BasePage.is_visible(self, remove_btn_loc)

        return img_remove_btn

    def right_rail_tags(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc, input_text):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        right_rail_txt_uri_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        if right_rail_txt_uri_txt == auto_sugg_txt: 
            self.driver.find_element(*input_loc).clear()
            BasePage.send_keys(self, input_loc, input_text) 
        label_txt = BasePage.get_element_text(self, label_loc)
        return  right_rail_txt_uri_txt, label_txt

    def link_type_ele(self,option_loc, label_loc, input_loc):
        links = self.driver.find_elements(*option_loc)
        index_no = random.randint(1,2)

        BasePage.select_dropdown_by_index(self, input_loc, index_no)
        label = BasePage.get_element_text(self,label_loc)
        link_type_section_val = links[index_no].text
        
        return label, link_type_section_val

    
    

    def link_title_ele(self, label_loc, input_loc, helper_loc, txt):

        link_type_title_helper_txt = BasePage.get_element_text(self, helper_loc)
        link_type_title_label_txt = BasePage.get_element_text(self, label_loc)

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        if len(BasePage.get_elemet_attribute(self, input_loc, "value")) == 0:
            BasePage.send_keys(self, input_loc, txt)

        return link_type_title_helper_txt, link_type_title_label_txt



    def link_uri_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc, input_text ):
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        link_uri = BasePage.get_elemet_attribute(self, input_loc, "value")
        if link_uri == auto_sugg_txt: 
            self.driver.find_element(*input_loc).clear()
            BasePage.send_keys(self, input_loc, input_text) 
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt

    

    def add_inner_related_link_btn_ele(self,btn_loc):
        BasePage.press_button(self,btn_loc)

    def add_another_paragraph_btn_ele(self,btn_loc):
        BasePage.press_button(self,btn_loc)

    def page_bottom_drop_down_ele(self, btn_loc, drop_down_value):
        BasePage.press_button(self,btn_loc)
        BasePage.select_dropdown_by_value(self, btn_loc, drop_down_value)



    def tags_ele(self,tags_loc, label_loc):

        BasePage.press_button(self, tags_loc)
       
        BasePage.send_keys(self, tags_loc, "Novartis Social Business (406)")

        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt

    def add_another_item_ele(self , add_another_loc, tag_loc , draggable_items_loc ):

        BasePage.press_button(self, add_another_loc)
        BasePage.is_visible(self,tag_loc)
        list_items = self.driver.find_elements(*draggable_items_loc)
        len_list_items = len(list_items)
        BasePage.send_keys(self,tag_loc,"Novartis Gene Therapies (3381)")
    
        return len_list_items

    def media_categories_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc, input_text):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        media_cat_text = BasePage.get_elemet_attribute(self, input_loc, "value")
        if media_cat_text == auto_sugg_txt:
            self.driver.find_element(*input_loc).clear()
            BasePage.send_keys(self, input_loc, input_text)
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt

    def media_sub_categories_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt3, label_loc, input_text):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt3)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        media_sub_cat_text = BasePage.get_elemet_attribute(self, input_loc, "value")
        if media_sub_cat_text == auto_sugg_txt3:
            self.driver.find_element(*input_loc).clear()
            BasePage.send_keys(self, input_loc, input_text)
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt







    def searchable_section_ele(self, select_loc, option_loc, label_loc):

        total_searchable_section = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_searchable_section-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        searchable_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, searchable_txt

    def news_type_filters_ele(self,input_loc, auto_sugg_loc, auto_sugg_txt2, label_loc, helper_text,input_text):
        BasePage.send_keys(self, input_loc, auto_sugg_txt2)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        tag_text = BasePage.get_elemet_attribute(self, input_loc, "value")
        if tag_text == auto_sugg_txt2:
            self.driver.find_element(*input_loc).clear()
            BasePage.send_keys(self, input_loc, input_text)  
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_text = BasePage.get_element_text(self, helper_text)
        return  tag_text, label_txt, helper_text


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
        index_no = random.randint(1,2)
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


