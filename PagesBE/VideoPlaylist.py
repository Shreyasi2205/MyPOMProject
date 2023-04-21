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




class VideoPlaylist(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    video_playlist_xpath = (By.XPATH, "//input[contains(@value, 'Add Media Release')]")
    add_new_paragraph_btn_xpath = (By.XPATH,'//input[@value="Add new Paragraph"]')
    intro_text_xpath = (By.XPATH,'//input[contains(@id,"edit-field-body-0-subform-field-show-intro-text-value")]')
    playlist_title_txt_xpath = (By.XPATH, "//label[contains(@for, 'playlist-title') and contains(@for, 'edit-field-body-0')]")
    playlist_title_input_xpath = (By.XPATH, "//input[contains(@id, 'playlist-title') and contains(@id, 'edit-field-body-0')]")
    playlist_title_chars_limit_txt_xpath = (By.XPATH, "//div[contains(@id,'playlist-title') and contains(@class,'description') and contains(@id, 'edit-field-body-0')]")
    video_title_txt_xpath = (By.XPATH, "//label[contains(@for, 'video-title') and contains(@for, 'edit-field-body-0-subform-field-playlist-video-0')]")
    video_title_input_xpath = (By.XPATH, "//input[contains(@id, 'video-title') and contains(@id, 'edit-field-body-0-subform-field-playlist-video-0')]")
    video_title_chars_limit_txt_xpath = (By.XPATH, "//div[contains(@id,'video-title') and contains(@id, 'edit-field-body-0-subform-field-playlist-video-0') and contains(@class,'description')]")
    playlist_description_txt_xpath = (By.XPATH,"//label[contains(@for,'playlist-description') and contains(@for, 'edit-field-body-0-subform-field-playlist')]")
    playlist_description_input_xpath = (By.XPATH,"//textarea[contains(@id, 'playlist-description') and contains(@id, 'edit-field-body-0-subform-field-playlist')]")
    video_description_txt_xpath = (By.XPATH,"//label[contains(@for,'video-description') and contains(@for, 'edit-field-body-0-subform-field-playlist-video-0')]")
    video_description_input_xpath = (By.XPATH,"//textarea[contains(@id, 'video-description') and contains(@id, 'edit-field-body-0-subform-field-playlist-video-0')]")
    video_thumbnail_xpath = (By.XPATH,"//div[contains(@id, 'video-thumbnail') and contains(@id, 'edit-field-body-0-subform-field-playlist-video-0')]/details/summary[contains(@aria-controls,'video-thumbnail')]/span[@class='summary']")
    video_thumbnail_select_image_xpath = (By.XPATH, "//input[contains(@id,'video-thumbnail') and contains(@id, 'open-modal') and contains(@id, 'edit-field-body-0-subform-field-playlist-video-0')]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    img_remove_button_xpath = (By.XPATH,"//input[contains(@id,'remove-button') and contains(@id,'video-thumbnail') and contains(@id, 'edit-field-body-0-subform-field-playlist-video-0')]")
    alternative_text_title_xpath = (By.XPATH,"//label[contains(@for,'video-thumbnail') and contains(@for,'field-playlist-video')  and not (contains(@for,'remove')) and contains(@for, 'edit-field-body-0-subform-field-playlist-video-0') and contains(@for, 'alt')]")
    alternative_text_input_xpath = (By.XPATH,"//input[contains(@id,'video-thumbnail') and contains(@id,'field-playlist-video')  and not (contains(@id,'remove')) and contains(@id, 'edit-field-body-0-subform-field-playlist-video-0')]")
    video_embed_tag_xpath = (By.XPATH,"//div[contains(@id,'playlist-video') and contains(@id, 'edit-field-body-0-subform-field-playlist-video-0')]//summary[contains(@aria-controls,'public-file')]/span[@class='summary']")
    upload_btn_xpath = (By.XPATH,"//input[contains(@id,'edit-field-body-0-subform-field-playlist-video-0') and contains(@id, 'field-document-public-file-entity') and contains(@id, 'open-modal')]")
    media_iframe_xpath = (By.XPATH,"//iframe[contains(@id, 'entity_browser_iframe_media_browser')]")
    current_selection_xpath = (By.XPATH,'//span[text()="Current selection"]')
    video_edit_button_xpath = (By.XPATH, "//input[contains(@id, 'playlist-video') and contains(@id, 'edit-button') and contains(@id, 'field-document') and contains(@id,'edit-field-body-0-subform-field-playlist-video-0')]")
    video_remove_button_xpath = (By.XPATH, "//input[contains(@id, 'playlist-video') and contains(@id, 'remove-button') and contains(@id, 'field-document') and contains(@id,'edit-field-body-0-subform-field-playlist-video-0')]")
    episode_number_txt_xpath = (By.XPATH, "//label[contains(@for, 'episode-number') and contains(@for,'edit-field-body-0-subform-field-playlist-video-0')]")
    episode_number_input_xpath = (By.XPATH, "//input[contains(@id, 'episode-number') and contains(@id,'edit-field-body-0-subform-field-playlist-video-0')]")
    episode_number_chars_limit_txt_xpath = (By.XPATH, "//div[contains(@id,'episode-number') and contains(@class,'description') and contains(@id,'edit-field-body-0-subform-field-playlist-video-0')]")

    # accordion_xpath = (By.XPATH,'//select[@name="field_body[actions][bundle]"]')

    episode_txt= "sample episode number"
    stripe_value = "video_playlist"
    title = "playlist_title"
    video_title = "video_title"
    description ="sample description"
    video_description = "sample video description"
    alternative_txt = "sample_alt_txt"


    def click_paragraph_dropdown(self,input_loc,value):
        
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):

        BasePage.press_button(self, btn_loc)


    def intro_text_checkbox(self, playlist_title_loc, intro_txt_loc):

        BasePage.is_visible(self,playlist_title_loc)
        default_intro_text_checkbox_status = True
        intro_text_checkbox_status = False
        if len(self.driver.find_elements(*playlist_title_loc)) > 0 :
            default_intro_text_checkbox_status = BasePage.is_selected(self,intro_txt_loc)
            BasePage.press_button(self,intro_txt_loc)
            intro_text_checkbox_status = BasePage.is_selected(self,intro_txt_loc)


        return default_intro_text_checkbox_status, intro_text_checkbox_status


    def playlist_title_ele(self, input_loc, label_loc, helper_loc, txt):

        title_txt = BasePage.get_element_text(self, label_loc)
        BasePage.send_keys(self, input_loc, txt)
        title_chars_limit_txt = BasePage.get_element_text(self, helper_loc)

        return title_txt, title_chars_limit_txt


    def playlist_description(self, input_loc, label_loc, txt):

        description_txt = BasePage.get_element_text(self, label_loc)
        BasePage.send_keys(self, input_loc, txt)

        return description_txt


    def video_playlist_title_ele(self, input_loc, lable_loc, helper_loc, txt):

        video_title_txt = BasePage.get_element_text(self, lable_loc)
        BasePage.send_keys(self, input_loc, txt)
        video_title_chars_limit_txt = BasePage.get_element_text(self, helper_loc)

        return video_title_txt, video_title_chars_limit_txt 

    def video_playlist_description(self, input_loc, label_loc, txt):

        video_description_txt = BasePage.get_element_text(self, label_loc)
        BasePage.send_keys(self, input_loc, txt)

        return video_description_txt


    def video_thumbnail(self, video_thumbnail_loc, select_img_loc, remove_btn_loc):

        BasePage.press_button(self,video_thumbnail_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        remove_btn_txt = BasePage.get_elemet_attribute(self, remove_btn_loc, "value")

        return remove_btn_txt


    def alternative_text_ele(self, input_loc, label_loc, txt):

        alternative_txt = BasePage.get_element_text(self, label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, txt)

        return alternative_txt

    def video_embed_tag(self, video_embed_loc, upload_btn_loc, edit_btn_loc, remove_btn_loc):

        BasePage.press_button(self,video_embed_loc)
        BasePage.press_button(self, upload_btn_loc)
        if len(self.driver.find_elements(*self.media_iframe_xpath)) == 0:
            BasePage.press_button(self, upload_btn_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.media_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        # current_selection_status = BasePage.is_displayed(self,self.current_selection_xpath)
        edit_btn_txt = BasePage.get_elemet_attribute(self, edit_btn_loc, "value")
        remove_btn_txt = BasePage.get_elemet_attribute(self, remove_btn_loc, "value")



        return edit_btn_txt, remove_btn_txt

    def episode_number(self, input_loc, label_loc, helper_loc, txt):

        episode_txt = BasePage.get_element_text(self, label_loc)
        BasePage.send_keys(self, input_loc, txt)
        episode_chars_limit_txt = BasePage.get_element_text(self, helper_loc)

        return episode_txt, episode_chars_limit_txt








    


            



