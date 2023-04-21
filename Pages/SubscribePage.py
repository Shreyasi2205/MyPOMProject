import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
import random
from Utilities.config import Utilities

class SubscribePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    first_name = "Williams"
    last_name = "Phillips"
    email = "test9@gmail.com"
    phone_no = "+12015558970"
    employer = "Novartis"
    occupation = "Scientist"
    location_value = "United States"
    quantity = "2"
    street_address = "1809 Spruce Drive"
    city = "Pittsburgh"
    zip_code = "15203"
    country = "United States"
    captcha_warning_txt = "The answer you entered for the CAPTCHA was not correct."
    first_name_label_xpath = (By.XPATH, "//label[contains(@for,'edit-f-name')]")
    first_name_id = (By.ID, "edit-f-name")
    last_name_label_xpath = (By.XPATH, "//label[contains(@for,'edit-l-name')]")
    last_name_id = (By.ID, "edit-l-name")
    email_label_xpath = (By.XPATH, "//label[contains(@for,'edit-email')]")
    email_id = (By.ID, "edit-email")
    phone_label_xpath = (By.CSS_SELECTOR, "#edit-phone--wrapper > legend > span")
    phone_id = (By.ID, "edit-phone-phone")
    employer_label_xpath = (By.XPATH, "//label[contains(@for,'edit-work-name')]")
    employer_id = (By.ID, "edit-work-name")
    occupation_label_xpath = (By.XPATH, "//label[contains(@for,'edit-work-title')]")
    occupation_id = (By.ID, "edit-work-title")
    location_label_xpath = (By.XPATH, "//label[contains(@for,'edit-country-country')]")
    location_id = (By.ID, "edit-country-country")
    agree_id = (By.ID, "edit-accept-privacy-policy--description")
    agree_checkbox_id = (By.ID, "edit-accept-privacy-policy")
    submit_btn_id = (By.ID, "edit-actions-submit")
    danger_alert_css = (By.CSS_SELECTOR, "div.alert.alert-danger")
    lang_checkbox_css = (By.CSS_SELECTOR, "div#edit-p-list-id > div")
    label_tag_css = (By.CSS_SELECTOR, "label")
    input_tag_css = (By.CSS_SELECTOR, "input")
    stay_up_to_date_css = (By.CSS_SELECTOR, "ol.breadcrumb > li:last-child > a")
    remove_btn_xpath = (By.XPATH, "//*[contains(@id,'operations-remove')]")
    add_publication_btn = (By.ID, "edit-order-information-add-submit")
    street_address_xpath = (By.XPATH, "//label[contains(@for,'edit-address-address')]")
    city_town_xpath = (By.XPATH, "//label[contains(@for,'edit-address-city')]")
    zip_xpath = (By.XPATH, "//label[contains(@for,'edit-address-postal-code')]")
    country_xpath = (By.XPATH, "//label[contains(@for,'edit-address-country')]")
    publication_name_field_xpath = (By.XPATH, "//select[contains(@id,'publication-name')]")
    quantity_field_xpath = (By.XPATH, "//input[contains(@id,'quantity')]")
    street_address_field_id = (By.ID, "edit-address-address")
    city_town_field_id = (By.ID, "edit-address-city")
    zip_field_id = (By.ID, "edit-address-postal-code")
    country_field_id = (By.ID, "edit-address-country")
    edit_subscribe_id = (By.ID, "edit-subscribe")
    edit_unsubscribe_id = (By.ID, "edit-unsubscribe")
    publication_order_form_id = (By.ID, "edit-publication-order-form")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li")
    anchor_tag_loc = (By.TAG_NAME, "a")
    publication_css = (By.CSS_SELECTOR, "td > fieldset > div > select.form-select.form-control > option")
    publication_label_css = (By.CSS_SELECTOR, ".order_information-table--publication_name")
    quantity_label_css = (By.CSS_SELECTOR, ".order_information-table--quantity")
    lang_label_css = (By.CSS_SELECTOR, "#edit-p-list-id--wrapper > legend > span")
    location_dropdown_xpath = (By.XPATH, "//select[starts-with(@id, 'edit-country-country')]//parent::div/ul/li")
    publication_dropdown_xpath = (By.XPATH, "//select[starts-with(@id, 'edit-order-information-items')]//parent::div/ul/li")
    country_dropdown_xpath = (By.XPATH, "//select[starts-with(@id, 'edit-address-country')]//parent::div/ul/li")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    mega_menu_news_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]//parent::li/p[@class='we-icon']")
    mega_menu_news_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]")
    mega_menu_subscribe_xapth= (By.XPATH, "(//a[contains(@href,'/news/stay-up-to-date')])[2]")
    breadcrumb_lists_anchor_tag_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    subscribe_last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child > a")
    subscribe_page_title_css = (By.CSS_SELECTOR, "#block-pagetitle > div > h1")

    def launch_subscribePage(self,env_name):

        self.press_button(self.mega_menu_btn_css)
        if self.driver.get_window_size().get("width") <= 1050:
            self.press_button(self.mega_menu_news_arrow_xpath)
        else:
            self.move_to_element(self.mega_menu_news_xpath)

        self.press_button(self.mega_menu_subscribe_xapth)
       

    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

    def click_subscribe(self):

        self.press_button(self.edit_subscribe_id)

    def click_unsubscribe(self):

        self.press_button(self.edit_unsubscribe_id)

    def click_publication_order_form(self):

        self.press_button(self.publication_order_form_id)

    def fill_mandatory_fields(self):

        self.send_keys(self.first_name_id, self.first_name)
        self.send_keys(self.last_name_id, self.last_name)
        self.send_keys(self.email_id, self.email)

    def fill_mandatory_fields_unsubscribe(self):

        self.send_keys(self.email_id, self.email)

    def fill_optional_fields(self):

        self.send_keys(self.phone_id, self.phone_no)
        self.send_keys(self.employer_id, self.employer)
        self.send_keys(self.occupation_id, self.occupation)
        locations = self.driver.find_elements(*self.location_dropdown_xpath)
        locations_len = len(locations)
        random_location = random.randint(1, locations_len-1)
        self.driver.execute_script("arguments[0].click()", locations[random_location])

    def agree_checkbox_ele(self):

        self.press_button(self.agree_checkbox_id)

    def click_submit_btn(self):

        self.press_button(self.submit_btn_id)

    def alert_danger(self):

        alert_txt = self.get_element_text(self.danger_alert_css)

        return alert_txt

    def publication_mandatory_fields(self):

        publications = self.driver.find_elements(*self.publication_dropdown_xpath)
        publication_len = len(publications)
        random_publication = random.randint(1, publication_len-1)
        # self.select_dropdown_by_index(self.publication_name_field_xpath[1], publication_index, self.publication_name_field_xpath[0])
        self.driver.execute_script("arguments[0].click()", publications[random_publication])
        self.send_keys(self.quantity_field_xpath, self.quantity)
        self.send_keys(self.street_address_field_id, self.street_address)
        self.send_keys(self.city_town_field_id, self.city)
        self.send_keys(self.zip_field_id, self.zip_code)
        # self.select_dropdown_by_value(self.country_field_id[1], self.country, self.country_field_id[0])
        countries = self.driver.find_elements(*self.country_dropdown_xpath)
        country_len = len(countries)
        random_country = random.randint(1, country_len-1)
        self.driver.execute_script("arguments[0].click()", countries[random_country])


    def breadcrumb_ele(self):

        breadcrumb_items = []
        breadcrumb_lists = self.driver.find_elements(self.breadcrumb_lists_css[0], self.breadcrumb_lists_css[1])
        for breadcrumb_list in breadcrumb_lists:
            breadcrumb_items.append(breadcrumb_list.find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).text)


        breadcrumb_first_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').getPropertyValue('content')";
        breadcrumb_first_arrow_element = self.driver.execute_script(breadcrumb_first_arrow_script);

        breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child'),'::before').getPropertyValue('content')";
        breadcrumb_second_arrow_element = self.driver.execute_script(breadcrumb_second_arrow_script);

        return breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element

    def check_all_breadcrumb_url(self):

        breadcumb_anchor_url_list = []
        breadcumb_anchor_current_url_list = []
        breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_tag_css[0], self.breadcrumb_lists_anchor_tag_css[1])
        breadcumb_index = 0
        for breadcumb_anchor in breadcumb_anchor_elements:

            breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_tag_css[0], self.breadcrumb_lists_anchor_tag_css[1])
            breadcumb_anchor_url_list.append(breadcumb_anchor_elements[breadcumb_index].get_attribute("href"))
            self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
            breadcumb_anchor_current_url_list.append(self.driver.current_url)
            self.driver.back()

            breadcumb_index = breadcumb_index + 1

            if breadcumb_index == 2:
                break

        return breadcumb_anchor_url_list, breadcumb_anchor_current_url_list 
