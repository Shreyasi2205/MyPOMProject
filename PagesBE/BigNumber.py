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

class BigNumber(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    body_dropdown_btn_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    body_dropdown_btn_after_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    add_new_paragraph_btn_xpath = (By.XPATH,'//input[@value="Add new Paragraph"]')
    accordion_xpath  = (By.XPATH,'//select[@name="field_body[actions][bundle]"]')
    big_number_stripe_xpath = (By.XPATH, "//li/input[contains(@value, 'Add Big Numbers')]")
    auto_sugg_css = (By.CSS_SELECTOR, "ul.ui-autocomplete > li > a")
    auto_sugg_txt = "novartis"
    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    big_numbers_parent_stripe_value = "big_numbers_parent"

    ############### First Column -- Single Column ####################

    first_col_layout_first_xpath = (By.XPATH, "( //select[contains(@id, 'subform-field-layout')])[1]")
    first_col_layout_label_first_xpath = (By.XPATH, "( //label[contains(@for, 'subform-field-layout')])[1]")
    first_col_main_title_first_xpath = (By.XPATH, "(//input[contains(@id, 'subform-field-title') and not(contains(@id, 'big-numbers'))])[1]")
    first_col_main_title_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'subform-field-title') and not(contains(@for, 'big-numbers'))])[1]")
    first_col_main_title_helper_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'subform-field-title') and contains(@class, 'desc') and not(contains(@id, 'big-numbers'))])[1]")
    
    first_col_numbers_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-title')])[1]")
    first_col_numbers_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-title')])[1]")
    first_col_numbers_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-title') and contains(@class, 'desc')])[1]")
    first_col_title_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-call-text') and contains(@class, 'desc')])[1]")
    first_col_title_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-call-text')])[1]")
    first_col_title_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-call-text')])[1]")
    first_col_desc_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-teaser') and contains(@class, 'desc')])[1]")
    first_col_desc_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-teaser')])[1]")
    first_col_desc_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-teaser')])[1]")
    first_col_url_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-url') and contains(@id, 'uri')])[1]")
    first_col_url_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-url') and contains(@for, 'uri')])[1]")
    first_col_link_txt_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-url') and contains(@id, 'title')])[1]")
    first_col_link_txt_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-url') and contains(@for, 'title')])[1]")

    first_col_numbers_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-title')])[1]")
    first_col_numbers_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-title')])[1]")
    first_col_numbers_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-title') and contains(@class, 'desc')])[1]")
    first_col_title_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-call-text') and contains(@class, 'desc')])[1]")
    first_col_title_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-call-text')])[1]")
    first_col_title_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-call-text')])[1]")
    first_col_desc_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-teaser') and contains(@class, 'desc')])[1]")
    first_col_desc_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-teaser')])[1]")
    first_col_desc_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-teaser')])[1]")
    first_col_url_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-url') and contains(@id, 'uri')])[1]")
    first_col_url_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-url') and contains(@for, 'uri')])[1]")
    first_col_link_txt_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-url') and contains(@id, 'title')])[1]")
    first_col_link_txt_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-url') and contains(@for, 'title')])[1]")

    first_col_add_more_big_number_tile_xpath = (By.XPATH, "(//div/input[contains(@id, 'add-more-button-big-numbers')])[1]")

    ############### Second Column -- Two Column ####################

    second_col_layout_first_xpath = (By.XPATH, "( //select[contains(@id, 'subform-field-layout')])[2]")
    second_col_layout_label_first_xpath = (By.XPATH, "( //label[contains(@for, 'subform-field-layout')])[2]")
    second_col_main_title_first_xpath = (By.XPATH, "(//input[contains(@id, 'subform-field-title') and not(contains(@id, 'big-numbers'))])[2]")
    second_col_main_title_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'subform-field-title') and not(contains(@for, 'big-numbers'))])[2]")
    second_col_main_title_helper_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'subform-field-title') and contains(@class, 'desc') and not(contains(@id, 'big-numbers'))])[2]")
    
    second_col_numbers_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-title')])[2]")
    second_col_numbers_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-title')])[2]")
    second_col_numbers_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-title') and contains(@class, 'desc')])[2]")
    second_col_title_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-call-text') and contains(@class, 'desc')])[2]")
    second_col_title_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-call-text')])[2]")
    second_col_title_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-call-text')])[2]")
    second_col_desc_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-teaser') and contains(@class, 'desc')])[2]")
    second_col_desc_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-teaser')])[2]")
    second_col_desc_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-teaser')])[2]")
    second_col_url_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-url') and contains(@id, 'uri')])[2]")
    second_col_url_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-url') and contains(@for, 'uri')])[2]")
    second_col_link_txt_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-url') and contains(@id, 'title')])[2]")
    second_col_link_txt_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-url') and contains(@for, 'title')])[2]")

    second_col_numbers_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-title')])[2]")
    second_col_numbers_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-title')])[2]")
    second_col_numbers_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-title') and contains(@class, 'desc')])[2]")
    second_col_title_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-call-text') and contains(@class, 'desc')])[2]")
    second_col_title_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-call-text')])[2]")
    second_col_title_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-call-text')])[2]")
    second_col_desc_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-teaser') and contains(@class, 'desc')])[2]")
    second_col_desc_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-teaser')])[2]")
    second_col_desc_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-teaser')])[2]")
    second_col_url_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-url') and contains(@id, 'uri')])[2]")
    second_col_url_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-url') and contains(@for, 'uri')])[2]")
    second_col_link_txt_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-url') and contains(@id, 'title')])[2]")
    second_col_link_txt_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-url') and contains(@for, 'title')])[2]")

    second_col_add_more_big_number_tile_xpath = (By.XPATH, "(//div/input[contains(@id, 'add-more-button-big-numbers')])[2]")

    ############### Third Column -- Three Column One ####################

    third_col_one_layout_first_xpath = (By.XPATH, "( //select[contains(@id, 'subform-field-layout')])[3]")
    third_col_one_layout_label_first_xpath = (By.XPATH, "( //label[contains(@for, 'subform-field-layout')])[3]")
    third_col_one_main_title_first_xpath = (By.XPATH, "(//input[contains(@id, 'subform-field-title') and not(contains(@id, 'big-numbers'))])[3]")
    third_col_one_main_title_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'subform-field-title') and not(contains(@for, 'big-numbers'))])[3]")
    third_col_one_main_title_helper_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'subform-field-title') and contains(@class, 'desc') and not(contains(@id, 'big-numbers'))])[3]")
    
    third_col_one_numbers_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-title')])[3]")
    third_col_one_numbers_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-title')])[3]")
    third_col_one_numbers_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-title') and contains(@class, 'desc')])[3]")
    third_col_one_title_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-call-text') and contains(@class, 'desc')])[3]")
    third_col_one_title_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-call-text')])[3]")
    third_col_one_title_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-call-text')])[3]")
    third_col_one_desc_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-teaser') and contains(@class, 'desc')])[3]")
    third_col_one_desc_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-teaser')])[3]")
    third_col_one_desc_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-teaser')])[3]")
    third_col_one_url_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-url') and contains(@id, 'uri')])[3]")
    third_col_one_url_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-url') and contains(@for, 'uri')])[3]")
    third_col_one_link_txt_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-url') and contains(@id, 'title')])[3]")
    third_col_one_link_txt_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-url') and contains(@for, 'title')])[3]")

    third_col_one_add_more_big_number_tile_xpath = (By.XPATH, "(//div/input[contains(@id, 'add-more-button-big-numbers')])[3]")

    ############### Fourth Column -- Three Columnn Second ####################

    fourth_col_two_layout_first_xpath = (By.XPATH, "( //select[contains(@id, 'subform-field-layout')])[4]")
    fourth_col_two_layout_label_first_xpath = (By.XPATH, "( //label[contains(@for, 'subform-field-layout')])[4]")
    fourth_col_two_main_title_first_xpath = (By.XPATH, "(//input[contains(@id, 'subform-field-title') and not(contains(@id, 'big-numbers'))])[4]")
    fourth_col_two_main_title_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'subform-field-title') and not(contains(@for, 'big-numbers'))])[4]")
    fourth_col_two_main_title_helper_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'subform-field-title') and contains(@class, 'desc') and not(contains(@id, 'big-numbers'))])[4]")
    
    fourth_col_two_numbers_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-title')])[4]")
    fourth_col_two_numbers_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-title')])[4]")
    fourth_col_two_numbers_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-title') and contains(@class, 'desc')])[4]")
    fourth_col_two_title_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-call-text') and contains(@class, 'desc')])[4]")
    fourth_col_two_title_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-call-text')])[4]")
    fourth_col_two_title_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-call-text')])[4]")
    fourth_col_two_desc_help_txt_first_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-0-subform-field-teaser') and contains(@class, 'desc')])[4]")
    fourth_col_two_desc_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-teaser')])[4]")
    fourth_col_two_desc_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-teaser')])[4]")
    fourth_col_two_url_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-url') and contains(@id, 'uri')])[4]")
    fourth_col_two_url_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-url') and contains(@for, 'uri')])[4]")
    fourth_col_two_link_txt_first_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-0-subform-field-url') and contains(@id, 'title')])[4]")
    fourth_col_two_link_txt_label_first_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-0-subform-field-url') and contains(@for, 'title')])[4]")

    fourth_col_two_numbers_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-title') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_numbers_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-title') and contains(@for, 'edit-field-body-3')])")
    fourth_col_two_numbers_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-title') and contains(@class, 'desc') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_title_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-call-text') and contains(@class, 'desc') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_title_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-call-text') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_title_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-call-text') and contains(@for, 'edit-field-body-3')])")
    fourth_col_two_desc_help_txt_second_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-1-subform-field-teaser') and contains(@class, 'desc') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_desc_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-teaser') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_desc_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-teaser') and contains(@for, 'edit-field-body-3')])")
    fourth_col_two_url_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-url') and contains(@id, 'uri') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_url_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-url') and contains(@for, 'uri') and contains(@for, 'edit-field-body-3')])")
    fourth_col_two_link_txt_second_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-1-subform-field-url') and contains(@id, 'title') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_link_txt_label_second_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-1-subform-field-url') and contains(@for, 'title') and contains(@for, 'edit-field-body-3')])")

    fourth_col_two_numbers_third_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-2-subform-field-title') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_numbers_label_third_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-2-subform-field-title') and contains(@for, 'edit-field-body-3')])")
    fourth_col_two_numbers_help_txt_third_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-2-subform-field-title') and contains(@class, 'desc') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_title_help_txt_third_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-2-subform-field-call-text') and contains(@class, 'desc') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_title_third_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-2-subform-field-call-text') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_title_label_third_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-2-subform-field-call-text') and contains(@for, 'edit-field-body-3')])")
    fourth_col_two_desc_help_txt_third_xpath = (By.XPATH, "(//div[contains(@id, 'field-big-numbers-rows-2-subform-field-teaser') and contains(@class, 'desc') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_desc_third_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-2-subform-field-teaser') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_desc_label_third_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-2-subform-field-teaser') and contains(@for, 'edit-field-body-3')])")
    fourth_col_two_url_third_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-2-subform-field-url') and contains(@id, 'uri') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_url_label_third_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-2-subform-field-url') and contains(@for, 'uri') and contains(@for, 'edit-field-body-3')])")
    fourth_col_two_link_txt_third_xpath = (By.XPATH, "(//input[contains(@id, 'field-big-numbers-rows-2-subform-field-url') and contains(@id, 'title') and contains(@id, 'edit-field-body-3')])")
    fourth_col_two_link_txt_label_third_xpath = (By.XPATH, "(//label[contains(@for, 'field-big-numbers-rows-2-subform-field-url') and contains(@for, 'title') and contains(@for, 'edit-field-body-3')])")


    fourth_col_two_add_more_big_number_tile_xpath = (By.XPATH, "(//div/input[contains(@id, 'add-more-button-big-numbers')])[4]")

    first_col_main_title = "Full Width - 1 Column"
    first_col_number_first = "123456"
    first_col_number_second = "654321"
    first_col_title_first = "Innovation in data"
    first_col_title_second = "AI driver diagonistics"
    first_col_desc_first = "TEST"
    first_col_desc_second = "TEST"
    first_col_link_txt_first = "Google"
    first_col_link_txt_second = "Bing"
    first_col_single_col = "1up"

    second_col_main_title = "Full Width - 2 Column"
    second_col_number_first = "123456"
    second_col_number_second = "654321"
    second_col_title_first = "Innovation in data"
    second_col_title_second = "AI driver diagonistics"
    second_col_desc_first = "TEST"
    second_col_desc_second = "TEST"
    second_col_link_txt_first = "Google"
    second_col_link_txt_second = "Bing"
    second_col_two_col = "2up"

    third_col_one_main_title = "Full Width - 3 Column One"
    third_col_one_number_first = "123456"
    third_col_one_title_first = "Innovation in data"
    third_col_one_desc_first = "TEST"
    third_col_one_link_txt_first = "Google"
    third_col_one_three_col = "3up"

    fourth_col_two_main_title = "Full Width - 3 Column Two"
    fourth_col_two_number_first = "123456"
    fourth_col_two_number_second = "654321"
    fourth_col_two_number_third = "655665"
    fourth_col_two_title_first = "Innovation in data"
    fourth_col_two_title_second = "AI driver diagonistics"
    fourth_col_two_title_third = "BI driver diagonistics"
    fourth_col_two_desc_first = "TEST"
    fourth_col_two_desc_second = "TEST"
    fourth_col_two_desc_third = "TEST"
    fourth_col_two_link_txt_first = "Google"
    fourth_col_two_link_txt_second = "Bing"
    fourth_col_two_link_txt_third = "Facebook"
    fourth_col_two_three_col = "3up"

    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)


    def click_body_dropdown(self, body_dropdown_flag):

        if body_dropdown_flag == 0:
            BasePage.press_button(self, self.body_dropdown_btn_first_time_xpath)
        else:
            BasePage.press_button(self, self.body_dropdown_btn_after_first_time_xpath)

    def big_number_stripe(self):

        # BasePage.is_visible(self, self.accordion_xpath )
        # BasePage.select_dropdown_by_value(self, self.accordion_xpath ,'button')
        BasePage.press_button(self, self.big_number_stripe_xpath)

    def layout_ele(self, select_loc, label_loc, value):

        BasePage.select_dropdown_by_value(self, select_loc, value)
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt

    def main_title_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)

        return label_txt, helper_txt

    def number_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)

        return label_txt, helper_txt

    def title_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)

        return label_txt, helper_txt

    def desc_ele(self, input_loc, label_loc, helper_txt_loc, txt):

        BasePage.send_keys(self, input_loc, txt)
        label_txt = BasePage.get_element_text(self, label_loc)
        helper_txt = BasePage.get_element_text(self, helper_txt_loc)

        return label_txt, helper_txt

    def cta_url_ele(self, input_loc, label_loc):

        BasePage.send_keys(self, input_loc, self.auto_sugg_txt)
        self.driver.find_element(*input_loc).clear()
        BasePage.send_keys(self, input_loc, self.auto_sugg_txt)
        auto_suggestions = self.driver.find_elements(*self.auto_sugg_css)
        sugg_len = len(auto_suggestions)
        rand_num = random.randint(0, sugg_len-1)
        self.driver.execute_script("arguments[0].click()", auto_suggestions[rand_num])
        sugg_txt = BasePage.get_elemet_attribute(self, input_loc, "value")
        label_txt = BasePage.get_element_text(self, label_loc)
        return sugg_txt, label_txt

    def button_link_txt_ele(self, input_loc, label_loc, link_txt):

        BasePage.send_keys(self, input_loc, link_txt)
        label_txt = BasePage.get_element_text(self, label_loc)

        return label_txt

    def add_more_big_number_tile_ele(self, btn_loc):

        BasePage.press_button(self, btn_loc)

