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





class NewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    content_box_xpath = (By.XPATH, "(//div[contains(@class, 'content_box')])[1]")
    banner_img_css = (By.CSS_SELECTOR, "picture > img")
    carousel_wrapper_xpath = (By.XPATH, "(//div[contains(@class, 'carousel_inner--wrapper')])[1]")
    carousel_item_xpath = (By.XPATH, "(//div[contains(@class, 'carousel-item')])[1]")
    hero_title_css = (By.CSS_SELECTOR, "h1.stripe_title > a")
    hero_desc_css = (By.CSS_SELECTOR, "p.carousel_desc")
    carousel_link_txt_css = (By.CSS_SELECTOR, "div.carousel_link_button > a")
    intro_txt_css = (By.CSS_SELECTOR, "div.page_content > div.arctic_intro_text > div.field")
    card_css = (By.CSS_SELECTOR, "a.card_wrapper")
    card_img_css = (By.CSS_SELECTOR, ".card_img img")
    card_title_css = (By.CSS_SELECTOR, "a.col-lg-4 h3.card_title")
    card_desc_css = (By.CSS_SELECTOR, "a.col-lg-4 p.basic_paragraph")
    first_call_to_action_title_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]/h3)[1]")
    first_call_to_action_desc_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]//p)[1]")
    first_call_to_action_link_css = (By.XPATH, "(//div[contains(@class, 'field__item')]/div[contains(@class, 'cta-teaser')]//a)[1]")
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
    media_release_title_css = (By.CSS_SELECTOR, "h2.media_release_main_title")
    media_release_view_more_btn_css = (By.CSS_SELECTOR, "div.paragraph--type--media-release a.button_text")
    media_release_items_css = (By.CSS_SELECTOR, "div.paragraph--type--media-release a.media-releases-item")


    def header_slideshow_layout_ele(self, content_box_loc):

        return self.get_elemet_attribute(content_box_loc, "class")

    def banner_img_ele(self):

        img_alt_list = []
        img_title_list = []
        img_src_list = []
        img_naturalWidth_list = []
        images = self.driver.find_elements(*self.banner_img_css)
        for img in images:
            img_src_list.append(img.get_attribute("src"))
            img_alt_list.append(img.get_attribute("alt"))
            img_title_list.append(img.get_attribute("title"))
            img_naturalWidth_list.append(img.get_attribute("naturalWidth"))
        
        return img_src_list, img_alt_list, img_title_list, img_naturalWidth_list

    def carousel_text_color_ele(self, wrapper_loc):

        return self.get_elemet_attribute(wrapper_loc, "class")

    def header_variation_ele(self, carousel_item_loc):

        return self.get_elemet_attribute(carousel_item_loc, "class")

    def hero_desc_ele(self):

        hero_desc_list = []
        hero_descs = self.driver.find_elements(*self.hero_desc_css)
        for desc in hero_descs:
            hero_desc_list.append(desc.text)
        return hero_desc_list

    def hero_title_ele(self):

        hero_title_list = []
        hero_url_list = []
        hero_titles = self.driver.find_elements(*self.hero_title_css)
        for title in hero_titles:
            hero_title_list.append(title.text)
            hero_url_list.append(title.get_attribute("href"))

        return hero_title_list, hero_url_list

    def carousel_link_txt_ele(self):

        carousel_link_txt_list = []
        carousel_link_txt_href_list = []
        links_txts = self.driver.find_elements(*self.carousel_link_txt_css)
        for link_txt in links_txts:
            carousel_link_txt_list.append(link_txt.text)
            carousel_link_txt_href_list.append(link_txt.get_attribute("href"))

        return carousel_link_txt_list, carousel_link_txt_href_list

    def intro_txt_ele(self):

        return self.get_element_text(self.intro_txt_css)

    def media_content_copy_txt_ele(self):

        return self.get_element_text(self.media_content_copy_txt_css)
    
    def media_content_teaser_ele(self):

        return self.get_element_text(self.media_content_teaser_css)
    
    def media_content_cta_link_txt_ele(self):

        return self.get_element_text(self.media_content_cta_link_txt_css)

    def media_content_img_ele(self):

        image_src = self.get_elemet_attribute(self.media_content_img_css, "src")
        image_alt = self.get_elemet_attribute(self.media_content_img_css, "alt")

        return image_src, image_alt

    def media_content_cta_url_ele(self):

        return self.get_elemet_attribute(self.media_content_cta_link_txt_css, "href")
    
    def media_content_cta_url_target_ele(self):

        return self.get_elemet_attribute(self.media_content_cta_link_txt_css, "target")

    def media_content_txt_layout_ele(self):

        return self.get_elemet_attribute(self.media_content_txt_layout_css, "class")
    
    def call_to_action_title_ele(self):

        first_call_action_title = self.get_element_text(self.first_call_to_action_title_css)

        return first_call_action_title

    def call_to_action_desc_ele(self):

        first_call_action_desc = self.get_element_text(self.first_call_to_action_desc_css)

        return first_call_action_desc
    
    def rich_text_bold_ele(self):

        return self.get_css_property(self.rich_txt_content_bold_css, "font-weight")

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

    def media_release_title_ele(self):

        return BasePage.get_element_text(self, self.media_release_title_css)
    
    def media_release_view_more_btn_ele(self):

        btn_value = BasePage.get_element_text(self, self.media_release_view_more_btn_css)
        btn_href = BasePage.get_elemet_attribute(self, self.media_release_view_more_btn_css, "href")

        return btn_value, btn_href

    def media_release_items_ele(self):

        return len(self.driver.find_elements(*self.media_release_items_css))

    