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

class HealthCareLandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    content_box_css = (By.CSS_SELECTOR, "div.content_box")
    banner_img_css = (By.CSS_SELECTOR, "picture > img")
    carousel_wrapper_css = (By.CSS_SELECTOR, "div.carousel_inner--wrapper")
    carousel_item_css = (By.CSS_SELECTOR, "div.carousel-item")
    hero_title_css = (By.CSS_SELECTOR, "h1.stripe_title > a")
    hero_desc_css = (By.CSS_SELECTOR, "p.carousel_desc")
    carousel_link_txt_css = (By.CSS_SELECTOR, "div.carousel_link_button > a")
    intro_txt_css = (By.CSS_SELECTOR, "div.page_content > div.arctic_intro_text > div.field")
    card_css = (By.CSS_SELECTOR, "a.card_wrapper")
    card_img_css = (By.CSS_SELECTOR, ".card_img img")
    card_title_css = (By.CSS_SELECTOR, "a.col-lg-4 h3.card_title")
    card_desc_css = (By.CSS_SELECTOR, "a.col-lg-4 p")
    first_call_to_action_title_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]/h3)[2]")
    second_call_to_action_title_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]/h3)[3]")
    first_call_to_action_desc_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]//p)[2]")
    second_call_to_action_desc_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]//p)[3]")
    first_call_to_action_link_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]//a)[2]")
    second_call_to_action_link_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]//a)[3]")
    accordion_title_css = (By.CSS_SELECTOR, "button.accordion-toggle.accordion-title")
    accordion_body_css = (By.CSS_SELECTOR, "div.accordion-stripe-body p")
    accordion_heading_css = (By.CSS_SELECTOR, "div.accordion_item_wrapper div.arctic_intro_text div.field")
    tab_content_title_css = (By.CSS_SELECTOR, "div.paragraph--type--tab-content > ul a.nav-link")
    tab_content_body_css = (By.CSS_SELECTOR, "div.paragraph--type--tab-content-fields > div.clearfix p")
    tab_contents_css = (By.CSS_SELECTOR, "div.paragraph--type--tab-content-fields div.paragraph--type--rich-text-content div")
    media_content_img_css = (By.CSS_SELECTOR, "div.media_stripe_img > img")
    media_content_copy_txt_css = (By.CSS_SELECTOR, "div.media_stripe_text > h2.stripe_title")
    media_content_teaser_css = (By.CSS_SELECTOR, "div.media_stripe_text > p.stripe_subtitle")
    media_content_cta_title_css = (By.CSS_SELECTOR, "div.media_stripe_text h3.cta_title")
    media_content_cta_desc_css = (By.CSS_SELECTOR, "div.media_stripe_text div.clearfix > p")
    media_content_cta_link_txt_css = (By.CSS_SELECTOR, "div.media_stripe_text div.button-teaser > a")
    media_content_txt_layout_css = (By.CSS_SELECTOR, "div.paragraph--type--media-content > div")
    rich_txt_content_bold_css = (By.CSS_SELECTOR, "div.paragraph--type--rich-text-content p > strong")
    legend_txt_xpath = (By.XPATH, "//div[contains(@class, 'legend')]/p")
    disclaimer_txt_xpath = (By.XPATH, "//div[contains(@class, 'disclaimer')]/p")
    publish_xpath = (By.XPATH, "//a[contains(@data-dialog-type, 'dialog')]")

    def header_slideshow_layout_ele(self):

        return self.get_elemet_attribute(self.content_box_css, "class")

    def banner_img_ele(self):

        img_src = self.get_elemet_attribute(self.banner_img_css, "src")
        img_alt = self.get_elemet_attribute(self.banner_img_css, "alt")
        img_title = self.get_elemet_attribute(self.banner_img_css, "title")
        img_naturalWidth = self.get_elemet_attribute(self.banner_img_css, "naturalWidth")
        
        return img_src, img_alt, img_title, img_naturalWidth

    def carousel_text_color_ele(self):

        return self.get_elemet_attribute(self.carousel_wrapper_css, "class")

    def header_variation_ele(self):

        return self.get_elemet_attribute(self.carousel_item_css, "class")

    def hero_desc_ele(self):

        return self.get_element_text(self.hero_desc_css)

    def hero_title_ele(self):

        hero_title_txt = self.get_element_text(self.hero_title_css)
        hero_title_url = self.get_elemet_attribute(self.hero_title_css, "href")

        return hero_title_txt, hero_title_url

    def carousel_link_txt_ele(self):

        carousel_link_txt = self.get_element_text(self.carousel_link_txt_css)
        carousel_link_href = self.get_elemet_attribute(self.carousel_link_txt_css, "href")

        return carousel_link_txt, carousel_link_href

    def intro_txt_ele(self):

        return self.get_element_text(self.intro_txt_css)

    def cards_col_ele(self):

        card_col = []
        cards = self.driver.find_elements(*self.card_css)
        
        for card in cards:
            card_col.append(card.get_attribute("class"))

        return card_col

    def card_img_ele(self):

        card_img_src_list = []
        card_img_title_list = []
        card_img_alt_list = []
        card_img_naturalWidth_list = []
        card_images = self.driver.find_elements(*self.card_img_css)

        for card_img in card_images:
            card_img_src_list.append(card_img.get_attribute("src"))
            card_img_title_list.append(card_img.get_attribute("title"))
            card_img_alt_list.append(card_img.get_attribute("alt"))
            card_img_naturalWidth_list.append(card_img.get_attribute("naturalWidth"))

        return card_img_src_list, card_img_title_list, card_img_alt_list, card_img_naturalWidth_list

    def card_title_ele(self):

        card_title_list = []

        card_titles = self.driver.find_elements(*self.card_title_css)
        for card_title in card_titles:
            card_title_list.append(card_title.text)

        return card_title_list

    def card_desc_ele(self):

        card_desc_list = []

        card_descs = self.driver.find_elements(*self.card_desc_css)
        for card_desc in card_descs:
            card_desc_list.append(card_desc.text)

        return card_desc_list

    def card_href_ele(self):

        card_href_list = []
        card_hrefs = self.driver.find_elements(*self.card_css)
        for card_href in card_hrefs:
            card_href_list.append(card_href.get_attribute("href"))

        return card_href_list

    def call_to_action_title_ele(self):

        first_call_action_title = self.get_element_text(self.first_call_to_action_title_css)
        second_call_action_title = self.get_element_text(self.second_call_to_action_title_css)

        return first_call_action_title, second_call_action_title

    def call_to_action_desc_ele(self):

        first_call_action_desc = self.get_element_text(self.first_call_to_action_desc_css)
        second_call_action_desc = self.get_element_text(self.second_call_to_action_desc_css)

        return first_call_action_desc, second_call_action_desc

    def call_to_action_link_ele(self):

        first_call_action_label = self.get_element_text(self.first_call_to_action_link_css)
        first_call_action_link = self.get_elemet_attribute(self.first_call_to_action_link_css, "href")
        first_call_action_target = self.get_elemet_attribute(self.first_call_to_action_link_css, "target")
        second_call_action_target = self.get_elemet_attribute(self.second_call_to_action_link_css, "target")
        second_call_action_label = self.get_element_text(self.second_call_to_action_link_css)
        second_call_action_link = self.get_elemet_attribute(self.second_call_to_action_link_css, "href")

        return first_call_action_link, second_call_action_link, first_call_action_label, second_call_action_label, first_call_action_target, second_call_action_target

    def publish_ele(self):

        return self.get_elemet_attribute(self.publish_xpath, "data-label")

    def media_content_img_ele(self):

        image_src = self.get_elemet_attribute(self.media_content_img_css, "src")
        image_alt = self.get_elemet_attribute(self.media_content_img_css, "alt")

        return image_src, image_alt

    def media_content_copy_txt_ele(self):

        return self.get_element_text(self.media_content_copy_txt_css)
    
    def media_content_teaser_ele(self):

        return self.get_element_text(self.media_content_teaser_css)
    
    def media_content_cta_title_ele(self):

        return self.get_element_text(self.media_content_cta_title_css)

    def media_content_cta_desc_ele(self):

        return self.get_element_text(self.media_content_cta_desc_css)
    
    def media_content_cta_link_txt_ele(self):

        return self.get_element_text(self.media_content_cta_link_txt_css)

    def media_content_cta_url_ele(self):

        return self.get_elemet_attribute(self.media_content_cta_link_txt_css, "href")
    
    def media_content_cta_url_target_ele(self):

        return self.get_elemet_attribute(self.media_content_cta_link_txt_css, "target")

    def media_content_txt_layout_ele(self):

        return self.get_elemet_attribute(self.media_content_txt_layout_css, "class")

    def accordion_ele(self):

        arrow_down_list = []
        arrow_up_list = []
        accordion_title_list = []
        accordion_body_list = []
        accordion_heading = self.get_element_text(self.accordion_heading_css)
        accordion_buttons = self.driver.find_elements(*self.accordion_title_css)
        accordion_body = self.driver.find_elements(*self.accordion_body_css)
        index = 0
        for accordion_btn in accordion_buttons:
            accordion_buttons = self.driver.find_elements(*self.accordion_title_css)
            if index == 0:
                arrow_down_script = "return window.getComputedStyle(document.querySelector('button.accordion-toggle.accordion-title'),'::after').getPropertyValue('background-image')";
                arrow_down_list.append(self.driver.execute_script(arrow_down_script))
            self.driver.execute_script("arguments[0].click()", accordion_buttons[index])
            if index == 0:
                arrow_up_script = "return window.getComputedStyle(document.querySelector('button.accordion-toggle.accordion-title'),'::after').getPropertyValue('background-image')";
                arrow_up_list.append(self.driver.execute_script(arrow_up_script))
            accordion_title_list.append(accordion_buttons[index].text)
            accordion_body_list.append(accordion_body[index].text)
            index += 1

        return arrow_down_list, arrow_up_list, accordion_title_list, accordion_body_list, accordion_heading

    def tab_title_ele(self):

        return self.get_element_text(self.tab_content_title_css)

    def tab_body_ele(self):

        return self.get_element_text(self.tab_content_body_css)

    def tab_contents_ele(self):

        return self.get_elements(self.tab_contents_css)

    def rich_text_bold_ele(self):

        return self.get_css_property(self.rich_txt_content_bold_css, "font-weight")

    def legend_ele(self):

        return self.get_element_text(self.legend_txt_xpath)

    def disclaimer_ele(self):

        return self.get_element_text(self.disclaimer_txt_xpath)