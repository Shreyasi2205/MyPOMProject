import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from BaseTest import BaseTest
from Helper import Helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Utilities.config import Utilities
import time

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.global_site
@pytest.mark.migration
@pytest.mark.singapore
@pytest.mark.usa
@pytest.mark.eg
@pytest.mark.sandoz
@pytest.mark.de
@pytest.mark.jp
@pytest.mark.it
@pytest.mark.za
@pytest.mark.tw
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.lv
@pytest.mark.ar
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ru
@pytest.mark.ie
@pytest.mark.fi
@pytest.mark.at
# @pytest.mark.no
# @pytest.mark.cz
# @pytest.mark.rs
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.ve
@pytest.mark.bd
@pytest.mark.be
@pytest.mark.au
@pytest.mark.pl
class Test_FeaturedNews(BaseTest):

     def test_ARC_5647_featuredNews_get_featuredNews(self):

        """
        Launches Featured News Page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)


     def test_ARC_5647_featuredNews_tab_greyedOut(self):

        """
        Checks if Featured News Tab is greyed out or not.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        assert "#f1f1f1" == self.basePage.get_css_color(self.featuredNewsPage.featuredNews_tab_xpath, "background-color")


     def test_ARC_5647_featuredNews_check_url(self):

        """
        Checks if it is in the correct tab or not.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        assert "type=news" in self.driver.current_url



     def test_ARC_5647_featuredNews_menu(self):

        """
        Checks if Mega Menu button is available or not after clicking on the Featured News Tab.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        assert self.basePage.is_displayed(self.featuredNewsPage.menu_css) == True
        assert len(self.basePage.get_element_text(self.featuredNewsPage.menu_css)) > 0
        menu_icon_script = "return window.getComputedStyle(document.querySelector('.menu > button'),'::before').getPropertyValue('background')";
        assert "icon-menu.svg" in self.driver.execute_script(menu_icon_script)
 

     def test_ARC_5647_featuredNews_logo(self):

        """
        Checks if Novartis logo is available or not after clicking on the Featured News Tab.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        assert self.basePage.is_displayed(self.featuredNewsPage.novartis_logo_css) == True
       
     def test_ARC_5647_featuredNews_search(self):

        """
        Checks if Global Search Icon is available or not after clicking on the Featured News Tab.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        assert self.basePage.is_displayed(self.featuredNewsPage.search_css) == True
        assert len(self.basePage.get_element_text(self.featuredNewsPage.search_css)) > 0
        #search_icon_script = "return window.getComputedStyle(document.querySelector('.search > button'),'::before').getPropertyValue('background')";
        assert "icon-search.svg" in self.basePage.get_elemet_attribute(self.featuredNewsPage.search_icon_css, "src")


     def test_ARC_5647_featuredNews_tags(self):

        """
        Checks if in every card, filter name is available.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)

        total_cards = self.driver.find_elements(*self.featuredNewsPage.content_pages_css)
        total_tags = self.driver.find_elements(*self.featuredNewsPage.tags_css)
        assert len(total_cards) == len(total_tags)


     def test_ARC_5647_featuredNews_date(self):

        """
        Checks if dates are in descending order or not.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)

        desc_sort = self.featuredNewsPage.date_format(self.env_name)
        assert desc_sort == True
        

     def test_ARC_5647_featuredNews_duplicate_contents(self):

        """
        Checks for duplicate featured news.
        """

        duplicate_values = []
        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        content_title_list, content_title_set = self.featuredNewsPage.duplicate_contents()
        for i in range(0, len(content_title_list)):    
            for j in range(i+1, len(content_title_list)):    
                if(content_title_list[i] == content_title_list[j]):    
                   duplicate_values.append(content_title_list[j])
        assert len(content_title_list) == len(content_title_set),f"Duplicate titles are {duplicate_values}" 


     def test_ARC_5647_featuredNews_pagination(self):

        """
        Checks Pagination
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name) 
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)   
        if len(self.driver.find_elements(self.featuredNewsPage.pagination_heading_xpath[0], self.featuredNewsPage.pagination_heading_xpath[1])) > 0:    
            num_content_page,pagination_heading, page_content_list = self.featuredNewsPage.pagination_validation()
            if num_content_page == 12 and pagination_heading > 0 :
                  page_count_len = len(page_content_list)
                  while page_count_len > 0:
                     assert len(page_content_list) > 0
                     page_count_len = page_count_len - 1


     def test_ARC_5647_featuredNews_pagination_front_arrow_back_arrow(self):

        """
        Checks if front and back arrows are working in the pagination section.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 
        if len(self.driver.find_elements(self.featuredNewsPage.pagination_heading_xpath[0], self.featuredNewsPage.pagination_heading_xpath[1])) > 0:
            num_content_page,pagination_heading,page_one_contents, page_zero_contents = self.featuredNewsPage.pagination_front_arrow_back_arrow_validation()
            if num_content_page == 12 and pagination_heading > 0 :
                  assert len(page_one_contents) > 0
                  assert len(page_zero_contents) > 0


     def test_ARC_5647_featuredNews_detailPage_pattern(self):

         """
         Checks if Pattern is available or not in Featured News Details Page.
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 
         row_index, pattern_stripe_paths = self.featuredNewsPage.pattern_verify()
         index = 0
         assert row_index > 0
         for row in range(row_index):
                  assert "patterns" in pattern_stripe_paths[index]
                  index += 1
               

   # Already covered in test_breadcrumb
   #   def test_ARC_5647_featuredNews_detailPage_breadcrumbs(self):

   #       self.driver.get(self.env)
   #       self.newsPage.launch_newsArchive(self.env_name)
   #       self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 
   #       row_index, breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_thirdLevel_color = self.featuredNewsPage.breadcrumb_elements()
   #       index = 0
   #       for row in range(row_index):
               
   #             assert breadcrumb_items[index] == 3
   #             assert "#656565" == breadcrumb_thirdLevel_color[index]

   #             assert ">" in breadcrumb_first_arrow_element[index]
   #             assert ">" in breadcrumb_second_arrow_element[index]

   #             index += 1

   # Already covered in test_breadcrumb
   #   def test_ARC_5647_featuredNews_detailPage_first_second_third_level_breadcrumbs(self):

   #      self.driver.get(self.env)
   #      self.newsPage.launch_newsArchive(self.env_name)
   #      self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 
   #      row_index,home_url, home_current_url, news_url, news_current_url = self.featuredNewsPage.breadcrumbs_firstLevel_secondLevel_thirdLevel()
   #      index = 0
   #      for row in range(row_index):
            
   #          assert home_current_url[index] ==  home_url[index]
   #          assert news_current_url[index] ==  news_url[index]
            
   #          index += 1


     def test_ARC_5647_featuredNews_detailPage_title(self):

        """
        Checks if Title is available or not in Featured News Details Page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 
        row_index , tile_status = self.featuredNewsPage.title_verify()
        index = 0
        assert row_index > 0
        for row in range(row_index):
               assert True == tile_status[index]
               index += 1
 
   
     def  test_ARC_5647_featuredNews_detailPage_print_button(self):

        """
        Checks the Following things in Featured News Details Page :-
        1. Print button
        2. Print Icon
        3. Print Button Opening the correct page
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 
        row_index,print_btn_list, print_btn_clickable_status, print_icon_list,print_url_list,print_page_url_list = self.featuredNewsPage.print_btn_ele()
        index = 0
        assert row_index > 0
        for row in range(row_index):

            assert print_btn_list[index] == True
            assert print_btn_clickable_status[index] == True
            assert "print" in print_icon_list[index]
            assert print_url_list[index] == print_page_url_list[index]
            index += 1

     def  test_ARC_5647_featuredNews_detailPage_save_button(self):

        """
        Checks the Following things in Featured News Details Page :-
        1. Save button
        2. Save Icon
        3. Save Button has href or not in <a> tag
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 
        row_index,save_btn_list,save_btn_clickable_status,save_icon_list,save_href_list = self.featuredNewsPage.save_btn_ele()
        index = 0
        assert row_index > 0
        for row in range(row_index):

            assert save_btn_list[index] == True
            assert save_btn_clickable_status[index] == True
            assert "save" in save_icon_list[index]
            assert len(save_href_list[index]) > 0

            index += 1

     def  test_ARC_5647_featuredNews_detailPage_share_button(self):

        """
        Checks the Following things in Featured News Details Page :-
        1. Share button
        2. Share Icon
        3. Twitter Icon
        4. Facebook Icon
        5. Whatsapp Icon
        6. Linkedin Icon
        7. Email Icon
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 
        row_index , share_btn_icon_list,share_btn_list, twitter_icon_list,facebook_icon_list,whatsapp_icon_list,linkedin_icon_list,email_icon_list = self.featuredNewsPage.share_btn_ele()
        index = 0
        for row in range(row_index):

            assert "share" in share_btn_icon_list[index]
            assert share_btn_list[index] == True
            assert "twitter" in twitter_icon_list[index]
            assert "facebook" in facebook_icon_list[index]
            assert "whatsapp" in whatsapp_icon_list[index]
            assert "linkedin" in linkedin_icon_list[index]
            assert "email" in email_icon_list[index]

            index += 1


     def test_ARC_5647_featuredNews_detailPage_related_links(self):

        """
        Checks if Related links are available or not in Featured News Details Page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 

        related_links_list,related_links_href,related_links_url = self.featuredNewsPage.related_links_ele()
        if len(related_links_list) > 0:
            index = 0
            for  href , url in zip(related_links_href,related_links_url):
                href[index] == url[index]
                index += 1



     def test_ARC_5647_featuredNews_detailPage_menu(self):

        """
        Checks if Mega Menu is there or not in Featured News Details Page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 


        menu_display_list, menu_len_list, menu_icon_list = self.featuredNewsPage.menu_ele()
        for menu_display, menu_len, menu_icon in zip(menu_display_list, menu_len_list, menu_icon_list):
            assert "icon-menu.svg" in menu_icon
            assert menu_len > 0
            assert menu_display == True


     def test_ARC_5647_featuredNews_detailPage_logo(self):

        """
        Checks if Logo is there or not in Featured News Details Page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 

        menu_display_list = self.featuredNewsPage.logo_ele()
        for menu_display in menu_display_list:
            assert menu_display == True


     def test_ARC_5647_featuredNews_detailPage_search(self):

        """
        Checks if Search Button is there or not in Featured News Details Page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 

        search_display_list, search_len_list, search_icon_list = self.featuredNewsPage.search_ele()
        for search_display, search_len, search_icon in zip(search_display_list, search_len_list, search_icon_list):
            assert "icon-search.svg" in search_icon
            assert search_len > 0
            assert search_display == True



     def test_ARC_5647_featuredNews_detailPage_date(self):

         """
         Checks if Date is there or not in Featured News Details Page.
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 

         date_display_list, date_len_list = self.featuredNewsPage.date_ele()
         for date_display, date_len in zip(date_display_list, date_len_list):
            assert date_len > 0
            assert date_display == True

        


     def test_ARC_5647_featuredNews_detailPage_print_block(self):

         """
         Checks if there is no duplicate print button in Featured News Details Page.
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 

         print_list = self.featuredNewsPage.print_block_ele()
         for print in print_list:
            assert print == 1


     def test_ARC_5647_featuredNews_detailPage_save_block(self):

         """
         Checks if there is no duplicate save button in Featured News Details Page.
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 

         save_list  = self.featuredNewsPage.save_block_ele()
         for save in save_list:
            assert save == 1
         

     def test_ARC_5647_featuredNews_detailPage_share_block(self):

         """
         Checks if there is no duplicate share button in Featured News Details Page.
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 

         share_list  = self.featuredNewsPage.share_block_ele()
         for share in share_list:
            assert share == 1


     def test_ARC_5647_featuredNews_detailPage_share_print_misalignment(self):

         """
         Checks if Print, Save and Share buttons are not misaligned.
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath) 

         row_index, share_block, print_save_block = self.featuredNewsPage.print_share_misalignment()
         index = 0
         for row in range(row_index):
                  assert "block-addtoanybuttons" in share_block[index] 
                  assert "block-printablelinksblockcontent" in  print_save_block[index] 
                  index += 1
