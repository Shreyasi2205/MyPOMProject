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
import random

class BiographyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    mega_menu_about_arrow_xpath = (By.XPATH, "//li[contains(@class, 'dropdown-menu')]/a[contains(@href, 'about')  and not(contains(@href,'about/'))]//parent::li/p")
    mega_menu_about_xpath = (By.XPATH, "//li[contains(@class, 'dropdown-menu')]/a[contains(@href, '/about') and not(contains(@href,'about/'))]")
    mega_menu_board_of_directors_xpath = (By.XPATH, "(//li[contains(@class, 'we-mega-menu-li')]/a[contains(@href, '/about/board-directors')])[1]")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li")
    anchor_tag_loc = (By.TAG_NAME, "a")
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    breadcrumb_lists_anchor_tag_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    link_button_css = (By.CSS_SELECTOR,'a[class="link_button button_text element_margin"]')
    boardOfDirectors_last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child > a")
    breadcrumb_lists_anchor_css = (By.CSS_SELECTOR, "ol.breadcrumb > li > a")
    share_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(2)")
    print_save_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(1)")
    anchor_tag_css = (By.CSS_SELECTOR,'a')
    share_btn_css = (By.CSS_SELECTOR, ".addtoany_share")
    print_css = (By.CSS_SELECTOR, "li.print > a")
    save_css = (By.CSS_SELECTOR, "li.pdf > a")


    def launch_board_of_directors(self,env_name):

        self.press_button(self.mega_menu_btn_css)
     
        if self.driver.get_window_size().get("width") <= 1050:
            self.press_button(self.mega_menu_about_arrow_xpath)
        else:
            self.move_to_element(self.mega_menu_about_xpath)

        self.press_button(self.mega_menu_board_of_directors_xpath)

    def print_block_ele(self):       

        print_block = len(self.driver.find_elements(*self.print_css))
        
        return print_block


    def share_block_ele(self):

        share_block = len(self.driver.find_elements(*self.share_btn_css))

        return share_block

    def save_block_ele(self):

        save_block = len(self.driver.find_elements(*self.save_css))

        return save_block

    def print_share_misalignment(self):

        share_block = self.get_elemet_attribute(self.share_block_css, "id")
        print_save_block = self.get_elemet_attribute(self.print_save_block_css, "id")

        return share_block, print_save_block


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


    def detailPage_breadcrumb_ele(self):

        index = 0
        breadcrumb_items = []
        breadcrumb_text =[]
        breadcrumb_first_arrow_element = []
        breadcrumb_second_arrow_element =[]
        breadcrumb_third_arrow_element = []
        breadcrumb_fourthLevel_color = []

        link_buttons = self.driver.find_elements(*self.link_button_css)
        for button in link_buttons : 
            
            link_buttons = self.driver.find_elements(*self.link_button_css)
            self.driver.execute_script("arguments[0].click()", link_buttons[index])
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
          

            breadcrumb_third_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child'),'::before').getPropertyValue('content')";
            element = self.driver.execute_script(breadcrumb_third_arrow_script);
            breadcrumb_third_arrow_element.append(element)
            
            breadcrumb_fourthLevel_color.append(self.get_css_color(self.boardOfDirectors_last_child_breadcrumb_color_css,"color"))
            index += 1
            self.driver.back()
            
        
        return index, breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_third_arrow_element,breadcrumb_fourthLevel_color


    def breadcrumbs_firstLevel_secondLevel_thirdLevel(self):

        
        home_url = []
        home_current_url = []
        boardOfDirectors_url = []
        boardOfDirectors_current_url = []
        boardOfDirectors_search_url = []
        boardOfDirectors_current_search_url = []
        breadcrumb_index = 0
        index = 0

        link_buttons = self.driver.find_elements(*self.link_button_css)
        for button in link_buttons : 
            
            link_buttons = self.driver.find_elements(*self.link_button_css)
            self.driver.execute_script("arguments[0].click()", link_buttons[index])
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
                    boardOfDirectors_url.append(breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href"))
                    self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
                    boardOfDirectors_current_url.append(self.driver.current_url)
                    self.driver.back()
                elif breadcrumb_index == 2:
                    breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
                    boardOfDirectors_search_url.append(breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href"))
                    self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
                    boardOfDirectors_current_search_url.append(self.driver.current_url)
                    self.driver.back()
                else:
                    break
                breadcrumb_index = breadcrumb_index + 1
                if breadcrumb_index == 3:
                    breadcrumb_index = 0
            index += 1
            self.driver.back()
            
        
        return index ,home_url, home_current_url, boardOfDirectors_url, boardOfDirectors_current_url, boardOfDirectors_search_url, boardOfDirectors_current_search_url




    

   