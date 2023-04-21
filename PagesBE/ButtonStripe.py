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

class ButtonStripe(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    button_stripe_xpath = (By.XPATH, "//input[contains(@value, 'Add Button')]")
    button_uri_first_xpath = (By.XPATH, "(//input[contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-button') and contains(@id, 'uri')])")
    button_uri_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'edit-field-body-0') and contains(@for, 'subform-field-button') and contains(@for, 'uri')])")
    button_uri_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'subform-field-button') and contains(@for, 'uri')])[2]")
    button_uri_second_xpath = (By.XPATH, "(//input[contains(@id, 'subform-field-button') and contains(@id, 'uri')])[2]")
    button_link_txt_first_xpath = (By.XPATH, "(//input[contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-button') and contains(@id, 'title')])")
    button_link_txt_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'edit-field-body-0') and contains(@for, 'subform-field-button') and contains(@for, 'title')])")
    button_link_txt_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'subform-field-button') and contains(@for, 'title')])[2]")
    button_link_txt_second_xpath = (By.XPATH, "(//input[contains(@id, 'subform-field-button') and contains(@id, 'title')])[2]")
    button_window_first_xpath = (By.XPATH, "(//select[contains(@id, 'edit-field-body-0') and contains(@id, 'subform-field-link-open')])")
    button_window_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'edit-field-body-0') and contains(@for, 'subform-field-link-open')])")
    button_window_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'subform-field-link-open')])[2]")
    button_window_second_xpath = (By.XPATH, "(//select[contains(@id, 'subform-field-link-open')])[2]")
    button_link_txt_one = "BUTTON_ONE"
    button_link_txt_two = "BUTTON_TWO"
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    auto_sugg_txt = "nov"
    new_window = "_blank"
    same_window = "_self"
    stripe_value = "button"
    add_new_paragraph_btn_xpath = (By.XPATH,'//input[@value="Add new Paragraph"]')
    accordion_xpath  = (By.XPATH,'//select[@name="field_body[actions][bundle]"]')

    """
    Data related to Investors
    """

    investors_button_link_txt = "Explore the ESG Indices"

    
    def click_paragraph_dropdown(self,input_loc,value):
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def button_url_ele(self, button_uri_selector, label):

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

    def button_link_txt_ele(self, link_txt_selector, link_txt, label):

        BasePage.send_keys(self, link_txt_selector, link_txt)
        label_txt = BasePage.get_element_text(self, label)

        return label_txt

    def button_window_ele(self, button_window_selector, value, label):

        BasePage.select_dropdown_by_value(self, button_window_selector, value)
        label_txt = BasePage.get_element_text(self, label)

        return label_txt
