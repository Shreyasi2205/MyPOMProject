#from email import header
import time
#from numpy import var
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

class OurTeamsLandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    content_box_css= (By.CSS_SELECTOR,"div.d-md-block")
    banner_img_css= (By.CSS_SELECTOR,"picture > img")
    carousel_wrapper_css = (By.CSS_SELECTOR, "div.carousel_inner--wrapper")
    carousel_item_css = (By.CSS_SELECTOR, "div.carousel-item")
    hero_text_css = (By.CSS_SELECTOR, "h1.stripe_title")
    hero_desc_css = (By.CSS_SELECTOR, "p.carousel_desc")
    carousel_link_txt_css= (By.CSS_SELECTOR, "div.carousel_link_button > a")
    slideshow_video_css= (By.CSS_SELECTOR,"iframe.mwEmbedKalturaIframe")
    intro_txt_css = (By.CSS_SELECTOR,"div.page_content > div.arctic_intro_text > div.field")
    media_content_copy_txt_css= (By.CSS_SELECTOR,"div.media_stripe_text > h2.stripe_title")
    media_content_teaser_txt_css= (By.CSS_SELECTOR,"div.media_stripe_text > p.stripe_subtitle")
    media_content_cta_title_css= (By.CSS_SELECTOR,"div.cta-teaser > h3.cta_title")
    media_content_cta_desc_css = (By.CSS_SELECTOR,"div.cta_description > div.clearfix")
    media_content_link_txt_css= (By.CSS_SELECTOR,"div.button-teaser > a.button_text")
    media_content_img_css= (By.CSS_SELECTOR,"div.media_stripe_img > img")
    media_content_txt_layout_css=(By.CSS_SELECTOR,"div.paragraph--type--media-content > div")
    rich_txt_content_bold_css= (By.CSS_SELECTOR, "div.paragraph--type--rich-text-content >div > p >strong")
    legend_txt_css= (By.CSS_SELECTOR,"div.field--name-field-legend > p")
    disclaimer_txt_css= (By.CSS_SELECTOR,"div.field--name-field-disclaimer > p")
    publish_xpath= (By.XPATH,"//a[contains(@data-dialog-type, 'dialog')]")

    def slideshow_layout_ele(self):
        slideshow_layouts= []
        layouts=self.driver.find_elements(*self.content_box_css)
        for layout in layouts:
            slideshow_layouts.append(layout.get_attribute("class"))
        return slideshow_layouts


    def banner_img_ele(self):
        banner_img_src_list= []
        banner_img_alt_list= []
        banner_img_title_list= []
        banner_imgs=self.driver.find_elements(*self.banner_img_css)
        for img in banner_imgs:
            banner_img_src_list.append(img.get_attribute("src"))
            banner_img_alt_list.append(img.get_attribute("alt"))
            banner_img_title_list.append(img.get_attribute("title"))
        return banner_img_src_list, banner_img_alt_list, banner_img_title_list
    
    def carousel_txt_color_ele(self):
        carousel_txt_colour_list= []
        txt_colors= self.driver.find_elements(*self.carousel_wrapper_css)
        for txt_color in txt_colors:
            carousel_txt_colour_list.append(txt_color.get_attribute("class"))
        return carousel_txt_colour_list
    
    def slideshow_header_variation_ele(self):
        slideshow_header_variation_list = []
        header_variations=self.driver.find_elements(*self.carousel_item_css)
        for variation in header_variations:
            slideshow_header_variation_list.append(variation.get_attribute("class"))
        return slideshow_header_variation_list
    
    def hero_title_ele(self):
        hero_title_list=[]
        titles=self.driver.find_elements(*self.hero_text_css)
        for title in titles:
            hero_title_list.append(title.text)
        return hero_title_list
    
    def hero_desc_ele(self):
        hero_desc_list=[]
        descs=self.driver.find_elements(*self.hero_desc_css)
        for desc in descs:
            hero_desc_list.append(desc.text)
        return hero_desc_list
    
    def hero_carousel_link_txt_ele(self):
        hero_carousel_link_txt_list=[]
        hero_carousel_link_href_list= []
        hero_link_txts=self.driver.find_elements(*self.carousel_link_txt_css)
        for link_txt in hero_link_txts:
            hero_carousel_link_txt_list.append(link_txt.text)
            hero_carousel_link_href_list.append(link_txt.get_attribute("href"))
        return hero_carousel_link_txt_list, hero_carousel_link_href_list
    
    def slideshow_video_ele(self):
        video_list=[]
        src=self.driver.find_elements(*self.slideshow_video_css)
        for s in src:
            video_list.append(s.get_attribute("class"))
        return video_list

    def intro_txt_ele(self):
        return self.get_element_text(self.intro_txt_css)
    
    def media_content_copy_txt_ele(self):
        media_content_copy_txt_list= []
        copy_txts=self.driver.find_elements(*self.media_content_copy_txt_css)
        for txt in copy_txts:
            media_content_copy_txt_list.append(txt.text)
        return media_content_copy_txt_list
    
    def media_content_teaser_txt_ele(self):
        media_content_teaser_txt_list= []
        teaser_txts=self.driver.find_elements(*self.media_content_teaser_txt_css)
        for teaser in teaser_txts:
            media_content_teaser_txt_list.append(teaser.text)
        return media_content_teaser_txt_list
    
    def media_content_cta_title_ele(self):
        media_content_cta_title_list= []
        cta_titles=self.driver.find_elements(*self.media_content_cta_title_css)
        for cta_title in cta_titles:
            media_content_cta_title_list.append(cta_title.text)
        return media_content_cta_title_list
    
    def media_content_cta_desc_ele(self):
        media_content_cta_desc_list= []
        cta_descs= self.driver.find_elements(*self.media_content_cta_desc_css)
        for desc in cta_descs:
            media_content_cta_desc_list.append(desc.text)
        return media_content_cta_desc_list
    
    def media_content_link_txt_ele(self):
        media_content_link_txt_list= []
        links= self.driver.find_elements(*self.media_content_link_txt_css)
        for link in links:
            media_content_link_txt_list.append(link.text)
        return media_content_link_txt_list
    
    def media_content_txt_layout_ele(self):
        media_content_txt_layout_list= []
        txt_layouts= self.driver.find_elements(*self.media_content_txt_layout_css)
        for layout in txt_layouts:
            media_content_txt_layout_list.append(layout.get_attribute("class"))
        return media_content_txt_layout_list
    
    def rich_txt_content_bold_ele(self):
        return self.get_css_property(self.rich_txt_content_bold_css,"font-weight")
    
    def legend_txt_ele(self):
        return self.get_element_text(self.legend_txt_css)

    def disclaimer_txt_ele(self):
        return self.get_element_text(self.disclaimer_txt_css)
    
    def publish_xpath_ele(self):
        return self.get_elemet_attribute(self.publish_xpath,"data-label")







