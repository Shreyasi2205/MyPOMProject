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
@pytest.mark.uk
@pytest.mark.eg
@pytest.mark.sandoz
@pytest.mark.de
@pytest.mark.ph
@pytest.mark.ch
@pytest.mark.fr
@pytest.mark.za
@pytest.mark.fi
@pytest.mark.es
# @pytest.mark.jp
@pytest.mark.pt
@pytest.mark.tw
@pytest.mark.kr
@pytest.mark.at
@pytest.mark.it
@pytest.mark.ar
@pytest.mark.br
@pytest.mark.lv
# @pytest.mark.cn
@pytest.mark.scn
@pytest.mark.foundation
@pytest.mark.gr
# @pytest.mark.cz
@pytest.mark.ca
@pytest.mark.tr
@pytest.mark.co
@pytest.mark.ve
@pytest.mark.ru
@pytest.mark.bd
@pytest.mark.be
@pytest.mark.au
@pytest.mark.pl
@pytest.mark.hu
class Test_MediaReleasePage(BaseTest):

   #   def test_ARC_5547_mediaRelease_get_mediaRelease(self):

   #      self.driver.get(self.env)
   #      self.newsPage.launch_newsArchive(self.env_name)
   #      self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)


     def test_ARC_5547_mediaRelease_duplicate_contents(self):

        """
        Checks for duplicate media release content.
        """

        duplicate_values = []
        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
         
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        content_title_list, content_title_set = self.mediaReleasePage.duplicate_contents()
        for i in range(0, len(content_title_list)):    
            for j in range(i+1, len(content_title_list)):    
                if(content_title_list[i] == content_title_list[j]):    
                   duplicate_values.append(content_title_list[j])
        assert len(content_title_list) == len(content_title_set),f"Duplicate titles are {duplicate_values}" 


     def test_ARC_5547_mediaRelease_pattern(self):

         """
         Checks for pattern in media release details page.
         """
         
         self.driver.get(self.env)
         if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
         else:
           self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
         row_index, pattern_stripe_paths = self.mediaReleasePage.pattern_verify()
         index = 0
         for row in range(row_index):
                  assert "patterns" in pattern_stripe_paths[index]
                  index += 1
               

   # Already covered in test_breadcrumb
   #   def  test_ARC_5547_mediaRelease_breadcrumbs(self):

   #       self.driver.get(self.env)
   # #       if self.env_name == "france":
   #         self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
   #         self.basePage.press_button(self.newsRoomPage.link_btn_css)
   #      else:
   #         self.newsPage.launch_newsArchive(self.env_name)
   #       self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
   #       row_index, breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_thirdLevel_color = self.mediaReleasePage.breadcrumb_elements()
   #       index = 0
   #       for row in range(row_index):
               
   #             assert breadcrumb_items[index] == 3
   #             assert "#656565" == breadcrumb_thirdLevel_color[index]

   #             assert ">" in breadcrumb_first_arrow_element[index]
   #             assert ">" in breadcrumb_second_arrow_element[index]

   #             index += 1

   # Already covered in test_breadcrumb            
   #   def test_ARC_5547_mediaRelease_first_second_third_level_breadcrumbs(self):

   #      self.driver.get(self.env)
   # #      if self.env_name == "france":
   #         self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
   #         self.basePage.press_button(self.newsRoomPage.link_btn_css)
   #        else:
   #         self.newsPage.launch_newsArchive(self.env_name)
   #      self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
   #      row_index,home_url, home_current_url, news_url, news_current_url = self.mediaReleasePage.breadcrumbs_firstLevel_secondLevel_thirdLevel()
   #      index = 0
   #      for row in range(row_index):
            
   #          assert home_current_url[index] ==  home_url[index]
   #          assert news_current_url[index] ==  news_url[index]
            
   #          index += 1


     def test_ARC_5547_mediaRelease_title(self):

        """
        Checks for title in media release details page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        row_index , tile_status = self.mediaReleasePage.title_verify()
        index = 0
        for row in range(row_index):
               assert True == tile_status[index]
               index += 1
 
   
     def  test_ARC_5547_mediaRelease_print_button(self):

        """
        Checks the following :-
        1. Print button is displaying.
        2. Clickable or not.
        3. Print text is there.
        4. It's navigating to correct url.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        row_index,print_btn_list, print_btn_clickable_status, print_icon_list,print_url_list,print_page_url_list = self.mediaReleasePage.print_btn_ele()
        index = 0
        for row in range(row_index):

            assert print_btn_list[index] == True
            assert print_btn_clickable_status[index] == True
            assert "print" in print_icon_list[index]
            assert print_url_list[index] == print_page_url_list[index]
            index += 1

     def  test_ARC_5547_mediaRelease_save_button(self):

        """
        Checks the following :-
        1. Save button is displaying.
        2. Clickable or not.
        3. save text is there.
        4. It's navigating to correct url.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        row_index,save_btn_list,save_btn_clickable_status,save_icon_list,save_href_list = self.mediaReleasePage.save_btn_ele()
        index = 0
        for row in range(row_index):

            assert save_btn_list[index] == True
            assert save_btn_clickable_status[index] == True
            assert "save" in save_icon_list[index]
            assert len(save_href_list[index]) > 0

            index += 1

     def  test_ARC_5547_mediaRelease_share_button(self):

        """
        Checks the following :-
        1. Share Button is displaying.
        2. Share button is clickable.
        3. Twitter Button is displaying.
        4. Facebook Button is displaying.
        5. Whatsapp Button is displaying.
        6. Linkedin Button is displaying.
        7. Email Button is displaying.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        row_index , share_btn_icon_list,share_btn_list, twitter_icon_list,facebook_icon_list,whatsapp_icon_list,linkedin_icon_list,email_icon_list = self.mediaReleasePage.share_btn_ele()
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


     def test_ARC_5547_mediaRelease_related_links(self):

        """
        Checks if there is no related links.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)

        related_links_list = self.mediaReleasePage.related_links_ele()
        for related_links in related_links_list:
            assert related_links == 0



     def test_ARC_5547_mediaRelease_menu(self):

        """
        Checks mega menu is displaying in media release details page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)

        menu_display_list, menu_len_list, menu_icon_list = self.mediaReleasePage.menu_ele()
        for menu_display, menu_len, menu_icon in zip(menu_display_list, menu_len_list, menu_icon_list):
            assert "icon-menu.svg" in menu_icon
            assert menu_len > 0
            assert menu_display == True


     def test_ARC_5547_mediaRelease_logo(self):

        """
        Checks logo is displaying in media release details page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)

        menu_display_list = self.mediaReleasePage.logo_ele()
        for menu_display in menu_display_list:
            assert menu_display == True


     def test_ARC_5547_mediaRelease_search(self):

        """
        Checks search icon is displaying in media release details page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        search_display_list, search_len_list, search_icon_list = self.mediaReleasePage.search_ele()
        for search_display, search_len, search_icon in zip(search_display_list, search_len_list, search_icon_list):
            assert "icon-search.svg" in search_icon
            assert search_len > 0
            assert search_display == True



     def test_ARC_5547_mediaRelease_date(self):

         """
         Checks date is displaying in media release details page.
         """
         
         self.driver.get(self.env)
         if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
         else:
           self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)

         row_index , card_date, interior_card_date= self.mediaReleasePage.date_verify()
         index = 0
         for row in range(row_index):
                  assert card_date[index] in interior_card_date[index]
                  index += 1
        


     def test_ARC_5547_mediaRelease_print_block(self):

        """
        Checks print button is displaying in media release details page and there is no duplicate print button.
        """
         
        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        print_list = self.mediaReleasePage.print_block_ele()
        for print in print_list:
            assert print == 1

     def test_ARC_5547_mediaRelease_save_block(self):

        """
        Checks save button is displaying in media release details page and there is no duplicate save button.
        """
         
        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        save_list  = self.mediaReleasePage.save_block_ele()
        for save in save_list:
            assert save == 1

     def test_ARC_5547_mediaRelease_share_block(self):

        """
        Checks share button is displaying in media release details page and there is no duplicate share button.
        """
         
        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        share_list  = self.mediaReleasePage.share_block_ele()
        for share in share_list:
            assert share == 1


     def test_ARC_5547_mediaRelease_share_print_misalignment(self):

         """
         Checks Share and print block are not misaligned.
         """
         
         self.driver.get(self.env)
         if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
         else:
           self.newsPage.launch_newsArchive(self.env_name)
         self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
         row_index, share_block, print_save_block = self.mediaReleasePage.print_share_misalignment()
         index = 0
         for row in range(row_index):
            assert "block-addtoanybuttons" in share_block[index] 
            assert "block-printablelinksblockcontent" in  print_save_block[index] 
            index += 1



     def test_ARC_5547_mediaRelease_print_save_block_alignment(self):

        """
        Checks Print and Save block are not misaligned.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        print_block_list , save_block_list = self.mediaReleasePage.print_save_block_alignment()
        for print_block , save_block in zip(print_block_list , save_block_list):
            assert 'print' in print_block
            assert 'pdf' in save_block


     def test_ARC_5547_mediaRelease_print_save_block_alignment_under_tags_block(self):

        """
        Checks Tags are coming above print and share block.
        """


        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.mediaReleasePage.mediaRelease_tab_xpath)
        if self.env_name == "global":
            tags_block_list, share_block_list , print_save_block_list = self.mediaReleasePage.tags_share_print_save_block_alignment()
            for tags_block, share_block , print_save_block in zip(tags_block_list, share_block_list , print_save_block_list):
               assert "related-tags" in tags_block
               assert "block-addtoanybuttons" in share_block
               assert "print" in print_save_block

 
        
        
