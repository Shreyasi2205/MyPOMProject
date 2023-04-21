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
@pytest.mark.migration
@pytest.mark.singapore
@pytest.mark.pakistan
@pytest.mark.usa
@pytest.mark.uk
@pytest.mark.eg
@pytest.mark.sandoz
@pytest.mark.it
@pytest.mark.de
@pytest.mark.at
@pytest.mark.lv
@pytest.mark.jp
@pytest.mark.global_site
@pytest.mark.malaysia
@pytest.mark.ph
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.ru
@pytest.mark.fr
@pytest.mark.no
@pytest.mark.za
@pytest.mark.fi
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.pt
@pytest.mark.tw
@pytest.mark.th
@pytest.mark.kr
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.ar
@pytest.mark.hk
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ie
# @pytest.mark.gr
@pytest.mark.dk
# @pytest.mark.cz
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.tr
# @pytest.mark.rs
@pytest.mark.ro
@pytest.mark.il
@pytest.mark.co
# @pytest.mark.sk
@pytest.mark.bg
@pytest.mark.ve
@pytest.mark.campus
@pytest.mark.id
@pytest.mark.ee
@pytest.mark.bd
@pytest.mark.pl
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.lt
@pytest.mark.be
@pytest.mark.au
@pytest.mark.sandozcn
class Test_ExternalLinkHeader(BaseTest):

    def test_ARC_2412_ExternalLinkHeader_sandoz(self):

        """
        Checks the following in external link popup
        1. novartis logo
        2. pop up title
        3. pop up description
        4. continue button
        5. cancel button
        6. continue and cancel button functionality
        7. font weight, font family and font color of popup title
        8. country name present in popup title
        """

        self.driver.get(self.env)
        page_title_start = self.driver.title
        
        if self.env_name == "global":
            link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list = self.homePage.external_link(self.homePage.sandoz_css, self.env_name)
            assert len(pop_up_title_list) > 0
            for link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title,pop_up_title_color,country_name,font_weight,font_family in zip(link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list):
                assert len(link_txt) > 0
                assert self.homePage.novartis_logo in pop_up_logo
                assert self.homePage.external_popup_title in pop_up_title
                assert self.homePage.external_popup_desc in pop_up_desc
                assert len(continue_btn) > 0
                assert continue_btn_clickable == True
                assert len(cancel_btn) > 0
                assert cancel_btn_clickable == True
                assert page_title == page_title_start
                assert font_weight >= '700'
                assert pop_up_title_color == "#1a1a1a"
                assert "volta_modern_display75_bold" in font_family
                assert country_name in pop_up_title

            


    def test_ARC_2412_ExternalLinkHeader_advanced_accelerator_applications(self):

        """
        Checks the following in external link popup
        1. novartis logo
        2. pop up title
        3. pop up description
        4. continue button
        5. cancel button
        6. continue and cancel button functionality
        7. font weight, font family and font color of popup title
        8. country name present in popup title
        """

        self.driver.get(self.env)
        page_title_start = self.driver.title

        if self.env_name == "global":

            link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list = self.homePage.external_link(self.homePage.advanced_accelerator_applications_xpath, self.env_name)
            assert len(pop_up_title_list) > 0
            for link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title,pop_up_title_color,country_name,font_weight,font_family in zip(link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list):
                assert len(link_txt) > 0
                assert self.homePage.novartis_logo in pop_up_logo
                assert self.homePage.external_popup_title in pop_up_title
                assert self.homePage.external_popup_desc in pop_up_desc
                assert len(continue_btn) > 0
                assert continue_btn_clickable == True
                assert len(cancel_btn) > 0
                assert cancel_btn_clickable == True
                assert page_title == page_title_start
                assert font_weight >= '700'
                assert pop_up_title_color == "#1a1a1a"
                assert "volta_modern_display75_bold" in font_family
                assert country_name in pop_up_title

                


    def test_ARC_2412_ExternalLinkHeader_all_icons(self):

        """
        Checks the following in external link popup
        1. novartis logo
        2. pop up title
        3. pop up description
        4. continue button
        5. cancel button
        6. continue and cancel button functionality
        7. font weight, font family and font color of popup title
        8. country name present in popup title
        """

        self.driver.get(self.env)
        page_title_start = self.driver.title

        link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list = self.homePage.external_link(self.homePage.social_media_icons_link_xpath, self.env_name)
        assert len(pop_up_title_list) > 0
        for link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title,pop_up_title_color,country_name,font_weight,font_family in zip(link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list):
            assert "" in link_txt
            assert len(pop_up_logo) > 0
            assert len(pop_up_title) > 0
            assert len(pop_up_desc) > 0
            assert len(continue_btn) > 0
            assert continue_btn_clickable == True
            assert len(cancel_btn) > 0
            assert cancel_btn_clickable == True
            assert page_title == page_title_start
            assert font_weight >= '700'
            assert pop_up_title_color == "#1a1a1a"
            assert "volta_modern_display75_bold" in font_family
            assert str(country_name.encode("UTF-8"))[1:].replace("'","") in str(pop_up_title.encode("UTF-8"))[1:].replace("'","")
        


    # def test_ARC_2412_ExternalLinkHeader_linkedin(self):

    #     """
    #     Checks the following in external link popup
    #     1. novartis logo
    #     2. pop up title
    #     3. pop up description
    #     4. continue button
    #     5. cancel button
    #     6. continue and cancel button functionality
    #     7. font weight, font family and font color of popup title
    #     8. country name present in popup title
    #     """

    #     self.driver.get(self.env)
    #     page_title_start = self.driver.title

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title, pop_up_title_color,country_name,font_weight,font_family  = self.homePage.external_link(self.homePage.linkedin,self.env_name)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start
    #     assert font_weight >= '700'
    #     assert pop_up_title_color == "#1a1a1a"
    #     assert "volta_modern_display75_bold" in font_family
    #     assert country_name in pop_up_title


    # def test_ARC_2412_ExternalLinkHeader_youTube(self):

    #     """
    #     Checks the following in external link popup
    #     1. novartis logo
    #     2. pop up title
    #     3. pop up description
    #     4. continue button
    #     5. cancel button
    #     6. continue and cancel button functionality
    #     7. font weight, font family and font color of popup title
    #     8. country name present in popup title
    #     """

    #     self.driver.get(self.env)
    #     page_title_start = self.driver.title

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title ,pop_up_title_color,country_name,font_weight,font_family = self.homePage.external_link(self.homePage.youtube,self.env_name)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start
    #     assert font_weight >= '700'
    #     assert pop_up_title_color == "#1a1a1a"
    #     assert "volta_modern_display75_bold" in font_family
    #     assert country_name in pop_up_title


    # def test_ARC_2412_ExternalLinkHeader_faceBook(self):

    #     """
    #     Checks the following in external link popup
    #     1. novartis logo
    #     2. pop up title
    #     3. pop up description
    #     4. continue button
    #     5. cancel button
    #     6. continue and cancel button functionality
    #     7. font weight, font family and font color of popup title
    #     8. country name present in popup title
    #     """

    #     self.driver.get(self.env)
    #     page_title_start = self.driver.title

    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title ,pop_up_title_color,country_name,font_weight,font_family = self.homePage.external_link(self.homePage.facebook,self.env_name)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start
    #     assert font_weight >= '700'
    #     assert pop_up_title_color == "#1a1a1a"
    #     assert "volta_modern_display75_bold" in font_family
    #     assert country_name in pop_up_title

    # def test_ARC_2412_ExternalLinkHeader_instagram(self):

    #     """
    #     Checks the following in external link popup
    #     1. novartis logo
    #     2. pop up title
    #     3. pop up description
    #     4. continue button
    #     5. cancel button
    #     6. continue and cancel button functionality
    #     7. font weight, font family and font color of popup title
    #     8. country name present in popup title
    #     """

    #     self.driver.get(self.env)
    #     page_title_start = self.driver.title


    #     link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title ,pop_up_title_color,country_name,font_weight,font_family = self.homePage.external_link(self.homePage.instagram,self.env_name)
    #     assert "" in link_txt
    #     assert len(pop_up_logo) > 0
    #     assert len(pop_up_title) > 0
    #     assert len(pop_up_desc) > 0
    #     assert len(continue_btn) > 0
    #     assert continue_btn_clickable == True
    #     assert len(cancel_btn) > 0
    #     assert cancel_btn_clickable == True
    #     assert page_title == page_title_start
    #     assert font_weight >= '700'
    #     assert pop_up_title_color == "#1a1a1a"
    #     assert "volta_modern_display75_bold" in font_family
    #     assert country_name in pop_up_title

