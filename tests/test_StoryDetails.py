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
import random

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.migration
@pytest.mark.singapore
@pytest.mark.usa
@pytest.mark.uk
# @pytest.mark.eg
@pytest.mark.global_site
@pytest.mark.de
# @pytest.mark.ph
@pytest.mark.ch
@pytest.mark.ch_fr
# @pytest.mark.fr
@pytest.mark.malaysia
@pytest.mark.jp
@pytest.mark.za
@pytest.mark.es
@pytest.mark.pt
# @pytest.mark.it
@pytest.mark.kr
@pytest.mark.at
@pytest.mark.lv
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.fi
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ie
@pytest.mark.no
@pytest.mark.dk
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.tr
#@pytest.mark.ro
#@pytest.mark.id
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.bd
@pytest.mark.be
@pytest.mark.pl
class Test_StoryDetails(BaseTest):

    # @pytest.mark.ph
    # def test_ARC_5748_StoryDetails_get_storypage(self):

    #     self.driver.get(self.env)
    #     self.storiesPage.launch_story_page(self.env_name)

    # If banner images,hero text  are missing in overview and detail pages -No need to fail [Content issue] [PH]
    def test_ARC_5748_StoryDetails_banner_image(self):

        """
        Checks for Banner image in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        banner_img_list, banner_img_broken_list = self.storyDetailsPage.banner_img()

        for banner_img, banner_img_broken in zip(banner_img_list, banner_img_broken_list):
            assert banner_img == True
            assert len(banner_img_broken) > 0

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_pattern(self):

        """
        Checks for pattern in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        pattern_list = self.storyDetailsPage.pattern_ele()
        for pattern in pattern_list:
            assert "patterns" in pattern

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_title(self):

        """
        Checks for title in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        title_display_list, title_length_list = self.storyDetailsPage.title_ele()

        for title_display, title_length in zip(title_display_list, title_length_list):

            assert title_display == True
            assert title_length > 0

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_image(self):

        """
        Checks for image in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        img_ele_list = self.storyDetailsPage.images_ele()
        for img in img_ele_list:
            assert len(img) > 0


    # Already covered in test_breadcrumb
    # def test_ARC_5748_StoryDetails_breadcrumb_display(self):

    #     self.driver.get(self.env)
    #     self.storiesPage.launch_story_page(self.env_name)

    #     breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, content_title_list, breadcrumb_items_len_list, breadcrumb_items_list,color_list = self.storiesPage.story_details_breadcrumb_display()

    #     for breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, content_title, breadcrumb_items_len, breadcrumb_items ,color in zip(breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, content_title_list, breadcrumb_items_len_list, breadcrumb_items_list,color_list):

    #         assert ">" in breadcrumb_first_arrow_element
    #         assert ">" in breadcrumb_second_arrow_element
    #         # assert content_title in breadcrumb_items
    #         assert breadcrumb_items_len == 3
    #         assert "#656565" == color


    # Already covered in test_breadcrumb
    # def test_ARC_5748_StoryDetails_breadcrumb_navigation(self):

    #     self.driver.get(self.env)
    #     self.storiesPage.launch_story_page(self.env_name)

    #     story_contents = self.driver.find_elements(self.storyDetailsPage.story_contents_css[0], self.storyDetailsPage.story_contents_css[1])
    #     story_contents_len = len(story_contents)
    #     random_content_number = random.randint(0,story_contents_len-1)
    #     index = 0

    #     for story in story_contents:

    #         random_content_number = random.randint(0,story_contents_len-1)

    #         story_contents = self.driver.find_elements(self.storyDetailsPage.story_contents_css[0], self.storyDetailsPage.story_contents_css[1])

    #         story_contents = self.driver.find_elements(self.storyDetailsPage.story_contents_css[0], self.storyDetailsPage.story_contents_css[1])
    #         self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storyDetailsPage.anchor_tag_css[0], self.storyDetailsPage.anchor_tag_css[1]))

    #         breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.storyDetailsPage.check_all_breadcrumb_url()
    #         for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
    #             assert breadcumb_anchor_url in breadcumb_anchor_current_url

    #         index = index + 1
    #         if index == 4:
    #             break

    #         self.driver.back()

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_related_links(self):

        """
        Checks if there is no related links in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        related_links_list = self.storyDetailsPage.related_links_ele()
        for related_links in related_links_list:
            assert related_links == 0

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_twitter(self):

        """
        Clicks on random stories and checks the following :-
        1. Twitter icon
        2. Tweet text
        3. Clickable
        4. Twitter href is there in <a> tag.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        twitter_icon_list, twitter_clickable_list, twitter_txt_element_list,twitter_href_list = self.storyDetailsPage.twitter_icon()
        for twitter_icon, twitter_clickable, twitter_txt_element , twitter_href  in zip(twitter_icon_list, twitter_clickable_list, twitter_txt_element_list ,twitter_href_list):
            assert "twitter.svg" in twitter_icon
            assert "Tweet" in twitter_txt_element
            assert twitter_clickable == True
            assert len(twitter_href) > 0 

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_facebook(self):

        """
        Clicks on random stories and checks the following :-
        1. Facebook icon
        2. Share text
        3. Clickable
        4. Facebook href is there in <a> tag.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        facebook_icon_list, facebook_clickable_list, facebook_txt_element_list , facebook_href_list = self.storyDetailsPage.facebook_icon()
        for facebook_icon, facebook_clickable, facebook_txt_element , facebook_href in zip(facebook_icon_list, facebook_clickable_list, facebook_txt_element_list, facebook_href_list):
            assert "facebook.svg" in facebook_icon
            assert "Share" in facebook_txt_element
            assert facebook_clickable == True
            assert len(facebook_href) > 0


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_whatsapp(self):

        """
        Clicks on random stories and checks the following :-
        1. Whatsapp icon
        2. Clickable
        3. Whatsapp href is there in <a> tag.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        whatsapp_icon_list, whatsapp_clickable_list, whatsapp_href_list  = self.storyDetailsPage.whatsapp_icon()
        for whatsapp_icon, whatsapp_clickable, whatsapp_href in zip(whatsapp_icon_list, whatsapp_clickable_list, whatsapp_href_list):
            assert "whatsapp.svg" in whatsapp_icon
            assert whatsapp_clickable == True
            assert len(whatsapp_href) > 0

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_linkedin(self):

        """
        Clicks on random stories and checks the following :-
        1. Linkedin icon
        2. Clickable
        3. Linkedin href is there in <a> tag.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        linkedin_icon_list, linkedin_clickable_list ,  linkedIn_href_list = self.storyDetailsPage.linkedin_icon()
        for linkedin_icon, linkedin_clickable , linkedIn_href in zip(linkedin_icon_list, linkedin_clickable_list, linkedIn_href_list):
            assert "linkedin.svg" in linkedin_icon
            assert linkedin_clickable == True
            assert  len(linkedIn_href) > 0

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_email(self):

        """
        Clicks on random stories and checks the following :-
        1. Email icon
        2. Clickable
        3. Email href is there in <a> tag.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        email_icon_list, email_clickable_list, email_href_list = self.storyDetailsPage.email_icon()
        for email_icon, email_clickable , email_href in zip(email_icon_list, email_clickable_list, email_href_list):
            assert "email.svg" in email_icon
            assert email_clickable == True
            assert len(email_href) > 0


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_print(self):

        """
        Clicks on random stories and checks the following :-
        1. Print icon
        2. Print text
        3. It's navigating to correct url or not.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        print_icon_list, print_txt_list, print_href_url_list, print_current_url_list = self.storyDetailsPage.print_icon()
        for print_icon, print_txt, print_href_url, print_current_url in zip(print_icon_list, print_txt_list, print_href_url_list, print_current_url_list):
            assert "print.svg" in print_icon
            assert len(print_txt) > 0
            assert print_current_url == print_href_url


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_save(self):

        """
        Clicks on random stories and checks the following :-
        1. Save icon
        2. Print text
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        save_icon_list, save_txt_list = self.storyDetailsPage.save_icon()
        for save_icon, save_txt in zip(save_icon_list, save_txt_list):
            assert "save.svg" in save_icon
            assert len(save_txt) > 0

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_search(self):

        """
        Checks for search icon in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        search_display_list, search_len_list, search_icon_list = self.storyDetailsPage.search_ele()
        for search_display, search_len, search_icon in zip(search_display_list, search_len_list, search_icon_list):
            assert "icon-search.svg" in search_icon
            assert search_len > 0
            assert search_display == True

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_menu(self):

        """
        Checks for mega menu in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        menu_display_list, menu_len_list, menu_icon_list = self.storyDetailsPage.menu_ele()
        for menu_display, menu_len, menu_icon in zip(menu_display_list, menu_len_list, menu_icon_list):
            assert "icon-menu.svg" in menu_icon
            assert menu_len > 0
            assert menu_display == True


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_date(self):

        """
        Checks for date in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        date_display_list, date_len_list = self.storyDetailsPage.date_ele()
        for date_display, date_len in zip(date_display_list, date_len_list):
            assert date_len > 0
            assert date_display == True

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_logo(self):

        """
        Checks for logo in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        menu_display_list = self.storyDetailsPage.logo_ele()
        for menu_display in menu_display_list:
            assert menu_display == True


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_related_stories_title(self):

        """
        Checks the following :-
        1.If more than 1 story is there related stories title should be there.
        2. Else Related stories title should not be there.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        related_stories_title_display_list, related_stories_title_length_list, story_contents_len = self.storyDetailsPage.related_stories_title()
        if story_contents_len == 1:
            assert related_stories_title_length_list == 0
        else:    
            for related_stories_title_display, related_stories_title_length in zip(related_stories_title_display_list, related_stories_title_length_list):
                assert related_stories_title_display == True
                assert related_stories_title_length > 0


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_related_stories_content(self):

        """
        Checks if related storied content is there or not if there or not and if there
        are more than 4 stories available, then view all button should be there.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        related_stories_content_len_list, card_label_list, card_title_list, card_href_list, card_current_url_list, view_all_list, story_contents_len = self.storyDetailsPage.related_stories_content()
        
        if story_contents_len > 1:
            for related_stories_content_len in related_stories_content_len_list:
                assert related_stories_content_len >= 1
                assert related_stories_content_len <= 3

        if related_stories_content_len_list == 3 and story_contents_len > 4:
            assert len(view_all_list) > 0
            for view_all in view_all_list:
                assert view_all == True

        for card_label, card_title in zip(card_label_list, card_title_list):
            assert card_label == True
            assert card_title == True

        for card_href, card_current_url in zip(card_href_list, card_current_url_list):
            assert card_href == card_current_url

    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_tags(self):

        """
        Checks tags are there or not in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        if self.env_name == 'global':
            tags_list = self.storyDetailsPage.tags_ele()
            for tag in tags_list:
                assert tag > 0


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_share_block(self):

        """
        Checks that there is no share block.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        share_block_list = self.storyDetailsPage.share_block()
        for block in share_block_list :
            assert block == 0


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_print_save_block_alignment(self):

        """
        Checks that print and save buttons are not misaligned.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        print_block_list , save_block_list = self.storyDetailsPage.print_save_block_alignment()
        for print_block , save_block in zip(print_block_list , save_block_list):
            assert 'print' in print_block
            assert 'pdf' in save_block



    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_social_media_alignment(self):

        """
        Checks the social media icons are coming in the following order :-
        Twitter - Facebook - Whatsapp - Linkedin - Email
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        twitter_block_list, fshare_block_list , wattsapp_block_list, linkedIn_block_list,  email_block_list = self.storyDetailsPage.socail_media_alignment()
        for twitter_block, fshare_block , wattsapp_block, linkedIn_block,  email_block in zip(twitter_block_list, fshare_block_list , wattsapp_block_list, linkedIn_block_list,  email_block_list):
            assert 'Twitter' in twitter_block
            assert 'Facebook' in fshare_block
            assert 'Whatsapp' in wattsapp_block
            assert 'Linkedin' in linkedIn_block
            assert 'Email' in email_block


    @pytest.mark.ph
    def test_ARC_5748_StoryDetails_view_all_bold_verify(self):

        """
        Checks that View all button is bold in story details page.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        if len(self.driver.find_elements(self.storyDetailsPage.view_all_css[0], self.storyDetailsPage.view_all_css[1])) > 0:
            view_all_bold_list = self.storyDetailsPage.view_all_bold()
            for bold in view_all_bold_list:
                assert bold == '700'
