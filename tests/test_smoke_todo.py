import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
from BaseTest import BaseTest
from Helper import Helper
import os
import logging



from Pages.CareerSearchPage import CareerSearchPage

now = datetime.now() 



# If any more library is needed import it here.

# Holds down the alt key


@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
class TestSmokeToDo(BaseTest):

    logging.basicConfig(filename="C:\\Users\\PODDEDE2.APNET\\arctic-selenium-testing\\logs\\test.log",
    format='%(asctime)s: %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')

    logger = logging.getLogger()
    


    def test_ARC_2411_VideoLinksVerify(self):
        # move ID & XPATH selectors into the appropriate page location (line 99 and line 107)

        self.driver.get(self.env)
        # 1. put this Accept Cookies button in an IF (to execute only if they have not been accepted)
        # 2. ask Padma/Kothaima to add this condition explicitly in the test case (Xray Manual)
        self.basePage.press_button((By.ID, "onetrust-accept-btn-handler"))
        if len(self.driver.find_elements(self.homePage.research_dev_video_xpath[0], self.homePage.research_dev_video_xpath[1])) > 0:
            pause_clip, play_pause_btn, link, play_clip, video_render_state = self.homePage.youtube_videos(self.homePage.research_dev_video_xpath, (By.XPATH, "//iframe[@title='YouTube video player']"))
            assert "Pause clip" in pause_clip
            assert "playPauseBtn" in play_pause_btn
            assert "Play clip" in play_clip
            assert "play-state" in video_render_state


        
        pause_clip, play_pause_btn, link, play_clip, video_render_state = self.homePage.youtube_videos(self.homePage.esg_video_xpath, self.homePage.novartis_video_link_css)
        assert "Pause clip" in pause_clip
        assert "playPauseBtn" in play_pause_btn
        assert "Play clip" in play_clip
        assert "play-state" in video_render_state


    
    
        


    # def test_ARC_2659_MediaLibraryDetails(self):

    #     self.driver.get(self.env + "news/media-library")


    #     dict_img_unprotected = self.mediaLibraryPage.check_unprotected_img()
    #     if len(dict_img_unprotected) > 0:
    #         assert dict_img_unprotected['img_url'] in dict_img_unprotected['page_url']
    #         assert len(dict_img_unprotected['img_src']) > 0
    #         assert dict_img_unprotected['btn_clickable'] == True
    #         for unprotected_img_page_label, unprotected_img_desc_page_label, label in zip(dict_img_unprotected['unprotected_img_page_label_list'],dict_img_unprotected['unprotected_img_desc_page_label_list'], self.mediaLibraryPage.label_list):
    #             if unprotected_img_page_label == label:
    #                 assert unprotected_img_page_label == label
    #                 assert len(unprotected_img_desc_page_label) > 0

    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))
            
    #     if len(self.driver.find_elements(By.LINK_TEXT, "Back to Previous Page")) > 0:
    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))

    #     dict_img_protected = self.mediaLibraryPage.check_protected_img()
    #     if len(dict_img_protected) > 0:
    #         assert dict_img_protected['img_url'] in dict_img_protected['page_url']
    #         assert "lock-image" in dict_img_protected['img_src']
    #         assert "Download" in dict_img_protected['download_btn']
    #         assert "dialog" in dict_img_protected['pop_up_window']
    #         assert dict_img_protected['yes_btn_clickable'] == True
    #         assert dict_img_protected['current_page_url'] == dict_img_protected['current_page_url_one']
    #         for protected_img_page_label, protected_img_desc_page_label, label in zip(dict_img_protected['protected_img_page_label_list'],dict_img_protected['protected_img_desc_page_label_list'], self.mediaLibraryPage.label_list):
    #             if protected_img_page_label == label:
    #                 assert protected_img_page_label == label
    #                 assert len(protected_img_desc_page_label) > 0
                
    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))

    #     if len(self.driver.find_elements(By.LINK_TEXT, "Back to Previous Page")) > 0:
    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))

    #     dict_doc_unprotected = self.mediaLibraryPage.check_unprotected_doc()
    #     if len(dict_doc_unprotected) > 0:
    #         assert dict_doc_unprotected['img_url'] in dict_doc_unprotected['page_url']
    #         assert dict_doc_unprotected['btn_clickable'] == True
    #         assert 'Download' in dict_doc_unprotected['btn']
    #         for unprotected_doc_page_label, unprotected_doc_page_desc_label, label in zip(dict_doc_unprotected['unprotected_doc_page_label_list'], dict_doc_unprotected['unprotected_doc_desc_page_label_list'], self.mediaLibraryPage.label_list):
    #             if unprotected_doc_page_label == label:
    #                 assert unprotected_doc_page_label == label
    #                 assert len(unprotected_doc_page_desc_label) > 0
                
    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))

    #     if len(self.driver.find_elements(By.LINK_TEXT, "Back to Previous Page")) > 0:
    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))

    #     dict_doc_protected = self.mediaLibraryPage.check_protected_doc()
    #     if len(dict_doc_protected) > 0:
    #         assert dict_doc_protected['img_url'] in dict_doc_protected['page_url']
    #         assert "lock-image" in dict_doc_protected['img_src']
    #         assert "Download" in dict_doc_protected['download_btn']
    #         assert "dialog" in dict_doc_protected['pop_up_window']
    #         assert dict_doc_protected['yes_btn_clickable'] == True
    #         assert dict_doc_protected['current_page_url'] == dict_doc_protected['current_page_url_one']
    #         for protected_doc_page_label, protected_doc_page_desc_label, label in zip(dict_doc_protected['protected_doc_page_label_list'], dict_doc_protected['protected_doc_desc_page_label_list'], self.mediaLibraryPage.label_list):
    #             if protected_doc_page_label == label:
    #                 assert protected_doc_page_label == label
    #                 assert len(protected_doc_page_desc_label) > 0

    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))

    #     if len(self.driver.find_elements(By.LINK_TEXT, "Back to Previous Page")) > 0:
    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))

    #     video_page_label_list, video_page_desc_label_list, flag, video_frame_len = self.mediaLibraryPage.check_video_page()

    #     assert flag == 1
    #     assert video_frame_len > 0
    #     for video_page_label, video_page_desc_label, label in zip(video_page_label_list, video_page_desc_label_list, self.mediaLibraryPage.label_list):
    #         if video_page_label == label:
    #             assert video_page_label == label
    #             assert len(video_page_desc_label) > 0
                

    #     if len(self.driver.find_elements(By.LINK_TEXT, "Back to Previous Page")) > 0:
    #         self.basePage.press_button((By.LINK_TEXT, "Back to Previous Page"))




    


    # def test_ARC_1111_menu(self):

    #     self.driver.get(self.env)

    #     self.basePage.press_button((By.CSS_SELECTOR, "#block-nvs-arctic-account-menu > li.nav-item.menu > span"))
    #     # self.basePage.press_button((By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(14) > p"))
    #     time.sleep(5)





    # def test_ARC_999_hello(self):

    #     <ul>
    #     <li></li>
    #     <li></li>
    #     <li></li>
    #     <li></li>
    #     </ul>

    #     self.driver.get(self.env + "news/news-archive")
    #     self.basePage.press_button((By.LINK_TEXT, "Media Releases"))
    #     list = []
    #     flag=0
    #     elements = self.driver.find_elements(By.XPATH, "//*[@id='block-views-block-news-archive-block-1']/div/div/div/div/div[1]/ul/li")
    #     for element in elements:
    #         a = element.find_element(By.ID, "list-card-wrapper")
    #         list.append(int(a.find_element(By.CSS_SELECTOR, "span.views-field-field-date > span").text.split(" ")[1].split(",")[0]))

    #     list1 = list[:]
    #     list1.sort(reverse = True)
    #     if (list1 == list):
	#         flag = 1

    #     assert flag == 1


  


    # def test_ARC_1010_demo(self):

    #     self.driver.get(self.env + "careers/career-search")
    #     self.basePage.send_keys((By.ID, "edit-search-api-fulltext--2"), "sales")
    #     assert "(Senior) Sales Executive" in self.basePage.get_element_text((By.CSS_SELECTOR, "#ui-id-3 > div > span"))




    # def test_ARC_2317_MegaMenuVerify(self):


    #     self.driver.get(self.env)
    #     self.basePage.click_button((By.ID, "onetrust-accept-btn-handler"))
    #     self.megaMenuPage.clickMegaMenuButton()
    #     # self.megaMenuPage.rightSideImgEle()
    #     self.megaMenuPage.aboutEle()
    #     self.megaMenuPage.healthCareProfessionalEle()

    # def test_ARC_1212_footer(self):

    #     self.driver.get(self.env)
    #     self.basePage.press_button(self.twitter)
    #     self.basePage.press_button((By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)"))
    #     assert "Twitter" in self.driver.page_source
    #     self.driver.switch_to.window(self.driver.window_handles[0])

    #     time.sleep(5)

    #     self.basePage.press_button(self.linkedin)
    #     self.basePage.press_button((By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)"))
    #     assert "LinkedIn" in self.driver.page_source
    #     self.driver.switch_to.window(self.driver.window_handles[0])

    #     time.sleep(5)

    # def test_ARC_2647_MediaLibrary(self):

    #     self.driver.get(self.env)

    #     self.homePage.news_mega_menu(self.homePage.mega_menu_media_library_xpath,self.env_name,'media-library')



    #     assert "patterns" in self.basePage.get_css_property(self.mediaLibraryPage.pattern_css, "background-image")

    #     assert "arctic_grid_view" in self.basePage.get_elemet_attribute(self.mediaLibraryPage.arctic_list_grid_view_css, "class")
    #     assert "rgba(101, 101, 101, 1)" in self.basePage.get_css_property(self.mediaLibraryPage.media_library_breadcrumb_color_css, "color")

    #     assert len(self.driver.title) > 0

    #     # BreadCrumb Validation #
    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.mediaLibraryPage.breadcrumb_ele()

    #     # assert "Home" in breadcrumb_items
    #     # assert "News" in breadcrumb_items
    #     # assert "Media Library" in breadcrumb_items

    #     assert len(breadcrumb_items) == 3

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    #     for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
    #         assert breadcumb_anchor_url in breadcumb_anchor_current_url


    #     # Pagination #
    #     num_content_page = len(self.driver.find_elements(self.mediaLibraryPage.content_pages_css[0], self.mediaLibraryPage.content_pages_css[1]))

    #     if num_content_page == 12 and len(self.driver.find_elements(self.mediaLibraryPage.pagination_heading_xpath[0], self.mediaLibraryPage.pagination_heading_xpath[1])) > 0:

    #         page_content_list = self.mediaLibraryPage.pagination_validation()
    #         page_count_len = len(page_content_list)
    #         while page_count_len > 0:
    #             assert len(page_content_list) > 0
    #             page_count_len = page_count_len - 1

            
    #         page_one_contents, page_zero_contents = self.mediaLibraryPage.pagination_front_arrow_back_arrow_validation()
    #         assert len(page_one_contents) > 0
    #         assert len(page_zero_contents) > 0


    #     # List & Grid View #
    #     grid_view_btn, list_view_btn, list_view, grid_view, grid_icon, list_icon = self.mediaLibraryPage.list_grid_view()

    #     assert "Grid View" in grid_view_btn
    #     assert "arctic_list_view" in list_view
    #     assert "grid.svg" in grid_icon

    #     assert "List View" in list_view_btn
    #     assert "arctic_grid_view" in grid_view
    #     assert "list.svg" in list_icon

        
    #     # Lock Icon Verify
    #     content_pages_locked = self.driver.find_elements(self.mediaLibraryPage.protected_items_css[0], self.mediaLibraryPage.protected_items_css[1])

    #     index = 0
    #     pages = 2

    #     for p in range(pages):
    #         index = 0
    #         content_pages_locked = self.driver.find_elements(self.mediaLibraryPage.protected_items_css[0], self.mediaLibraryPage.protected_items_css[1])
    #         for i in content_pages_locked:

    #             content_pages_locked = self.driver.find_elements(self.mediaLibraryPage.protected_items_css[0], self.mediaLibraryPage.protected_items_css[1])
    #             assert "rgb(228, 228, 228)" in content_pages_locked[index].value_of_css_property("background")


    #             if len(content_pages_locked[index].find_elements(self.mediaLibraryPage.lock_icon_overview_img_css[0], self.mediaLibraryPage.lock_icon_overview_img_css[1])) > 0:

    #                 lock_img_ele = content_pages_locked[index].find_element(self.mediaLibraryPage.lock_icon_overview_img_css[0], self.mediaLibraryPage.lock_icon_overview_img_css[1])
    #                 lock_img_attr = content_pages_locked[index].find_element(self.mediaLibraryPage.lock_icon_overview_img_css[0], self.mediaLibraryPage.lock_icon_overview_img_css[1]).get_attribute("class")
                    
    #                 if "no-img" in lock_img_attr:
    #                     assert "document-type-locked" in lock_img_ele.find_element(self.mediaLibraryPage.lock_icon_no_img_css[0], self.mediaLibraryPage.lock_icon_no_img_css[1]).get_attribute("class")
    #                 else:
    #                     assert "document-type-locked" in lock_img_ele.find_element(self.mediaLibraryPage.lock_icon_css[0], self.mediaLibraryPage.lock_icon_css[1]).get_attribute("class")


    #             index = index + 1
    #         self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)
    #         # if "No results found" in self.driver.page_source:
    #         #     break
        
    #     self.basePage.press_button(self.mediaLibraryPage.media_library_breadcrumb_color_css)


    #     # Grey BGcolor #
    #     hex_color_list = self.mediaLibraryPage.grey_menu_verify()

    #     hex_color_list_len = len(hex_color_list)
    #     while hex_color_list_len > 0:

    #         assert "#f1f1f1" in hex_color_list[hex_color_list_len-1]
    #         hex_color_list_len = hex_color_list_len - 1



    # @pytest.mark.migration
    # @pytest.mark.singapore
    # def test_ARC_2586_NewsArchive(self):

    #     self.driver.get(self.env)
    #     # self.driver.get(self.env + "news/news-archive")
    #     self.homePage.news_mega_menu(self.homePage.mega_menu_news_archive_xapth,self.env_name,'news-archive')

        

    #     # assert len(self.basePage.get_elemet_attribute(self.newsPage.banner_img_css, "src")) > 0
    #     assert "patterns" in self.basePage.get_css_property(self.newsPage.pattern_css, "background-image")
        
    #     search_bar, search_btn = self.newsPage.search_bar_and_btn()
    #     assert self.newsPage.search_txt in search_bar
    #     assert self.newsPage.search_txt in search_btn

    #     assert "arctic_grid_view" in self.basePage.get_elemet_attribute(self.newsPage.news_page_view_css, "class")
    #     assert "list.svg" in self.basePage.get_css_property(self.newsPage.view_toggle_icon, "background")

    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.newsPage.breadcrumb_ele()

    #     # assert "Home" in breadcrumb_items
    #     # assert "News" in breadcrumb_items
    #     # assert "News Archive" in breadcrumb_items
    #     assert len(breadcrumb_items) == 3

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    #     assert "rgba(101, 101, 101, 1)" in self.basePage.get_css_property(self.newsPage.news_archive_last_child_breadcrumb_color_css, "color")

    #     assert len(self.basePage.get_element_text(self.newsPage.from_date_xpath)) > 0
    #     assert len(self.basePage.get_element_text(self.newsPage.to_date_xpath)) > 0

    #     # Pagination #
    #     num_content_page = len(self.driver.find_elements(self.newsPage.content_pages_css[0], self.newsPage.content_pages_css[1]))

    #     if num_content_page == 12 and len(self.driver.find_elements(self.newsPage.pagination_numbers_css[0], self.newsPage.pagination_numbers_css[1])) > 0:

    #         pagination = self.driver.find_elements(self.newsPage.pagination_numbers_css[0], self.newsPage.pagination_numbers_css[1])
    #         pagination_len = len(pagination)
    #         count = 0
    #         pagination_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #         while pagination_len > 0:
    #             if pagination[count].find_element(self.newsPage.pagination_links_css[0], self.newsPage.pagination_links_css[1]).text in pagination_list:
    #                 assert pagination[count].find_element(self.newsPage.pagination_links_css[0], self.newsPage.pagination_links_css[1]).text in pagination_list
    #             pagination_len = pagination_len - 1
    #             count = count + 1


    #     all_topics_txt, hex_code = self.newsPage.all_topics_grey_color()
    #     assert len(all_topics_txt) > 0
    #     assert "#f1f1f1" in hex_code

    #     breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.newsPage.check_all_breadcrumb_url()
    #     for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
    #         assert breadcumb_anchor_url in breadcumb_anchor_current_url


    #     desc_sort, language_tab_txt = self.newsPage.media_release(self.env_name)
    #     assert desc_sort == True
    #     if self.env_name == "global":
    #         assert "Language" in language_tab_txt

    #     if self.env_name == "global":
    #         language_tab_txt = self.newsPage.key_releases(self.env_name)
    #         assert "Language" in language_tab_txt

    #     toggle_btn_txt, current_view_txt, view_icon = self.newsPage.toggle_view()
    #     assert len(toggle_btn_txt) > 0
    #     assert "arctic_list_view" in current_view_txt
    #     assert "grid.svg" in view_icon

    #     hex_color_list, empty_list = self.newsPage.grey_menu_verify()

    #     empty_list_len = len(empty_list)
    #     hex_color_list_len = len(hex_color_list)

    #     while hex_color_list_len > 0:
    #         if empty_list_len > 0:
    #             if "view-empty" in empty_list[empty_list_len-1]:
    #                 assert "view-empty" in empty_list[empty_list_len-1]
    #         assert "#f1f1f1" in hex_color_list[hex_color_list_len-1]
    #         hex_color_list_len = hex_color_list_len - 1
    #         empty_list_len = empty_list_len - 1



    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # def test_ARC_2601_StoriesPageAndDetails(self):

    #     self.driver.get(self.env)
    #     # self.driver.get(self.env + "stories")
    #     self.homePage.news_mega_menu(self.homePage.mega_menu_stories_xpath,self.env_name,'stories')


    #     assert "logo.svg" in self.basePage.get_elemet_attribute(self.storiesPage.novartis_logo_xpath, "src")

    #     search_icon = self.storiesPage.search_icon_ele()
    #     assert "icon-search.svg" in search_icon

    #     assert len(self.basePage.get_element_text(self.storiesPage.mega_menu_css)) > 0

    #     assert "/themes/custom/nvs_arctic/patterns/images/blue_carbon_open_pattern_tile_120.png" in self.basePage.get_css_property(self.storiesPage.pattern_css, "background-image")
       
    #     all_topics_txt, hex_code = self.storiesPage.all_topics_grey_color()
    #     assert len(all_topics_txt) > 0
    #     assert "#f1f1f1" in hex_code

    #     # ARC-3217
    #     # assert "breadcrumb-item" not in self.driver.page_source

    #     menu_items = self.storiesPage.verify_menu_names()
    #     for menu_item in menu_items:

    #         assert len(menu_item.find_element(self.storiesPage.anchor_tag_loc[0], self.storiesPage.anchor_tag_loc[1]).text) > 0

    #     toggle_btn_txt, current_view_txt, view_icon = self.storiesPage.default_view()
    #     assert len(toggle_btn_txt) > 0
    #     assert "arctic_grid_view" in current_view_txt
    #     assert "/themes/custom/nvs_arctic/patterns/images/list.svg" in view_icon

    #     # ARC-3217
    #     # home_url, current_url = self.storiesPage.check_home_breadcrumb()
    #     # assert current_url == home_url

    #     # ARC-3217
    #     # stories_url, current_url = self.storiesPage.check_media_center_breadcrumb()
    #     # assert current_url == stories_url

    #     all_topics_txt, hex_code = self.storiesPage.all_topics_grey_color()
    #     assert len(all_topics_txt) > 0
    #     assert "#f1f1f1" in hex_code


    #     # Pagination #
    #     num_content_page = len(self.driver.find_elements(self.storiesPage.content_pages_css[0], self.storiesPage.content_pages_css[1]))

    #     if num_content_page == 12 and len(self.driver.find_elements(self.storiesPage.pagination_heading_xpath[0], self.storiesPage.pagination_heading_xpath[1])) > 0:

    #         assert num_content_page == 12
    #         assert "pagination" in self.basePage.get_elemet_attribute(self.storiesPage.pagination_heading_txt_xpath, "id")
            
    #         page_one_content_len, page_zero_content_len = self.storiesPage.pagination_front_arrow_back_arrow_validation()
    #         assert page_one_content_len > 0
    #         assert page_zero_content_len > 0


    #     toggle_btn_txt, current_view_txt, view_icon = self.storiesPage.toggle_view()
    #     assert len(toggle_btn_txt) > 0
    #     assert "arctic_list_view" in current_view_txt
    #     assert "grid.svg" in view_icon


    #     hex_color_list, page_src_list = self.storiesPage.menu_items()

    #     hex_color_list_len = len(hex_color_list)
    #     while hex_color_list_len > 0:

    #         assert "#f1f1f1" in hex_color_list[hex_color_list_len-1]
    #         # ARC-3217
    #         # if hex_color_list_len - 1 != 0:
    #         #     assert "breadcrumb-item" in page_src_list[hex_color_list_len-2]
    #         hex_color_list_len = hex_color_list_len - 1


    #     self.driver.get(self.env + "stories")
    #     content_title = self.basePage.get_element_text(self.storiesPage.first_content_title_css)
    #     self.basePage.press_button(self.storiesPage.first_content_css)

    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.storiesPage.content_breadcrumb_ele()

    #     # assert "Home" in breadcrumb_items
    #     # assert "Stories" in breadcrumb_items
    #     assert len(breadcrumb_items) == 3
    #     assert content_title in breadcrumb_items

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    #     twitter_icon_element, twitter_txt_element, twitter_clickable, facebook_icon_element, facebook_txt_element, facebook_clickable, whatsapp_icon_element, whatsapp_clickable, linkedin_icon_element, linkedin_clickable, email_icon_element, email_clickable = self.storiesPage.social_media_icons()

    #     assert "twitter.svg" in twitter_icon_element
        
    #     assert "Tweet" in twitter_txt_element
    #     assert twitter_clickable == True

    #     assert "facebook.svg" in facebook_icon_element
    #     assert "Share" in facebook_txt_element
    #     assert facebook_clickable == True

    #     assert "whatsapp.svg" in whatsapp_icon_element
    #     assert whatsapp_clickable == True

    #     assert "linkedin.svg" in linkedin_icon_element
    #     assert linkedin_clickable == True

    #     assert "email.svg" in email_icon_element
    #     assert email_clickable == True

    #     print_icon, print_txt, pdf_icon, pdf_txt = self.storiesPage.print_and_save_btn()

    #     assert "print.svg" in print_icon
    #     assert len(print_txt) > 0
    #     assert "save.svg" in pdf_icon
    #     assert len(pdf_txt) > 0



    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # def test_ARC_2736_JobDetails(self):

    #     self.driver.get(self.env)
    #     # self.driver.get(self.env + "careers/career-search")
    #     self.homePage.career_mega_menu(self.homePage.mega_menu_career_search_xpath,self.env_name)

    #     total_rows = self.driver.find_elements(self.jobDetailsPage.total_row_css[0], self.jobDetailsPage.total_row_css[1])
    #     row_index = 0

    #     assert len(total_rows) > 0       

    #     for row in total_rows:

    #         total_rows = self.driver.find_elements(self.jobDetailsPage.total_row_css[0], self.jobDetailsPage.total_row_css[1])
    #         rand_num = random.randint(0,len(total_rows) - 1)
    #         job_title = total_rows[rand_num].find_element(self.jobDetailsPage.job_title_css[0], self.jobDetailsPage.job_title_css[1]).text
    #         self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.jobDetailsPage.job_title_css[0], self.jobDetailsPage.job_title_css[1]))
    #         current_page_url = self.driver.current_url

    #         assert "#656565" == self.basePage.get_css_color((By.LINK_TEXT, job_title), "color")

    #         # BreadCrumb Validation #
    #         breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_third_arrow_element, home_url, home_current_url, careers_url, careers_current_url, careers_search_url, careers_current_search_url = self.jobDetailsPage.breadcrumb_ele()

    #         # assert "Home" in breadcrumb_items
    #         # assert "Careers" in breadcrumb_items
    #         # assert "Career Search" in breadcrumb_items
    #         assert len(breadcrumb_items) == 4
    #         assert job_title in breadcrumb_items

    #         assert ">" in breadcrumb_first_arrow_element
    #         assert ">" in breadcrumb_second_arrow_element
    #         assert ">" in breadcrumb_third_arrow_element

    #         assert home_current_url in  home_url
    #         assert careers_current_url in  careers_url
    #         assert careers_current_search_url in  careers_search_url

    #         assert "patterns" in self.basePage.get_css_property(self.jobDetailsPage.pattern_css, "background-image")
    #         assert job_title == self.basePage.get_element_text(self.jobDetailsPage.job_page_title_css)
    #         assert len(self.basePage.get_element_text(self.jobDetailsPage.job_id_css)) > 0
    #         assert len(self.basePage.get_element_text(self.jobDetailsPage.job_date_css)) > 0
    #         assert len(self.basePage.get_element_text(self.jobDetailsPage.job_location_css)) > 0

    #         # assert len(self.basePage.get_elemet_attribute(self.jobDetailsPage.job_img_css, "src")) > 0
    #         # assert self.jobDetailsPage.box_color in self.basePage.get_css_property(self.jobDetailsPage.frame_css, "border-right-color")
    #         # assert self.jobDetailsPage.box_color in self.basePage.get_css_property(self.jobDetailsPage.frame_css, "border-left-color")
    #         # assert self.jobDetailsPage.box_color in self.basePage.get_css_property(self.jobDetailsPage.frame_css, "border-bottom-color")
    #         # assert "none" in self.basePage.get_css_property(self.jobDetailsPage.frame_css, "border-top")

    #         if self.driver.get_window_size().get("width") > 1050:
    #             assert len(self.basePage.get_elemet_attribute(self.jobDetailsPage.job_img_css, "src")) > 0
    #             assert job_title == self.basePage.get_element_text(self.jobDetailsPage.frame_job_title_css)
    #             assert len(self.basePage.get_element_text(self.jobDetailsPage.frame_job_id_css)) > 0
                
    #         jobs = self.jobDetailsPage.apple_access_job_by_screen_size()
    #         job_index = 0

    #         for job in jobs:
    #             jobs = self.jobDetailsPage.apple_access_job_by_screen_size()
    #             assert len(jobs[job_index].text) > 0
    #             pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_url = self.jobDetailsPage.external_link(jobs[job_index])

    #             assert self.homePage.novartis_logo in pop_up_logo
    #             assert len(pop_up_title) > 0
    #             assert self.homePage.external_popup_desc in pop_up_desc
    #             assert self.homePage.continue_button_txt in continue_btn
    #             assert continue_btn_clickable == True
    #             assert self.homePage.cancel_button_txt in cancel_btn
    #             assert cancel_btn_clickable == True
    #             assert current_page_url == page_url

    #             jobs = self.jobDetailsPage.apple_access_job_by_screen_size()
    #             class_name = jobs[job_index].get_attribute("href")
    #             job_url, apply_access_job_page_url = self.jobDetailsPage.apply_access_job_page(jobs[job_index], class_name)
                
    #             assert len(job_url) > 0
    #             assert len(apply_access_job_page_url) > 0

    #             job_index = job_index + 1

    #         tag_elements_len, tag_elements_list, tag_elements_url_list, tag_elements_page_url_list = self.jobDetailsPage.tag_ele()
    #         assert tag_elements_len > 0

    #         for tag_element, tag_element_url, tag_element_page_url in zip(tag_elements_list, tag_elements_url_list, tag_elements_page_url_list):

    #             assert len(tag_element) > 0
    #             assert tag_element_url == tag_element_page_url

            

    #         share_btn_icon, share_btn_txt, twitter_icon, facebook_icon, whatsapp_icon, linkedin_icon, email_icon = self.jobDetailsPage.share_btn_ele()
    #         assert "share" in share_btn_icon
    #         assert len(share_btn_txt) > 0
    #         assert "twitter" in twitter_icon
    #         assert "facebook" in facebook_icon
    #         assert "whatsapp" in whatsapp_icon
    #         assert "linkedin" in linkedin_icon
    #         assert "email" in email_icon

    #         print_btn_txt, print_btn_clickable, print_icon, print_url, print_page_url = self.jobDetailsPage.print_btn_ele()
    #         assert len(print_btn_txt) > 0
    #         assert print_btn_clickable == True
    #         assert "print" in print_icon
    #         assert print_url == print_page_url

    #         save_btn_txt, save_btn_clickable, save_icon = self.jobDetailsPage.save_btn_ele()
    #         assert len(save_btn_txt) > 0
    #         assert save_btn_clickable == True
    #         assert "save" in save_icon

    #         assert self.basePage.get_elemet_attribute(self.jobDetailsPage.jobs_content_css, "class") == "jobs-content"

    #         job_detail_label_list, job_detail_value_list = self.jobDetailsPage.label_name_value_ele()
    #         for job_detail_label, job_detail_value in zip(job_detail_label_list, job_detail_value_list):
    #             assert len(job_detail_label) > 0
    #             assert len(job_detail_value) > 0

    #         self.driver.back()

    #         row_index = row_index + 1
    #         if row_index == 4:
    #             break


    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # def test_ARC_2673_CareersLandingPage(self):

    #     self.driver.get(self.env)

    #     # self.driver.get(self.env + "careers")
    #     self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_career_xpath,'careers')

    #     hero_img_len, hero_txt_len = self.careerLandingPage.hero_ele()
    #     assert hero_img_len > 0
    #     assert hero_txt_len > 0


    #     stripe_list = self.careerLandingPage.stripe_ele()

    #     for stripe in stripe_list:
    #         assert "stripe" in stripe

    #     assert len(self.basePage.get_elemet_attribute(self.careerLandingPage.search_input_field_xpath, "placeholder")) > 0
    #     assert len(self.basePage.get_element_text(self.careerLandingPage.function_txt_css)) > 0
    #     assert len(self.basePage.get_element_text(self.careerLandingPage.location_txt_css)) > 0
    #     assert len(self.basePage.get_elemet_attribute(self.careerLandingPage.search_btn_xpath, "value")) > 0

    #     if self.driver.find_elements(self.careerLandingPage.careers_txt_css[0], self.careerLandingPage.careers_txt_css[1]):
    #         assert len(self.basePage.get_element_text(self.careerLandingPage.careers_txt_css)) > 0

    #     filtered_elements_list, filterd_attributes_list = self.careerLandingPage.filter_location()
    #     for filtered_attr, filtered_ele in zip(filterd_attributes_list,filtered_elements_list):
    #         assert filtered_attr in filtered_ele

     # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.usa
    # @pytest.mark.uk
    # def test_ARC_2723_ProductOverviewPage(self):

    #     self.driver.get(self.env)
    #     self.homePage.about_product_mega_menu(self.env_name)

    #     page_title = self.driver.title
    #     assert len(self.basePage.get_element_text(self.productPage.page_title_css)) > 0
    #     assert len(self.basePage.get_element_text(self.productPage.page_intro_text_css)) > 0

    #     assert len(self.driver.find_elements(self.productPage.product_list_css[0], self.productPage.product_list_css[1])) > 0

    #     available_in_list = self.productPage.available_in_ele()

    #     for available_in in available_in_list:

    #         assert len(available_in) > 0

    #     assert len(self.basePage.get_elemet_attribute(self.productPage.search_input_field_xpath, "placeholder")) > 0
    #     assert len(self.basePage.get_elemet_attribute(self.productPage.search_btn_field_xpath, "value")) > 0

    #     filter_tab_list = self.productPage.filter_tabs_presence()

    #     for filter_tab in filter_tab_list:

    #         assert len(filter_tab) > 0


    #     if len(self.driver.find_elements(self.productPage.total_row_css[0], self.productPage.total_row_css[1])) == 6 and "pagination-heading" in self.driver.page_source:

    #         assert "pagination-heading" in self.driver.page_source

    #         next_page_url, prev_page_url = self.productPage.pagination_check()
    #         assert "page=1" in next_page_url
    #         assert "page=0" in prev_page_url

        
    #     else:

    #         assert "pagination-heading" not in self.driver.page_source

    #     self.driver.get(self.env)
    #     self.homePage.about_product_mega_menu(self.env_name)

    #     if len(self.driver.find_elements(self.productPage.total_row_css[0], self.productPage.total_row_css[1])) == 6 and "pagination-heading" in self.driver.page_source:

    #         pagination_index = 3
    #         flag = 0
    #         while pagination_index > 0:
    #             if len(self.driver.find_elements(self.productPage.download_btn_css[0], self.productPage.download_btn_css[1])) > 0:

    #                 download_btn_txt, download_btn_clickable, flag = self.productPage.download_btn_ele()
    #                 assert len(download_btn_txt) > 0
    #                 assert download_btn_clickable == True

    #             pagination_index = pagination_index - 1
    #             if flag == 1:
    #                 break
    #             self.basePage.press_button(self.productPage.next_page_arrow_xpath)

    #     else:

    #         if len(self.driver.find_elements(self.productPage.download_btn_css[0], self.productPage.download_btn_css[1])) > 0:

    #                 download_btn_txt, download_btn_clickable, flag = self.productPage.download_btn_ele()
    #                 assert len(download_btn_txt) > 0
    #                 assert download_btn_clickable == True


    #     self.productPage.no_result_check()
    #     assert len(self.basePage.get_element_text(self.productPage.empty_css)) > 0
    #     self.driver.get(self.env)
    #     self.homePage.about_product_mega_menu(self.env_name)

    #     search_result_list = self.productPage.verify_search_result()

    #     for search_result in search_result_list:
    #         assert "afinitor" in search_result.lower()

    #     self.driver.get(self.env)
    #     self.homePage.about_product_mega_menu(self.env_name)

    #     alphabetical_order_list, grey_color_list = self.productPage.check_filter_tab()
    #     for alphabetical_order, grey_color in zip(alphabetical_order_list, grey_color_list):
    #         assert "A-Z" in alphabetical_order
    #         assert "#f1f1f1" in grey_color

    #     self.driver.get(self.env)
    #     self.homePage.about_product_mega_menu(self.env_name)

    #     a_z_view, z_a_view = self.productPage.toggle_view()
    #     assert "Z-A" in z_a_view
    #     assert "A-Z" in a_z_view
                
    #     self.driver.get(self.env)
    #     self.homePage.about_product_mega_menu(self.env_name)
    #     domain_url, domain_current_url = self.productPage.internal_hyperlink_check()
    #     assert domain_current_url == domain_url

    #     external_domain_url, external_domain_current_url, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, cancel_btn, current_page_title = self.productPage.external_hyperlink_check()

    #     if len(external_domain_current_url) > 0:
    #         assert external_domain_current_url == external_domain_url
    #         assert len(pop_up_logo) > 0
    #         assert len(pop_up_title) > 0
    #         assert len(pop_up_desc) > 0
    #         assert self.productPage.continue_button_txt in continue_btn
    #         assert self.productPage.cancel_button_txt in cancel_btn
    #         assert page_title == current_page_title



    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # @pytest.mark.sandoz
    # def test_ARC_2493_HeaderSearch(self):

    #     self.driver.get(self.env)
    #     page_title = self.driver.title
    #     self.homePage.click_search_icon()

    #     hex_code, search, global_search, css_txt = self.homePage.verify_search_window()
    #     assert "#c7c7c7" in hex_code
    #     assert len(search) > 0
    #     assert len(global_search) > 0
    #     assert "icon-search.svg" in css_txt

    #     global_search_txt, search_txt, search_txt_url = self.homePage.search_text(self.homePage.search_keyword, self.searchPage.search_result_xpath)
    #     assert len(global_search_txt) > 0
    #     assert self.homePage.search_keyword in search_txt
    #     assert self.homePage.search_keyword in search_txt_url

    #     self.searchPage.click_global_search()

    #     global_search_window_list, clear_all = self.searchPage.verify_global_search_window()
    #     count=0
    #     for global_search_window in global_search_window_list:
    #         assert len(global_search_window) > 0
    #         count = count + 1
    #     assert len(clear_all) > 0
        
    #     global_search_number = self.searchPage.select_filter_global_search()
    #     assert  len(global_search_txt) < len(global_search_number) 

    #     global_search_without_number = self.searchPage.clear_all()
    #     assert global_search_without_number == global_search_txt

    #     home_page_url = self.searchPage.close_search()
    #     # assert self.env in home_page_url
    #     assert page_title == self.driver.title


    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # @pytest.mark.sandoz
    # def test_ARC_2479_FooterSearch(self):

    #     self.driver.get(self.env) 
    #     page_title = self.driver.title
    #     global_search_txt, search_txt, search_txt_url = self.homePage.search_txt_footer(self.homePage.search_keyword, self.searchPage.search_result_xpath)
    #     assert len(global_search_txt) > 0
    #     assert self.homePage.search_keyword in search_txt
    #     assert self.homePage.search_keyword in search_txt_url

    #     self.searchPage.click_global_search()

    #     global_search_window_list, clear_all = self.searchPage.verify_global_search_window()
    #     count=0
    #     for global_search_window_txt in global_search_window_list:
    #         assert len(global_search_window_txt) > 0
    #         count = count + 1
    #     assert len(clear_all) > 0
        
    #     global_search_number = self.searchPage.select_filter_global_search()
    #     assert len(global_search_txt) < len(global_search_number) 

    #     global_search_without_number = self.searchPage.clear_all()
    #     assert global_search_without_number == global_search_txt

    #     home_page_url = self.searchPage.close_search()
    #     # assert self.env in home_page_url
    #     assert page_title == self.driver.title



    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # @pytest.mark.eg
    # @pytest.mark.sandoz
    # @pytest.mark.de
    # @pytest.mark.at
    # def test_ARC_2499_FooterLink(self):

    #     self.driver.get(self.env) 

    #     # if self.env_name == "global":
    #         # navigate, topics, explore, companies = self.homePage.footer_sections_get_titles()
    #         # assert "Navigate" in navigate
    #         # assert "Topics" in topics
    #         # assert "Explore" in explore
    #         # assert "Companies" in companies

    #     footer_sub_menu_list = self.driver.find_elements(*self.homePage.footerLinks_xpath)
    #     footer_sub_menu_index = 0
    #     for footer_sub_menu in footer_sub_menu_list:
    #         footer_sub_menu_list = self.driver.find_elements(*self.homePage.footerLinks_xpath)
    #         footer_sub_menu_href = footer_sub_menu_list[footer_sub_menu_index].get_attribute("href")
    #         self.driver.execute_script("arguments[0].click()", footer_sub_menu_list[footer_sub_menu_index])

    #         if footer_sub_menu_href in self.driver.current_url:
                
    #             assert footer_sub_menu_href in self.driver.current_url
    #             try:
    #                 assert self.env in self.driver.current_url
    #             except:
    #                 assert self.env.split("@")[1] in self.driver.current_url
  
                
    #         else:
    #             self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.homePage.continue_button_css[0], self.homePage.continue_button_css[1]))
    #             # assert "Page Not Found" not in self.driver.page_source
    #             assert footer_sub_menu_href in self.driver.current_url
    #         self.driver.back()
    #         footer_sub_menu_index = footer_sub_menu_index + 1

    #     # if self.env_name == "german":
    #     #     self.driver.get(self.env1 + "sitemap.xml")
    #     #     self.driver.back()

    #     portfolio_urls = self.driver.find_elements(*self.homePage.footer_link_portfolio_css)
    #     portfolio_index = 0
    #     for portfolio_link in portfolio_urls:
    #         portfolio_urls = self.driver.find_elements(*self.homePage.footer_link_portfolio_css)
    #         portfolip_sub_menu_href = portfolio_urls[portfolio_index].get_attribute("href")
    #         self.driver.execute_script("arguments[0].click()", portfolio_urls[portfolio_index])
    #         if portfolip_sub_menu_href in self.driver.current_url:
    #              assert portfolip_sub_menu_href in self.driver.current_url
    #         else:
    #             self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.homePage.continue_button_css[0], self.homePage.continue_button_css[1]))
    #             assert portfolip_sub_menu_href in self.driver.current_url
    #         self.driver.back()
    #         portfolio_index += 1
        




    #     if self.env_name == "uk" or self.env_name == "usa" or self.env_name == "singapore":
    #         footer_sub_menu_list = self.driver.find_elements(*self.homePage.footer_link_portfolio_css)
    #         footer_sub_menu_index = 0
    #         for footer_sub_menu in footer_sub_menu_list:
    #             footer_sub_menu_list = self.driver.find_elements(*self.homePage.footer_link_portfolio_css)
    #             footer_sub_menu_href = footer_sub_menu_list[footer_sub_menu_index].get_attribute("href")
    #             if "products" in footer_sub_menu_href:
    #                 self.driver.execute_script("arguments[0].click()", footer_sub_menu_list[footer_sub_menu_index])
    #                 self.driver.back()
    #             footer_sub_menu_index = footer_sub_menu_index + 1



    #     link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.site_map_xpath)
    #     assert len(link_txt) > 0
    #     assert site_url in primary_url

    #     try:
    #         if self.env_name == 'france':
    #             link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_france_xpath)
    #         elif self.env_name == 'italy':
    #             link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_italy_xpath)
    #         elif self.env_name == 'spain':
    #             link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_spain_xpath)
    #     except:
    #         link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_xpath)
    #     assert len(link_txt) > 0
    #     assert primary_url in site_url

    #     try:
    #         if self.env_name == 'france':
    #             link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.privacy_france_xpath)
    #         elif self.env_name == 'italy':
    #             link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.privacy_italy_xpath)
    #         elif self.env_name == 'spain':
    #             link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.privacy_spain_xpath)
    #     except:
    #         link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.privacy_xpath)
    #     assert len(link_txt) > 0
    #     assert primary_url in site_url

    #     link_txt,primary_url,site_url = self.homePage.footer_links_under_copyright(self.homePage.site_directory_css)
    #     assert len(link_txt) > 0
    #     assert site_url in primary_url

    #     site_map_urls = self.homePage.sitemap_validation()
    #     for url in site_map_urls:
    #         try:
    #             assert self.env in url
    #         except:
    #             assert self.env.split("@")[1]  in url


############# PopupDisclaimerSocialMediaIcon ###############

    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # @pytest.mark.eg
    # @pytest.mark.sandoz
    # @pytest.mark.de
    # @pytest.mark.at
    # def test_ARC_2502_PopupDisclaimerSocialMediaIcon(self):

    #     self.driver.get(self.env)
    #     page_title_start = self.driver.title

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.twitter)
    #     assert "" in link_txt
    #     assert self.homePage.novartis_logo in pop_up_logo
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start
    #     twitter_page_title = self.homePage.footer_popup_disclaimer(self.homePage.twitter)
    #     assert "Twitter" in twitter_page_title

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.linkedin)
    #     assert "" in link_txt
    #     assert self.homePage.novartis_logo in pop_up_logo
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start
    #     linkedin_page_title = self.homePage.footer_popup_disclaimer(self.homePage.linkedin)
    #     assert "LinkedIn" in linkedin_page_title

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.youtube)
    #     assert "" in link_txt
    #     assert self.homePage.novartis_logo in pop_up_logo
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start 
    #     youtube_page_title = self.homePage.footer_popup_disclaimer(self.homePage.youtube)
    #     assert "Novartis" in youtube_page_title

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.facebook)
    #     assert "" in link_txt
    #     assert self.homePage.novartis_logo in pop_up_logo
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start
    #     facebook_page_title = self.homePage.footer_popup_disclaimer(self.homePage.facebook)
    #     assert "novartis" in facebook_page_title.lower()

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.instagram)
    #     assert "" in link_txt
    #     assert self.homePage.novartis_logo in pop_up_logo
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start
    #     instagram_page_title = self.homePage.footer_popup_disclaimer(self.homePage.instagram)
    #     assert "Instagram" in instagram_page_title



    ############# ExternalLinkHeader ###############

    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # @pytest.mark.eg
    # @pytest.mark.sandoz
    # @pytest.mark.de
    # @pytest.mark.at
    # def test_ARC_2412_ExternalLinkHeader(self):

    #     self.driver.get(self.env)
    #     page_title_start = self.driver.title
        
    #     # is there a way to loop through all possible external links instead of have them hardcoded?
    #     if self.env_name == "global":
    #         link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.sandoz_css)
    #         assert len(link_txt) > 0
    #         assert self.homePage.novartis_logo in pop_up_logo
    #         assert self.homePage.external_popup_title in pop_up_title
    #         assert self.homePage.external_popup_desc in pop_up_desc
    #         assert len(continue_btn) > 0
    #         assert continue_btn_clickable == True
    #         assert len(cancel_btn) > 0
    #         assert cancel_btn_clickable == True
    #         assert page_title == page_title_start


    #         link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.advanced_accelerator_applications_xpath)
    #         assert len(link_txt) > 0
    #         assert self.homePage.novartis_logo in pop_up_logo
    #         assert self.homePage.external_popup_title in pop_up_title
    #         assert self.homePage.external_popup_desc in pop_up_desc
    #         assert len(continue_btn) > 0
    #         assert continue_btn_clickable == True
    #         assert len(cancel_btn) > 0
    #         assert cancel_btn_clickable == True
    #         assert page_title == page_title_start


    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.twitter)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.linkedin)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.youtube)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.facebook)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title = self.homePage.external_link(self.homePage.instagram)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start



    ############## News Room #############
    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # @pytest.mark.eg
    # @pytest.mark.sandoz
    # @pytest.mark.de
    # @pytest.mark.at
    # def test_ARC_2379_NewsRoom(self):

    #     self.driver.get(self.env)
    #     self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')

    #     hero_img_len, hero_txt_len = self.newsRoomPage.hero_image_text()
    #     assert hero_img_len > 0
    #     assert hero_txt_len > 0

    #     pattern = self.basePage.get_css_property(self.homePage.pattern_css, "background-image")
    #     assert len(pattern) > 0
       
    #     stripe_list = self.newsRoomPage.stripe_ele()

    #     for stripe in stripe_list:
    #         assert "stripe" in stripe

    #     cards,twitter = self.newsRoomPage.stripe_card_val(self.newsRoomPage.card_image_css,self.newsRoomPage.card_title_css,self.newsRoomPage.card_desc_css)
    #     for card in cards:
    #         assert card > 0
    #     if self.driver.find_elements(self.newsRoomPage.tweeter_id[0], self.newsRoomPage.tweeter_id[1]):
    #         assert twitter > 0
    #         assert self.basePage.get_css_color(self.newsRoomPage.tweeter_css,'color') == "#035697"

    #     displayed_status, len_media_card ,len_media_label= self.newsRoomPage.media_release_label()

    #     if displayed_status == True:

    #         assert len_media_card == len_media_label

    #         original_date, sorted_date =self.newsRoomPage.media_date_val()
    #         assert original_date == sorted_date

    #     if len(self.driver.find_elements(*self.newsRoomPage.link_button_css)) > 0:
        
    #         links_button_url_list, links_button_current_url_list = self.newsRoomPage.links_button()
    #         assert links_button_url_list == links_button_current_url_list
            
    #     if len(self.driver.find_elements(*self.newsRoomPage.media_stripe_img_css)) > 0:
    #         assert self.newsRoomPage.stripe_img() == True


    # def test_ARC_2724_NovartisPipeline(self):

    #     self.driver.get(self.env)
    #     self.homePage.about_pipeline_mega_menu()

    #     assert len(self.basePage.get_element_text(self.globalPipelinePage.page_title_css)) > 0
    #     assert len(self.basePage.get_element_text(self.globalPipelinePage.page_intro_css)) > 0

    #     assert self.basePage.get_css_property(self.globalPipelinePage.content_elements_css, "display") == "grid"
    #     assert self.basePage.get_css_property(self.globalPipelinePage.content_elements_css, "grid-template-columns").split(" ")[0] == self.basePage.get_css_property(self.globalPipelinePage.content_elements_css, "grid-template-columns").split(" ")[1]
    #     assert len(self.basePage.get_elemet_attribute(self.globalPipelinePage.search_input_field_xpath, "placeholder")) > 0
    #     assert self.basePage.get_elemet_attribute(self.globalPipelinePage.search_btn_field_xpath, "value") == "Search"

    #     for filter in self.driver.find_elements(self.globalPipelinePage.filter_elements_css[0], self.globalPipelinePage.filter_elements_css[1]):

    #         assert len(filter.text) > 0

    #     for indication in self.driver.find_elements(self.globalPipelinePage.indication_css[0], self.globalPipelinePage.indication_css[1]):

    #         assert len(indication.text) > 0
    #         assert indication.get_attribute("style") in self.globalPipelinePage.indication_tag_border_color
    #         value_of_css = indication.value_of_css_property("color")
    #         hex = Color.from_string(value_of_css).hex
    #         assert "#221f1f" == hex
        

    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.globalPipelinePage.breadcrumb_ele()

    #     assert "Home" in breadcrumb_items
    #     assert "Research & Development" in breadcrumb_items
    #     assert "Novartis Pipeline" in breadcrumb_items

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    #     assert "#656565" == self.basePage.get_css_color(self.globalPipelinePage.pipeline_last_child_breadcrumb_color_css, "color")
       
    #     breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.globalPipelinePage.breadcrumb_url()
    #     for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
    #         assert breadcumb_anchor_url in breadcumb_anchor_current_url

    #     if len(self.driver.find_elements(self.globalPipelinePage.content_elements_list_css[0], self.globalPipelinePage.content_elements_list_css[1])) == 10 and self.globalPipelinePage.pagination_txt in self.driver.page_source:

    #         assert self.globalPipelinePage.pagination_txt in self.driver.page_source

    #         page_one_url, page_zero_url = self.globalPipelinePage.pagination_front_arrow_back_arrow_validation()
    #         assert "page=1" in page_one_url
    #         assert "page=0" in page_zero_url

    #         pages = self.driver.find_elements(self.globalPipelinePage.pagination_links_css[0], self.globalPipelinePage.pagination_links_css[1])
    #         random_page_number = random.randint(2, len(pages))
    #         self.driver.execute_script("arguments[0].click()", pages[random_page_number-1])
    #         assert "page=" in self.driver.current_url

    #     else:

    #         assert self.globalPipelinePage.pagination_txt not in self.driver.page_source


    #     empty_txt = self.globalPipelinePage.check_no_result("Test")
    #     assert len(empty_txt) > 0

    #     self.basePage.press_button(self.globalPipelinePage.novartis_pipeline_css)

    #     content_title_list = self.globalPipelinePage.check_search_result("AAA")
    #     if len(content_title_list) > 0:
    #         for content_title in content_title_list:
    #             assert "AAA" in content_title
    #     else:
    #         assert self.basePage.get_element_text(self.globalPipelinePage.empty_css) > 0

    #     phase_index, phase_title_list, phase_filter_tag_list, phase_checkbox_color_list, phase_result_list, development_phase_txt, development_phase_font_weight = self.globalPipelinePage.development_phase_ele()

    #     for phase_checkbox_color in phase_checkbox_color_list:
    #         assert "#221f1f" in phase_checkbox_color

    #     assert f"Development Phase ({phase_index})" == development_phase_txt
    #     assert "75" in development_phase_font_weight

    #     for phase_title, phase_filter_tag in zip(phase_title_list, phase_filter_tag_list):
    #         assert phase_title in phase_filter_tag

    #     for phase_result in phase_result_list:
    #         assert phase_result in phase_title_list

    #     filter_tag_len = self.globalPipelinePage.clear_all_ele()
    #     assert filter_tag_len == 0

    #     filling_date_index, filling_date_title_list, filling_date_filter_tag_list, filling_date_checkbox_color_list, filling_date_txt, filling_date_font_weight, filling_date_result_list = self.globalPipelinePage.filling_date_ele()

    #     for filling_date_checkbox_color in filling_date_checkbox_color_list:
    #         assert "#221f1f" in filling_date_checkbox_color

    #     assert f"Filing Date ({filling_date_index})" == filling_date_txt
    #     assert "75" in filling_date_font_weight

    #     for filling_date_title, filling_date_filter_tag in zip(filling_date_title_list, filling_date_filter_tag_list):
    #         assert filling_date_title in filling_date_filter_tag

    #     for filling_date_result in filling_date_result_list:
    #         assert filling_date_result in filling_date_title_list

        

    #     filter_tag_len = self.globalPipelinePage.clear_all_ele()
    #     assert filter_tag_len == 0


    #     therapeutic_area_index, therapeutic_area_title_list, therapeutic_area_filter_tag_list, therapeutic_area_checkbox_color_list, therapeutic_area_result_list, therapeutic_area_txt, therapeutic_area_font_weight = self.globalPipelinePage.therapeutic_area_ele()

    #     for therapeutic_area_checkbox_color in therapeutic_area_checkbox_color_list:
    #         assert "#221f1f" in therapeutic_area_checkbox_color

    #     assert f"Therapeutic Area ({therapeutic_area_index})" == therapeutic_area_txt
    #     assert "75" in therapeutic_area_font_weight

    #     for phase_title, phase_filter_tag in zip(therapeutic_area_title_list, therapeutic_area_filter_tag_list):
    #         assert phase_title in phase_filter_tag

    #     for therapeutic_area_result in therapeutic_area_result_list:
    #         assert therapeutic_area_result in therapeutic_area_title_list

    #     filter_tag_len = self.globalPipelinePage.clear_all_ele()
    #     assert filter_tag_len == 0


    #     indication_name_index, indication_name_title_list, indication_name_filter_tag_list, indication_name_checkbox_color_list, indication_name_result_list, indication_name_txt, indication_name_font_weight = self.globalPipelinePage.indication_name_ele()

    #     for indication_name_checkbox_color, indication_name_color in zip(indication_name_checkbox_color_list, self.globalPipelinePage.indication_name_color_list):
    #         assert indication_name_checkbox_color == indication_name_color

    #     assert f"Indication Name ({indication_name_index})" == indication_name_txt
    #     assert "75" in indication_name_font_weight

    #     for indication_name_title, indication_name_filter_tag in zip(indication_name_title_list, indication_name_filter_tag_list):
    #         assert indication_name_title in indication_name_filter_tag

    #     for indication_name_result in indication_name_result_list:
    #         assert indication_name_result in indication_name_title_list
        
    #     filter_tag_len = self.globalPipelinePage.clear_all_ele()
    #     assert filter_tag_len == 0


    #     assert self.basePage.get_element_text(self.globalPipelinePage.legend_title_xpath) == "Legend"
    #     assert self.basePage.get_element_text(self.globalPipelinePage.disclaimer_title_xpath) == "Disclaimer"


    # def test_ARC_2702_FormService(self):

    #     self.driver.get(self.env + "news/stay-up-to-date")    

    #     assert "patterns" in self.basePage.get_css_property(self.subscribePage.pattern_css, "background-image")
    #     assert "Stay Up-to-Date" in self.basePage.get_element_text(self.subscribePage.subscribe_page_title_css)
    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.subscribePage.breadcrumb_ele()

    #     assert "Home" in breadcrumb_items
    #     assert "News" in breadcrumb_items
    #     assert "Stay Up To Date" in breadcrumb_items

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    #     assert "#656565" == self.basePage.get_css_color(self.globalPipelinePage.pipeline_last_child_breadcrumb_color_css, "color")

    #     assert self.basePage.get_element_text(self.subscribePage.first_name_label_xpath) == "First Name"
    #     assert self.basePage.get_element_text(self.subscribePage.last_name_label_xpath) == "Last Name"
    #     assert self.basePage.get_element_text(self.subscribePage.email_label_xpath) == "Email"
    #     assert self.basePage.get_element_text(self.subscribePage.phone_label_xpath) == "Phone"
    #     assert self.basePage.get_element_text(self.subscribePage.employer_label_xpath) == "Employer"
    #     assert self.basePage.get_element_text(self.subscribePage.occupation_label_xpath) == "Occupation"
    #     assert self.basePage.get_element_text(self.subscribePage.location_label_xpath) == "Location"
    #     assert "I agree" in self.basePage.get_element_text(self.subscribePage.agree_id)
    #     assert self.basePage.get_elemet_attribute(self.subscribePage.agree_checkbox_id, "type") == "checkbox"
    #     assert self.basePage.get_elemet_attribute(self.subscribePage.submit_btn_id, "value") == "Submit"

    #     self.subscribePage.click_subscribe()
    #     assert "true" == self.basePage.get_elemet_attribute(self.subscribePage.edit_unsubscribe_id, "disabled")
    #     assert None == self.basePage.get_elemet_attribute(self.subscribePage.publication_order_form_id, "disabled")
    #     assert self.basePage.get_element_text(self.subscribePage.lang_label_css) == "Language"
       
    #     lang_checkboxes = self.driver.find_elements(self.subscribePage.lang_checkbox_css[0], self.subscribePage.lang_checkbox_css[1])
    #     for lang_checkbox in lang_checkboxes:

    #         if "English" in lang_checkbox.find_element(self.subscribePage.label_tag_css[0], self.subscribePage.label_tag_css[1]).text:
    #             is_checked = lang_checkbox.find_element(self.subscribePage.input_tag_css[0], self.subscribePage.input_tag_css[1]).get_attribute("checked")
    #             break
    #     assert is_checked == "true"


    #     self.subscribePage.fill_mandatory_fields()
    #     self.subscribePage.agree_checkbox_ele()
    #     self.subscribePage.click_submit_btn()

    #     alert_txt = self.subscribePage.alert_danger()
    #     assert self.subscribePage.captcha_warning_txt in alert_txt

    #     self.basePage.press_button(self.subscribePage.stay_up_to_date_css)

    #     self.subscribePage.click_subscribe()
    #     self.subscribePage.fill_mandatory_fields()
    #     self.subscribePage.fill_optional_fields()
    #     self.subscribePage.agree_checkbox_ele()
    #     self.subscribePage.click_submit_btn()

    #     alert_txt = self.subscribePage.alert_danger()
    #     assert self.subscribePage.captcha_warning_txt in alert_txt

    #     self.basePage.press_button(self.subscribePage.stay_up_to_date_css)
    #     self.subscribePage.click_unsubscribe()
    #     assert "true" == self.basePage.get_elemet_attribute(self.subscribePage.edit_subscribe_id, "disabled")
    #     assert "true" == self.basePage.get_elemet_attribute(self.subscribePage.publication_order_form_id, "disabled")
        
    #     assert self.basePage.get_element_text(self.subscribePage.email_label_xpath) == "Email"
    #     assert "I agree" in self.basePage.get_element_text(self.subscribePage.agree_id)

    #     self.subscribePage.fill_mandatory_fields_unsubscribe()
    #     self.subscribePage.agree_checkbox_ele()
    #     self.subscribePage.click_submit_btn()
    #     alert_txt = self.subscribePage.alert_danger()
    #     assert self.subscribePage.captcha_warning_txt in alert_txt

    #     self.basePage.press_button(self.subscribePage.stay_up_to_date_css)

    #     self.subscribePage.click_publication_order_form()
    #     assert "Select Publication" == self.basePage.get_element_text(self.subscribePage.publication_label_css)
    #     assert "Quantity" == self.basePage.get_element_text(self.subscribePage.quantity_label_css)
    #     assert "Remove" in self.basePage.get_elemet_attribute(self.subscribePage.remove_btn_xpath, "title")
    #     assert "Add another Publication" == self.basePage.get_elemet_attribute(self.subscribePage.add_publication_btn, "value")
    #     assert "Street Address" in self.basePage.get_element_text(self.subscribePage.street_address_xpath)
    #     assert "City/Town" in self.basePage.get_element_text(self.subscribePage.city_town_xpath)
    #     assert "ZIP/Postal Code" in self.basePage.get_element_text(self.subscribePage.zip_xpath)
    #     assert "Country" in self.basePage.get_element_text(self.subscribePage.country_xpath)

    #     self.subscribePage.fill_mandatory_fields()
    #     self.subscribePage.publication_mandatory_fields()
    #     self.subscribePage.agree_checkbox_ele()
    #     self.subscribePage.click_submit_btn()
    #     alert_txt = self.subscribePage.alert_danger()
    #     assert self.subscribePage.captcha_warning_txt in alert_txt

    #     self.basePage.press_button(self.subscribePage.stay_up_to_date_css)

    #     self.basePage.element_clickable(self.subscribePage.edit_subscribe_id)
    #     self.basePage.element_clickable(self.subscribePage.edit_unsubscribe_id)
    #     self.basePage.element_clickable(self.subscribePage.publication_order_form_id)
    #     assert self.driver.find_element(self.subscribePage.location_id[0], self.subscribePage.location_id[1]).tag_name == "select"
        


################ Media Library Details Page #####################


# def test_ARC_2658_MediaLibraryDetails(self):

#         self.driver.get(self.env)
#         self.homePage.news_mega_menu(self.homePage.mega_menu_media_library_xpath,self.env_name,'media-library')


#         # #reset - negative scenario
#         # self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)
#         # reset_button = self.driver.find_elements(*self.mediaLibraryPage.reset_button)

#         # assert len(reset_button) == 0 

#         pages = 2

#         # PROTECTED IMAGE CONTENT #
#         self.basePage.press_button(self.mediaLibraryPage.media_library_breadcrumb_color_css)
#         self.basePage.press_button(self.mediaLibraryPage.image_tab_xpath)


#         for page in range(pages):

#             protected_img_index, protected_img_src_list, protected_img_btn_clickable_list, protected_img_page_label_list, protected_img_desc_page_label_list, protected_img_pop_up_window_list, protected_img_yes_btn_clickable_list, protected_img_current_page_url_list, protected_img_current_page_url_one_list, protected_img_page_url_list, protected_img_nav_current_page_url_list = self.mediaLibraryPage.protected_img()

#             for img_src, btn_clickable, pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one, protected_img_page_url, protected_img_nav_current_page_url in zip(protected_img_src_list, protected_img_btn_clickable_list, protected_img_pop_up_window_list, protected_img_yes_btn_clickable_list, protected_img_current_page_url_list, protected_img_current_page_url_one_list, protected_img_page_url_list, protected_img_nav_current_page_url_list):
#                 assert "lock" in img_src
#                 assert btn_clickable == True
#                 assert yes_btn_clickable == True
#                 assert "dialog" in pop_up_window
#                 assert current_page_url == current_page_url_one
#                 assert protected_img_page_url in protected_img_nav_current_page_url

#             for protected_img_page_label, protected_img_desc_page_label in zip(protected_img_page_label_list, protected_img_desc_page_label_list):

#                 if len(protected_img_page_label) > 0:
#                     assert len(protected_img_page_label) > 0
#                     assert len(protected_img_desc_page_label) > 0

#             if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and protected_img_index <=3:
#                 self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)


#         # UNPROTECTED IMAGE CONTENT #
#         self.basePage.press_button(self.mediaLibraryPage.media_library_breadcrumb_color_css)
#         self.basePage.press_button(self.mediaLibraryPage.image_tab_xpath)
        
#         for page in range(pages):

#             unprotected_img_index, unprotected_img_src_list, unprotected_img_btn_clickable_list, unprotected_img_page_label_list, unprotected_img_desc_page_label_list, unprotected_img_page_url_list, unprotected_img_current_page_url_list = self.mediaLibraryPage.unprotected_img()

#             for img_src, btn_clickable, unprotected_img_page_url, unprotected_img_current_page_url in zip(unprotected_img_src_list, unprotected_img_btn_clickable_list, unprotected_img_page_url_list, unprotected_img_current_page_url_list):

#                 assert len(img_src) > 0
#                 assert btn_clickable == True
#                 assert unprotected_img_page_url in unprotected_img_current_page_url


#             for unprotected_doc_page_label, unprotected_doc_desc_page_label in zip(unprotected_img_page_label_list, unprotected_img_desc_page_label_list):

#                 if len(unprotected_doc_page_label) > 0:
#                     assert len(unprotected_doc_page_label) > 0
#                     assert len(unprotected_doc_desc_page_label) > 0

#             if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and unprotected_img_index <=3:
#                 self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)

#         # PROTECTED DOCUMENT CONTENT #
#         self.basePage.press_button(self.mediaLibraryPage.media_library_breadcrumb_color_css)
#         self.basePage.press_button(self.mediaLibraryPage.doc_tab_xpath)
        
#         for page in range(pages):

#             protected_doc_index, protected_doc_img_src_list, protected_doc_btn_clickable_list, protected_doc_page_label_list, protected_doc_desc_page_label_list, protected_doc_pop_up_window_list, protected_doc_yes_btn_clickable_list, protected_doc_current_page_url_list, protected_doc_current_page_url_one_list, protected_doc_page_url_list, protected_doc_navigate_current_page_url_list = self.mediaLibraryPage.protected_doc()

#             for img_src, btn_clickable, pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one, protected_doc_page_url, protected_doc_navigate_current_page_url in zip(protected_doc_img_src_list, protected_doc_btn_clickable_list, protected_doc_pop_up_window_list, protected_doc_yes_btn_clickable_list, protected_doc_current_page_url_list, protected_doc_current_page_url_one_list, protected_doc_page_url_list, protected_doc_navigate_current_page_url_list):
#                 assert "lock" in img_src
#                 assert btn_clickable == True
#                 assert yes_btn_clickable == True
#                 assert "dialog" in pop_up_window
#                 assert current_page_url == current_page_url_one
#                 assert protected_doc_page_url in protected_doc_navigate_current_page_url

#             for protected_img_page_label, protected_img_desc_page_label in zip(protected_doc_page_label_list, protected_doc_desc_page_label_list):

#                 if len(protected_img_page_label) > 0:
#                     assert len(protected_img_page_label) > 0
#                     assert len(protected_img_desc_page_label) > 0

#             if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and protected_doc_index <=3:
#                 self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)


#         # UNPROTECTED DOCUMENT CONTENT #
#         self.basePage.press_button(self.mediaLibraryPage.media_library_breadcrumb_color_css)
#         self.basePage.press_button(self.mediaLibraryPage.doc_tab_xpath)
        
#         for page in range(pages):

#             unprotected_doc_index, unprotected_doc_btn_clickable_list, unprotected_doc_page_label_list, unprotected_doc_desc_page_label_list,unprotected_doc_page_url_list, unprotected_doc_current_page_url_list = self.mediaLibraryPage.unprotected_doc()

#             for btn_clickable, unprotected_doc_page_url, unprotected_doc_current_page_url in zip(unprotected_doc_btn_clickable_list, unprotected_doc_page_url_list, unprotected_doc_current_page_url_list):

#                 assert btn_clickable == True
#                 assert unprotected_doc_page_url in unprotected_doc_current_page_url

#             for unprotected_doc_page_label, unprotected_doc_desc_page_label in zip(unprotected_doc_page_label_list, unprotected_doc_desc_page_label_list):

#                 if len(unprotected_doc_page_label) > 0:
#                     assert len(unprotected_doc_page_label) > 0
#                     assert len(unprotected_doc_desc_page_label) > 0

#             if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and unprotected_doc_index <=3:
#                 self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)


#         # VIDEO TAB CONTENT #
#         self.basePage.press_button(self.mediaLibraryPage.media_library_breadcrumb_color_css)
#         self.basePage.press_button(self.mediaLibraryPage.video_tab_xpath)
        
#         for page in range(pages):

#             video_index, video_page_label_list, video_desc_page_label_list, video_frame_len_list, flag_list, video_page_url_list, video_current_page_url_list = self.mediaLibraryPage.video()

#             for video_frame_len, flag, video_page_url, current_page_url in zip(video_frame_len_list, flag_list, video_page_url_list, video_current_page_url_list):

#                 assert video_frame_len > 0
#                 assert flag == 1
#                 assert video_page_url in current_page_url

#             for video_page_label, video_desc_page_label in zip(video_page_label_list, video_desc_page_label_list):

#                 if len(video_page_label) > 0:
#                     assert len(video_page_label) > 0
#                     assert len(video_desc_page_label) > 0

#             if len(self.driver.find_elements(self.mediaLibraryPage.next_page_arrow_xpath[0], self.mediaLibraryPage.next_page_arrow_xpath[1])) > 0 and video_index <=3:
#                 self.basePage.press_button(self.mediaLibraryPage.next_page_arrow_xpath)

#         #related items
#         self.homePage.news_mega_menu(self.homePage.mega_menu_media_library_xpath,self.env_name,'media-library')

#         index, related_items_len, related_items_href_list ,current_page_url_list, = self.mediaLibraryPage.related_items()
            
#         count = 0
        
#         for i in range(index):

#             assert related_items_len[count] == 4
#             assert current_page_url_list[count] in related_items_href_list[count]



################## HyperlinkVerify ####################


    # @pytest.mark.migration
    # @pytest.mark.singapore
    # @pytest.mark.pakistan
    # @pytest.mark.usa
    # @pytest.mark.uk
    # @pytest.mark.eg
    # @pytest.mark.sandoz
    # @pytest.mark.de
    # @pytest.mark.at
    # @pytest.mark.ph
    # @pytest.mark.ch
    # @pytest.mark.fr
    # @pytest.mark.jp
    # @pytest.mark.za
    # @pytest.mark.it
    # @pytest.mark.es
    # @pytest.mark.nl
    # @pytest.mark.pt
    # @pytest.mark.malaysia
    # @pytest.mark.tw
    # @pytest.mark.ar
    # @pytest.mark.hk
    # @pytest.mark.kr
    # @pytest.mark.scn
    # @pytest.mark.br
    # @pytest.mark.cn
    # @pytest.mark.hu
    # @pytest.mark.ie
    # @pytest.mark.biome
    # @pytest.mark.foundation
    # @pytest.mark.gr
    # def test_ARC_2409_HyperlinkVerify(self):

    #     self.driver.get(self.env)

    #     if len(self.driver.find_elements(self.homePage.card_wrapper_css[0], self.homePage.card_wrapper_css[1])) > 0:

    #         card_link_url_list, card_link_current_url_list = self.homePage.card_links()
    #         for card_link_url, card_link_current_url in zip(card_link_url_list, card_link_current_url_list):
    #             assert card_link_url in card_link_current_url

    #     if len(self.driver.find_elements(self.homePage.link_button_css[0], self.homePage.link_button_css[1])) > 0:

    #         links_button_url_list, links_button_current_url_list = self.homePage.links_button_ele(self.env)
    #         for links_button_url, links_button_current_url in zip(links_button_url_list, links_button_current_url_list):
    #             assert links_button_url in links_button_current_url

    #     # DO NOT REMOVE THIS COMMENT. WE MAY NEED IT IN FUTURE
    #     # if len(self.driver.find_elements(self.homePage.all__news_css[0], self.homePage.all__news_css[1])) > 0:

    #     #     news_url = self.basePage.get_elemet_attribute((self.homePage.all__news_css[0], self.homePage.all__news_css[1]), "href")
    #     #     self.basePage.press_button((self.homePage.all__news_css[0], self.homePage.all__news_css[1]))
    #     #     assert news_url == self.driver.current_url
    #     #     self.driver.back()

    #     if len(self.driver.find_elements(self.homePage.banner_link_css[0], self.homePage.banner_link_css[1])) > 0:

    #         banner_url_list, banner_current_url_list = self.homePage.banner_links()
    #         for banner_url, banner_current_url in zip(banner_url_list, banner_current_url_list):
    #             if '/2021/' in banner_current_url:
    #                 banner_current_url.replace("/2021/", "/")
    #             assert banner_url in banner_current_url

    #     # for link in self.homePage.link_url_xpaths:
    #     #     if len(self.driver.find_elements(link[0], link[1])) > 0:
    #     #         link_href = self.basePage.get_elemet_attribute(link, "href")
    #     #         self.basePage.click_button(link)
    #     #         assert link_href in self.driver.current_url
    #     #         assert "Page Not Found" not in self.driver.page_source
    #     #         self.driver.back()

        