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

class Iframe(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    body_dropdown_btn_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    body_dropdown_btn_after_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    iframe_stripe_xpath = (By.XPATH, "//input[contains(@value, 'Add Arctic Iframe')]")
    iframe_input_xpath = (By.XPATH,"//input[contains(@id,'iframe') and contains(@id,'edit-field-body-0')]")
    iframe_label_xpath = (By.XPATH,"//label[contains(@for,'iframe') and contains(@for,'edit-field-body-0')]")
    iframe_input_text = "nov"
    auto_suggestions_css = (By.CSS_SELECTOR,"body .ui-autocomplete>li")
    iframe_second_input_xpath = (By.XPATH,"//input[contains(@id,'iframe') and contains(@id,'edit-field-body-1')]")
    iframe_second_label_xpath = (By.XPATH,"//label[contains(@for,'iframe') and contains(@for,'edit-field-body-1')]")

    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    arctic_iframe_stripe_value = "arctic_iframe"


    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def click_body_dropdown(self, body_dropdown_flag):

        if body_dropdown_flag == 0:
            BasePage.press_button(self, self.body_dropdown_btn_first_time_xpath)
        else:
            BasePage.press_button(self, self.body_dropdown_btn_after_first_time_xpath)


    def iframe_stripe(self):

        BasePage.press_button(self, self.iframe_stripe_xpath)


    def iframe_ele(self, iframe_label_txt, iframe_input):

        iframe_label = BasePage.get_element_text(self, iframe_label_txt)
        BasePage.send_keys(self, iframe_input, self.iframe_input_text)
        auto_suggestions = self.driver.find_elements(*self.auto_suggestions_css)
        for suggestion in auto_suggestions:
            self.driver.execute_script("arguments[0].click()",suggestion)
            break

        return iframe_label


