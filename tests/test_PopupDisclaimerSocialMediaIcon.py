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
@pytest.mark.de
@pytest.mark.at
@pytest.mark.global_site
@pytest.mark.ph
@pytest.mark.ch_fr
@pytest.mark.ch
@pytest.mark.fr
@pytest.mark.fi
@pytest.mark.za
@pytest.mark.malaysia
@pytest.mark.jp
@pytest.mark.es
@pytest.mark.it
@pytest.mark.nl
@pytest.mark.lv
@pytest.mark.pt
@pytest.mark.ar
@pytest.mark.tw
@pytest.mark.campus
@pytest.mark.hk
@pytest.mark.kr
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ie
# @pytest.mark.gr
@pytest.mark.dk
@pytest.mark.no
# @pytest.mark.cz
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.ee
# @pytest.mark.rs
@pytest.mark.tr
@pytest.mark.ro
@pytest.mark.il
@pytest.mark.co
# @pytest.mark.sk
@pytest.mark.bg
@pytest.mark.ru
@pytest.mark.th
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.ve
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.pl
@pytest.mark.lt
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.be
@pytest.mark.au
@pytest.mark.sandozcn
class Test_PopupDisclaimerSocialMediaIcon(BaseTest):

     def test_ARC_2502_PopupDisclaimerSocialMediaIcon_all_icons(self):

        """
        Checks the following in external link popup
        1. pop up title
        2. pop up description
        3. continue button
        3. cancel button
        4. continue and cancel button functionality
        5. page is opening or not
        6. country name present in popup title
        """

        self.driver.get(self.env)
        page_title_start = self.driver.title

        link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list = self.homePage.external_link(self.homePage.social_media_icons_link_xpath, self.env_name)
        assert len(pop_up_title_list) > 0
        for link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title,pop_up_title_color,country_name,font_weight,font_family in zip(link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list):
            # assert "" in link_txt
            assert self.homePage.novartis_logo in pop_up_logo
            assert len(pop_up_title) > 0
            assert len(pop_up_desc) > 0
            assert len(continue_btn) > 0
            assert continue_btn_clickable == True
            assert len(cancel_btn) > 0
            assert cancel_btn_clickable == True
            assert page_title == page_title_start
            assert str(country_name.encode("UTF-8"))[1:].replace("'","") in str(pop_up_title.encode("UTF-8"))[1:].replace("'","")
      #   twitter_page_title = self.homePage.footer_popup_disclaimer(self.homePage.twitter)
      #   assert "Twitter" in twitter_page_title


   #   def test_ARC_2502_PopupDisclaimerSocialMediaIcon_linkedin(self):

   #      """
   #      Checks the following in external link popup
   #      1. pop up title
   #      2. pop up description
   #      3. continue button
   #      3. cancel button
   #      4. continue and cancel button functionality
   #      5. page is opening or not
   #      6. country name present in popup title
   #      """

   #      self.driver.get(self.env)
   #      page_title_start = self.driver.title

   #      link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title,pop_up_title_color,country_name,font_weight,font_family = self.homePage.external_link(self.homePage.linkedin, self.env_name)
   #    #   assert "" in link_txt
   #      assert self.homePage.novartis_logo in pop_up_logo
   #      assert len(pop_up_title) > 0
   #      assert len(pop_up_desc) > 0
   #      assert len(continue_btn) > 0
   #      assert continue_btn_clickable == True
   #      assert len(cancel_btn) > 0
   #      assert cancel_btn_clickable == True
   #      assert page_title == page_title_start
   #      linkedin_page_title = self.homePage.footer_popup_disclaimer(self.homePage.linkedin)
   #      assert "LinkedIn" in linkedin_page_title
   #      assert country_name in pop_up_title


   #   def test_ARC_2502_PopupDisclaimerSocialMediaIcon_youtube(self):

   #      """
   #      Checks the following in external link popup
   #      1. pop up title
   #      2. pop up description
   #      3. continue button
   #      3. cancel button
   #      4. continue and cancel button functionality
   #      5. page is opening or not
   #      6. country name present in popup title
   #      """

   #      self.driver.get(self.env)
   #      page_title_start = self.driver.title

   #      link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title,pop_up_title_color,country_name,font_weight,font_family = self.homePage.external_link(self.homePage.youtube, self.env_name)
   #    #   assert "" in link_txt
   #      assert self.homePage.novartis_logo in pop_up_logo
   #      assert len(pop_up_title) > 0
   #      assert len(pop_up_desc) > 0
   #      assert len(continue_btn) > 0
   #      assert continue_btn_clickable == True
   #      assert len(cancel_btn) > 0
   #      assert cancel_btn_clickable == True
   #      assert page_title == page_title_start 
   #      youtube_page_title = self.homePage.footer_popup_disclaimer(self.homePage.youtube)
   #      assert "YouTube" in youtube_page_title
   #      assert country_name in pop_up_title


   #   def test_ARC_2502_PopupDisclaimerSocialMediaIcon_facebook(self):

   #      """
   #      Checks the following in external link popup
   #      1. pop up title
   #      2. pop up description
   #      3. continue button
   #      3. cancel button
   #      4. continue and cancel button functionality
   #      5. page is opening or not
   #      6. country name present in popup title
   #      """

   #      self.driver.get(self.env)
   #      page_title_start = self.driver.title

   #      link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title,pop_up_title_color,country_name,font_weight,font_family = self.homePage.external_link(self.homePage.facebook, self.env_name)
   #    #   assert "" in link_txt
   #      assert self.homePage.novartis_logo in pop_up_logo
   #      assert len(pop_up_title) > 0
   #      assert len(pop_up_desc) > 0
   #      assert len(continue_btn) > 0
   #      assert continue_btn_clickable == True
   #      assert len(cancel_btn) > 0
   #      assert cancel_btn_clickable == True
   #      assert page_title == page_title_start
   #      facebook_page_title = self.homePage.footer_popup_disclaimer(self.homePage.facebook)
   #      if self.env_name == "sandoz":
   #          assert "sandoz" in facebook_page_title.lower()
   #      else :
   #         assert "novartis" in facebook_page_title.lower()
   #      assert country_name in pop_up_title


   #   def test_ARC_2502_PopupDisclaimerSocialMediaIcon_instagram(self):

   #      """
   #      Checks the following in external link popup
   #      1. pop up title
   #      2. pop up description
   #      3. continue button
   #      3. cancel button
   #      4. continue and cancel button functionality
   #      5. page is opening or not
   #      6. country name present in popup title
   #      """

   #      self.driver.get(self.env)
   #      page_title_start = self.driver.title

   #      link_txt, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_title,pop_up_title_color,country_name,font_weight,font_family = self.homePage.external_link(self.homePage.instagram, self.env_name)
   #    #   assert "" in link_txt
   #      assert self.homePage.novartis_logo in pop_up_logo
   #      assert len(pop_up_title) > 0
   #      assert len(pop_up_desc) > 0
   #      assert len(continue_btn) > 0
   #      assert continue_btn_clickable == True
   #      assert len(cancel_btn) > 0
   #      assert cancel_btn_clickable == True
   #      assert page_title == page_title_start
   #      instagram_page_title = self.homePage.footer_popup_disclaimer(self.homePage.instagram)
   #      assert "Instagram" in instagram_page_title
   #      assert country_name in pop_up_title
