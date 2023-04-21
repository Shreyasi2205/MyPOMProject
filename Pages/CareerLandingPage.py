import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from Utilities.config import Utilities

class CareerLandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    hero_img_css = (By.CSS_SELECTOR, "div.carousel_img_video > div > picture > img")
    hero_txt_css = (By.CSS_SELECTOR, "div.carousel-caption > div.container > div.carousel_inner--wrapper > h1.stripe_title")
    function_txt_css = (By.CSS_SELECTOR, "#ms-list-3 > button > span")
    location_txt_css = (By.CSS_SELECTOR, "#ms-list-2 > button > span")
    search_input_field_xpath = (By.XPATH, "//*[starts-with(@id,'edit-search-api-fulltext')]")
    filter_attr_css = (By.CSS_SELECTOR, "div.exposed-filters-wrapper > div")
    location_labels_css = (By.CSS_SELECTOR, "#ms-list-2 > div > ul > li > label")
    location_btn_css = (By.CSS_SELECTOR, "#ms-list-2 > button")
    input_css = (By.CSS_SELECTOR, "input")
    search_btn_xpath = (By.XPATH, "//*[starts-with(@id,'edit-submit-career-search')]")
    stripe_css = (By.CSS_SELECTOR, "div.field__item > div.paragraph.paragraph--type--_-columns-equal-size-card-stripe")
    careers_txt_css = (By.CSS_SELECTOR, "div.content > h1.title > span")
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    mega_menu_career_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/careers') and not(contains(@target,'_self'))]")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")

    def launch_careerLandingPage(self,env_name):
        self.press_button(self.mega_menu_btn_css)
        try:
            self.press_button(self.mega_menu_career_xpath)

        except:
            menu = Utilities.multi_language[env_name]["careers"]
            
            self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}') and not(contains(@target,'_self')) and not(contains(@href,'{menu}/'))]"))


    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

    def hero_ele(self):

        hero_img_display_status = self.is_displayed(self.hero_img_css)
        hero_txt_display_status = self.is_displayed(self.hero_txt_css)

        return hero_img_display_status, hero_txt_display_status


    def stripe_ele(self):

        stripe_elements = self.driver.find_elements(self.stripe_css[0], self.stripe_css[1])
        stripe_list = []

        for stripe_element in stripe_elements:

            stripe_elements = self.driver.find_elements(self.stripe_css[0], self.stripe_css[1])
            stripe_list.append(stripe_element.get_attribute("class"))

        return stripe_list


    def filter_location(self):

        filtered_elements_list = []

        self.press_button(self.location_btn_css)
        location_elements = self.driver.find_elements(self.location_labels_css[0], self.location_labels_css[1])
        location_count = 0
        for ele in location_elements:

            self.driver.execute_script("arguments[0].click()", ele.find_element(self.input_css[0], self.input_css[1]))
            filtered_elements_list.append(ele.find_element(self.input_css[0], self.input_css[1]).get_attribute("title"))
            location_count = location_count + 1
            if location_count == 4:
                break

        self.press_button(self.search_btn_xpath)

        filterd_attributes = self.driver.find_elements(self.filter_attr_css[0], self.filter_attr_css[1])

        filterd_attributes_list = []
        for filtered_attr in filterd_attributes:

            if filtered_attr.text[-1] == "X":
                filterd_attributes_list.append(filtered_attr.text[:-1])
            else:
                filterd_attributes_list.append(filtered_attr.text)

        return filtered_elements_list, filterd_attributes_list
    
