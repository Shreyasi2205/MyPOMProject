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
# @pytest.mark.eg
@pytest.mark.global_site
class Test_Breadcrumb(BaseTest):

    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.pakistan
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.nl
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.it
    @pytest.mark.jp
    @pytest.mark.malaysia
    @pytest.mark.ar
    @pytest.mark.hk
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.sandoz
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.hu
    @pytest.mark.ie
    @pytest.mark.gr
    @pytest.mark.de
    @pytest.mark.fi
    @pytest.mark.dk
    @pytest.mark.no
    @pytest.mark.ca
    @pytest.mark.cz
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.ro
    @pytest.mark.il
    @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.sk
    @pytest.mark.bg
    @pytest.mark.ve
    @pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.lt
    @pytest.mark.ee
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.th
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_5852_Breadcrumb_careerSearch_display(self):

        """
        Function -- Breadcrumb is available or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)

        breadcrumb_items_status, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.careerSearchPage.breadcrumb_ele()
        assert len(breadcrumb_items_status) == 3
        for breadcrumb in breadcrumb_items_status:
            breadcrumb == True

        assert ">" in breadcrumb_first_arrow_element
        assert ">" in breadcrumb_second_arrow_element
        assert "#656565" == self.basePage.get_css_color(self.careerSearchPage.career_last_child_breadcrumb_color_css, "color")

    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.pakistan
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.nl
    @pytest.mark.pt
    @pytest.mark.jp
    @pytest.mark.tw
    @pytest.mark.it
    @pytest.mark.malaysia
    @pytest.mark.ar
    @pytest.mark.kr
    @pytest.mark.hk
    @pytest.mark.br
    @pytest.mark.sandoz
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.hu
    @pytest.mark.ie
    @pytest.mark.gr
    @pytest.mark.de
    @pytest.mark.fi
    @pytest.mark.dk
    @pytest.mark.no
    @pytest.mark.cz
    @pytest.mark.ca
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.ro
    @pytest.mark.il
    @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.sk
    @pytest.mark.bg
    @pytest.mark.ve
    @pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.lt
    @pytest.mark.be
    @pytest.mark.ee
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.th
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_5852_Breadcrumb_careerSearch_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        
        breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.careerSearchPage.check_all_breadcrumb_url()
        for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
            assert breadcumb_anchor_current_url in breadcumb_anchor_url


    def test_ARC_5852_Breadcrumb_pipeline_display(self):

        """
        Function -- Breadcrumb is available or not.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()

        breadcrumb_items_status, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.globalPipelinePage.breadcrumb_ele()
        assert len(breadcrumb_items_status) == 3
        for breadcrumb in breadcrumb_items_status:
            breadcrumb == True

        assert ">" in breadcrumb_first_arrow_element
        assert ">" in breadcrumb_second_arrow_element
        assert "#656565" == self.basePage.get_css_color(self.globalPipelinePage.pipeline_last_child_breadcrumb_color_css, "color")


    def test_ARC_5852_Breadcrumb_pipeline_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()

        breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.globalPipelinePage.breadcrumb_url()
        for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
            assert breadcumb_anchor_current_url in breadcumb_anchor_url

    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.jp
    @pytest.mark.fi
    # @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.malaysia
    @pytest.mark.pt
    @pytest.mark.kr
    @pytest.mark.it
    @pytest.mark.ca
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.de
    @pytest.mark.no
    @pytest.mark.dk
    @pytest.mark.se
    @pytest.mark.tr
    #@pytest.mark.ro
    @pytest.mark.co
    @pytest.mark.sk
    #@pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.lv
    @pytest.mark.pl
    def test_ARC_5852_Breadcrumb_story_details_page_display(self):

        """
        Function -- Breadcrumb is available or not.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, content_title_list, breadcrumb_items_len_list, breadcrumb_items_list,color_list = self.storiesPage.story_details_breadcrumb_display()

        for breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, content_title, breadcrumb_items_len, breadcrumb_items ,color_list in zip(breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, content_title_list, breadcrumb_items_len_list, breadcrumb_items_list,color_list):

            assert ">" in breadcrumb_first_arrow_element
            assert ">" in breadcrumb_second_arrow_element
            assert breadcrumb_items_len == 3
            assert "#656565" == color_list
           

    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.ch
    @pytest.mark.ch_fr
    # @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.jp
    @pytest.mark.ca
    @pytest.mark.usa
    @pytest.mark.kr
    @pytest.mark.malaysia
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.pt
    @pytest.mark.it
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.fi
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.de
    @pytest.mark.dk
    @pytest.mark.no
    @pytest.mark.se
    @pytest.mark.tr
    #@pytest.mark.ro
    @pytest.mark.co
    @pytest.mark.sk
    #@pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.lv
    @pytest.mark.pl
    def test_ARC_5852_Breadcrumb_story_details_page_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])

            story_contents = self.driver.find_elements(self.storiesPage.story_contents_css[0], self.storiesPage.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.storiesPage.anchor_tag_css[0], self.storiesPage.anchor_tag_css[1]))

            breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.storiesPage.check_all_breadcrumb_url()
            for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
                assert breadcumb_anchor_current_url in breadcumb_anchor_url

            index = index + 1
            if index == 4:
                break

            self.driver.back()

    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.tw
    @pytest.mark.jp
    @pytest.mark.sandoz
    @pytest.mark.it
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.fi
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.de
    # @pytest.mark.no
    # @pytest.mark.cz
    # @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.ru
    @pytest.mark.sk
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.eg
    @pytest.mark.lv
    @pytest.mark.pl
    def test_ARC_5852_Breadcrumb_featured_news_page_display(self):

        """
        Function -- Breadcrumb is available or not.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)

        self.basePage.press_button(self.newsPage.featured_news_tab_xpath)

        breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list, breadcrumb_items_list, color_list = self.newsPage.featured_news_details_breadcrumb_display()

        for breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_items_len, breadcrumb_items,color_list in zip(breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list, breadcrumb_items_list,color_list):

            assert ">" in breadcrumb_first_arrow_element
            assert ">" in breadcrumb_second_arrow_element
            assert breadcrumb_items_len == 3
            assert "#656565" == color_list
            
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.jp
    @pytest.mark.singapore
    @pytest.mark.tw
    @pytest.mark.it
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.sandoz
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.fi
    @pytest.mark.hu
    @pytest.mark.ie
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.de
    # @pytest.mark.no
    # @pytest.mark.cz
    # @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.sk
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.be
    @pytest.mark.eg
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.pl
    def test_ARC_5852_Breadcrumb_featured_news_page_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.newsPage.featured_news_tab_xpath)

        featured_news_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])
        featured_news_contents_len = len(featured_news_contents)
        random_content_number = random.randint(0,featured_news_contents_len-1)
        index = 0

        for featured_news in featured_news_contents:

            random_content_number = random.randint(0,featured_news_contents_len-1)

            featured_news_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])

            featured_news_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])
            self.driver.execute_script("arguments[0].click()", featured_news_contents[random_content_number])

            

            breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.newsPage.check_all_breadcrumb_url()
            for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
                assert breadcumb_anchor_current_url in breadcumb_anchor_url

            index = index + 1
            if index == 4:
                break

            self.driver.back()

    # @pytest.mark.uk
    # @pytest.mark.at
    # @pytest.mark.migration
    # @pytest.mark.ph
    # @pytest.mark.ch
    # @pytest.mark.ch_fr
    # @pytest.mark.fr
    # @pytest.mark.fi
    # @pytest.mark.za
    # @pytest.mark.usa
    # @pytest.mark.singapore
    # @pytest.mark.es
    # @pytest.mark.pt
    # @pytest.mark.jp
    # @pytest.mark.tw
    # @pytest.mark.malaysia
    # @pytest.mark.it
    # @pytest.mark.sandoz
    # @pytest.mark.ar
    # @pytest.mark.kr
    # @pytest.mark.cn
    # @pytest.mark.br
    # @pytest.mark.scn
    # @pytest.mark.hu
    # @pytest.mark.biome
    # @pytest.mark.foundation
    # @pytest.mark.ca
    # @pytest.mark.ie
    # @pytest.mark.gr
    # @pytest.mark.de
    # @pytest.mark.dk
    # @pytest.mark.no
    # @pytest.mark.cz
    # @pytest.mark.ru
    # @pytest.mark.se
    # @pytest.mark.tr
    # @pytest.mark.ro
    # @pytest.mark.rs
    # @pytest.mark.co
    # @pytest.mark.sk
    # @pytest.mark.ve
    # @pytest.mark.id
    # @pytest.mark.bd
    # @pytest.mark.lv
    # def test_ARC_5852_Breadcrumb_news_page_display(self):

    #     """
    #     Function -- Breadcrumb is available or not.
    #     """

    #     self.driver.get(self.env)
    #     if self.env_name == "france":
    #        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
    #        self.basePage.press_button(self.newsRoomPage.link_btn_css)
    #     else:
    #        self.newsPage.launch_newsArchive(self.env_name)

    #     breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list, breadcrumb_items_list, color_list = self.newsPage.news_details_breadcrumb_display()

    #     for breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_items_len, breadcrumb_items ,color in zip(breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list, breadcrumb_items_list, color_list):

    #         assert ">" in breadcrumb_first_arrow_element
    #         assert ">" in breadcrumb_second_arrow_element
    #         assert breadcrumb_items_len == 3
    #         assert "#656565" == color

    # @pytest.mark.uk
    # @pytest.mark.at
    # @pytest.mark.migration
    # @pytest.mark.ph
    # @pytest.mark.ch
    # @pytest.mark.ch_fr
    # @pytest.mark.fr
    # @pytest.mark.za
    # @pytest.mark.usa
    # @pytest.mark.singapore
    # @pytest.mark.jp
    # @pytest.mark.es
    # @pytest.mark.pt
    # @pytest.mark.malaysia
    # @pytest.mark.sandoz
    # @pytest.mark.tw
    # @pytest.mark.it
    # @pytest.mark.ar
    # @pytest.mark.kr
    # @pytest.mark.scn
    # @pytest.mark.br
    # @pytest.mark.cn
    # @pytest.mark.ca
    # @pytest.mark.fi
    # @pytest.mark.hu
    # @pytest.mark.ie
    # @pytest.mark.biome
    # @pytest.mark.foundation
    # @pytest.mark.gr
    # @pytest.mark.de
    # @pytest.mark.dk
    # @pytest.mark.no
    # @pytest.mark.cz
    # @pytest.mark.ru
    # @pytest.mark.se
    # @pytest.mark.tr
    # @pytest.mark.ro
    # @pytest.mark.rs
    # @pytest.mark.co
    # @pytest.mark.sk
    # @pytest.mark.ve
    # @pytest.mark.id
    # @pytest.mark.bd
    # @pytest.mark.lv
    # def test_ARC_5852_Breadcrumb_news_page_navigation(self):

    #     """
    #     Breadcrumb is navigating to the correct page or not.
    #     """

    #     self.driver.get(self.env)
    #     if self.env_name == "france":
    #        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
    #        self.basePage.press_button(self.newsRoomPage.link_btn_css)
    #     else:
    #        self.newsPage.launch_newsArchive(self.env_name)

    #     news_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])
    #     news_contents_len = len(news_contents)
    #     random_content_number = random.randint(0,news_contents_len-1)
    #     index = 0

    #     for news in news_contents:

    #         random_content_number = random.randint(0,news_contents_len-1)

    #         news_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])

    #         news_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])
    #         self.driver.execute_script("arguments[0].click()", news_contents[random_content_number])

    #         if self.driver.find_elements(By.CSS_SELECTOR, ".ui-dialog-buttonset"):
    #             self.basePage.press_button((By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(2)"))
    #         else:
    #             breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.newsPage.check_all_breadcrumb_url()
    #             for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
    #                 assert breadcumb_anchor_current_url in breadcumb_anchor_url
                    
    #             self.driver.back()

    #         index = index + 1
    #         if index == 4:
    #             break

            

    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.ph
    # @pytest.mark.jp
    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.it
    @pytest.mark.sandoz
    @pytest.mark.ar
    @pytest.mark.kr
    @pytest.mark.fi
    @pytest.mark.br
    # @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.foundation
    @pytest.mark.gr
    @pytest.mark.de
    # @pytest.mark.cz
    @pytest.mark.ru
    @pytest.mark.ca
    @pytest.mark.tr
    @pytest.mark.co
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    @pytest.mark.hu
    def test_ARC_5852_Breadcrumb_media_release_page_display(self):

        """
        Function -- Breadcrumb is available or not.1
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)

        if self.driver.find_elements(self.newsPage.media_release_css[0], self.newsPage.media_release_css[1]):
            self.basePage.press_button(self.newsPage.media_release_css)
        elif self.driver.find_elements(self.newsPage.media_release_secondary_xpath[0], self.newsPage.media_release_secondary_xpath[1]):
            self.basePage.press_button(self.newsPage.media_release_secondary_xpath)

        breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list , color_list = self.newsPage.media_release_details_breadcrumb_display()

        for breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_items_len, color in zip(breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list,color_list):

            assert ">" in breadcrumb_first_arrow_element
            assert ">" in breadcrumb_second_arrow_element
            assert breadcrumb_items_len == 3 or breadcrumb_items_len == 4
            assert "#656565" == color

    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.it
    # @pytest.mark.jp
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.fi
    @pytest.mark.ar
    @pytest.mark.sandoz
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.scn
    @pytest.mark.foundation
    # @pytest.mark.cn
    @pytest.mark.gr
    @pytest.mark.de
    @pytest.mark.ca
    @pytest.mark.ru
    # @pytest.mark.cz
    @pytest.mark.eg
    @pytest.mark.tr
    @pytest.mark.co
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.pl
    @pytest.mark.hu
    def test_ARC_5852_Breadcrumb_media_release_page_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)
        
        if self.driver.find_elements(self.newsPage.media_release_css[0], self.newsPage.media_release_css[1]):
            self.basePage.press_button(self.newsPage.media_release_css)
        elif self.driver.find_elements(self.newsPage.media_release_secondary_xpath[0], self.newsPage.media_release_secondary_xpath[1]):
            self.basePage.press_button(self.newsPage.media_release_secondary_xpath)

        media_release_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])
        media_release_contents_len = len(media_release_contents)
        random_content_number = random.randint(0,media_release_contents_len-1)
        index = 0

        for media_release in media_release_contents:

            random_content_number = random.randint(0,media_release_contents_len-1)

            media_release_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])

            media_release_contents = self.driver.find_elements(self.newsPage.news_contents_css[0], self.newsPage.news_contents_css[1])
            self.driver.execute_script("arguments[0].click()", media_release_contents[random_content_number])

            breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.newsPage.check_all_breadcrumb_url()
            for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
                assert breadcumb_anchor_current_url in breadcumb_anchor_url

            index = index + 1
            if index == 4:
                break

            self.driver.back()

    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.pakistan
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.jp
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.malaysia
    @pytest.mark.nl
    @pytest.mark.it
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.fi
    @pytest.mark.ar
    @pytest.mark.sandoz
    @pytest.mark.hk
    @pytest.mark.kr
    @pytest.mark.cn
    @pytest.mark.br
    @pytest.mark.scn
    @pytest.mark.ie
    @pytest.mark.ca
    @pytest.mark.hu
    @pytest.mark.gr
    @pytest.mark.de
    @pytest.mark.dk
    @pytest.mark.no
    @pytest.mark.cz
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.ro
    @pytest.mark.il
    @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.ru
    @pytest.mark.sk
    @pytest.mark.bg
    @pytest.mark.ve
    @pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.lt
    @pytest.mark.be
    @pytest.mark.ee
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.eg
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.th
    @pytest.mark.pl
    def test_ARC_5852_Breadcrumb_jobDetails_page_display(self):

        """
        Function -- Breadcrumb is available or not.
        """


        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)

        row_index ,breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_third_arrow_element, breadcrumb_fourthLevel_color=self.jobDetailsPage.breadcrumb_elements()
        index = 0
        for row in range(row_index):
            
            assert breadcrumb_items[index] == 4 or breadcrumb_items[index] == 3
            assert "#656565" == breadcrumb_fourthLevel_color[index]

            assert ">" in breadcrumb_first_arrow_element[index]
            assert ">" in breadcrumb_second_arrow_element[index]
            assert ">" in breadcrumb_third_arrow_element[index]

            index += 1

    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.pakistan
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.it
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.nl
    @pytest.mark.ca
    @pytest.mark.malaysia
    @pytest.mark.jp
    @pytest.mark.sandoz
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.hk
    @pytest.mark.ar
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.ie
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.no
    @pytest.mark.eg
    @pytest.mark.hu
    @pytest.mark.fi
    @pytest.mark.ru
    @pytest.mark.gr
    @pytest.mark.de
    @pytest.mark.dk
    @pytest.mark.cz
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.ro
    @pytest.mark.il
    @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.sk
    @pytest.mark.bg
    @pytest.mark.ve
    @pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.lt
    @pytest.mark.be
    @pytest.mark.ee
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.th
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.pl
    def test_ARC_5852_Breadcrumb_jobDetails_page_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        # self.driver.get(self.env)
        # self.jobDetailsPage.launch_jobDetails(self.env_name)
        # row_index,home_url, home_current_url, careers_url, careers_current_url, careers_search_url, careers_current_search_url = self.jobDetailsPage.breadcrumbs_firstLevel_secondLevel_thirdLevel()
        # index = 0
        # for row in range(row_index):
            
        #     assert home_current_url[index] in  home_url[index]
        #     assert careers_current_url[index] in careers_url[index]
        #     assert careers_current_search_url[index] in careers_search_url[index]

        #     index += 1

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)

        if self.driver.find_elements(*self.jobDetailsPage.clear_all_css):
            self.basePage.press_button(self.jobDetailsPage.clear_all_css)

        job_contents = self.driver.find_elements(*self.jobDetailsPage.total_row_css)
        job_contents_len = len(job_contents)
        random_content_number = random.randint(0,job_contents_len-1)
        index = 0

        for job in job_contents:

            random_content_number = random.randint(0,job_contents_len-1)

            job_contents = self.driver.find_elements(*self.jobDetailsPage.total_row_css)

            # job_contents = self.driver.find_elements(self.jobDetailsPage.total_row_css)
            self.driver.execute_script("arguments[0].click()", job_contents[random_content_number].find_element(self.jobDetailsPage.anchor_tag_css[0], self.jobDetailsPage.anchor_tag_css[1]))

            breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.jobDetailsPage.check_all_breadcrumb_url()
            for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
                assert breadcumb_anchor_current_url in breadcumb_anchor_url

            index = index + 1
            if index == 4:
                break

            self.driver.back()

    def test_ARC_5852_Breadcrumb_subscribe_page_display(self):

        """
        Function -- Breadcrumb is available or not.
        """

        self.driver.get(self.env)
        self.subscribePage.launch_subscribePage(self.env_name)
        breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.subscribePage.breadcrumb_ele()

        assert len(breadcrumb_items) == 3
        assert ">" in breadcrumb_first_arrow_element
        assert ">" in breadcrumb_second_arrow_element

        assert "#656565" == self.basePage.get_css_color(self.subscribePage.subscribe_last_child_breadcrumb_color_css, "color")


    def test_ARC_5852_Breadcrumb_subscribe_page_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        self.driver.get(self.env)
        self.subscribePage.launch_subscribePage(self.env_name)
        breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.subscribePage.check_all_breadcrumb_url()
        for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
            assert breadcumb_anchor_current_url in breadcumb_anchor_url


    def test_ARC_5852_Breadcrumb_biography_page_display(self):

        """
        Function -- Breadcrumb is available or not.
        """

        self.driver.get(self.env)
        self.bioGraphyPage.launch_board_of_directors(self.env_name)
        breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.bioGraphyPage.breadcrumb_ele()

        assert len(breadcrumb_items) == 3
        assert ">" in breadcrumb_first_arrow_element
        assert ">" in breadcrumb_second_arrow_element

        assert "#656565" == self.basePage.get_css_color(self.bioGraphyPage.boardOfDirectors_last_child_breadcrumb_color_css, "color")

    def test_ARC_5852_Breadcrumb_biography_page_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """


        self.driver.get(self.env)
        self.bioGraphyPage.launch_board_of_directors(self.env_name)
        breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.bioGraphyPage.check_all_breadcrumb_url()
        for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
            assert breadcumb_anchor_current_url in breadcumb_anchor_url


    def test_ARC_5852_Breadcrumb_biographyDetail_page_display(self):

        """
        Function -- Breadcrumb is available or not.
        """

        self.driver.get(self.env)
        self.bioGraphyPage.launch_board_of_directors(self.env_name)
        row_index ,breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_third_arrow_element, breadcrumb_fourthLevel_color=self.bioGraphyPage.detailPage_breadcrumb_ele()
        index = 0
        for row in range(row_index):
            
            assert breadcrumb_items[index] == 4
            assert "#656565" == breadcrumb_fourthLevel_color[index]

            assert ">" in breadcrumb_first_arrow_element[index]
            assert ">" in breadcrumb_second_arrow_element[index]
            assert ">" in breadcrumb_third_arrow_element[index]

            index += 1

    def test_ARC_5852_Breadcrumb_biographyDetail_page_navigation(self):

        """
        Breadcrumb is navigating to the correct page or not.
        """

        self.driver.get(self.env)
        self.bioGraphyPage.launch_board_of_directors(self.env_name)
        index ,home_url, home_current_url, boardOfDirectors_url, boardOfDirectors_current_url, boardOfDirectors_search_url, boardOfDirectors_current_search_url= self.bioGraphyPage.breadcrumbs_firstLevel_secondLevel_thirdLevel()
        index = 0
        for row in range(index):
            
            assert home_current_url[index] ==  home_url[index]
            assert boardOfDirectors_current_url[index] ==  boardOfDirectors_url[index]
            assert boardOfDirectors_current_search_url[index] ==  boardOfDirectors_search_url[index]

            index += 1





            