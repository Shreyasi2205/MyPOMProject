import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from BaseTest import BaseTest
from Helper import Helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
from selenium.webdriver.support.color import Color
from Utilities.config import Utilities

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.migration
@pytest.mark.usa
@pytest.mark.uk
@pytest.mark.global_site
@pytest.mark.de
@pytest.mark.at
# @pytest.mark.ph
@pytest.mark.malaysia
@pytest.mark.ch
@pytest.mark.ch_fr
# @pytest.mark.fr
@pytest.mark.za
@pytest.mark.es
# @pytest.mark.it
@pytest.mark.fi
@pytest.mark.kr
@pytest.mark.pt
@pytest.mark.br
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ie
@pytest.mark.dk
@pytest.mark.no
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.tr
#@pytest.mark.id
#@pytest.mark.ro
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.bd
@pytest.mark.be
@pytest.mark.pl
class Test_StoriesPageAndDetails(BaseTest):

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_get_storypage(self):

        """
        Launches the story overview page.
        """

        self.driver.get(self.env)
        self.homePage.news_mega_menu(self.homePage.mega_menu_stories_xpath,self.env_name,'stories')

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_novartis_logo(self):

        """
        Checks for novartis logo in story overview page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        assert "logo.svg" in self.basePage.get_elemet_attribute(self.storiesPage.novartis_logo_xpath, "src")

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_search_icon(self):

        """
        Checks for search icon in story overview page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        search_icon = self.storiesPage.search_icon_ele()
        assert "icon-search.svg" in search_icon

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_megamenu_display(self):

        """
        Checks for mega menu in story overview page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        assert len(self.basePage.get_element_text(self.storiesPage.mega_menu_css)) > 0

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_pattern_display(self):

        """
        Checks for pattern in story overview page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        assert "patterns" in self.basePage.get_css_property(self.storiesPage.pattern_css, "background-image")

    @pytest.mark.singapore
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_all_topics(self): 

        """
        Checks if All topics is greyed out by default.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        all_topics_txt, hex_code = self.storiesPage.all_topics_grey_color()
        assert len(all_topics_txt) > 0
        assert "#f1f1f1" in hex_code

    @pytest.mark.singapore
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_menu_names(self):

        """
        Checks for menu names are displayed or not in story overview page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
        # That's why we are pressing on mega menu two times to ignore the issue.
        self.basePage.press_button(self.storiesPage.mega_menu_btn_css)
        self.basePage.press_button(self.storiesPage.mega_menu_btn_css)
        
        menu_items = self.driver.find_elements(self.storiesPage.menus_items_css[0], self.storiesPage.menus_items_css[1])
        index = 0
        for menu_item in menu_items:

            menu_items = self.driver.find_elements(self.storiesPage.menus_items_css[0], self.storiesPage.menus_items_css[1])
            assert len(menu_items[index].find_element(self.storiesPage.anchor_tag_loc[0], self.storiesPage.anchor_tag_loc[1]).text) > 0
            index += 1

    @pytest.mark.singapore
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_default_view(self):

        """
        Checks the following :-
        1. Toggle button is there or not.
        2. By Default content is showing in grid view.
        3. list.svg icon is showing.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        toggle_btn_txt, current_view_txt, view_icon = self.storiesPage.default_view()
        assert len(toggle_btn_txt) > 0
        assert "arctic_grid_view" in current_view_txt
        assert "list.svg" in view_icon

    # @pytest.mark.si
    # @pytest.mark.jp
    # ngap@pytest.mark.lvore
    # def test_ARC_2601_StoryPageAndDetails_all_topics_grey_color(self):

    #     """
        
    #     """

    #     self.driver.get(self.env)
    #     self.storiesPage.launch_story_page(self.env_name)
    #     all_topics_txt, hex_code = self.storiesPage.all_topics_grey_color()
    #     assert len(all_topics_txt) > 0
    #     assert "#f1f1f1" in hex_code

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_pagination_display(self):

        """
        Checks pagination is there only if more than 12 content is there in the story overview page.
        """

    
        # Pagination #
        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        num_content_page = len(self.driver.find_elements(self.storiesPage.content_pages_css[0], self.storiesPage.content_pages_css[1]))
        if num_content_page == 12 and len(self.driver.find_elements(self.storiesPage.pagination_heading_xpath[0], self.storiesPage.pagination_heading_xpath[1])) > 0:

            assert num_content_page == 12
            assert "pagination" in self.basePage.get_elemet_attribute(self.storiesPage.pagination_heading_txt_xpath, "id")

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_pagination_forward_and_backward_button(self):

        """
        Checks forward and backward arrow in pagination are working as expected or not.
        """
    
        # Pagination #
        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        num_content_page = len(self.driver.find_elements(self.storiesPage.content_pages_css[0], self.storiesPage.content_pages_css[1]))
        if num_content_page == 12 and len(self.driver.find_elements(self.storiesPage.pagination_heading_xpath[0], self.storiesPage.pagination_heading_xpath[1])) > 0:
            
            page_one_content_len, page_zero_content_len = self.storiesPage.pagination_front_arrow_back_arrow_validation()
            assert page_one_content_len > 0
            assert page_zero_content_len > 0

    @pytest.mark.singapore
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_toggle_view(self):

        """
        Checks the following :-
        1. Toggle button is there or not.
        2. After clicking on the toggle button, content is displaying in list view,
        3. grid.svg icon is showing.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        toggle_btn_txt, current_view_txt, view_icon = self.storiesPage.toggle_view()
        assert len(toggle_btn_txt) > 0
        assert "arctic_list_view" in current_view_txt
        assert "grid.svg" in view_icon

    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_menu_items_grey_background(self):

        """
        Checks when clicking on menu, it is getting greyed out.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        hex_color_list, page_src_list = self.storiesPage.menu_items()

        hex_color_list_len = len(hex_color_list)
        while hex_color_list_len > 0:

            assert "#f1f1f1" in hex_color_list[hex_color_list_len-1]
            hex_color_list_len = hex_color_list_len - 1

 
    def test_ARC_2601_StoryPageAndDetails_tab_present_in_url(self):
        """
        Checks while changing menu tabs, that tab name should appear in the url.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        tab_name_list, current_url_list = self.storiesPage.menu_items_url()

        for tab_name, current_url in zip(tab_name_list, current_url_list):
            assert tab_name in current_url



    # @pytest.mark.singapore
    # @pytest.mark.ph
    # @pytest.mark.jp
    # @pytest.mark.lv
    # def test_ARC_2601_StoryPageAndDetails_click_random_content(self):

    #     self.driver.get(self.env)
    #     self.storiesPage.launch_story_page(self.env_name)
        
    #     story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
    #     story_contents_len = len(story_contents)
    #     random_content_number = random.randint(0,story_contents_len-1)
        
    #     global content_title

    #     content_title = story_contents[random_content_number].find_element(self.storiesPage.random_content_title_css[0], self.storiesPage.random_content_title_css[1]).text
    #     story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
    #     self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))

    # Already covered in test_breadcrumb
    # @pytest.mark.singapore
    # @pytest.mark.ph
    # @pytest.mark.jp
    # @pytest.mark.lv
    # def test_ARC_2601_StoryPageAndDetails_breadcrumb_random_content(self):

    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.storiesPage.content_breadcrumb_ele()

    #     assert len(breadcrumb_items) == 3
    #     # assert content_title in breadcrumb_items

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_twitter_random_content(self):

        """
        Clicks on a random story and checks the following :-
        1. Twitter icon
        2. Tweet text
        3. Clickable
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        
        global content_title

        content_title = story_contents[random_content_number].find_element(self.storiesPage.random_content_title_css[0], self.storiesPage.random_content_title_css[1]).text
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))


        twitter_icon_element, twitter_txt_element, twitter_clickable = self.storiesPage.twitter_icon()
        assert "twitter.svg" in twitter_icon_element
        assert "Tweet" in twitter_txt_element
        assert twitter_clickable == True

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_facebook_random_content(self):

        """
        Clicks on a random story and checks the following :-
        1. Facebook icon
        2. Share text
        3. Clickable
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        
        global content_title

        content_title = story_contents[random_content_number].find_element(self.storiesPage.random_content_title_css[0], self.storiesPage.random_content_title_css[1]).text
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))


        facebook_icon_element, facebook_txt_element, facebook_clickable = self.storiesPage.facebook_icon()
        assert "facebook.svg" in facebook_icon_element
        assert "Share" in facebook_txt_element
        assert facebook_clickable == True

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_whatsapp_random_content(self):

        """
        Clicks on a random story and checks the following :-
        1. Whatsapp icon
        2. Clickable
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        
        global content_title

        content_title = story_contents[random_content_number].find_element(self.storiesPage.random_content_title_css[0], self.storiesPage.random_content_title_css[1]).text
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))


        whatsapp_icon_element, whatsapp_clickable = self.storiesPage.whatsapp_icon()
        assert "whatsapp.svg" in whatsapp_icon_element
        assert whatsapp_clickable == True

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_linkedin_random_content(self):

        """
        Clicks on a random story and checks the following :-
        1. Linkedin icon
        2. Clickable
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        
        global content_title

        content_title = story_contents[random_content_number].find_element(self.storiesPage.random_content_title_css[0], self.storiesPage.random_content_title_css[1]).text
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))


        linkedin_icon_element, linkedin_clickable = self.storiesPage.linkedin_icon()
        assert "linkedin.svg" in linkedin_icon_element
        assert linkedin_clickable == True

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_email_random_content(self):

        """
        Clicks on a random story and checks the following :-
        1. Email icon
        2. Clickable
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        
        global content_title

        content_title = story_contents[random_content_number].find_element(self.storiesPage.random_content_title_css[0], self.storiesPage.random_content_title_css[1]).text
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))


        email_icon_element, email_clickable = self.storiesPage.email_icon()
        assert "email.svg" in email_icon_element
        assert email_clickable == True

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_print_btn_random_content(self):

        """
        Clicks on a random story and checks the following :-
        1. Print icon
        2. Print Text is displayed or not.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        
        global content_title

        content_title = story_contents[random_content_number].find_element(self.storiesPage.random_content_title_css[0], self.storiesPage.random_content_title_css[1]).text
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))


        print_icon, print_txt = self.storiesPage.print_btn()

        assert "print.svg" in print_icon
        assert len(print_txt) > 0

    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_save_btn_random_content(self):

        """
        Clicks on a random story and checks the following :-
        1. Save icon.
        2. Save text is displayed or not.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        
        global content_title

        content_title = story_contents[random_content_number].find_element(self.storiesPage.random_content_title_css[0], self.storiesPage.random_content_title_css[1]).text
        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))


        pdf_icon, pdf_txt = self.storiesPage.save_btn()

        assert "save.svg" in pdf_icon
        assert len(pdf_txt) > 0

    
    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_duplicate_content(self):

        """
        Checks for duplicate stories.
        """
        
        duplicate_values = []
        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        content_title_list, content_title_set = self.storiesPage.duplicate_contents()
        for i in range(0, len(content_title_list)):    
            for j in range(i+1, len(content_title_list)):    
                if(content_title_list[i] == content_title_list[j]):    
                   duplicate_values.append(content_title_list[j])
        assert len(content_title_list) == len(content_title_set),f"Duplicate titles are {duplicate_values}" 


    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_title(self):

        """
        Checks story title is there in story overview page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        assert self.basePage.is_displayed(self.storiesPage.page_title_css) == True


    @pytest.mark.singapore
    @pytest.mark.ph
    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_stories_url(self):

        """
        Checks while clicking on any random story, that url should contain the default url.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
        # That's why we are pressing on mega menu two times to ignore the issue.
        self.basePage.press_button(self.storiesPage.mega_menu_btn_css)
        self.basePage.press_button(self.storiesPage.mega_menu_btn_css)
        current_storyPage_url = self.driver.current_url
        try:
                assert self.env in current_storyPage_url
        except:
                assert self.env.split("@")[1] in current_storyPage_url

    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_verify_filters(self):

        """
        Checks filters are working or not.
        """
        
        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        menu_tab_list ,card_label_set = self.storiesPage.verify_filters()
        menu_tab_sorted_list = sorted(menu_tab_list)
        card_label_sorted_set = sorted(card_label_set)
        print(card_label_sorted_set)
        print(menu_tab_sorted_list)
        for menu_tab,card_label in zip(menu_tab_sorted_list,card_label_sorted_set):
            assert menu_tab.lower() in card_label.lower()

    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_grey_bg_only_one_tab(self):

        """
        Checks that at a time, only one tab is getting greyed out.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        first_tab_color, second_tab_color = self.storiesPage.menu_tab_one_grey_bg()
        assert "#000000" == first_tab_color
        assert "#f1f1f1" == second_tab_color

    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_ellipses_displayed(self):

        """
        Checks ellipse is getting displayed.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        if self.env_name == "global":
            assert self.basePage.is_displayed(self.storiesPage.ellipse_css) == True

    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_ellipses_validation(self):

        """
        Checks elements inside ellipse.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        if self.env_name == "global":
            self.basePage.press_button(self.storiesPage.ellipse_css)
            elements =  self.driver.find_elements(*self.storiesPage.non_visible_ellipses_xpath)
            assert len(elements) > 0

    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_ellipses_greyed_out(self):

        """
        Checks after clicking on the element in ellipse, that element is getting selected or not and
        It's getting greyed out or not.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        if self.env_name == "global":
            self.basePage.press_button(self.storiesPage.ellipse_css)
            non_visible_element_text = self.basePage.get_element_text(self.storiesPage.non_visible_ellipses_xpath)
            self.basePage.press_button(self.storiesPage.non_visible_ellipses_xpath)
            length = len(self.driver.find_elements(*self.storiesPage.visible_element_xpath))
            element = self.driver.find_element(By.CSS_SELECTOR,f'ul#block-storynavigation>li:nth-child({length}) > a')
            value_of_css = element.value_of_css_property('background-color')
            hex = Color.from_string(value_of_css).hex
            assert '#f1f1f1' == hex
            assert non_visible_element_text == element.text

    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_multiple_tab_greyed_out(self):

        """
        Checks while clicking on pagination and changing menu tabs, that should be greyed out.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        tab_grey_before_pagination_list , tab_grey_after_pagination_list = self.storiesPage.multiple_tab_greyed_out()
        for tab_grey_before_pagination , tab_grey_after_pagination in zip(tab_grey_before_pagination_list , tab_grey_after_pagination_list):
            assert tab_grey_before_pagination in tab_grey_after_pagination

    @pytest.mark.cn
    @pytest.mark.jp
    @pytest.mark.lv
    def test_ARC_2601_StoryPageAndDetails_no_paragraph_tag(self):

        """
        Checks <p> tag should not be there in the content name.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        content_titles_list = self.storiesPage.story_title_no_paragraph_tag()

        for title in content_titles_list:
            assert "<p>" not in title
        
            




