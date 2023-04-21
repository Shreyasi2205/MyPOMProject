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

class StoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    add_story_page_xpath=(By.XPATH,"//li[contains(@class, 'clearfix')]/a[contains(@href, 'story_page')]")
    title_label_xpath=(By.XPATH,"//input[contains(@id,'edit-title')]/parent::div/label")
    title_xpath=(By.XPATH,"//input[contains(@id,'edit-title')]")
    title_description_xpath = (By.XPATH,"//input[contains(@id,'edit-title')]/parent::div/div")

    author_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-story-author-0-target-id')]")
    author_xpath=(By.XPATH,"//input[contains(@id,'edit-field-story-author-0-target-id') and contains(@class,'form-text ui-autocomplete-input')]")
    published_on_title_xpath=(By.XPATH,"//span[contains(@class,'fieldset-legend')]")
    published_date_xpath=(By.XPATH,"//input[@id='edit-field-date-0-value-date']")
    published_time_xpath=(By.XPATH,"//input[@id='edit-field-date-0-value-time']")
    page_main_category_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-category')]/option")
    page_main_category_select_xpath=(By.XPATH, "//select[contains(@id, 'edit-field-category')]")
    page_main_sub_category_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-sub-category')]/option")
    page_main_sub_category_select_xpath=(By.XPATH, "//select[contains(@id, 'edit-field-sub-category')]")
    page_main_category_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-category')]")
    page_main_sub_category_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-sub-category')]")
    searchable_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]/option")
    searchable_section_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]")
    searchable_section_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-section')]")

    header_image_carousel_xpath=(By.XPATH,"//div[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-wrapper')]/details/summary/span[contains(@class, 'summary')]")
    header_image_carousel_select_css=(By.XPATH,"//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-entity') and contains(@id,'open-modal')]")
    img_select_button_xpath=(By.XPATH,"//input[contains(@class,'is-entity-browser-submit') and contains(@class,'form-submit')]")
    image_iframe_xpath=(By.XPATH,"//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    header_remove_image_xpath=(By.XPATH,"//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-current') and contains(@id, 'remove')]")
    video_iframe_xpath=(By.XPATH,"//iframe[contains(@id, 'entity_browser_iframe_media_browser')]")
    video_submit_btn_xpath=(By.XPATH,"//input[contains(@class,'is-entity-browser-submit') and contains(@class,'form-submit')]")
    header_video_carousel_xpath=(By.XPATH,"//div[contains(@id,'edit-field-header-0') and contains(@id,'subform-field-slideshow-stripe-0') and contains(@id,'subform-field-document-public-file-wrapper')]/details/summary/span")
    header_video_upload_xpath=(By.XPATH,"//input[contains(@id,'edit-field-header-0') and contains(@id,'subform-field-slideshow-stripe-0') and contains(@id,'subform-field-document-public-file-entity') and contains(@id,'browser-open-modal')]")
    video_remove_btn_xpath=(By.XPATH,"//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-document-public-file') and contains(@id, 'remove-button')]")
    video_edit_btn_xpath=(By.XPATH,"//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-document-public-file') and contains(@id, 'edit-button')]")
    save_button_xpath=(By.XPATH,"//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")

    img_css = (By.CSS_SELECTOR, 'img')
    paragraph_css = (By.CSS_SELECTOR, "p")
    header_video_upload_xpath=(By.XPATH,"//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-document-public-file-entity') and contains(@id, 'open-modal')]")
    header_text_color_with_no_panel_xpath=(By.XPATH,"//label[contains(@for,'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@for,'text-color-with-no-panel')]")
    header_text_color_with_no_panel_select_xpath=(By.XPATH,"//select[contains(@id,'edit-field-header-0-subform-field-slideshow-stripe-0-') and contains(@id,'text-color-with-no-panel')]")
    header_text_color_with_no_panel_option_xpath=(By.XPATH,"//select[contains(@id,'edit-field-header-0-subform-field-slideshow-stripe-0-') and contains(@id,'text-color-with-no-panel')]/option")
    header_hero_txt_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-header-0') and contains(@for,'field-hero-title-0-value')]")
    header_hero_txt_input_xpath=(By.XPATH,"//input[contains(@id,'edit-field-header-0') and contains(@id,'field-hero-title-0-value')]")
    header_hero_helper_txt_xpath=(By.XPATH,"//div[contains(@id,'edit-field-header-0') and contains(@id,'field-hero-title-0-value')]")
    header_hero_desc_txt_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-header-0') and contains(@for,'field-carousel-description-0-value')]")
    header_hero_desc_txt_input_xpath=(By.XPATH,"//input[contains(@id,'edit-field-header-0') and contains(@id,'field-carousel-description-0-value')]")
    header_hero_desc_helper_txt_xpath=(By.XPATH,"//div[contains(@id,'edit-field-header-0') and contains(@id,'field-carousel-description-0-value')]")
    header_hero_url_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-header-0') and contains(@for,'field-hero-text-link-0-uri')]")
    header_hero_url_input_xpath=(By.XPATH,"//input[contains(@id,'edit-field-header-0') and contains(@id,'field-hero-text-link-0-uri')]")
    header_hero_link_txt_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-header-0') and contains(@for,'field-hero-text-link-0-title')]")
    header_hero_link_txt_input_xpath=(By.XPATH,"//input[contains(@id,'edit-field-header-0') and contains(@id,'field-hero-text-link-0-title')]")
    header_hero_link_txt_helper_txt_xpath=(By.XPATH,"//div[contains(@id,'edit-field-header-0') and contains(@id,'field-hero-text-link-0--description')]")
    header_carousel_txt_layout_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-header-0') and contains(@for,'field-carousel-text-layout')]")
    header_carousel_txt_layout_select_xpath=(By.XPATH,"//select[contains(@id,'edit-field-header-0') and contains(@id,'field-carousel-text-layout')]")
    header_carousel_txt_layout_option_xpath=(By.XPATH,"//select[contains(@id,'edit-field-header-0') and contains(@id,'field-carousel-text-layout')]/option")
    header_header_variation_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-header-0') and contains(@for,'field-header-variations')]")
    header_header_variation_select_xpath=(By.XPATH,"//select[contains(@id,'edit-field-header-0') and contains(@id,'field-header-variations')]")
    header_header_variation_option_xpath=(By.XPATH,"//select[contains(@id,'edit-field-header-0') and contains(@id,'field-header-variations')]")
    add_slideshow_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-add-more-add-more-button-slideshow')]")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")

    add_paragraph_btn_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]/option")
    add_paragraph_btn_select_xpath=(By.XPATH,"//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_body_xpath=(By.XPATH,"//input[contains(@id,'edit-field-body-add-more-add-more-button')]")

    add_right_hand_rail_option_xpath=(By.XPATH,"//select[contains(@id,'edit-field-right-rail-add-more-add-more-select')]/option")
    add_right_hand_rail_select_xpath=(By.XPATH,"//select[contains(@id,'edit-field-right-rail-add-more-add-more-select')]")
    add_paragraph_right_hand_rail_xpath=(By.XPATH,"//input[(contains(@id,'edit-field-right-rail-add-more-add-more-button'))]")
    related_link_type_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-right-rail') and contains(@for,'subform-field-link-type')]")
    related_link_type_select_xpath=(By.XPATH,"//select[contains(@id,'edit-field-right-rail') and contains(@id,'subform-field-inner-related-links') and contains(@id,'subform-field-link-type')]")
    related_link_type_option_xpath=(By.XPATH,"//select[contains(@id,'edit-field-right-rail') and contains(@id,'subform-field-inner-related-links') and contains(@id,'subform-field-link-type')]/option")
    related_link_txt_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-right-rail') and contains(@for,'subform-field-related-links-title')]")
    related_link_input_xpath=(By.XPATH,"//input[contains(@id,'edit-field-right-rail') and contains(@id,'subform-field-related-links-title')]")
    related_link_helper_txt_xpath=(By.XPATH,"//div[contains(@class,'field--name-field-related-links-title')] /div/div[contains(@id,'edit-field-right-rail') and contains(@id,'subform-field-related-links-title')]")
    related_link_uri_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-right-rail') and contains(@for,'subform-field-inner-related-links') and contains(@for,'subform-field-url')]")
    related_link_uri_input_xpath=(By.XPATH,"//input[contains(@id,'edit-field-right-rail') and contains(@id,'subform-field-inner-related-links') and contains(@id,'subform-field-url')]")
    related_link_title="Related Links"
    related_link_url="Novartis Access fact sheet (17796)"
    button_label_right_hand_xpath=(By.XPATH,"//div[contains(@class,'js-form-type-entity-autocomplete')]/label[contains(@for,'edit-field-right-rail') and contains(@for,'subform-field-button')]")
    button_input_right_hand_xpath=(By.XPATH,"//div[contains(@class,'js-form-type-entity-autocomplete')]/input[contains(@id,'edit-field-right-rail') and contains(@id,'subform-field-button')]")
    button_link_txt_label_right_hand_xpath=(By.XPATH,"//div[contains(@class,'js-form-type-textfield')]/label[contains(@for,'edit-field-right-rail') and contains(@for,'subform-field-button')]")
    button_linl_txt_input_right_hand_xpath=(By.XPATH,"//div[contains(@class,'js-form-type-textfield')]/input[contains(@id,'edit-field-right-rail') and contains(@id,'subform-field-button')]")
    button_url_right_hand="Novartis Financial Results - Q2 2018 Infographic (19626)"
    button_link_txt_right_hand="Button Right Hand Text"

    feature_img_iframe_xpath=(By.XPATH,"//iframe[contains(@class,'entity-browser-modal-iframe')]")
    feature_img_xpath=(By.XPATH,"//div[contains(@class,'field--name-field-story-image')]/details/summary/span[1]")
    feature_img_select_xpath=(By.XPATH,"//input[contains(@id,'edit-field-story-image') and contains(@id,'browser-open-modal')]")
    feature_img_select_btn_xpath=(By.XPATH,"//input[contains(@class,'is-entity-browser-submit') and contains(@class,'button--primary') and contains(@class,'form-submit')]")
    feature_remove_btn_xpath=(By.XPATH,"//input[contains(@id,'edit-field-story-image-current') and contains(@id,'remove-button')]")

    error_msg_list = ["Searchable in section field is required."]
    error_msg_css = (By.CSS_SELECTOR, ".messages--error > div ")
    body_content_list = ["Call Out","Call to Action","Media Content","Rich Text Content","Big Numbers","Arctic Iframe","Image Gallery Slider","Contacts","Slideshow Carousel","Media Release","Video Playlist","Tab Content","In this section","Button","Webform","Paragraph Library Block Content","Related Stories"]

    right_hand_rail_list=["Related Links","Rich Text Content","Button"]

    language_label_xpath=(By.XPATH,"//label[contains(@for,'edit-langcode-0-value')]")
    language_option_xpath=(By.XPATH,"//select[contains(@id,'edit-langcode-0-value')]/option")
    language_select_xpath=(By.XPATH,"//select[contains(@id,'edit-langcode-0-value')]")

    legend_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Legend field')]")
    legend_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-legend-0-value')]")

    disclaimer_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Disclaimer field')]")
    disclaimer_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-disclaimer-0-value')]")

    feature_headline_iframe_xpath=(By.XPATH,"//iframe[contains(@class,'cke_wysiwyg_frame') and contains(@class,'cke_reset')]")
    feature_headline_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-story-intro-text-0-value')]")

    additional_subcat_xpath=(By.XPATH,"//input[contains(@id,'edit-field-tags-0-target-id')]")
    

    success_msg_css = (By.CSS_SELECTOR, ".alert.alert-dismissible")
    notify_index_id = (By.ID, "edit-index-now")

    news_type_filters_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-news-type-filters-0-target-id')]")
    news_type_filters_input_xpath=(By.XPATH,"//input[contains(@id,'edit-field-news-type-filters-0-target-id')]")

    save_as_label_xpath=(By.XPATH,"//label[contains(@for,'edit-moderation-state-0-state')]")
    save_as_select_xpath=(By.XPATH,"//select[contains(@id,'edit-moderation-state-0-state')]")
    save_as_option_xpath=(By.XPATH,"//select[contains(@id,'edit-moderation-state-0-state')]/option")
    save_as_txt="Published"
    languages=["en","de","fr"]
    header_hero_txt="Header Hero Text"
    header_hero_desc="Header Hero Description"

    date = now.strftime("%d/%M/%Y")
    time = now.strftime("%H:%M:%S")

    story_page="Sample Story Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    author_name="Maryse Jandrasits (1491)"
    header_url_auto_sugg_txt="nov"
    header_hero_link_txt="Header Link Text"
    featured_headline_txt="We aim for sustainable performance over time to benefit patients, employees, shareholders and society. Solid financial results and maintaining the trust of society underpin our ability to create value"
    header_variation=["large","small"]
    news_type_filter_txt="Pulse Update (2086)"
    additional_sub_cat_txt = "New Scientific Discoveries (576)"
    legend_txt = "SAMPLE LEGEND TEXT"
    disclaimer_txt = "SAMPLE DISCLAIMER TEXT"

    bold_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__bold_icon")
    iframe_rich_txt_rail_xpath=(By.XPATH,"//iframe[contains(@class,'cke_wysiwyg_frame') and contains(@class,'cke_reset')]")
    text_css = (By.CSS_SELECTOR,'body p')
    after_text_pass_css = (By.CSS_SELECTOR,"body p strong")
    
    def click_story_page(self):
        BasePage.press_button(self,self.add_story_page_xpath)
    
    def body_dropdown_ele(self):

        dropdown_contents = self.driver.find_elements(*self.add_paragraph_btn_option_xpath)
        dropdown_contents_list = []
        for content in dropdown_contents:
            dropdown_contents_list.append(content.text)

        return dropdown_contents_list
    
    def right_hand_rail_dropdown_ele(self):

        dropdown_contents = self.driver.find_elements(*self.add_right_hand_rail_option_xpath)
        dropdown_contents_list = []
        for content in dropdown_contents:
            dropdown_contents_list.append(content.text)

        return dropdown_contents_list
    
    
    def click_paragraph_dropdown_ele(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph_ele(self,btn_loc):
        BasePage.press_button(self, btn_loc)
    
    def related_link_type_ele(self,selec_loc,option_loc,label_loc):
        link_types_len=len(self.driver.find_elements(*option_loc))
        index_no=random.randint(1,link_types_len-1)
        BasePage.select_dropdown_by_index(self,selec_loc,index_no)
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def related_link_txt_ele(self,input_loc,label_loc,helper_txt_loc,txt):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        label_txt=BasePage.get_element_text(self,label_loc)
        helper_txt=BasePage.get_element_text(self,helper_txt_loc)
        return label_txt, helper_txt
    
    def related_link_uri_ele(self,input_loc,label_loc,txt):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def bold_icon(self,frame):
        display_status_bold = False
        display_status_bold =  BasePage.is_displayed(self,self.bold_icon_css) 
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        BasePage.press_button(self, self.text_css)
        BasePage.send_keys(self,self.text_css,Utilities.RichtextContent_data)
        self.driver.switch_to.default_content()
        BasePage.press_button(self, self.text_css)
        if 'Windows' in platform.system():
            a = ActionChains(self.driver)
            a.key_down(Keys.CONTROL).send_keys('a').perform()
        elif 'Darwin' in platform.system():
            a = ActionChains(self.driver)
            a.key_down(Keys.COMMAND).send_keys('a').perform()
        BasePage.press_button(self, self.bold_icon_css)
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        font_weight = BasePage.get_css_property(self,self.after_text_pass_css,'font-weight')
        self.driver.switch_to.default_content()

        return display_status_bold, font_weight
    
    def button_uri_ele(self,input_loc,label_loc,txt):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt

    def button_uri_link_txt_ele(self,input_loc,label_loc,txt):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def language_ele(self,select_loc,label_loc):
        language_index=random.randint(0,len(self.languages)-1)
        BasePage.select_dropdown_by_value(self,select_loc,self.languages[language_index])
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt
    
    
    def title_ele(self,input_loc,label_loc,helper_loc,txt):
        title_txt=BasePage.get_element_text(self,label_loc)
        BasePage.send_keys(self,input_loc,txt)
        title_char_limit_txt=BasePage.get_element_text(self,helper_loc)
        return title_txt, title_char_limit_txt
    
    def author_ele(self,input_loc,label_loc,txt):
        title_txt=BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        return title_txt
    
    
    def published_ele(self,label_loc,date_loc,time_loc,date,time):
        title_txt=BasePage.get_element_text(self,label_loc)
        BasePage.do_click(self,date_loc)
        BasePage.send_keys(self,date_loc,date)
        BasePage.do_click(self,time_loc)
        BasePage.send_keys(self,time_loc,time)
        return title_txt
    
    def page_main_category_ele(self,select_loc,option_loc,label_loc):
        total_category=len(self.driver.find_elements(*option_loc))
        index_no=random.randint(1,total_category-1)
        BasePage.select_dropdown_by_index(self,select_loc,index_no)
        page_main_category_txt=self.driver.find_elements(*option_loc)[index_no].text
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt,page_main_category_txt
    
    def page_main_sub_category_ele(self,select_loc,option_loc,label_loc):
        total_category=len(self.driver.find_elements(*option_loc))
        index_no=random.randint(1,total_category-1)
        BasePage.select_dropdown_by_index(self,select_loc,index_no)
        page_main_sub_category_txt=self.driver.find_elements(*option_loc)[index_no].text
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt, page_main_sub_category_txt
    
    def searchable_section_ele(self,select_loc,option_loc,label_loc):
        total_searchable_section=len(self.driver.find_elements(*option_loc))
        index_no=random.randint(1,total_searchable_section-1)
        BasePage.select_dropdown_by_index(self,select_loc,index_no)
        searchable_section_txt=self.driver.find_elements(*option_loc)[index_no].text
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt,searchable_section_txt
    
    def legend_ele(self,txt):
        self.driver.switch_to.frame(self.driver.find_element(*self.legend_iframe_xpath))
        BasePage.send_keys(self,self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        label_txt=BasePage.get_element_text(self,self.legend_label_xpath)
        return label_txt
    
    def disclaimer_ele(self,txt):
        self.driver.switch_to.frame(self.driver.find_element(*self.disclaimer_iframe_xpath))
        BasePage.send_keys(self,self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        label_txt=BasePage.get_element_text(self,self.disclaimer_label_xpath)
        return label_txt
    
    def header_slideshow_carousel_img_ele(self,img_loc,select_img_loc,select_btn_loc,remove_btn_loc):

        #Adding image
        BasePage.press_button(self,img_loc)
        BasePage.press_button(self,select_img_loc)
        if(len(self.driver.find_elements(*self.image_iframe_xpath))==0):
            BasePage.press_button(self,select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        images=self.driver.find_elements(*self.img_css)
        random_img_indx=random.randint(0,len(images)-1)
        for img in images:
            self.driver.execute_script("arguments[0].click()",images[random_img_indx])
            break
        BasePage.press_button(self,select_btn_loc)
        self.driver.switch_to.default_content()
        img_remove_btn=BasePage.is_visible(self,remove_btn_loc)
        return img_remove_btn
    
    def header_video_carousel_ele(self,video_loc,upload_video_loc,submit_btn_loc,edit_btn_loc,remove_btn_loc):
        BasePage.press_button(self,video_loc)
        BasePage.press_button(self,upload_video_loc)
        if(len(self.driver.find_elements(*self.video_iframe_xpath))==0):
            BasePage.press_button(self,upload_video_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.video_iframe_xpath))
        videos=self.driver.find_elements(*self.img_css)
        random_video_indx=random.randint(0,len(videos)-1)
        for video in videos:
            self.driver.execute_script("arguments[0].click()",videos[random_video_indx])
            break
        BasePage.press_button(self,submit_btn_loc)
        self.driver.switch_to.default_content()
        video_edit_btn=BasePage.get_elemet_attribute(self,edit_btn_loc,"value")
        video_remove_btn=BasePage.get_elemet_attribute(self,remove_btn_loc,"value")
        return video_edit_btn,video_remove_btn

    def add_more_slideshow(self):
        BasePage.press_button(self,self.add_slideshow_xpath)
    
    def text_color_ele(self,label_loc,option_loc,select_loc):
        text_colors=self.driver.find_elements(*option_loc)
        title_txt=BasePage.get_element_text(self,label_loc)
        index_no=random.randint(0,2)
        BasePage.select_dropdown_by_index(self,select_loc,index_no)
        text_color_val=text_colors[index_no].text
        return title_txt,text_color_val
    
    def hero_txt_ele(self,input_loc,label_loc,helper_txt_loc,txt):
        hero_title_txt=BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self,input_loc,txt)
        if len(BasePage.get_elemet_attribute(self, input_loc, "value")) == 0:
            BasePage.send_keys(self, input_loc, txt)
        hero_helper_txt=BasePage.get_element_text(self,helper_txt_loc)
        return hero_title_txt,hero_helper_txt
    
    def hero_txt_desc_ele(self,input_loc,label_loc,helper_txt_loc,txt):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        hero_desc_helper_txt = BasePage.get_element_text(self, helper_txt_loc)
        hero_desc_label_txt = BasePage.get_element_text(self, label_loc)
        return hero_desc_helper_txt, hero_desc_label_txt
    
    def hero_txt_uri_ele(self,input_loc,label_loc, auto_sugg_loc,auto_sugg_txt):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,auto_sugg_txt)
        auto_suggestions=self.driver.find_elements(*auto_sugg_loc)
        sugg_len=len(auto_suggestions)
        random_num=random.randint(0,sugg_len-1)
        self.driver.execute_script("arguments[0].click()",auto_suggestions[random_num])
        #hero_txt_uri_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        label_txt = BasePage.get_element_text(self, label_loc)
        return   label_txt
    
    def hero_link_txt_ele(self,input_loc,label_loc,helper_txt_loc,txt):
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        hero_txt_link_txt_helper_txt = BasePage.get_element_text(self, helper_txt_loc)
        hero_txt_link_txt_label_txt = BasePage.get_element_text(self, label_loc)
        return hero_txt_link_txt_helper_txt, hero_txt_link_txt_label_txt
    
    def carousel_txt_layout_ele(self,select_loc,option_loc,label_loc):
        txt_layouts=self.driver.find_elements(*option_loc)
        index_no=random.randint(1,2)
        BasePage.select_dropdown_by_index(self,select_loc,index_no)
        title_txt=BasePage.get_element_text(self,label_loc)
        layout_txt=txt_layouts[index_no].text
        return title_txt,layout_txt
    
    def field_header_variation_ele(self, select_loc, label_loc,txt):

        BasePage.select_dropdown_by_value(self,select_loc,txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        
        return label_txt
    
    

    
    def featured_headline_ele(self,label_loc,txt):
        self.driver.switch_to.frame(self.driver.find_element(*self.feature_headline_iframe_xpath))
        BasePage.send_keys(self,self.paragraph_css,txt)
        self.driver.switch_to.default_content()
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def featured_img_ele(self,img_loc,select_img_loc,select_btn_loc,remove_btn_loc):

        #Adding image
        BasePage.press_button(self,img_loc)
        BasePage.press_button(self,select_img_loc)
        if(len(self.driver.find_elements(*self.feature_img_iframe_xpath))==0):
            BasePage.press_button(self,select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.feature_img_iframe_xpath))
        images=self.driver.find_elements(*self.img_css)
        random_img_indx=random.randint(0,len(images)-1)
        for img in images:
            self.driver.execute_script("arguments[0].click()",images[random_img_indx])
            break
        BasePage.press_button(self,select_btn_loc)
        self.driver.switch_to.default_content()
        img_remove_btn=BasePage.is_visible(self,remove_btn_loc)
        return img_remove_btn
    
    def news_type_filter_ele(self,input_loc,label_loc,txt):
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self,input_loc,txt)
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt
    
    def additional_subcats_ele(self, input_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
    
    def save_as_ele(self,select_loc,label_loc):
        #save_as_types=self.driver.find_elements(*option_loc)
        BasePage.select_dropdown_by_value(self,select_loc,"published")
        label_txt=BasePage.get_element_text(self,label_loc)
        return label_txt

    def save_btn_ele(self):

        BasePage.press_button(self, self.save_button_xpath)

    def error_msg_ele(self):

        error_msgs = []
        BasePage.press_button(self, self.save_button_xpath)
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

    
        

    


    







