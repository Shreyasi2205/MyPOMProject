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
from selenium.webdriver.support.color import Color
import time

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.migration
@pytest.mark.singapore
@pytest.mark.uk
@pytest.mark.usa
@pytest.mark.sandoz
@pytest.mark.eg
@pytest.mark.global_site
@pytest.mark.de
@pytest.mark.at
@pytest.mark.ph
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.fr
@pytest.mark.za
@pytest.mark.malaysia
@pytest.mark.es
@pytest.mark.pt
@pytest.mark.tw
@pytest.mark.jp
@pytest.mark.lv
@pytest.mark.it
@pytest.mark.ar
@pytest.mark.fi
@pytest.mark.kr
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ie
@pytest.mark.gr
@pytest.mark.dk
# @pytest.mark.no
@pytest.mark.ca
# @pytest.mark.se
@pytest.mark.tr
# @pytest.mark.cz
@pytest.mark.ru
# @pytest.mark.rs
@pytest.mark.ro
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.ve
#@pytest.mark.id
@pytest.mark.bd
@pytest.mark.be
@pytest.mark.au
@pytest.mark.pl
class Test_NewsArchive(BaseTest):

    # @pytest.mark.malaysia
    # def test_ARC_2586_NewsArchive_get_newsArchive(self):

    #     self.driver.get(self.env)
    #     self.newsPage.launch_newsArchive(self.env_name)
    
    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_bannerImage(self):

        """
        Checks banner image in news archive page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        if len(self.driver.find_elements(*self.newsPage.banner_img_css)) > 0:
            assert len(self.basePage.get_elemet_attribute(self.newsPage.banner_img_css, "src")) > 0

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_pattern(self):

        """
        Checks pattern in news archive page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        assert "patterns" in self.basePage.get_css_property(self.newsPage.pattern_css, "background-image")

    # Already covered in test_breadcrumb
    # def test_ARC_2586_NewsArchive_breadcrumbs(self):

    #     self.driver.get(self.env)
    #     if self.env_name == "france":
        #    self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        #    self.basePage.press_button(self.newsRoomPage.link_btn_css)
        # else:
        #    self.newsPage.launch_newsArchive(self.env_name)
    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.newsPage.breadcrumb_ele()

    #     assert len(breadcrumb_items) == 3
    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    #     assert "#656565" == self.basePage.get_css_color(self.newsPage.news_archive_last_child_breadcrumb_color_css, "color")

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_search_bar_button(self):

        """
        Checks search bar and button in news archive page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        search_bar, search_btn = self.newsPage.search_bar_and_btn()
        assert search_bar == True
        assert search_btn == True

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_default_view(self):

        """
        Checks default view - grid view and list.svg icon in news archive page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        assert "arctic_grid_view" in self.basePage.get_elemet_attribute(self.newsPage.news_page_view_css, "class")
        assert "list.svg" in self.basePage.get_css_property(self.newsPage.view_toggle_icon, "background")
    
    # This is disabled in all sites now
    # def test_ARC_2586_NewsArchive_calendar_from_to(self):

    #     if self.env_name == "france":
    #        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
    #        self.basePage.press_button(self.newsRoomPage.link_btn_css)
    #     else:
    #        self.newsPage.launch_newsArchive(self.env_name)
    # #     assert len(self.basePage.get_element_text(self.newsPage.from_date_xpath)) > 0
    #     assert len(self.basePage.get_element_text(self.newsPage.to_date_xpath)) > 0

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_all_topics_grey_color(self):

        """
        Checks All topics is greyed out by default in news archive page.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        all_topics_text_status, hex_code= self.newsPage.all_topics_grey_color()
        assert all_topics_text_status == True
        assert "#f1f1f1" in hex_code

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_pagination_num(self):

        """
        Checks pagination numbers are correctly displayed.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        current_page_num , page_num = self.newsPage.pagination_number()
        assert current_page_num == page_num

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_right_hand_rail(self):

        """
        Checks if there is no right hand rail.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        assert len(self.driver.find_elements(*self.newsPage.right_hand_rail_xpath)) == 0

    # Already covered in test_breadcrumb
    # def test_ARC_2586_NewsArchive_first_second_level_breadcrumbs(self):

    #     self.driver.get(self.env)
    #     if self.env_name == "france":
        #    self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        #    self.basePage.press_button(self.newsRoomPage.link_btn_css)
        # else:
        #    self.newsPage.launch_newsArchive(self.env_name)
    #     breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.newsPage.check_all_breadcrumb_url()
    #     for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
    #         assert breadcumb_anchor_url in breadcumb_anchor_current_url

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_pagination(self):

        """
        Checks pagination is working as expected or not.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)   
        if len(self.driver.find_elements(self.newsPage.pagination_heading_xpath[0], self.newsPage.pagination_heading_xpath[1])) > 0:     
            num_content_page,pagination_heading, page_content_list = self.newsPage.pagination_validation()
            if num_content_page == 12 and pagination_heading > 0 :
                page_count_len = len(page_content_list)
                while page_count_len > 0:
                    assert len(page_content_list) > 0
                    page_count_len = page_count_len - 1

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_menuTabs_viewEmpty(self):

        """
        Checks menu tabs are getting greyed out or not and if under any menu tab, no content is there,
        It should display No Result Found.
        """

        empty_list = []
        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        hex_color_list, empty_list = self.newsPage.grey_menu_verify()
        
        hex_color_list_len = len(hex_color_list)

        while hex_color_list_len > 0:
            
            assert "#f1f1f1" in hex_color_list[hex_color_list_len-1]
            hex_color_list_len = hex_color_list_len - 1
            

    # def test_ARC_2586_NewsArchive_viewEmpty(self):

    #     self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name) 
        empty_list_len = len(empty_list)
        if empty_list_len > 0:
            if "view-empty" in empty_list[empty_list_len-1]:
                assert "view-empty" in empty_list[empty_list_len-1]
                empty_list_len = empty_list_len - 1

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_listview(self):

        """
        Checks the following :-
        1. list.svg icon.
        2. list view button.
        3. Default view.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)     
        list_icon,list_view_btn,grid_view  = self.newsPage.list_view()
        
        assert "list.svg" in list_icon
        assert list_view_btn == True
        assert "arctic_grid_view" in grid_view

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_gridView(self):

        """
        Checks the following :-
        1. grid.svg icon.
        2. grid view button.
        3. view is in list view.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)     
        grid_icon,grid_view_btn,list_view  = self.newsPage.grid_view()

        assert "grid.svg" in grid_icon
        assert grid_view_btn == True
        assert "arctic_list_view" in list_view

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_randomText_search_url(self):

         """
         Checks the searched text is coming in the url.
         """

         self.driver.get(self.env)
         if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
         else:
           self.newsPage.launch_newsArchive(self.env_name)
         searched_keyword = self.newsPage.verify_search_result()
         current_url = self.driver.current_url
         assert searched_keyword in current_url


    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_randomText_search_keyword(self):

        """
        Checks searched keyword is coming in the text box while changing the tabs.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        searched_keyword_list = self.newsPage.verify_searchText_with_Tabs()
        for search_keyword in searched_keyword_list:
            assert search_keyword == self.newsPage.test_data


    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_randomText_greyMenu_verify(self):

        """
        After searching some keyword, It checks tabs are getting greyed out or not.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        hex_color_list = self.newsPage.grey_menu_verify_with_Tabs()
        for hex_color in hex_color_list:
            assert "#f1f1f1" == hex_color

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_randomText_menuTab_url(self):

         """
         Checks menu tab name is coming in the url.
         """

         self.driver.get(self.env)
         if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
         else:
           self.newsPage.launch_newsArchive(self.env_name)
         tab_href_list, selected_tab_url_list = self.newsPage.verify_menuTab_url()
         for tab_href, selected_tab_url in zip(tab_href_list, selected_tab_url_list):
            assert tab_href in selected_tab_url


    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_randomText_searchKeyword_url(self):

        """
        Checks searched keyword is coming in the url while changing tabs.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        searched_keyword,selected_tab_url_list = self.newsPage.verify_searchText_with_url()
        for url in selected_tab_url_list:
            assert searched_keyword in url

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_pagination_front_arrow_back_arrow(self):

        """
        Checks front and back pagination arrow is working.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        if len(self.driver.find_elements(self.newsPage.pagination_heading_xpath[0], self.newsPage.pagination_heading_xpath[1])) > 0:  
            num_content_page,pagination_heading,page_one_contents, page_zero_contents = self.newsPage.pagination_front_arrow_back_arrow_validation()
            if num_content_page == 12 and pagination_heading > 0 :
                assert len(page_one_contents) > 0
                assert len(page_zero_contents) > 0

   #  @pytest.mark.malaysia
   #  def test_ARC_2586_NewsArchive_key_release_language_tab(self):

   #      """
   #      Checks language dropdown is coming under key release dropdown.
   #      """

   #      self.driver.get(self.env)
   #      if self.env_name == "france":
   #         self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
   #         self.basePage.press_button(self.newsRoomPage.link_btn_css)
   #      else:
   #         self.newsPage.launch_newsArchive(self.env_name)
   #      if self.env_name == "global":
   #          language_tab_txt = self.newsPage.key_releases(self.env_name)
   #          assert "Language" in language_tab_txt

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_media_release_language_tab(self):

        """
        Checks language dropdown is coming under media release dropdown and dates are coming in descending order.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        desc_sort = self.newsPage.media_release(self.env_name)
        assert desc_sort == True
      #   if self.env_name == "global":
      #       assert "Language" in language_tab_txt

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_randomText_verification(self):

        """
        Checks after searching a keyword, the keyword is coming in the search box or not and all topics is getting greyed out or not.
        """
        
        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        searched_keyword = self.newsPage.verify_search_result() 
        assert searched_keyword == self.newsPage.test_data
        all_topics_text_status, hex_code = self.newsPage.all_topics_grey_color()
        assert all_topics_text_status == True
        assert "#f1f1f1" in hex_code

        
    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_content_validation(self):

        """
        Checks if content is there in newsw archive page.
        """
        
        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        contents = self.basePage.get_elements(self.newsPage.content_pages_css)
        assert len(contents) > 0

    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_search_results(self):

        """
        Checks searched input is coming in the searched result or not.
        """
        
        self.driver.get(self.env) 
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        content_title = self.newsPage.search_results()
        for title in content_title:
            if self.newsPage.test_data_novartis in title: 
                assert self.newsPage.test_data_novartis in title
                break
        
    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_verify_filters(self):

        """
        Checks Filters are working or not.
        """

        media_release_list = ['key release', 'media release']
        featured_news_list = ['pulse update', 'statement','featured news']
        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        menu_tab_list , tab_label_list = self.newsPage.verify_filters()  
       
        for filter_name,tab_label in zip(menu_tab_list , tab_label_list):
            if filter_name == "media releases" and self.env_name == 'global':
                for tab in tab_label:
                    assert tab in media_release_list  
            elif filter_name == "key releases" and self.env_name == 'global':
                for tab in tab_label:
                    assert tab in media_release_list  
            elif filter_name == "featured news" and self.env_name == 'global':
                for tab in tab_label:
                    assert tab  in featured_news_list
            elif filter_name == "statements" and self.env_name == 'global':
                for tab in tab_label:
                    assert tab  in featured_news_list
            elif filter_name == "pulse updates" and self.env_name == 'global':
                for tab in tab_label:
                    assert tab  in featured_news_list
            elif filter_name == "statement" and self.env_name == 'biome':
                for tab in tab_label:
                    assert tab  in featured_news_list  
            elif filter_name == "statements" and self.env_name == 'usa':
                for tab in tab_label:
                    assert tab  in featured_news_list
            elif filter_name == "statement" and self.env_name == 'foundation':
                for tab in tab_label:
                    assert tab  in featured_news_list  
            else :
                for label in tab_label :
                    assert label in filter_name


    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_banner_title(self):

        """
        Checks if banner title is displaying.
        """
        
        self.driver.get(self.env) 
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        if self.env_name == "global":
            assert self.basePage.is_displayed(self.newsPage.banner_text_css) == True


    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_key_release_text(self):

        """
        Checks key release text is there above search bar.
        """

        self.driver.get(self.env) 
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        if self.env_name == "global":
            assert self.basePage.is_displayed(self.newsPage.key_releases_text_xpath) == True
            assert "Key Releases" in self.basePage.get_element_text(self.newsPage.key_releases_text_xpath)


    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_menu_ellipse(self):

        """
        Checks ellipse is displayed.
        """

        self.driver.get(self.env) 
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        if self.env_name == "global":
            visible_element = self.driver.find_elements(*self.newsPage.visible_element_xpath)
            if len(visible_element) == 7 :
                assert self.basePage.is_displayed(self.newsPage.ellipses_xpath) == True



    @pytest.mark.malaysia
    def test_ARC_2586_NewsArchive_ellipses_validation(self):

        """
        Checks any element is there inside ellipse.
        """
        
        self.driver.get(self.env) 
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        if self.env_name == "global":
            if self.basePage.is_displayed(self.newsPage.ellipses_xpath):
                self.basePage.press_button(self.newsPage.ellipses_xpath)
                elements =  self.driver.find_elements(*self.newsPage.non_visible_ellipses_xpath)
                assert len(elements) > 0



    @pytest.mark.malaysia
    def  test_ARC_2586_NewsArchive_ellipses_element_greyed_out(self):

        """
        Checks while clicking any element in ellipse, that element should greyed out.
        """

        self.driver.get(self.env) 
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        if self.env_name == "global":
             if self.basePage.is_displayed(self.newsPage.ellipses_xpath):
                self.basePage.press_button(self.newsPage.ellipses_xpath)
                non_visible_element_text = self.basePage.get_element_text(self.newsPage.non_visible_ellipses_xpath)
                self.basePage.press_button(self.newsPage.non_visible_ellipses_xpath)
                length = len(self.driver.find_elements(*self.newsPage.visible_element_xpath))
                element = self.driver.find_element(By.CSS_SELECTOR,f'ul#block-newsarchivenavigation>li:nth-child({length}) > a')
                value_of_css = element.value_of_css_property('background-color')
                hex = Color.from_string(value_of_css).hex
                assert '#f1f1f1' == hex
                assert non_visible_element_text == element.text


    def test_ARC_2586_NewsArchive_grey_bg_only_one_tab(self):

        """
        Checks only tab is getting greyed out at a time.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)

        first_tab_color, second_tab_color = self.newsPage.menu_tab_one_grey_bg()
        assert "#000000" == first_tab_color
        assert "#f1f1f1" == second_tab_color
        


