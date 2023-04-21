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
class Test_MediaLibraryDetails(BaseTest):

    # def test_ARC_2658_MediaLibraryDetails_get_mediaLibrary(self):

    #    self.driver.get(self.env)
    #    self.mediaLibraryPage.launch_mediaLibrary(self.env_name)

    def test_ARC_2658_MediaLibraryDetails_protected_image_content(self):

        """
        Opens image tab in the media library page and does the following :-
        1. Opens protected image if there is any 
        2. Checks lock icon is displaying in the image or not.
        3. checks download button is clickable or not.
        4. After clicking on protected image or download button, It should open a popup window.
        5. Popup window should work as expected.
        6. Checks Image Label & Desc is there or not.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)

        pages = 3
        self.basePage.press_button(self.mediaLibraryPage.image_tab_xpath)


        for page in range(pages):

            protected_img_index, protected_img_src_list, protected_img_btn_clickable_list, protected_img_page_label_list, protected_img_desc_page_label_list, protected_img_pop_up_window_list, protected_img_yes_btn_clickable_list, protected_img_current_page_url_list, protected_img_current_page_url_one_list, protected_img_page_url_list, protected_img_nav_current_page_url_list = self.mediaLibraryPage.protected_img()

            for img_src, btn_clickable, pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one, protected_img_page_url, protected_img_nav_current_page_url in zip(protected_img_src_list, protected_img_btn_clickable_list, protected_img_pop_up_window_list, protected_img_yes_btn_clickable_list, protected_img_current_page_url_list, protected_img_current_page_url_one_list, protected_img_page_url_list, protected_img_nav_current_page_url_list):
                assert "lock" in img_src
                assert btn_clickable == True
                assert yes_btn_clickable == True
                assert "dialog" in pop_up_window
                assert current_page_url == current_page_url_one
                assert protected_img_page_url in protected_img_nav_current_page_url

            for protected_img_page_label, protected_img_desc_page_label in zip(protected_img_page_label_list, protected_img_desc_page_label_list):

                if len(protected_img_page_label) > 0:
                    assert len(protected_img_page_label) > 0
                    assert len(protected_img_desc_page_label) > 0

            if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and protected_img_index <=3:
                self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)

    @pytest.mark.foundation
    def test_ARC_2658_MediaLibraryDetails_unprotected_image_content(self):

        """
        Opens image tab in the media library page and does the following :-
        1. Opens uprotected image if there is any.
        2. Checks image is displaying or not.
        3. Checks download button is clickable or not.
        4. Checks correct page has opened or not after clicking on the unprotected image.
        5. Checks Image Label & Desc is there or not.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)

        pages = 2
        if self.env_name == "global":
            self.basePage.press_button(self.mediaLibraryPage.image_tab_xpath)
            
        for page in range(pages):

            unprotected_img_index, unprotected_img_src_list, unprotected_img_btn_clickable_list, unprotected_img_page_label_list, unprotected_img_desc_page_label_list, unprotected_img_page_url_list, unprotected_img_current_page_url_list = self.mediaLibraryPage.unprotected_img()

            for img_src, btn_clickable, unprotected_img_page_url, unprotected_img_current_page_url in zip(unprotected_img_src_list, unprotected_img_btn_clickable_list, unprotected_img_page_url_list, unprotected_img_current_page_url_list):

                assert len(img_src) > 0
                assert btn_clickable == True
                assert unprotected_img_page_url in unprotected_img_current_page_url


            for unprotected_doc_page_label, unprotected_doc_desc_page_label in zip(unprotected_img_page_label_list, unprotected_img_desc_page_label_list):

                if len(unprotected_doc_page_label) > 0:
                    assert len(unprotected_doc_page_label) > 0
                    assert len(unprotected_doc_desc_page_label) > 0

            if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and unprotected_img_index <=3:
                self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)


    def test_ARC_2658_MediaLibraryDetails_protected_document_content(self):

        """
        Opens document tab in the media library page and does the following :-
        1. Opens protected document if there is any 
        2. Checks lock icon is displaying in the document or not.
        3. checks download button is clickable or not.
        4. After clicking on protected document or download button, It should open a popup window.
        5. Popup window should work as expected.
        6. Checks Image Label & Desc is there or not.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)


        pages = 2
        self.basePage.press_button(self.mediaLibraryPage.doc_tab_xpath)
        
        for page in range(pages):

            protected_doc_index, protected_doc_img_src_list, protected_doc_btn_clickable_list, protected_doc_page_label_list, protected_doc_desc_page_label_list, protected_doc_pop_up_window_list, protected_doc_yes_btn_clickable_list, protected_doc_current_page_url_list, protected_doc_current_page_url_one_list, protected_doc_page_url_list, protected_doc_navigate_current_page_url_list = self.mediaLibraryPage.protected_doc()

            for img_src, btn_clickable, pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one, protected_doc_page_url, protected_doc_navigate_current_page_url in zip(protected_doc_img_src_list, protected_doc_btn_clickable_list, protected_doc_pop_up_window_list, protected_doc_yes_btn_clickable_list, protected_doc_current_page_url_list, protected_doc_current_page_url_one_list, protected_doc_page_url_list, protected_doc_navigate_current_page_url_list):
                assert "lock" in img_src
                assert btn_clickable == True
                assert yes_btn_clickable == True
                assert "dialog" in pop_up_window
                assert current_page_url == current_page_url_one
                assert protected_doc_page_url in protected_doc_navigate_current_page_url

            for protected_img_page_label, protected_img_desc_page_label in zip(protected_doc_page_label_list, protected_doc_desc_page_label_list):

                if len(protected_img_page_label) > 0:
                    assert len(protected_img_page_label) > 0
                    assert len(protected_img_desc_page_label) > 0

            if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and protected_doc_index <=3:
                self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)


    def test_ARC_2658_MediaLibraryDetails_unprotected_document_content(self):

        """
        Opens document tab in the media library page and does the following :-
        1. Opens uprotected document if there is any.
        2. Checks document is displaying or not.
        3. Checks download button is clickable or not.
        4. Checks correct page has opened or not after clicking on the unprotected document.
        5. Checks Image Label & Desc is there or not.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)

        pages = 2
        self.basePage.press_button(self.mediaLibraryPage.doc_tab_xpath)
        
        for page in range(pages):

            unprotected_doc_index, unprotected_doc_btn_clickable_list, unprotected_doc_page_label_list, unprotected_doc_desc_page_label_list,unprotected_doc_page_url_list, unprotected_doc_current_page_url_list = self.mediaLibraryPage.unprotected_doc()

            for btn_clickable, unprotected_doc_page_url, unprotected_doc_current_page_url in zip(unprotected_doc_btn_clickable_list, unprotected_doc_page_url_list, unprotected_doc_current_page_url_list):

                assert btn_clickable == True
                assert unprotected_doc_page_url in unprotected_doc_current_page_url

            for unprotected_doc_page_label, unprotected_doc_desc_page_label in zip(unprotected_doc_page_label_list, unprotected_doc_desc_page_label_list):

                if len(unprotected_doc_page_label) > 0:
                    assert len(unprotected_doc_page_label) > 0
                    assert len(unprotected_doc_desc_page_label) > 0

            if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and unprotected_doc_index <=3:
                self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)


    def test_ARC_2658_MediaLibraryDetails_video_tab_content(self):

        """
        Opens video tab in the media library page and does the following :-
        1. Opens a video if there is any.
        2. Checks video is displaying or not.
        3. Checks correct page has opened or not after clicking on the unprotected video.
        4. Checks Image Label & Desc is there or not.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)

        pages = 2

        self.basePage.press_button(self.mediaLibraryPage.video_tab_xpath)
        
        for page in range(pages):

            video_index, video_page_label_list, video_desc_page_label_list, video_frame_len_list, flag_list, video_page_url_list, video_current_page_url_list = self.mediaLibraryPage.video()

            for video_frame_len, flag, video_page_url, current_page_url in zip(video_frame_len_list, flag_list, video_page_url_list, video_current_page_url_list):

                assert video_frame_len > 0
                assert flag == 1
                assert video_page_url in current_page_url

            for video_page_label, video_desc_page_label in zip(video_page_label_list, video_desc_page_label_list):

                if len(video_page_label) > 0:
                    assert len(video_page_label) > 0
                    assert len(video_desc_page_label) > 0

            if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and video_index <=3:
                self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)


    def test_ARC_2658_MediaLibraryDetails_related_items(self):

        """
        Checks the following :-
        For global site, 
        1. Related items title is displaying or not.
        2.  Min - 1, Max - 4 Related Items are displaying.
        3. Related Items are navigating to correct url.
        For foundation site,
        1. Related items title is displaying or not.
        2. Related Items are navigating to correct url.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)

        index, related_items_len, related_items_href_list ,current_page_url_list,related_items_title_len = self.mediaLibraryPage.related_items()
            
        count = 0
        if self.env_name == "global":
            for i in range(index):
                    assert related_items_title_len[count] > 0
                    assert related_items_len[count] >= 1
                    assert related_items_len[count] <= 4
                    assert current_page_url_list[count] in related_items_href_list[count]
                    count +=1

        else:
                
                if related_items_len[count] > 0:
                    assert related_items_title_len[count] > 0
                    assert current_page_url_list[count] in related_items_href_list[count]
                    count +=1



    def test_ARC_2658_MediaLibraryDetails_protected_image_fact_sheet(self):

        """
        Opens fact sheet tab in the media library page and does the following :-
        1. Opens protected fact sheet if there is any 
        2. Checks lock icon is displaying in the fact sheet or not.
        3. checks download button is clickable or not.
        4. After clicking on protected fact sheet or download button, It should open a popup window.
        5. Popup window should work as expected.
        6. Checks Image Label & Desc is there or not.
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)

        pages = 3
        self.basePage.press_button(self.mediaLibraryPage.fact_sheet_tab_xpath)


        for page in range(pages):

            protected_img_index, protected_img_src_list, protected_img_btn_clickable_list, protected_img_page_label_list, protected_img_desc_page_label_list, protected_img_pop_up_window_list, protected_img_yes_btn_clickable_list, protected_img_current_page_url_list, protected_img_current_page_url_one_list, protected_img_page_url_list, protected_img_nav_current_page_url_list = self.mediaLibraryPage.protected_img()

            for img_src, btn_clickable, pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one, protected_img_page_url, protected_img_nav_current_page_url in zip(protected_img_src_list, protected_img_btn_clickable_list, protected_img_pop_up_window_list, protected_img_yes_btn_clickable_list, protected_img_current_page_url_list, protected_img_current_page_url_one_list, protected_img_page_url_list, protected_img_nav_current_page_url_list):
                assert "lock" in img_src
                assert btn_clickable == True
                assert yes_btn_clickable == True
                assert "dialog" in pop_up_window
                assert current_page_url == current_page_url_one
                assert protected_img_page_url in protected_img_nav_current_page_url

            for protected_img_page_label, protected_img_desc_page_label in zip(protected_img_page_label_list, protected_img_desc_page_label_list):

                if len(protected_img_page_label) > 0:
                    assert len(protected_img_page_label) > 0
                    assert len(protected_img_desc_page_label) > 0

            if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and protected_img_index <=3:
                self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)




