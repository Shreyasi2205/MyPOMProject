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

class MediaContent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    copy_text_label_xpath = (By.XPATH, '//label[contains(@for, "edit-field-body-0-subform-field-copy-text-0-value")]')
    copy_text_input_xpath = (By.XPATH, '//input[contains(@id, "edit-field-body-0-subform-field-copy-text-0-value")]')
    copy_text_helper_text_xpath = (By.XPATH, '//div[contains(@id, "edit-field-body-0-subform-field-copy-text-0-value") and contains(@class, "description")]')
    cta_title_input_xpath = (By.XPATH, "//input[contains(@id, 'cta-title') and contains(@id,'edit-field-body-0')] ")
    cta_title_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'cta-title') and contains(@class, 'description') and contains(@id,'edit-field-body-0')]")
    cta_title_txt= "CTA Title"
    cta_title_txt1= "CTA Title 1"
    cta_title_txt2= "CTA Title 2"
    cta_title_txt3= "CTA Title 3"
    cta_title_txt4= "CTA Title 4"
    cta_desc_iframe_xpath = (By.XPATH, "(//iframe[contains(@title, 'Rich Text Editor, CTA Description field')])[1]")
    paragraph_css = (By.CSS_SELECTOR, "p")
    cta_title_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-body-0') and contains(@for,'cta-title-0')]")
    cta_description_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-body-0') and contains(@for,'cta-description-0')]")
    cta_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-body-0') and contains(@for,'field-call-text-0')]")
    cta_label_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-body-0') and contains(@id,'field-call-text-0')]")
    cta_label_helper_txt_xpath = (By.XPATH, "//div[contains(@id,'edit-field-body-0') and contains(@id,'field-call-text-0')]")
    cta_uri_xpath = (By.XPATH, "//input[contains(@id, 'cta-text') and contains(@id, 'uri') and contains(@id,'edit-field-body-0')]")
    cta_url_open_in_xpath = (By.XPATH, "(//select[contains(@id, 'cta-text') and contains(@id, 'link-open-in')])[1]")
    cta_url_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-body-0') and contains(@for,'url-0-uri')]")
    cta_url_open_in_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-body-0') and contains(@for,'field-link-open-in') and contains(@for,'cta-text')]")
    add_cta_button_xpath = (By.XPATH,"//input[contains(@id,'call-to-action') and contains(@id,'cta-text') and contains(@id,'edit-field-body-0')]")
    button_uri_xpath = (By.XPATH, "//input[contains(@id, 'field-button') and contains(@id, 'uri') and contains(@id,'edit-field-body-0')]")
    button_url_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-body-0') and contains(@for,'button-0-uri')]")
    button_link_txt_xpath = (By.XPATH, "//input[contains(@id, 'field-button') and contains(@id, 'title') and contains(@id,'edit-field-body-0')]")
    button_link_txt_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-body-0') and contains(@for,'field-button-0-title')]")
    button_url_open_in_xpath = (By.XPATH, "(//select[contains(@id, 'field-button') and contains(@id, 'link-open-in') and contains(@id,'edit-field-body-0')])[1]")
    button_url_open_in_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-body-0') and contains(@for,'subform-field-link-open-in') and contains(@for,'button-text')]")
    media_content_image_xpath = (By.XPATH, "//div[contains(@id, 'subform-field-image-wrapper') and contains(@id, 'edit-field-body-0')]/details/summary")
    media_content_select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'field-image') and contains(@id, 'open-modal')]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    media_content_selected_image_css = (By.CSS_SELECTOR,'.entities-list >tbody >[class="draggable odd"]')
    image_caption_xpath = (By.XPATH,"//input[contains(@id, 'field-caption') and contains(@id,'edit-field-body-0')]")
    image_caption_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'field-caption') and contains(@id,'edit-field-body-0') and contains(@id,'description')]")
    image_caption_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-body-0') and contains(@for,'field-caption-0')]")
    stripe_layout_xpath = (By.XPATH,"(//select[contains(@id,edit-field-body-0) and contains(@id, 'stripe-layout')])[1]")
    stripe_layout_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-body-0') and contains(@for,'field-stripe-layout')]")
    teaser_xpath = (By.XPATH,"//input[contains(@id, 'teaser') and contains(@id,'edit-field-body-0')]")
    teaser_helper_txt_xpath = (By.XPATH, "//div[contains(@id, 'teaser') and contains(@id,'edit-field-body-0') and contains(@id,'description')]")
    teaser_label_xpath = (By.XPATH, "//label[contains(@for, 'teaser') and contains(@for,'edit-field-body-0')]")
    media_content_upload_video_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'open-modal')]")
    video_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_media_browser')]")
    video_edit_button_xpath = (By.XPATH, "//input[contains(@id, 'edit-button') and contains(@id, 'edit-field-body-0')]")
    video_remove_button_xpath = (By.XPATH, "//input[contains(@id, 'remove-button') and contains(@id, 'edit-field-body-0') and contains(@id,'field-document')]")
    image_remove_btn_xpath = (By.XPATH,"//input[contains(@id,'edit-field-body-0') and contains(@id,'remove-button') and contains(@id,'image')]")
    

    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    media_content_stripe_value = "media_content"
    cta_description_txt = "sample cta description"
    cta_description_txt2 = "CTA description text 2"
    cta_description_txt3= "CTA description text 3"
    cta_description_txt4= "CTA description text 4"
    cta_description_txt5= "CTA description text 5"
    button_link_text = "sample button link text"
    index_no = "2"
    index_no2 = "1"
    button_url_text = "Novartis Financial Results – Q3 2022 (176931)"
    copy_text = "Novartis Financial Results - Q3 2022"
    copy_text2 = "Q3 2022 Novartis Financial results"
    teaser_text = "Novartis announced the company's financial results for the third quarter of 2022."
    teaser_text2 = "Financial results were announced by Novartis for the fourth quater"
    link_text = "Read More"
    copy_text1= "Our vision is to become the most valued and trusted medicines company in the world"

    """
    Data related to Investors
    """
    investors_copy_text = "Third quarter & Nine months 2022 results"
    investors_cta_description_txt = """View recent presentations and learn more about upcoming events. 
    November 16, 2022
    Jefferies Healthcare Conference
    London, UK """
    investors_button_link_text = "Learn More"


    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)


    # def click_body_dropdown(self, body_dropdown_flag):

    #     if body_dropdown_flag == 0:
    #         BasePage.press_button(self, self.body_dropdown_btn_first_time_xpath)
    #     else:
    #         BasePage.press_button(self, self.body_dropdown_btn_after_first_time_xpath)


    # def media_content_stripe(self):

    #     BasePage.is_visible(self, self.accordion_xpath )
    #     BasePage.select_dropdown_by_value(self, self.accordion_xpath ,'media_content')
    #     BasePage.press_button(self, self.add_new_paragraph_btn_xpath)

    def copy_text_ele(self, label_loc, input_loc, helper_loc,copy_text):
        copy_text_title = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, copy_text)
        copy_text_helper_txt = BasePage.get_element_text(self, helper_loc)
        return copy_text_title, copy_text_helper_txt



    def cta_title_ele(self, label_loc , input_loc , helper_loc, txt ):

        cta_title = self.get_element_text(label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)
        cta_title_helper_txt = BasePage.get_element_text(self, helper_loc)
        return cta_title_helper_txt, cta_title
        

    def cta_desc_ele(self, label_loc , desc_iframe_loc, text ):

        cta_description = self.get_element_text(label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*desc_iframe_loc))
        BasePage.send_keys(self, self.paragraph_css, text)
        self.driver.switch_to.default_content()
        return cta_description


    def cta_label_ele(self, label_loc , input_loc , helper_loc):

        cta_label = self.get_element_text(label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, "SAMPLE CTA LABEL")
        cta_label_helper_txt = BasePage.get_element_text(self, helper_loc)
        return cta_label_helper_txt, cta_label


    def cta_url_ele(self, cta_uri_loc , cta_uri_label_loc):

        BasePage.press_button(self, cta_uri_loc)
        BasePage.send_keys(self, cta_uri_loc, "The eye: the fastest muscle in the human body (12361)")
        cta_url_label = BasePage.get_element_text(self, cta_uri_label_loc)
        return cta_url_label

    def cta_url_open_in(self, cta_url_open_in , label_loc , index_no):

        

        BasePage.select_dropdown_by_index(self, cta_url_open_in, index_no)
        cta_url_open_in_label = BasePage.get_element_text(self, label_loc)
        return cta_url_open_in_label

    def add_cta(self, cta_button_loc , cta_title_label_loc , cta_des_label_loc,cta_label_loc, cta_url_label_loc, cta_url_open_in_label_loc):

        BasePage.press_button(self, cta_button_loc)
        cta_title = BasePage.is_displayed(self,cta_title_label_loc)
        cta_desc = BasePage.is_displayed(self,cta_des_label_loc)
        cta_label = BasePage.is_displayed(self,cta_label_loc)
        cta_url =BasePage.is_displayed(self,cta_url_label_loc)
        cta_url_opin_in = BasePage.is_displayed(self,cta_url_open_in_label_loc)

        return cta_title,cta_desc,cta_label,cta_url,cta_url_opin_in


    def button_url_ele(self, button_uri_loc, label_loc):

        BasePage.press_button(self, button_uri_loc)
        BasePage.send_keys(self, button_uri_loc, "The eye: the fastest muscle in the human body (12361)")
        button_url_label = BasePage.get_element_text(self, label_loc)
        return button_url_label

    def button_link_txt_ele(self, button_link_loc, label_loc, text):

        BasePage.press_button(self, button_link_loc)
        BasePage.send_keys(self, button_link_loc, text)
        button_link_text_label = BasePage.get_element_text(self, label_loc)
        return button_link_text_label

    def button_url_open_in(self, button_url_open_in_loc , label_loc , index_no):

        BasePage.select_dropdown_by_index(self, button_url_open_in_loc, index_no)
        button_url_open_in_label = BasePage.get_element_text(self, label_loc)
        return button_url_open_in_label


    def add_images(self , media_content_image_loc , media_content_select_image_loc, remove_btn_loc  ) :

        BasePage.press_button(self, media_content_image_loc)
        BasePage.press_button(self, media_content_select_image_loc )
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, media_content_select_image_loc )
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        images = self.driver.find_elements(*self.img_css)
        random_img_index = random.randint(0, len(images)-1)
        for img in images:
            self.driver.execute_script("arguments[0].click()", images[random_img_index])
            break
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        remove_btn = BasePage.is_displayed(self, remove_btn_loc)
        return remove_btn 


    def image_video_caption_ele(self, caption_loc , label_loc , helper_loc):

        BasePage.press_button(self, caption_loc)
        BasePage.send_keys(self, caption_loc, "SAMPLE IMAGE VIDEO CAPTION")
        image_caption_label = BasePage.get_element_text(self,  label_loc)
        image_caption_helper_txt = BasePage.get_element_text(self,  helper_loc)
        return image_caption_label , image_caption_helper_txt

    def stripe_layout(self, layout_loc , label_loc, index_no):

        BasePage.select_dropdown_by_index(self, layout_loc, index_no)
        stripe_layout_label = BasePage.get_element_text(self, label_loc)
        return stripe_layout_label

    def teaser_ele(self, teaser_loc , label_loc , helper_loc,teaser_text):

        BasePage.press_button(self, teaser_loc )
        BasePage.send_keys(self, teaser_loc, teaser_text)
        teaser_label = BasePage.get_element_text(self, label_loc)
        teaser_helper_txt = BasePage.get_element_text(self, helper_loc)
        return teaser_label , teaser_helper_txt


    def add_video(self, media_content_upload_video_loc , edit_loc , remove_loc):

      
        BasePage.press_button(self, media_content_upload_video_loc)
        if len(self.driver.find_elements(*self.video_iframe_xpath)) == 0:
            BasePage.press_button(self, media_content_upload_video_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.video_iframe_xpath))
        images = self.driver.find_elements(*self.img_css)
        random_img_index = random.randint(0, len(images)-1)
        for img in images:
            self.driver.execute_script("arguments[0].click()", images[random_img_index])
            break
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        edit_btn_txt = BasePage.get_elemet_attribute(self,  edit_loc , "value")
        remove_btn_txt = BasePage.get_elemet_attribute(self, remove_loc, "value")

        return edit_btn_txt, remove_btn_txt


    # def copy_text_ele(self,label_loc,input_loc,copy_text, helper_loc):


    #     copy_text_label = self.get_element_text(label_loc)
    #     BasePage.press_button(self, input_loc)
    #     BasePage.send_keys(self, input_loc, copy_text)
    #     copy_text_helper_txt = BasePage.get_element_text(self, helper_loc)
    #     return  copy_text_label, copy_text_helper_txt
        









        
        
        



