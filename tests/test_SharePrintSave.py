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
@pytest.mark.global_site
class Test_SharePrintSave(BaseTest):

    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.nl
    @pytest.mark.uk
    @pytest.mark.pt
    @pytest.mark.jp
    @pytest.mark.malaysia
    @pytest.mark.tw
    @pytest.mark.at
    @pytest.mark.it
    @pytest.mark.pakistan
    @pytest.mark.sandoz
    @pytest.mark.ph
    @pytest.mark.ar
    @pytest.mark.hk
    @pytest.mark.kr
    @pytest.mark.cn
    @pytest.mark.fi
    @pytest.mark.br
    @pytest.mark.scn
    @pytest.mark.hu
    @pytest.mark.ie
    @pytest.mark.gr
    @pytest.mark.no
    @pytest.mark.de
    @pytest.mark.dk
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
    @pytest.mark.ee
    @pytest.mark.bd
    @pytest.mark.lt
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.th 
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_job_details_misalignment(self):

        """
        Checks that share, print and save button are misaligned.
        Tha order should share - print - save.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)

        row_index, share_block, print_save_block = self.jobDetailsPage.print_share_misalignment()
        index = 0
        for row in range(row_index):
            assert "block-addtoanybuttons" in share_block[index] 
            assert "block-printablelinksblockcontent" in  print_save_block[index] 
            index += 1

    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.nl
    @pytest.mark.uk
    @pytest.mark.pt
    @pytest.mark.jp
    @pytest.mark.malaysia
    @pytest.mark.tw
    @pytest.mark.it
    @pytest.mark.at
    @pytest.mark.pakistan
    @pytest.mark.ph
    @pytest.mark.hk
    @pytest.mark.sandoz
    @pytest.mark.kr
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.fi
    @pytest.mark.scn
    @pytest.mark.ie
    @pytest.mark.hu
    @pytest.mark.gr
    @pytest.mark.de
    @pytest.mark.dk
    @pytest.mark.no
    @pytest.mark.ee
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
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.th
    @pytest.mark.lt
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_job_details_print_block_duplicate(self):

        """
        Checks for duplicate print button.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)

        row_index, print_list = self.jobDetailsPage.print_block_ele()
        index = 0
        for row  in range(row_index):
            assert print_list[index] == 1
            index += 1

    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.nl
    @pytest.mark.uk
    @pytest.mark.jp
    @pytest.mark.sandoz
    @pytest.mark.it
    @pytest.mark.malaysia
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.pakistan
    @pytest.mark.hk
    @pytest.mark.fi
    @pytest.mark.ph
    @pytest.mark.ar
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.ie
    @pytest.mark.hu
    @pytest.mark.gr
    @pytest.mark.de
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
    @pytest.mark.ee
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.th  
    @pytest.mark.lt
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_job_details_save_block_duplicate(self):

        """
        Checks for duplicate save button.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)

        row_index , save_list = self.jobDetailsPage.save_block_ele()
        index = 0
        for row in range(row_index):
            assert save_list[index] == 1
            index += 1

    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.nl
    @pytest.mark.uk
    @pytest.mark.it
    @pytest.mark.jp
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.sandoz
    @pytest.mark.at
    @pytest.mark.malaysia
    @pytest.mark.kr
    @pytest.mark.fi
    @pytest.mark.pakistan
    @pytest.mark.hk
    @pytest.mark.ph
    @pytest.mark.ar
    @pytest.mark.cn
    @pytest.mark.br
    @pytest.mark.scn
    @pytest.mark.ie
    @pytest.mark.hu
    @pytest.mark.gr
    @pytest.mark.de
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
    @pytest.mark.ee
    @pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.candean
    @pytest.mark.ua
    @pytest.mark.sa
    @pytest.mark.cl
    @pytest.mark.th
    @pytest.mark.lt
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_job_details_share_block_duplicate(self):

        """
        Checks for duplicate share button.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)

        row_index ,share_list = self.jobDetailsPage.share_block_ele()
        index = 0
        for row in range(row_index):
            assert share_list[index] == 1
            index += 1

    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.it
    @pytest.mark.es
    @pytest.mark.uk
    @pytest.mark.pt
    @pytest.mark.tw
    # @pytest.mark.jp
    @pytest.mark.at
    @pytest.mark.sandoz
    @pytest.mark.fi
    @pytest.mark.ph
    @pytest.mark.ar
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.foundation
    @pytest.mark.gr
    @pytest.mark.de
    # @pytest.mark.cz
    # @pytest.mark.no
    @pytest.mark.ca
    @pytest.mark.tr
    @pytest.mark.co
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    @pytest.mark.hu
    def test_ARC_6446_SharePrintSave_media_release_page_print_block_duplicate(self):

        """
        Checks for duplicate print button.
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

    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    # @pytest.mark.jp
    @pytest.mark.it
    @pytest.mark.uk
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.at
    @pytest.mark.ph
    @pytest.mark.kr
    @pytest.mark.sandoz
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.scn
    @pytest.mark.cn
    @pytest.mark.foundation
    @pytest.mark.gr
    @pytest.mark.de
    @pytest.mark.fi
    # @pytest.mark.cz
    @pytest.mark.ca
    @pytest.mark.tr
    @pytest.mark.co
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    @pytest.mark.hu
    def test_ARC_6446_SharePrintSave_media_release_page_save_block_duplicate(self):

        """
        Checks for duplicate save button.
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

    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.uk
    @pytest.mark.it
    @pytest.mark.fi
    # @pytest.mark.jp
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.at
    @pytest.mark.sandoz
    @pytest.mark.ph
    @pytest.mark.kr
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.foundation
    @pytest.mark.gr
    @pytest.mark.de
    # @pytest.mark.cz
    @pytest.mark.ca
    @pytest.mark.tr
    @pytest.mark.co
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    @pytest.mark.hu
    def test_ARC_6446_SharePrintSave_media_release_page_share_block_duplicate(self):

        """
        Checks for duplicate share button.
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

    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.uk
    @pytest.mark.es
    @pytest.mark.at
    # @pytest.mark.jp
    @pytest.mark.it
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.sandoz
    @pytest.mark.ph
    @pytest.mark.kr
    @pytest.mark.ar
    @pytest.mark.br
    @pytest.mark.scn
    @pytest.mark.cn
    @pytest.mark.foundation
    @pytest.mark.fi
    @pytest.mark.gr
    @pytest.mark.de
    # @pytest.mark.cz
    @pytest.mark.ca
    @pytest.mark.tr
    @pytest.mark.co
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    @pytest.mark.hu
    def test_ARC_6446_SharePrintSave_media_release_page_misalignment(self):

        """
        Checks that share, print and save button are misaligned.
        The order should be share - print - save.
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

    @pytest.mark.it
    @pytest.mark.jp
    @pytest.mark.singapore
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.ar
    @pytest.mark.sandoz
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.ie
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.de
    @pytest.mark.fi
    # @pytest.mark.no
    # @pytest.mark.cz
    # @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.sk
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_featured_news_page_print_block_duplicate(self):

        """
        Checks for duplicate print button.
        """
         
        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        print_list = self.featuredNewsPage.print_block_ele()
        for print in print_list:
            assert print == 1

    @pytest.mark.it
    @pytest.mark.jp
    @pytest.mark.singapore
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.ar
    @pytest.mark.sandoz
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.fi
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
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_featured_news_page_save_block_duplicate(self):

        """
        Checks for duplicate save button.
        """
         
        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        save_list  = self.featuredNewsPage.save_block_ele()
        for save in save_list:
            assert save == 1

    @pytest.mark.it
    @pytest.mark.jp
    @pytest.mark.singapore
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.sandoz
    @pytest.mark.ar
    @pytest.mark.fi
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
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
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_featured_news_page_share_block_duplicate(self):

        """
        Checks for duplicate share button.
        """
         
        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        share_list  = self.featuredNewsPage.share_block_ele()
        for share in share_list:
            assert share == 1

    @pytest.mark.it
    @pytest.mark.jp
    @pytest.mark.singapore
    @pytest.mark.ch
    @pytest.mark.ch_fr
    @pytest.mark.ar
    @pytest.mark.sandoz
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.fi
    @pytest.mark.biome
    @pytest.mark.foundation
    # @pytest.mark.no
    @pytest.mark.ie
    @pytest.mark.de
    # @pytest.mark.cz
    # @pytest.mark.rs
    @pytest.mark.co
    @pytest.mark.sk
    @pytest.mark.ve
    @pytest.mark.bd
    @pytest.mark.ru
    @pytest.mark.be
    @pytest.mark.au
    @pytest.mark.lv
    @pytest.mark.eg
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_featured_news_page_misalignment(self):

        """
        Checks that share, print and save button are misaligned.
        The order should be share - print - save.
        """
         
        self.driver.get(self.env)
        self.newsPage.launch_newsArchive(self.env_name)
        self.basePage.press_button(self.featuredNewsPage.featuredNews_tab_xpath)
        row_index, share_block, print_save_block = self.featuredNewsPage.print_share_misalignment()
        index = 0
        for row in range(row_index):
            assert "block-addtoanybuttons" in share_block[index] 
            assert "block-printablelinksblockcontent" in  print_save_block[index] 
            index += 1

    @pytest.mark.ch
    @pytest.mark.ch_fr
    # @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.jp
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.uk
    @pytest.mark.it
    @pytest.mark.malaysia
    @pytest.mark.pt
    @pytest.mark.at
    @pytest.mark.ph
    @pytest.mark.kr
    @pytest.mark.fi
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
    @pytest.mark.ca
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.ro
    @pytest.mark.co
    @pytest.mark.sk
    @pytest.mark.id
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.lv
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_story_details_print_block_duplicate(self):

        """
        Checks for duplicate print button.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        print_list = self.storyDetailsPage.print_block_ele()
        for print in print_list:
            assert print == 1

    @pytest.mark.ch
    @pytest.mark.ch_fr
    # @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.usa
    @pytest.mark.singapore
    @pytest.mark.es
    @pytest.mark.it
    @pytest.mark.at
    @pytest.mark.malaysia
    @pytest.mark.jp
    @pytest.mark.uk
    @pytest.mark.pt
    @pytest.mark.ph
    @pytest.mark.ar
    @pytest.mark.fi
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.no
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.de
    @pytest.mark.dk
    @pytest.mark.ca
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.ro
    @pytest.mark.co
    @pytest.mark.id
    @pytest.mark.sk
    @pytest.mark.bd
    @pytest.mark.be
    @pytest.mark.lv
    @pytest.mark.pl
    def test_ARC_6446_SharePrintSave_story_details_save_block_duplicate(self):

        """
        Checks for duplicate save button.
        """

        self.driver.get(self.env)
        self.storiesPage.launch_story_page(self.env_name)

        save_list = self.storyDetailsPage.save_block_ele()
        for save in save_list:
            assert save == 1

    
    def test_ARC_6446_SharePrintSave_biography_page_misalignment(self):

        """
        Checks that share, print and save button are misaligned.
        The order should be share - print - save.
        """

        self.driver.get(self.env)
        self.bioGraphyPage.launch_board_of_directors(self.env_name)

        share_block, print_save_block = self.bioGraphyPage.print_share_misalignment()
        
        assert "block-addtoanybuttons" in share_block 
        assert "block-printablelinksblockcontent" in  print_save_block 


    def test_ARC_6446_SharePrintSave_biography_page_print_block_duplicate(self):

        """
        Checks for duplicate print button.
        """

        self.driver.get(self.env)
        self.bioGraphyPage.launch_board_of_directors(self.env_name)

        print_block = self.bioGraphyPage.print_block_ele()
        assert print_block == 1


    def test_ARC_6446_SharePrintSave_biography_page_save_block_duplicate(self):

        """
        Checks for duplicate save button.
        """

        self.driver.get(self.env)
        self.bioGraphyPage.launch_board_of_directors(self.env_name)

        save_block = self.bioGraphyPage.save_block_ele()
        assert save_block == 1

    def test_ARC_6446_SharePrintSave_biography_page_share_block_duplicate(self):

        """
        Checks for duplicate share button.
        """

        self.driver.get(self.env)
        self.bioGraphyPage.launch_board_of_directors(self.env_name)

        share_block = self.bioGraphyPage.share_block_ele()
        assert share_block == 1


    def test_ARC_6446_SharePrintSave_diversity_inclusion_page_misalignment(self):

        """
        Checks that share, print and save button are misaligned.
        The order should be share - print - save.
        """

        self.driver.get(self.env)
        self.interiorPage.launch_novartis_commitment(self.env_name)

        share_block, print_save_block = self.interiorPage.print_share_misalignment()
        
        assert "block-addtoanybuttons" in share_block 
        assert "block-printablelinksblockcontent" in  print_save_block 

   
    def test_ARC_6446_SharePrintSave_diversity_inclusion_page_print_block_duplicate(self):

        """
        Checks for duplicate print button.
        """

        self.driver.get(self.env)
        self.interiorPage.launch_novartis_commitment(self.env_name)

        print_block = self.interiorPage.print_block_ele()
        assert print_block == 1

    
    def test_ARC_6446_SharePrintSave_diversity_inclusion_page_save_block_duplicate(self):

        """
        Checks for duplicate save button.
        """

        self.driver.get(self.env)
        self.interiorPage.launch_novartis_commitment(self.env_name)

        save_block = self.interiorPage.save_block_ele()
        assert save_block == 1

    def test_ARC_6446_SharePrintSave_diversity_inclusion_page_share_block_duplicate(self):

        """
        Checks for duplicate share button.
        """

        self.driver.get(self.env)
        self.interiorPage.launch_novartis_commitment(self.env_name)

        share_block = self.interiorPage.share_block_ele()
        assert share_block == 1

    def test_ARC_6446_SharePrintSave_strategy_page_misalignment(self):

        """
        Checks that share, print and save button are misaligned.
        The order should be share - print - save.
        """

        self.driver.get(self.env)
        self.interiorPage.launch_strategy(self.env_name)

        share_block, print_save_block = self.interiorPage.print_share_misalignment()
        
        assert "block-addtoanybuttons" in share_block 
        assert "block-printablelinksblockcontent" in  print_save_block 


    def test_ARC_6446_SharePrintSave_strategy_page_print_block_duplicate(self):

        """
        Checks for duplicate print button.
        """

        self.driver.get(self.env)
        self.interiorPage.launch_strategy(self.env_name)

        print_block = self.interiorPage.print_block_ele()
        assert print_block == 1


    def test_ARC_6446_SharePrintSave_strategy_page_save_block_duplicate(self):

        """
        Checks for duplicate save button.
        """

        self.driver.get(self.env)
        self.interiorPage.launch_strategy(self.env_name)

        save_block = self.interiorPage.save_block_ele()
        assert save_block == 1

    def test_ARC_6446_SharePrintSave_strategy_page_share_block_duplicate(self):

        """
        Checks for duplicate share button.
        """

        self.driver.get(self.env)
        self.interiorPage.launch_strategy(self.env_name)

        share_block = self.interiorPage.share_block_ele()
        assert share_block == 1




