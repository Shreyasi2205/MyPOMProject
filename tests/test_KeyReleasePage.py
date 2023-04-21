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
class Test_KeyReleasePage(BaseTest):

     def test_ARC_5547_KeyRelease_get_keyRelease(self):

        """
        Launch keyrelease page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)


     def test_ARC_5547_KeyRelease_duplicate_contents(self):

        """
        Checks for duplicate content in keyrelease page.
        """

        duplicate_values = []
        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
        content_title_list, content_title_set = self.keyReleasePage.duplicate_contents()
        for i in range(0, len(content_title_list)):    
            for j in range(i+1, len(content_title_list)):    
                if(content_title_list[i] == content_title_list[j]):    
                   duplicate_values.append(content_title_list[j])
        assert len(content_title_list) == len(content_title_set),f"Duplicate titles are {duplicate_values}" 


     def test_ARC_5547_KeyRelease_pattern(self):

         """
         Checks for pattern in keyrelease details page.
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
         row_index, pattern_stripe_paths = self.keyReleasePage.pattern_verify()
         index = 0
         for row in range(row_index):
                  assert "patterns" in pattern_stripe_paths[index]
                  index += 1
               

     def  test_ARC_5547_KeyRelease_breadcrumbs(self):

        """
        Function -- Breadcrumb is available or not.
        """


        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
        row_index, breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_thirdLevel_color = self.keyReleasePage.breadcrumb_elements()
        index = 0
        for row in range(row_index):
            
            assert breadcrumb_items[index] == 3
            assert "#656565" == breadcrumb_thirdLevel_color[index]

            assert ">" in breadcrumb_first_arrow_element[index]
            assert ">" in breadcrumb_second_arrow_element[index]

            index += 1

            
     def test_ARC_5547_KeyRelease_first_second_third_level_breadcrumbs(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
        row_index,home_url, home_current_url, news_url, news_current_url = self.keyReleasePage.breadcrumbs_firstLevel_secondLevel_thirdLevel()
        index = 0
        for row in range(row_index):
            
            assert home_current_url[index] ==  home_url[index]
            assert news_current_url[index] ==  news_url[index]
            
            index += 1


     def test_ARC_5547_KeyRelease_title(self):

        """
        Checks for title in keyrelease details page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
        row_index , tile_status = self.keyReleasePage.title_verify()
        index = 0
        for row in range(row_index):
               assert True == tile_status[index]
               index += 1
 
   
     def  test_ARC_5547_KeyRelease_print_button(self):

        """
        checks the following for print button -
        1. button is available
        2. clickable
        3. print icon
        4. navigating to correct page
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
        row_index,print_btn_list, print_btn_clickable_status, print_icon_list,print_url_list,print_page_url_list = self.keyReleasePage.print_btn_ele()
        index = 0
        for row in range(row_index):

            assert print_btn_list[index] == True
            assert print_btn_clickable_status[index] == True
            assert "print" in print_icon_list[index]
            assert print_url_list[index] == print_page_url_list[index]
            index += 1

     def  test_ARC_5547_KeyRelease_save_button(self):

        """
        checks the following for save button -
        1. button is available
        2. clickable
        3. save icon
        4. href is there in <a> tag
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
        row_index,save_btn_list,save_btn_clickable_status,save_icon_list,save_href_list = self.keyReleasePage.save_btn_ele()
        index = 0
        for row in range(row_index):

            assert save_btn_list[index] == True
            assert save_btn_clickable_status[index] == True
            assert "save" in save_icon_list[index]
            assert len(save_href_list[index]) > 0

            index += 1

     def  test_ARC_5547_KeyRelease_share_button(self):

        """
        checks the following for share button -
        1. button is available
        2. clickable
        3. share icon
        4. twitter, whatsapp, facebook, linkedin, email icons
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
        row_index , share_btn_icon_list,share_btn_list, twitter_icon_list,facebook_icon_list,whatsapp_icon_list,linkedin_icon_list,email_icon_list = self.keyReleasePage.share_btn_ele()
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


     def test_ARC_5547_KeyRelease_related_links(self):

        """
        Checks if there is no related links available.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)

        related_links_list = self.keyReleasePage.related_links_ele()
        for related_links in related_links_list:
            assert related_links == 0



     def test_ARC_5547_KeyRelease_menu(self):

        """
        Checks for mega menu in key release details page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)

        menu_display_list, menu_len_list, menu_icon_list = self.keyReleasePage.menu_ele()
        for menu_display, menu_len, menu_icon in zip(menu_display_list, menu_len_list, menu_icon_list):
            assert "icon-menu.svg" in menu_icon
            assert menu_len > 0
            assert menu_display == True


     def test_ARC_5547_KeyRelease_logo(self):

        """
        Checks for logo in key release details page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)

        menu_display_list = self.keyReleasePage.logo_ele()
        for menu_display in menu_display_list:
            assert menu_display == True


     def test_ARC_5547_KeyRelease_search(self):

        """
        Checks for search icon in key release details page.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)

        search_display_list, search_len_list, search_icon_list = self.keyReleasePage.search_ele()
        for search_display, search_len, search_icon in zip(search_display_list, search_len_list, search_icon_list):
            assert "icon-search.svg" in search_icon
            assert search_len > 0
            assert search_display == True



     def test_ARC_5547_KeyRelease_date(self):

        """
        Checks for date in key release details page.
        """
        
        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)

        row_index , card_date, interior_card_date= self.keyReleasePage.date_verify()
        index = 0
        for row in range(row_index):
                assert card_date[index] in interior_card_date[index]
                index += 1
        


     def test_ARC_5547_KeyRelease_print_block(self):

         """
         Checks for duplicate print button. 
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
         row_index,print_list = self.keyReleasePage.print_block_ele()
         assert row_index == len(print_list)

     def test_ARC_5547_KeyRelease_save_block(self):

         """
         Checks for duplicate save button. 
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
         row_index, save_list  = self.keyReleasePage.save_block_ele()
         assert row_index == len(save_list)

     def test_ARC_5547_KeyRelease_share_block(self):

         """
         Checks for duplicate share button. 
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
         row_index, share_list  = self.keyReleasePage.share_block_ele()
         assert row_index == len(share_list)


     def test_ARC_5547_KeyRelease_share_print_misalignment(self):

         """
         Checks for share & print button misalignment.
         """
         
         self.driver.get(self.env)
         self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
         row_index, share_block, print_save_block = self.keyReleasePage.print_share_misalignment()
         index = 0
         for row in range(row_index):
                  assert "block-addtoanybuttons" in share_block[index] 
                  assert "block-printablelinksblockcontent" in  print_save_block[index] 
                  index += 1


        
     def test_ARC_5547_KeyRelease_print_save_block_alignment(self):

        """
         Checks for print & save button misalignment.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.keyReleasePage.keyRelease_tab_xpath)
        print_block_list , save_block_list = self.keyReleasePage.print_save_block_alignment()
        for print_block , save_block in zip(print_block_list , save_block_list):
            assert 'print' in print_block
            assert 'pdf' in save_block
