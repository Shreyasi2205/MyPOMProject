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

class AddCallOut(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    body_dropdown_btn_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    body_dropdown_btn_after_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    add_new_paragraph_btn_xpath = (By.XPATH,'//input[@value="Add new Paragraph"]')
    add_call_out_stripe_xpath = (By.XPATH, "//li/input[contains(@value, 'Add Call Out')]")
    added_by_input_xpath = (By.XPATH,"//input[contains(@id,'field-title') and contains(@id,'edit-field-body-0')]")
    added_by_label_xpath = (By.XPATH,"//label[contains(@for,'field-title') and contains(@for,'edit-field-body-0')]")
    added_by_helper_xpath = (By.XPATH,"//div[contains(@id,'field-title') and contains(@id,'edit-field-body-0') and contains(@class,'description')]")
    added_by_text = "Sample added by"
    quote_iframe_xpath = (By.XPATH,"(//iframe[contains(@title,'Rich Text Editor, Quote / Text field')])[1]")
    quote_label_xpath = (By.XPATH,"//label[contains(@for,'field-description') and contains(@for,'edit-field-body-0')]")
    quote_text_css = (By.CSS_SELECTOR,'body p')
    quote_text = "sample quote text"
    quote_image_xpath = (By.XPATH,"(//summary[contains(@aria-controls,'field-quote-image')])[1]")
    quote_select_image_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-0') and contains(@id, 'field-quote-image') and contains(@id, 'open-modal')]")
    image_iframe_xpath = (By.XPATH, "(//iframe[contains(@id, 'entity_browser_iframe_image_browser')])[1]")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    quote_remove_button_xpath = (By.XPATH,"//input[contains(@id, 'quote-image') and contains(@id, 'remove-button') and contains(@id, 'edit-field-body-0')]")
    quote_image_position_xpath = (By.XPATH, "//select[contains(@id, 'quote-image-position')  and contains(@id,'edit-field-body-0')]")

    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    call_out_stripe_value = "call_out"


    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def click_body_dropdown(self, body_dropdown_flag):

        if body_dropdown_flag == 0:
            BasePage.press_button(self, self.body_dropdown_btn_first_time_xpath)
        else:
            BasePage.press_button(self, self.body_dropdown_btn_after_first_time_xpath)


    def addCallOut_stripe(self):

        BasePage.press_button(self, self.add_call_out_stripe_xpath)


    def added_by_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)

        return label_txt, helper_txt


    def quote_ele(self,iframe_loc, input_loc, label_loc, txt):

        label_txt = BasePage.get_element_text(self, label_loc)
        self.driver.switch_to.frame(self.driver.find_element(*iframe_loc))
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self,input_loc,txt)
        self.driver.switch_to.default_content()

        return label_txt


    def quote_image(self,quote_img_loc,select_img_loc,img_iframe_loc,img_loc,submit_loc,remove_btn):

        BasePage.press_button(self, quote_img_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*img_iframe_loc)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*img_iframe_loc))
        BasePage.press_button(self, img_loc)
        BasePage.press_button(self, submit_loc)
        self.driver.switch_to.default_content()
        BasePage.is_visible(self,remove_btn)
        remove_button = BasePage.get_elemet_attribute(self, remove_btn,'value')

        return remove_button



    def quote_image_position_ele(self,quote_img_pos):

        index_no = random.randint(1,2)

        BasePage.select_dropdown_by_index(self, quote_img_pos , index_no)
        