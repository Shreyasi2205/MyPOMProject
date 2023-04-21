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

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.global_site
class Test_MediaLibrary(BaseTest):

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_get_mediaLibrary(self):

        """
        Launches the medialibrary page
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
    
    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_title(self):

        """
        Checks the media library title is there or not.
        """
        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        assert len(self.driver.title) > 0

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_pattern(self):

        """
        Checks Pattern is available or not.
        """
        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        assert "patterns" in self.basePage.get_css_property(self.mediaLibraryPage.pattern_css, "background-image")

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_breadcrumbs(self):

        """
        Function -- Breadcrumb is available or not.
        """
        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element = self.mediaLibraryPage.breadcrumb_ele()
        assert len(breadcrumb_items) == 3

        assert ">" in breadcrumb_first_arrow_element
        assert ">" in breadcrumb_second_arrow_element
        assert "#656565" == self.basePage.get_css_color(self.mediaLibraryPage.media_library_breadcrumb_color_css, "color")


    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_view(self):

         """
         Checks default view is grid view or not.
         """
         self.driver.get(self.env)
         self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
         assert "arctic_grid_view" in self.basePage.get_elemet_attribute(self.mediaLibraryPage.arctic_list_grid_view_css, "class")

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_greyedMenu(self):

        """
        Checks All menu tab is greyed out or not.
        """
        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        assert "#f1f1f1" == self.basePage.get_css_color(self.mediaLibraryPage.all_menu_xpath, "background-color")

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_first_second_level_breadcrumbs(self):

        """
        Checks breadcrumb is navigating to the correct page or not.
        """
        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.mediaLibraryPage.breadcrumbs_firstLevel_secondLevel()

        for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
            assert breadcumb_anchor_url in breadcumb_anchor_current_url

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_pagination(self): 

        """
        Checks pagination
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        num_content_page,pagination_heading, page_content_list = self.mediaLibraryPage.pagination_validation()
        if num_content_page == 12 and pagination_heading > 0 :
            page_count_len = len(page_content_list)
            while page_count_len > 0:
                assert len(page_content_list) > 0
                page_count_len = page_count_len - 1

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_listView(self):

        """
        Checks for list view
        """
        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        list_icon,list_view_btn,grid_view  = self.mediaLibraryPage.list_view()
        
        assert "list.svg" in list_icon
        assert "List View" in list_view_btn
        assert "arctic_grid_view" in grid_view

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_gridView(self):

        """
        Checks for grid view
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        grid_icon,grid_view_btn,list_view  = self.mediaLibraryPage.grid_view()

        assert "grid.svg" in grid_icon
        assert "Grid View" in grid_view_btn 
        assert "arctic_list_view" in list_view

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_menuTabs(self): 

        """
        Checks while changing tabs, menus are getting greyed out or not.
        """
        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        hex_color_list = self.mediaLibraryPage.grey_menu_verify()
        for hex_color in hex_color_list:
            assert "#f1f1f1" in hex_color

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_pagination_front_arrow_back_arrow(self):

        """
        Checks forward and backward arrow is working or not.
        """
       
        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        num_content_page,pagination_heading,page_one_contents, page_zero_contents = self.mediaLibraryPage.pagination_front_arrow_back_arrow_validation()
        if num_content_page == 12 and pagination_heading > 0 :
            assert len(page_one_contents) > 0
            assert len(page_zero_contents) > 0


    def test_ARC_2647_MediaLibrary_lockIcon(self): 

        """
        Checks lock icon for protected content.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        hex_color_list,document_type_locked,document_type_locked_1  = self.mediaLibraryPage.lock_icon_verify()
        for hex_color in hex_color_list:
            assert "#e4e4e4" in hex_color

        for lock in document_type_locked:
            assert "document-type-locked" in lock

        for lock in document_type_locked_1:
            assert "document-type-locked" in lock
         
    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_search_bar(self): 

        """
        Checks search bar field.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        assert True == self.basePage.is_displayed(self.mediaLibraryPage.search_bar)

    @pytest.mark.foundation
    def test_ARC_2647_MediaLibrary_search_button(self): 

        """
        Checks search button is displayed or not.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        assert True == self.basePage.is_displayed(self.mediaLibraryPage.search_button)


    def test_ARC_2647_MediaLibrary_reset_button(self): 

        """
        Checks that reset button should not come after clicking on pagination button
        """

        # RESET BUTTON SHOULD NOT BE THERE

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)  

        self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)
        reset_button = self.basePage.get_css_property_without_ec(self.mediaLibraryPage.reset_button, "display")

        assert reset_button == "none"

    def test_ARC_2647_MediaLibrary_no_paragraph_tag(self):

        """
        Checks <p> tag should not be there in the content name.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)

        content_titles_list = self.mediaLibraryPage.media_title_no_paragraph_tag()

        for title in content_titles_list:
            assert "<p>" not in title



