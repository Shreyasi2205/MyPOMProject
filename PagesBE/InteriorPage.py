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

class InteriorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    interior_page = "Sample Interior Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")
    interior_healthcare_page = "Sample Interior HealthCare Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")


    add_interior_page_xpath = (By.XPATH, "//a[contains(@href, 'interior_page')]/span")
    title_txt_xpath = (By.XPATH, "//label[contains(@for, 'edit-title')]")
    title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-title')]")
    hide_title_input_xpath = (By.XPATH, "//input[contains(@id, 'hide-title')]")
    hide_title_txt_xpath = (By.XPATH, "//label[contains(@for, 'hide-title')]")
    title_chars_limit_txt_xpath = (By.XPATH, "//div[contains(@id, 'value--description') and contains(@id, 'edit-title')]")
    error_msg_css = (By.CSS_SELECTOR, ".messages--error > div ")
    save_btn_id = (By.CSS_SELECTOR, '[id="edit-submit"]')
    intro_txt_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-field-intro-text')]")
    intro_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-intro-text')]")
    page_main_category_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-category')]/option")
    page_main_sub_category_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-sub-category')]/option")
    page_main_category_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-category')]")
    page_main_category_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-category')]")
    page_main_sub_category_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-sub-category')]")
    page_main_sub_category_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-sub-category')]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    header_add_paragraph_xpath = (By.XPATH,"//input[contains(@class,'field-add-more-submit') and contains(@data-drupal-selector,'edit-field-header-add-more-add-more-button')]")
    header_hero_txt_uri_xpath= (By.XPATH,"//input[contains(@id,'edit-field-header-0') and contains(@id,'subform-field-slideshow-stripe-0') and contains(@id,'subform-field-hero-text-link-0-uri')]")
    header_hero_txt_uri_label_xpath=(By.XPATH,"//label[contains(@for,'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-hero-text-link-0-uri')]")
    right_hand_rail_uri_txt="Novartis Social Business Report 2018 (19786)"
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    header_carousel_image_xpath = (By.XPATH,"//div[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-wrapper')]/details/summary/span[contains(@class, 'summary')]")
    img_remove_button_xpath = (By.XPATH,"//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-current') and contains(@id, 'remove')]")
    slideshow_carousel_select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0-subform-field-image-entity') and contains(@id, 'open-modal')]")
    img_css = (By.CSS_SELECTOR, 'img')
    text_color_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@id, 'text-color')]")
    text_color_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@id, 'text-color')]/option")
    text_color_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@for, 'text-color')]")
    hero_title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@id, 'field-hero-title')]")
    hero_title_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-header-0-subform-field-slideshow-stripe-0') and contains(@for, 'field-hero-title')]")
    hero_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-hero-title') and contains(@class, 'description')]")
    hero_desc_input_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-carousel-description')]")
    hero_desc_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'field-carousel-description')]")
    hero_desc_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-carousel-description') and (@class = 'description')]")
    hero_txt_uri_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'hero-text-link') and contains(@id, 'uri')]")
    header_hero_text_uri_xpath=(By.XPATH,"//input[contains(@id, 'edit-field-header-0') and contains(@id, 'slideshow-stripe-0') and contains(@id, 'hero-text-link') and contains(@id, 'uri')]")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    hero_txt_uri_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'hero-text-link') and contains(@for, 'uri')]")
    header_hero_txt_uri_label_xpath=(By.XPATH,"//label[contains(@for, 'edit-field-header-0') and contains(@for, 'slideshow-stripe-0') and contains(@for, 'hero-text-link') and contains(@for, 'uri')]")
    hero_txt_link_txt_xpath = (By.XPATH, "//input[contains(@id, 'slideshow-stripe-0') and contains(@id, 'hero-text-link') and contains(@id, 'title')]")
    hero_txt_link_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'hero-text-link') and contains(@for, 'title')]")
    hero_txt_link_txt_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'slideshow-stripe-0') and contains(@id, 'hero-text-link') and contains(@id, 'desc') and not(contains(@id, 'uri'))]")
    carousel_text_layout_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'carousel-text-layout')]")
    carousel_text_layout_option_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'carousel-text-layout')]/option")
    carousel_text_layout_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'carousel-text-layout')]")
    field_header_variations_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-header-variations')]")
    field_header_variations_option_xpath = (By.XPATH, "//select[contains(@id, 'slideshow-stripe-0') and contains(@id, 'field-header-variations')]/option")
    field_header_variations_label_xpath = (By.XPATH, "//label[contains(@for, 'slideshow-stripe-0') and contains(@for, 'field-header-variations')]")

    body_dropdown_xpath=(By.XPATH,"//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    body_content_list= ["call_out", "call_to_action", "rich_text_content", "media_content", "careers_highlights", "biography", "accordion", "cards", "slideshow_carousel", "big_numbers_parent", "arctic_iframe", "image_galery_slider", "contacts", "media_release", "video_playlist", "tab_content", "in_this_section", "button","paragraph_library_block_content", "supplier_invoice", "webform", "image_content"]
    body_add_paragraph_xpath = (By.XPATH,"//input[@name='field_body_add_more']")
    
    right_hand_rail_select_xpath = (By.XPATH,"//select[contains(@id,'edit-field-right-rail')]")
    right_hand_rail_label_xpath = (By.XPATH,"//div[contains(@id,'edit-field-right-rail')]/strong")
    right_hand_rail_add_paragraph_xpath = (By.XPATH,"//input[contains(@id,'right-rail-add-more-add-more-button')]")
    right_hand_rail_title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'field-title')]")
    right_hand_rail_title_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'field-title-card')]")
    right_hand_rail_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'field-title') and contains(@class, 'description')]")
    right_hand_rail_desc_input_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-description-card')]")
    right_hand_rail_desc_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'field-description')]")
    right_hand_rail_txt_uri_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'cta-button') and contains(@id, 'uri')]")
    right_hand_rail_txt_uri_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'cta-button') and contains(@for, 'uri')]")
    right_hand_rail_link_txt_xpath = (By.XPATH, "//input[contains(@id, 'right-rail-0') and contains(@id, 'cta-button') and contains(@id, 'title')]")
    right_hand_rail_link_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'cta-button') and contains(@for, 'title')]")
    
    related_links_select_xpath = (By.XPATH,"//select[contains(@id,'edit-field-right-rail-add-more-add-more-select')]")
    related_links_title_input_xpath = (By.XPATH, "//input[contains(@id, 'field-related-links-title-0') and contains(@id, 'edit-field-right-rail-0')]")
    related_links_title_label_xpath = (By.XPATH, "//label[contains(@for, 'field-related-links-title-0') and contains(@for, 'edit-field-right-rail-0')]")
    related_links_desc_input_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subform-field-related-links')]")
    related_links_desc_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'field-related-links-desc')]")
    related_links_image_xpath = (By.XPATH,"//div[contains(@id, 'edit-field-right-rail-0')]/details/summary/span[contains(@class, 'summary')]")
    related_links_select_img_xpath = (By.XPATH,"//input[contains(@id, 'edit-field-right-rail-0-subform-field-image') and contains(@id, 'open-modal')]")
    related_links_img_remove_button_xpath = (By.XPATH,"//input[contains(@id, 'edit-field-right-rail-0-subform-field-image') and contains(@id, 'remove')]")
    related_links_tags_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'subcategory')]")
    related_links_tags_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'field-subcategory')]")
    links_url_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'inner-related-links') and contains(@id, 'uri')]")
    links_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'related-links') and contains(@for, 'uri')]")
    link_type_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-right-rail-0') and contains(@id,'inner-related-links') and contains(@id,'link-type')]")
    link_type_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-right-rail-0') and contains(@id,'inner-related-links') and contains(@id,'link-type')]/option")
    link_type_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for,'link-type')]")
    link_type_title_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id,'field-title')]")
    link_type_title_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for,'field-title')]")
    link_type_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'field-title') and contains(@class, 'description')]")
    
    button_select_xpath = (By.XPATH,"//select[contains(@id,'edit-field-right-rail-add-more-add-more-select')]")
    button_uri_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'button') and contains(@id, 'uri')]")
    button_txt_uri_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'button') and contains(@for, 'uri')]")
    button_link_txt_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-right-rail-0') and contains(@id, 'button') and contains(@id, 'title')]")
    button_link_txt_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-right-rail-0') and contains(@for, 'button') and contains(@for, 'title')]")
    
    searchable_section_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]")
    searchable_section_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-section')]")
    searchable_section_option_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-section')]/option")
    additional_subcats_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-tags') and contains(@id, 'target-id')]")
    legend_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Legend field')]")
    paragraph_css = (By.CSS_SELECTOR, "p")
    legend_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-legend-0-value')]")
    disclaimer_iframe_xpath = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor, Disclaimer field')]")
    disclaimer_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-field-disclaimer-0-value')]")
    publish_xpath = (By.XPATH, "//select[contains(@id, 'edit-moderation-state')]")
    success_msg_css = (By.CSS_SELECTOR, ".alert.alert-dismissible.alert-success")
    
    error_msg_list = ["Searchable in section field is required."]
    intro_txt = "Intro Text"
    hero_title_txt = "SAMPLE HERO TITLE"
    hero_desc_txt =  "SAMPLE HERO DESCRIPTION"
    auto_sugg_txt = "nov"
    hero_link_txt = "SAMPLE HERO TXT LINK TXT @#%^&124743"
    right_hand_rail_value = 'right_hand_rail_card'
    right_hand_rail_title_txt = "SAMPLE RIGHT HAND RAIL TITLE"
    right_hand_rail_desc_txt =  "SAMPLE RIGHT HAND RAIL DESCRIPTION"
    right_hand_rail_link_txt = "SAMPLE HERO TXT LINK TXT @#%^&124743"
    related_links_value = 'related_links'
    related_links_desc_txt =  "SAMPLE RELATED LINKS DESCRIPTION"
    link_type_title_txt = "SAMPLE LINK TITLE"
    button_value = 'button'
    button_link_txt = "SAMPLE BUTTON @#%^&124743"
    legend_txt = "SAMPLE LEGEND TEXT"
    disclaimer_txt = "SAMPLE DISCLAIMER TEXT"
    additional_sub_cat_txt = "New Scientific Discoveries (576)"
    sample_investors_page = "Sample Investors Page : " + now.strftime("%m/%d/%Y, %H:%M:%S")

    no_content_box_label_xpath= "//label[@for='edit-field-header-1-subform-field-slideshow-stripe-0-subform-field-no-content-box-value--3ImRwETJLMM']"
    no_content_box_input_xpath= "//input[@id='edit-field-header-1-subform-field-slideshow-stripe-0-subform-field-no-content-box-value--3ImRwETJLMM']"

    right_hand_rail_uri_txt= "Novartis Social Business Report 2018 (19786)"



    def click_interior_page(self):

        BasePage.press_button(self, self.add_interior_page_xpath)

    def title_ele(self, input_loc, title_label_loc, hide_title_label_loc, selected_status_loc, helper_loc, txt):

        title_txt = BasePage.get_element_text(self, title_label_loc)
        BasePage.send_keys(self, input_loc, txt)
        hide_title_txt = BasePage.get_element_text(self, hide_title_label_loc)
        self.press_button(self.hide_title_input_xpath)
        selectetd_status = BasePage.is_selected(self, selected_status_loc)
        title_chars_limit_txt = BasePage.get_element_text(self, helper_loc)

        return title_txt, hide_title_txt, selectetd_status, title_chars_limit_txt


    def error_msg_ele(self):

        error_msgs = []
        BasePage.press_button(self, self.save_btn_id)
        error_msg_contents = self.driver.find_elements(*self.error_msg_css)
        for err in error_msg_contents:
            error_msgs.append(err.text)

        return error_msgs


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


    def header_add_paragraph(self):

        BasePage.press_button(self,self.header_add_paragraph_xpath)

    # def no_content_box_ele(self, label_loc, input_loc, flag):
    #     is_checked_false=BasePage.is_selected(self,input_loc)
    #     is_checked_true= False
    #     if flag==1:
    #         BasePage.press_button(self,input_loc)
    #         is_checked_true=BasePage.is_selected(self,input_loc)
    #     label_txt=BasePage.get_element_text(self,label_loc)

    #     return is_checked_false, is_checked_true, label_txt


    def header_slideshow_carousel_img_ele(self, img_loc, select_img_loc, remove_btn_loc):

        # Adding Image
        if len(self.driver.find_elements(*self.header_carousel_image_xpath)) == 0:
            BasePage.press_button(self,self.header_add_paragraph_xpath)
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



    def text_color_ele(self, select_loc, option_loc, label_loc):

        text_colors = self.driver.find_elements(*option_loc)
        index_no = random.randint(0,2)
        BasePage.select_dropdown_by_index(self, select_loc , index_no)
        label_txt = BasePage.get_element_text(self, label_loc)
        text_color_val = text_colors[index_no].text

        return text_color_val, label_txt

    def hero_txt_ele(self, input_loc, label_loc, helper_loc, txt):

        hero_title_helper_txt = BasePage.get_element_text(self, helper_loc)
        hero_title_label_txt = BasePage.get_element_text(self, label_loc)

        BasePage.press_button(self, input_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        print(BasePage.get_elemet_attribute(self, input_loc, "value"))
        if len(BasePage.get_elemet_attribute(self, input_loc, "value")) == 0:
            BasePage.send_keys(self, input_loc, txt)
        return hero_title_helper_txt, hero_title_label_txt

    def hero_desc_ele(self, input_loc, label_loc, helper_loc, txt):

        hero_desc_label_txt = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        hero_desc_helper_txt = BasePage.get_element_text(self, helper_loc)
        return hero_desc_label_txt, hero_desc_helper_txt

    def hero_txt_uri_ele_auto_sugg(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        hero_txt_uri_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        label_txt = BasePage.get_element_text(self, label_loc)
        return  hero_txt_uri_txt, label_txt
    
    def hero_txt_uri_ele_manual(self, input_loc, label_loc):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, "Novartis Social Business Report 2018 (19786)")
        label_txt = BasePage.get_element_text(self, label_loc)
        return  label_txt

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


    def right_hand_rail_ele(self,select_loc,value_name, label_loc):

        BasePage.select_dropdown_by_value(self, select_loc, value_name)
        label_txt = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self,self.right_hand_rail_add_paragraph_xpath)

        return label_txt


    def right_hand_rail_title_ele(self, input_loc, label_loc, helper_loc, txt):

        right_hand_rail_title_helper_txt = BasePage.get_element_text(self, helper_loc)
        right_hand_rail_title_label_txt = BasePage.get_element_text(self, label_loc)

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        if len(BasePage.get_elemet_attribute(self, input_loc, "value")) == 0:
            BasePage.send_keys(self, input_loc, txt)

        return right_hand_rail_title_helper_txt, right_hand_rail_title_label_txt


    def right_hand_rail_desc_ele(self, input_loc, label_loc, txt):

        right_hand_rail_desc_label_txt = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        
        return right_hand_rail_desc_label_txt

    def right_hand_rail_manual_txt_uri_ele(self, input_loc, txt, label_loc):
        
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        return  label_txt


    def right_hand_rail_txt_uri_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        right_hand_rail_txt_uri_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        label_txt = BasePage.get_element_text(self, label_loc)
        return  right_hand_rail_txt_uri_txt, label_txt
    
    def right_hand_rail_manual_txt_uri_ele(self, input_loc, txt, label_loc):
        
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        return  label_txt

    def right_hand_rail_link_txt_ele(self, input_loc, label_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        right_hand_rail_txt_link_txt_label_txt = BasePage.get_element_text(self, label_loc)
        return  right_hand_rail_txt_link_txt_label_txt


    def related_links_ele(self,select_loc,value_name):

        BasePage.select_dropdown_by_value(self, select_loc, value_name)
        BasePage.press_button(self,self.right_hand_rail_add_paragraph_xpath)

       


    def related_links_title_ele(self, input_loc, label_loc, helper_loc, txt):

        related_links_title_helper_txt = BasePage.get_element_text(self, helper_loc)
        related_links_title_label_txt = BasePage.get_element_text(self, label_loc)

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        if len(BasePage.get_elemet_attribute(self, input_loc, "value")) == 0:
            BasePage.send_keys(self, input_loc, txt)

        return related_links_title_helper_txt, related_links_title_label_txt


    def related_links_desc_ele(self, input_loc, label_loc, txt):

        related_links_desc_label_txt = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        
        return related_links_desc_label_txt


    def related_links_img_ele(self, img_loc, select_img_loc, remove_btn_loc):

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


    def related_links_tags(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        right_hand_rail_txt_uri_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        label_txt = BasePage.get_element_text(self, label_loc)
        return  right_hand_rail_txt_uri_txt, label_txt


    def link_type_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, "Novartis Social Business Report 2018 (19786)")
        label_txt = BasePage.get_element_text(self, label_loc)
        return label_txt

    def link_type_title_ele(self, select_loc, option_loc, label_loc):

        total_category = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_category-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        link_tytpe_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, link_tytpe_txt

    def related_links_link_title_ele(self, input_loc, label_loc, helper_loc, txt):

        related_links_link_title_helper_txt = BasePage.get_element_text(self, helper_loc)
        related_links_link_title_label_txt = BasePage.get_element_text(self, label_loc)

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        if len(BasePage.get_elemet_attribute(self, input_loc, "value")) == 0:
            BasePage.send_keys(self, input_loc, txt)

        return related_links_link_title_helper_txt, related_links_link_title_label_txt


    def add_button_ele(self,select_loc,value_name):

        BasePage.select_dropdown_by_value(self, select_loc, value_name)
        BasePage.press_button(self,self.right_hand_rail_add_paragraph_xpath)


    def button_ele(self, input_loc, auto_sugg_loc, auto_sugg_txt, label_loc):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*auto_sugg_loc)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        right_hand_rail_txt_uri_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        label_txt = BasePage.get_element_text(self, label_loc)
        return  right_hand_rail_txt_uri_txt, label_txt


    def button_link_txt_ele(self, input_loc, label_loc, txt):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        right_hand_rail_txt_link_txt_label_txt = BasePage.get_element_text(self, label_loc)
        return  right_hand_rail_txt_link_txt_label_txt
    
    def click_body_dropdown_ele(self,select_loc, value_name):
        BasePage.select_dropdown_by_value(self, select_loc,value_name)
    
    def add_paragraph_body(self,btn_loc):
        BasePage.press_button(self,btn_loc)


    def searchable_section_ele(self, select_loc, option_loc, label_loc):

        total_searchable_section = len(self.driver.find_elements(*option_loc))

        index_no = random.randint(1,total_searchable_section-1)

        BasePage.select_dropdown_by_index(self, select_loc, index_no)
        searchable_txt = self.driver.find_elements(*option_loc)[index_no].text
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt, searchable_txt


    def additional_subcats_ele(self, input_loc):

        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc,  "Novartis Social Business Report 2018 (19786)")


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


    def publish_ele(self):

        BasePage.select_dropdown_by_value(self, self.publish_xpath, "published")

    def save_btn_ele(self):

        BasePage.press_button(self, self.save_btn_id)


    def success_msg_ele(self):

        success_msg_txt = BasePage.get_element_text(self, self.success_msg_css)
        return success_msg_txt

        







    









