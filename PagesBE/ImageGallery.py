import time
from selenium.webdriver.support.select import Select
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


class ImageGallery(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    image_gallery_variations_xpath = (By.XPATH, "//select[contains(@id, 'image-gallery-variations') and contains(@id, 'edit-field-body-0')]")
    image_gallery_variations_title_txt_xpath = (By.XPATH, "//label[contains(@for, 'image-gallery-variations') and contains(@for, 'edit-field-body-0')]")
    image_gallery_title_txt_xpath = (By.XPATH, "//label[contains(@for, 'image-gallery-title') and contains(@for, 'edit-field-body-0')]")
    image_gallery_title_input_xpath = (By.XPATH, "//input[contains(@id, 'image-gallery-title') and contains(@id, 'edit-field-body-0')]")
    image_gallery_title_chars_limit_txt_xpath = (By.XPATH, "//div[contains(@id,'image-gallery-title') and contains(@class,'description') and contains(@id, 'edit-field-body-0')]")
    title = "Sample Image Gallery"
    image_gallery_description_txt_xpath = (By.XPATH,"//label[contains(@for,'image-gallery-main') and contains(@for, 'edit-field-body-0')]")
    image_gallery_description_input_xpath = (By.XPATH,"//textarea[contains(@id, 'image-gallery-main') and contains(@id, 'edit-field-body-0')]")
    description = "Sample description"
    enable_numb_pagination_xpath = (By.XPATH,"//input[contains(@id, 'image-slider-pagination') and contains(@id, 'edit-field-body-0')]")
    frame_css = (By.XPATH,"(//iframe[contains(@title,'Rich Text Editor, Image Caption field')])[1]")
    text_css = (By.CSS_SELECTOR,'body p')
    image_caption_label_xpath = (By.XPATH,"//label[contains(@for, 'subform-field-image-galery-0-subform-field-gallery-intro-text-0') and contains(@for, 'edit-field-body-0')]")
    image_caption_text = "Sample Image Caption Text"
    select_image_xpath = (By.XPATH, "//input[contains(@id,'image-galery') and contains(@id, 'open-modal') and contains(@id, 'edit-field-body-0')]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    image_css = (By.CSS_SELECTOR,".field-content>img")
    # video_embed_tag_xpath = (By.XPATH,"//div[contains(@id,'playlist-video')]//summary[contains(@aria-controls,'public-file')]/span[@class='summary']")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    img_remove_button_xpath = (By.XPATH,"//input[contains(@id,'field-gallery-image') and contains(@id,'remove-button') and contains(@id, 'edit-field-body-0')]")
    add_image_gallery_xpath = (By.XPATH,"//input[contains(@id,'image-galery-add-more') and contains(@id, 'edit-field-body-0')]")
    create_Paragraph_xpath= (By.XPATH,"//input[contains(@id,'add-save') and contains(@id,'body')]")
    created_paragraph_xpath = (By.XPATH,'//div[@class="fieldset-wrapper"]/div[@class="tableresponsive-toggle-columns"]')
    stripe_value = "image_galery_slider"
    image_gallery_title = "History of Novartis"
    image_gallery_desc = "Novartis was created in 1996 through a merger of Ciba-Geigy and Sandoz. Novartis and its predecessor companies trace roots back more than 250 years, with a rich history of developing innovative products."
    image_caption_text1 = "In 1758, Johann Rudolf Geigy-Gemuseus (1733-1793) founds the trading company J.R. Geigy in Basel, Switzerland to deal in 'Materials, Chemicals, Dyes and Drugs of all Kinds'"

    def click_paragraph_dropdown(self,input_loc,value):
        
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def image_gallery_variation_ele(self, input_loc, label_loc):

        index_no = random.randint(0,1)

        BasePage.select_dropdown_by_index(self, input_loc, index_no)
        image_gallery_variations_txt = BasePage.get_element_text(self, label_loc)

        return image_gallery_variations_txt

    def image_gallery_title_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        title_txt = BasePage.get_element_text(self, label_loc)
        BasePage.send_keys(self, input_loc, txt)
        title_chars_limit_txt = BasePage.get_element_text(self, helper_txt_loc)

        return title_txt, title_chars_limit_txt


    def image_gallery_description(self, input_loc, label_loc, txt):

        description_txt = BasePage.get_element_text(self, label_loc)
        BasePage.send_keys(self, input_loc, txt)

        return description_txt


    def enable_num_pagination_ele(self, input_loc):

        BasePage.press_button(self,input_loc)
        enable_num_status = BasePage.is_selected(self,input_loc)
        
        return  enable_num_status 

    def image_caption(self, frame_loc, label_loc, txt):

        image_caption_txt = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*frame_loc))
        BasePage.press_button(self, self.text_css)
        BasePage.send_keys(self,self.text_css,txt)
        self.driver.switch_to.default_content()

        return image_caption_txt


    def image_gallery(self, select_loc, remove_loc):

       
        BasePage.press_button(self, select_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
             BasePage.press_button(self, select_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        remove_btn_txt = BasePage.get_elemet_attribute(self,remove_loc , "value")

        return remove_btn_txt


    def add_image_gallery(self, input_loc):

        BasePage.press_button(self, input_loc)


    # def create_paragraph(self):

    #     BasePage.press_button(self, self.create_Paragraph_xpath)
    #     created_field = BasePage.is_displayed(self,self.created_paragraph_xpath)

    #     return created_field 


        
        

        

