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
class Test_Images(BaseTest):

    @pytest.mark.migration
    @pytest.mark.ph
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
    @pytest.mark.pakistan
    @pytest.mark.uk
    @pytest.mark.fi
    @pytest.mark.at
    @pytest.mark.jp
    @pytest.mark.malaysia
    @pytest.mark.it
    @pytest.mark.hk
    @pytest.mark.ar
    @pytest.mark.br
    # @pytest.mark.eg
    @pytest.mark.sandoz
    @pytest.mark.kr
    # @pytest.mark.de
    @pytest.mark.lv
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.hu
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.gr
    @pytest.mark.de
    @pytest.mark.dk
    @pytest.mark.no
    @pytest.mark.cz
    @pytest.mark.se
    @pytest.mark.tr
    # @pytest.mark.rs
    @pytest.mark.ro
    @pytest.mark.il
    @pytest.mark.ru
    @pytest.mark.co
    @pytest.mark.campus
    @pytest.mark.sk
    @pytest.mark.bg
    @pytest.mark.ve
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.ee
    @pytest.mark.pl
    @pytest.mark.lt
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.th
    @pytest.mark.be
    @pytest.mark.au
    def test_ARC_4293_Images_homePage(self):

        """
        checks the following things for the images in homepage -
        1. src is there in <img> tag
        2. title is there in <img> tag
        3. alt is there in <img> tag
        2. image is not broken
        """

        self.driver.get(self.env)
        display_list , alt_list, title_list, natural_width_list= self.homePage.images_validation()
        images_len = len(self.driver.find_elements(*self.homePage.images_css))
        for display_src, alt, title, natural_width in zip(display_list, alt_list, title_list,natural_width_list):
            assert len(display_src) > 0
            assert  len(alt) > 0
            assert len(title) > 0
            assert natural_width  != 0

    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.ch
    @pytest.mark.ch_fr
    # @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.singapore
    @pytest.mark.it
    @pytest.mark.es
    @pytest.mark.pt
    @pytest.mark.usa
    @pytest.mark.malaysia
    @pytest.mark.uk
    @pytest.mark.at
    @pytest.mark.jp
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    # @pytest.mark.eg
    @pytest.mark.fi
    @pytest.mark.de
    @pytest.mark.kr
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.lv
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
    @pytest.mark.pl
    def test_ARC_4293_Images_storyPage(self):

        """
        checks the following things for the images in story details page -
        1. src is there in <img> tag
        2. title is there in <img> tag
        3. alt is there in <img> tag
        2. image is not broken
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)
        display_list , alt_list, title_list, natural_width_list= self.storiesPage.stories_images_validation()
        for display_src, alt, title, natural_width in zip(display_list, alt_list, title_list,natural_width_list):
            assert len(display_src) > 0
            assert  len(alt) > 0
            assert len(title) > 0
            assert natural_width  != 0

    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.singapore
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.usa
    @pytest.mark.es
    @pytest.mark.it
    @pytest.mark.uk
    @pytest.mark.fi
    @pytest.mark.jp
    @pytest.mark.at
    @pytest.mark.ar
    # @pytest.mark.eg
    @pytest.mark.cn
    @pytest.mark.sandoz
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.ru
    @pytest.mark.scn
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.de
    @pytest.mark.tr
    # @pytest.mark.cz
    @pytest.mark.co
    @pytest.mark.ve
    @pytest.mark.lv
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.pl
    @pytest.mark.hu
    def test_ARC_4293_Images_mediaReleasePage(self):

        """
        checks the following things for the images in media release details page -
        1. src is there in <img> tag
        2. title is there in <img> tag
        3. alt is there in <img> tag
        2. image is not broken
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name)   
        display_list , alt_list, title_list, natural_width_list= self.mediaReleasePage.mediaRelease_images_validation()
        for display_src, alt, title, natural_width in zip(display_list, alt_list, title_list,natural_width_list):
            assert len(display_src) > 0
            assert  len(alt) > 0
            assert len(title) > 0
            assert natural_width  != 0
    

    @pytest.mark.migration
    @pytest.mark.za
    @pytest.mark.singapore
    @pytest.mark.usa
    @pytest.mark.tw
    # @pytest.mark.uk
    @pytest.mark.uk
    @pytest.mark.jp
    @pytest.mark.it
    # @pytest.mark.eg
    @pytest.mark.sandoz
    @pytest.mark.de
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.ar
    @pytest.mark.cn
    @pytest.mark.br
    @pytest.mark.hu
    @pytest.mark.ie
    @pytest.mark.fi
    # @pytest.mark.no
    @pytest.mark.biome
    @pytest.mark.lv
    @pytest.mark.foundation
    # @pytest.mark.cz
    # @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.ru
    @pytest.mark.sk
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.pl
    def test_ARC_4293_Images_featuredNewsPage(self):

        """
        checks the following things for the images in featured news details page -
        1. src is there in <img> tag
        2. title is there in <img> tag
        3. alt is there in <img> tag
        2. image is not broken
        """

        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)    
        display_list , alt_list, title_list, natural_width_list= self.featuredNewsPage.featuredNews_images_validation()
        for display_src, alt, title, natural_width in zip(display_list, alt_list, title_list,natural_width_list):
            assert len(display_src) > 0
            assert  len(alt) > 0
            assert len(title) > 0
            assert natural_width  != 0

    @pytest.mark.foundation
    def test_ARC_4293_Images_mediaLibraryPage(self):

        """
        checks the following things for the images in media library details page -
        1. src is there in <img> tag
        2. title is there in <img> tag
        3. alt is there in <img> tag
        2. image is not broken
        """

        self.driver.get(self.env)
        self.mediaLibraryPage.launch_mediaLibrary(self.env_name)
        display_list , alt_list, title_list, natural_width_list= self.mediaLibraryPage.mediaLibrary_images_validation()
        assert len(alt_list) > 0
        assert len(title_list) > 0
        for display_src, alt, title, natural_width in zip(display_list, alt_list, title_list,natural_width_list):
            assert len(display_src) > 0
            assert  len(alt) > 0
            assert len(title) > 0
            assert natural_width  != 0


    @pytest.mark.migration
    @pytest.mark.ph
    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.singapore
    @pytest.mark.pt
    @pytest.mark.usa
    @pytest.mark.es
    @pytest.mark.tw
    # @pytest.mark.uk
    @pytest.mark.uk
    @pytest.mark.jp
    @pytest.mark.it
    @pytest.mark.fi
    @pytest.mark.at
    @pytest.mark.malaysia
    @pytest.mark.lv
    @pytest.mark.ar
    # @pytest.mark.eg
    @pytest.mark.sandoz
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.cn
    # @pytest.mark.no
    @pytest.mark.scn
    @pytest.mark.hu
    @pytest.mark.de
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.dk
    # @pytest.mark.se
    @pytest.mark.tr
    # @pytest.mark.cz
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
    def test_ARC_4293_Images_newsArchivePage(self):

        """
        checks the following things for the images in news archive details page -
        1. src is there in <img> tag
        2. title is there in <img> tag
        3. alt is there in <img> tag
        2. image is not broken
        """

        self.driver.get(self.env)
        if self.env_name == "france":
           self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
           self.basePage.press_button(self.newsRoomPage.link_btn_css)
        else:
           self.newsPage.launch_newsArchive(self.env_name) 
        display_list , alt_list, title_list, natural_width_list, href_images= self.newsPage.newsArchive_images_validation()
        for image,alt  in zip(href_images, alt_list) :
            if len(alt) == 0 :
                print(image)
            
        for display_src, alt, title, natural_width in zip(display_list, alt_list, title_list,natural_width_list):
            assert len(display_src) > 0
            assert  len(alt) > 0
            assert len(title) > 0
            assert natural_width  != 0


    @pytest.mark.migration
    @pytest.mark.ph
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
    @pytest.mark.pakistan
    @pytest.mark.uk
    @pytest.mark.fi
    @pytest.mark.at
    @pytest.mark.jp
    @pytest.mark.malaysia
    @pytest.mark.it
    @pytest.mark.hk
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.th
    # @pytest.mark.eg
    @pytest.mark.sandoz
    @pytest.mark.kr
    # @pytest.mark.de
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.hu
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.gr
    @pytest.mark.lv
    @pytest.mark.de
    @pytest.mark.dk
    @pytest.mark.no
    @pytest.mark.cz
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.rs
    @pytest.mark.ro
    @pytest.mark.il
    @pytest.mark.ru
    @pytest.mark.co
    @pytest.mark.campus
    @pytest.mark.ee
    @pytest.mark.sk
    @pytest.mark.bg
    @pytest.mark.ve
    @pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.pl
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.pl
    def test_ARC_4293_Images_bannerImage(self):

        """
        checks the following things for the banner image in homepage -
        1. src is there in <img> tag
        2. title is there in <img> tag
        3. alt is there in <img> tag
        2. image is not broken
        """

        self.driver.get(self.env)
        display_list , alt_list, title_list, natural_width_list= self.homePage.banner_image_validation()
        assert len(display_list) > 0
        for display_src, alt, title, natural_width in zip(display_list, alt_list, title_list,natural_width_list):
            assert len(display_src) > 0
            assert  len(alt) > 0
            assert len(title) > 0
            assert natural_width  != 0


    