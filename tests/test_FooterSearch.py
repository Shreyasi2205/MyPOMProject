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
@pytest.mark.it
@pytest.mark.global_site
@pytest.mark.at
@pytest.mark.ph
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.fr
@pytest.mark.malaysia
@pytest.mark.za
@pytest.mark.jp
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.lv
@pytest.mark.pt
@pytest.mark.tw
@pytest.mark.hk
@pytest.mark.kr
@pytest.mark.fi
@pytest.mark.campus
@pytest.mark.ar
@pytest.mark.cn
@pytest.mark.br
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ie
@pytest.mark.no
@pytest.mark.gr
@pytest.mark.dk
@pytest.mark.cz
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.tr
@pytest.mark.rs
@pytest.mark.ee
@pytest.mark.ro
@pytest.mark.il
@pytest.mark.co
@pytest.mark.ru
@pytest.mark.sk
@pytest.mark.bg
@pytest.mark.ve
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.pl
@pytest.mark.lt
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.th
@pytest.mark.be
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.au
@pytest.mark.sandozcn
class Test_FooterSearch(BaseTest):


    def test_ARC_2479_FooterSearch_searchIcon(self):

        """
        Checks the search icon in the footer search.
        """

        self.driver.get(self.env) 
        search_icon_element = self.searchPage.footer_search_icon()

        assert "icon-search" in search_icon_element

    def test_ARC_2479_FooterSearch_searchPlaceholder(self):

        """
        Checks placeholder text in footer search input field.
        """

        self.driver.get(self.env) 
        assert len(self.basePage.get_elemet_attribute(self.searchPage.search_input_footer_id, "placeholder")) > 0

    def test_ARC_2479_FooterSearch_searchValue(self):

        """
        Checks Footer search input field value is empty by default.
        """

        self.driver.get(self.env) 
        assert len(self.basePage.get_elemet_attribute(self.searchPage.search_input_footer_id, "value")) == 0


    def test_ARC_2479_FooterSearch_searchText(self):

        """
        Whatever text we are searching, It checks that the same text is there in the input field
        and also in the current url after pressing on the search button.
        """

        global page_title, search_txt, search_txt_url 
        self.driver.get(self.env) 
        page_title = self.driver.title
        search_txt, search_txt_url = self.homePage.search_txt_footer(self.homePage.search_keyword, self.searchPage.search_result_xpath)

        assert self.homePage.search_keyword in search_txt
        assert self.homePage.search_keyword in search_txt_url


    def test_ARC_2479_FooterSearch_globalSearch_status(self):

        """
        Checks global search is there or not after the input field.
        """

        self.driver.get(self.env)
        self.basePage.press_button(self.homePage.search_button_footer_css)
        global_search_status = self.homePage.global_search_display_status()
        assert global_search_status == True
        

    
    def test_ARC_2479_FooterSearch_globalSearch_options(self):

        """
        Checks the global search dropdown and clear all button.
        """

        self.driver.get(self.env)
        self.basePage.press_button(self.homePage.search_button_footer_css)
        self.searchPage.cookie_handler()
        self.searchPage.click_global_search()
        global_search_window_list, clear_all = self.searchPage.verify_global_search_window()
        for global_search_window in global_search_window_list:
            assert global_search_window == True
        assert clear_all == True 


    def test_ARC_2479_FooterSearch_filter_global_search(self):

        """
        Check the number we are clicking from the global search dropdown, the same number
        is coming or not after global search text.
        """

        self.driver.get(self.env)
        self.basePage.press_button(self.homePage.search_button_footer_css)
        len_selected_filter, global_search_after_select= self.searchPage.select_filter_global_search()
        assert str(len_selected_filter) in global_search_after_select


    def test_ARC_2479_FooterSearch_verify_clearAll(self):

        """
        Checks clear all button is working or not.
        """

        self.driver.get(self.env)
        self.basePage.press_button(self.homePage.search_button_footer_css)
        self.searchPage.select_filter_global_search()
        global_search_without_number, global_search_text, clear_all_status  = self.searchPage.clear_all()
        assert global_search_without_number == global_search_text
        for status in clear_all_status:
            assert status == False


    def test_ARC_2479_FooterSearch_verify_closeOption(self):

        """
        Checks that after clicking on the close search, It's navigating to the previous page.
        """

        self.driver.get(self.env)
        page_title = str(self.driver.title.encode("utf-8"))[1:].replace("'", "")
        self.basePage.press_button(self.homePage.search_button_footer_css)
        home_page_url = self.searchPage.close_search()
        assert page_title == str(self.driver.title.encode("utf-8"))[1:].replace("'", "")
