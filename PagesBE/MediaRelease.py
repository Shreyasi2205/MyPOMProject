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





class MediaRelease(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    title_label_xpath = (By.XPATH,"//label[contains(@for,'edit-field-body-0') and contains(@for,'field-title')]")
    title_input_xpath = (By.XPATH, "//input[contains(@id,'edit-field-body-0') and contains(@id,'field-title')]")
    title_helper_txt_xpath = (By.XPATH, "//div[contains(@id,'edit-field-body-0') and contains(@id, 'title') and contains(@class, 'description')]")
    number_of_media_releases = (By.XPATH,"//input[contains(@id,'number-of-media-releases') and contains(@id,'edit-field-body-0')]")
    manual_value_xpath = (By.XPATH, "//input[contains(@id,'is-manual-value') and contains(@id,'edit-field-body-0')]")
    media_release_list_xpath = (By.XPATH,"//input[contains(@id, 'media-releases-list-0') and contains(@id, 'target-id')]")
    cta_link_txt_xpath = (By.XPATH, "//input[contains(@id, 'media-cta-text-') and contains(@id, 'title') and contains(@id,'edit-field-body-0')]")
    cta_link_txt_label_xpath = (By.XPATH,"//label[contains(@for, 'media-cta-text-') and contains(@for, 'title') and contains(@for,'edit-field-body-0')]")
    cta_uri_xpath = (By.XPATH, "//input[contains(@id, 'cta-text') and contains(@id, 'uri') and contains(@id,'edit-field-body-0')]")
    cta_url_label_xpath = (By.XPATH, "//label[contains(@for,'edit-field-body-0') and contains(@for,'uri')]")
    add_another_item_xpath = (By.XPATH,"//input[contains(@id,'add-more') and contains(@id,'media-releases') and contains(@id,'edit-field-body')]")
    draggable_items_xpath = (By.XPATH,"//table[contains(@id,'media-releases')]//tr[contains(@class,'draggable')]")
    stripe_value = "media_release"
    title_text = "Latest news"
    uri_text = "/news/news-archive?type=media_release"
    link_txt = "View More"
   



    def click_paragraph_dropdown(self,input_loc,value):
        
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):

        BasePage.press_button(self, btn_loc)


    def title_ele(self,label_loc, input_loc , helper_loc, title_text):

        title = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc, title_text)
        title_helper_txt = BasePage.get_element_text(self, helper_loc)
        return title_helper_txt, title


    def click_no_of_media_releases(self,no_media_rel_loc):

       
        BasePage.press_button(self, no_media_rel_loc)
        min_value = int(BasePage.get_elemet_attribute(self,no_media_rel_loc,'min'))
        max_value = int(BasePage.get_elemet_attribute(self,no_media_rel_loc,'max'))
        num = random.randint(min_value,max_value)
        BasePage.send_keys(self, no_media_rel_loc, num)
        
        return min_value, max_value


    def is_manual_ele(self, input_loc):

        checked_status = False
        checked_status = BasePage.is_selected(self, input_loc)
        return checked_status


    def list_ele(self,media_rel_list_loc):

        BasePage.press_button(self, media_rel_list_loc)
       
        BasePage.send_keys(self, media_rel_list_loc, "Novartis drug Afinitor® significantly improves progression-free survival in advanced nonfunctional gastrointestinal and lung NET")
        # WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located((By.XPATH, "toolbar-tray-open toolbar-fixed user-logged-in path-node toolbar-vertical")))
        # BasePage.send_keys(self,media_rel_list_loc, Keys.TAB)

    def cta_url_ele(self, cta_uri_loc , label_loc, uri_text):

        BasePage.press_button(self, cta_uri_loc)
        # self.driver.find_element(*cta_uri_loc).clear()
        # BasePage.send_keys(self, cta_uri_loc, uri_text)
        input_value = BasePage.get_elemet_attribute(self, cta_uri_loc, "value")
        cta_url_label = BasePage.get_element_text(self, label_loc)
        return cta_url_label, input_value


    def cta_link_txt_ele(self,cta_link_txt_loc , cta_link_label,link_text):

        BasePage.press_button(self, cta_link_txt_loc)
        # self.driver.find_element(*cta_link_txt_loc).clear()
        # BasePage.send_keys(self, cta_link_txt_loc, link_text)
        input_value = BasePage.get_elemet_attribute(self, cta_link_txt_loc, "value")
        cta_link_text_label = BasePage.get_element_text(self, cta_link_label)
        return cta_link_text_label, input_value


    def add_another_item(self , add_another_loc, media_rel_list_loc , draggable_items_loc ):

        BasePage.press_button(self, add_another_loc)
        BasePage.is_visible(self,media_rel_list_loc)
        list_items = self.driver.find_elements(*draggable_items_loc)
        len_list_items = len(list_items)
        BasePage.send_keys(self,media_rel_list_loc,"Novartis' new heart failure medicine Entresto(TM) recommended by CHMP for EU approval (58966)")
        # WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located((By.XPATH, "toolbar-tray-open toolbar-fixed user-logged-in path-node toolbar-vertical")))
        return len_list_items
