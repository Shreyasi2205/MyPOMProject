import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from BaseTest import BaseTest
from Helper import Helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException, ElementNotSelectableException
import random
from Utilities.config import Utilities
from selenium.webdriver.support.color import Color


now = datetime.now() 



# If any more library is needed import it here.

# Holds down the alt key

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.global_site
@pytest.mark.migration
@pytest.mark.singapore
@pytest.mark.pakistan
@pytest.mark.usa
@pytest.mark.uk
@pytest.mark.eg
@pytest.mark.sandoz
@pytest.mark.de
@pytest.mark.at
@pytest.mark.ph
@pytest.mark.ch
@pytest.mark.lv
@pytest.mark.ch_fr
@pytest.mark.fr
@pytest.mark.fi
@pytest.mark.jp
@pytest.mark.no
@pytest.mark.za
@pytest.mark.it
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.pt
@pytest.mark.malaysia
@pytest.mark.tw
@pytest.mark.ar
@pytest.mark.hk
@pytest.mark.kr
@pytest.mark.scn
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.hu
@pytest.mark.ie
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.gr
@pytest.mark.ee
@pytest.mark.dk
@pytest.mark.cz
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.th
@pytest.mark.tr
@pytest.mark.rs
@pytest.mark.ro
@pytest.mark.campus
@pytest.mark.il
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.bg
@pytest.mark.ve
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.pl
@pytest.mark.ru
@pytest.mark.lt
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.be
@pytest.mark.au
@pytest.mark.sandozcn
class Test_HyperlinkVerify(BaseTest):

    def test_ARC_2409_HyperlinkVerify_card_wrapper_links(self):

        """
        Check the card links are navigating to correct url or not.
        """

        self.driver.get(self.env)

        if len(self.driver.find_elements(self.homePage.card_wrapper_css[0], self.homePage.card_wrapper_css[1])) > 0:

            card_link_url_list, card_link_current_url_list = self.homePage.card_links()
            for card_link_url, card_link_current_url in zip(card_link_url_list, card_link_current_url_list):
                if '/2021/' in card_link_current_url:
                    card_link_current_url = card_link_current_url.replace("/2021/", "/")
                assert card_link_url in card_link_current_url


    def test_ARC_2409_HyperlinkVerify_link_btn_links(self):

        """
        Check the link buttons are navigating to correct url or not.
        """

        self.driver.get(self.env)
        if len(self.driver.find_elements(self.homePage.link_button_css[0], self.homePage.link_button_css[1])) > 0:

                links_button_url_list, links_button_current_url_list = self.homePage.links_button_ele(self.env)
                for links_button_url, links_button_current_url in zip(links_button_url_list, links_button_current_url_list):
                    if '/2021/' in links_button_current_url:
                        links_button_current_url = links_button_current_url.replace("/2021/", "/")
                    assert links_button_url in links_button_current_url

    def test_ARC_2409_HyperlinkVerify_banner_links(self):

        """
        Check the banner image links are navigating to correct url or not.
        """

        self.driver.get(self.env)
        if len(self.driver.find_elements(self.homePage.banner_link_css[0], self.homePage.banner_link_css[1])) > 0:

            banner_url_list, banner_current_url_list = self.homePage.banner_links()
            for banner_url, banner_current_url in zip(banner_url_list, banner_current_url_list):
                if '/2021/' in banner_current_url:
                    banner_current_url = banner_current_url.replace("/2021/", "/")
                assert banner_url in banner_current_url