import time
import pytest
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.color import Color
from Utilities.config import Utilities
import random



class KeyReleasePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    keyRelease_tab_xpath = (By.XPATH,"//li[contains(@class,'nav-item')]/a[contains(@href,'Release&language')]")
    content_title_css = (By.CSS_SELECTOR,'.views-field-title >  span.field-content')
    pagination_heading_xpath = (By.XPATH, "//nav[contains(@aria-label,'pagination-heading')]")
    next_page_arrow_xpath = (By.XPATH, "//a[@rel='next']")
    total_row_css = (By.CSS_SELECTOR,'.whole-item >.each-item')
    anchor_tag_css = (By.CSS_SELECTOR,'a')
    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "ol.breadcrumb > li")
    anchor_tag_loc = (By.TAG_NAME, "a")
    last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3) > a")
    breadcrumb_lists_anchor_css = (By.CSS_SELECTOR, "ol.breadcrumb > li > a")
    title_css = (By.CSS_SELECTOR,'.title')
    print_css = (By.CSS_SELECTOR, "li.print > a")
    save_css = (By.CSS_SELECTOR, "li.pdf > a")
    share_btn_css = (By.CSS_SELECTOR, ".addtoany_share")
    date_css = (By.CSS_SELECTOR,' a > span >.field-content >.datetime')
    related_links_xpath = (By.XPATH, "//*[contains(@class, 'right-hand-rail')]")
    menu_css = (By.CSS_SELECTOR, ".menu > button")
    novartis_logo_css = (By.CSS_SELECTOR, "#navbar-main > a > img")
    search_css = (By.CSS_SELECTOR, ".search > button")
    interior_date_css = (By.CSS_SELECTOR,'.item_value')
    share_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(2)")
    print_save_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(1)")
    prev_page_arrow_xpath = (By.XPATH, "//a[@rel='prev']")
    blocks_css =(By.CSS_SELECTOR,'[class="pre_links"] >li')
    search_icon_css = (By.CSS_SELECTOR, "li.nav-item.search > button img.icon-search")
    


    def duplicate_contents(self):

        content_title_list = []
        content_title_set = set()
        for i in range(2):
            content_titles = self.driver.find_elements(*self.content_title_css)
            for title in content_titles:
                content_title_list.append(str(title.text.encode("utf-8"))[1:].replace("'", ""))
                content_title_set.add(str(title.text.encode("utf-8"))[1:].replace("'", ""))
            if len(self.driver.find_elements(*self.pagination_heading_xpath)) > 0:
                self.press_button(self.next_page_arrow_xpath) 
                WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.prev_page_arrow_xpath))
                
            else :
                 break
        
        return content_title_list, content_title_set


    def pattern_verify(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        pattern_stripe_paths = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            pattern_stripe_paths.append(self.get_css_property(self.pattern_css, "background-image"))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index , pattern_stripe_paths


    def breadcrumb_elements(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        breadcrumb_items = []
        breadcrumb_text =[]
        breadcrumb_first_arrow_element = []
        breadcrumb_second_arrow_element =[]
        breadcrumb_thirdLevel_color = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            keyRelease_card = total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]).text
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            
            breadcrumb_lists = self.driver.find_elements(self.breadcrumb_lists_css[0], self.breadcrumb_lists_css[1])
            for breadcrumb_list in breadcrumb_lists:
                breadcrumb_text.append(breadcrumb_list.find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).text)
            breadcrumb_items.append(len(breadcrumb_text))
            breadcrumb_text.clear()

            breadcrumb_first_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').getPropertyValue('content')";
            element = self.driver.execute_script(breadcrumb_first_arrow_script);
            breadcrumb_first_arrow_element.append(element)

            breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3)'),'::before').getPropertyValue('content')";
            element = self.driver.execute_script(breadcrumb_second_arrow_script);
            breadcrumb_second_arrow_element.append(element)
          
            breadcrumb_thirdLevel_color.append(self.get_css_color(self.last_child_breadcrumb_color_css,"color"))
            self.driver.back()
            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index, breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_thirdLevel_color



    def breadcrumbs_firstLevel_secondLevel_thirdLevel(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        home_url = []
        home_current_url = []
        news_url = []
        news_current_url = []
        breadcrumb_index = 0
        row_index = 0

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
            for breadcrumb in breadcrumb_lists_anchor_elements:
                if breadcrumb_index == 0:
                    breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
                    home_url.append(breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href"))
                    self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
                    home_current_url.append(self.driver.current_url)
                    self.driver.back()
                elif breadcrumb_index == 1:
                    breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
                    news_url.append(breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href"))
                    self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
                    news_current_url.append(self.driver.current_url)
                    self.driver.back()
                else:
                    break
                breadcrumb_index = breadcrumb_index + 1
                if breadcrumb_index == 2:
                    breadcrumb_index = 0

            self.driver.back()
            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index,home_url, home_current_url, news_url, news_current_url


    def title_verify(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        tile_status = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            tile_status.append(self.is_displayed(self.title_css))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index , tile_status


    def print_btn_ele(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        print_btn_list = []
        print_btn_clickable_status = []
        print_icon_list = []
        print_url_list = []
        print_page_url_list = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            print_btn_list.append(self.is_displayed(self.print_css))
            print_btn_clickable_status.append(self.element_clickable(self.print_css))
            print_url_list.append(self.get_elemet_attribute(self.print_css, "href"))
            print_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('li.print > a'),'::before').getPropertyValue('background')");
            print_icon_list.append(print_icon)
            self.press_button(self.print_css)
            print_page_url_list.append(self.driver.current_url)
            self.driver.back()

            self.driver.back()
            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index,print_btn_list, print_btn_clickable_status, print_icon_list,print_url_list,print_page_url_list



    def save_btn_ele(self):


        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        save_btn_list = []
        save_btn_clickable_status = []
        save_icon_list = []
        save_href_list = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            save_btn_list.append(self.is_displayed(self.save_css))
            save_btn_clickable_status.append(self.element_clickable(self.save_css))
            save_href_list.append(self.get_elemet_attribute(self.save_css, "href"))
            save_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('li.pdf > a'),'::before').getPropertyValue('background')");
            save_icon_list.append(save_icon)
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
            
        return row_index,save_btn_list,save_btn_clickable_status,save_icon_list,save_href_list



    def share_btn_ele(self):


        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        share_btn_icon_list = []
        share_btn_list = []
        twitter_icon_list = []
        facebook_icon_list = []
        whatsapp_icon_list = []
        linkedin_icon_list = []
        email_icon_list = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            share_btn_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.addtoany_share'),'::before').getPropertyValue('background')");
            share_btn_icon_list.append(share_btn_icon)
            share_btn_list.append(self.is_displayed(self.share_btn_css))
            self.press_button(self.share_btn_css)

            twitter_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_twitter'),'::before').getPropertyValue('background')");
            twitter_icon_list.append(twitter_icon)
            facebook_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_facebook'),'::before').getPropertyValue('background')");
            facebook_icon_list.append(facebook_icon)
            whatsapp_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_whatsapp'),'::before').getPropertyValue('background')");
            whatsapp_icon_list.append(whatsapp_icon)
            linkedin_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_linkedin'),'::before').getPropertyValue('background')");
            linkedin_icon_list.append(linkedin_icon)
            email_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_email'),'::before').getPropertyValue('background')");
            email_icon_list.append(email_icon)
            self.driver.back()

            row_index = row_index + 1
            if row_index == 4:
                break

        return row_index , share_btn_icon_list,share_btn_list, twitter_icon_list,facebook_icon_list,whatsapp_icon_list,linkedin_icon_list,email_icon_list



    def date_verify(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        card_date = []
        interior_card_date = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            content_date = total_rows[rand_num].find_element(self.date_css[0], self.date_css[1])
            card_date.append(content_date.text)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            interior_card_date.append(self.get_element_text(self.interior_date_css))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index , card_date, interior_card_date



    def related_links_ele(self):

        related_links_list = []
        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        total_rows_len = len(total_rows)
        random_content_number = random.randint(0,total_rows_len-1)
        index = 0

        for row in total_rows :

            random_content_number = random.randint(0,total_rows_len-1)

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            self.driver.execute_script("arguments[0].click()", total_rows[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            related_links_list.append(len(self.driver.find_elements(*self.related_links_xpath)))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return related_links_list



    def menu_ele(self):

        menu_display_list = []
        menu_len_list = []
        menu_icon_list = []
        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        total_rows_len = len(total_rows )
        random_content_number = random.randint(0,total_rows_len-1)
        index = 0

        for row in total_rows:

            random_content_number = random.randint(0,total_rows_len-1)

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            self.driver.execute_script("arguments[0].click()", total_rows[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            menu_display_list.append(self.is_displayed(self.menu_css))
            menu_len_list.append(len(self.get_element_text(self.menu_css)))
            menu_icon_script = "return window.getComputedStyle(document.querySelector('.menu > button'),'::before').getPropertyValue('background')";
            menu_icon_list.append(self.driver.execute_script(menu_icon_script))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return menu_display_list, menu_len_list, menu_icon_list



    def logo_ele(self):

        menu_display_list = []
        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        total_rows_len = len(total_rows)
        random_content_number = random.randint(0,total_rows_len -1)
        index = 0

        for row in total_rows:

            random_content_number = random.randint(0,total_rows_len -1)

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            self.driver.execute_script("arguments[0].click()", total_rows [random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            menu_display_list.append(self.is_displayed(self.novartis_logo_css))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return menu_display_list



    def search_ele(self):

        search_display_list = []
        search_len_list = []
        search_icon_list = []
        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        total_rows_len = len(total_rows)
        random_content_number = random.randint(0,total_rows_len -1)
        index = 0

        for row in total_rows:

            random_content_number = random.randint(0,total_rows_len -1)

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])

            self.driver.execute_script("arguments[0].click()", total_rows[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            search_display_list.append(self.is_displayed(self.search_css))
            search_len_list.append(len(self.get_element_text(self.search_css)))
            search_icon_list.append(self.get_elemet_attribute(self.search_icon_css, "src"))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return search_display_list, search_len_list, search_icon_list



    def print_block_ele(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        print_list = []
       

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            print_list.append(self.get_elemet_attribute(self.print_css, "href"))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index, print_list



    def save_block_ele(self):


        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        save_list = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            save_list.append(self.get_elemet_attribute(self.save_css, "href"))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
            
        return row_index, save_list


    def print_share_misalignment(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        share_block = []
        print_save_block = []
       

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            share_block.append(self.get_elemet_attribute(self.share_block_css, "id"))
            print_save_block.append(self.get_elemet_attribute(self.print_save_block_css, "id"))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index, share_block, print_save_block


    def share_block_ele(self):


        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        save_list = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            save_list.append(self.get_elemet_attribute(self.share_btn_css, "class"))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
            
        return row_index, save_list



    def print_save_block_alignment(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        print_block_list = []
        save_block_list =[]
       

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            blocks = self.driver.find_elements(*self.blocks_css)
            count = 0
            print_block_list.append(blocks[count].get_attribute('class'))
            save_block_list.append(blocks[count+1].get_attribute('class'))
                
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
        
        return print_block_list ,  save_block_list 











