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
@pytest.mark.th
@pytest.mark.sandoz
@pytest.mark.de
@pytest.mark.global_site
@pytest.mark.at
@pytest.mark.ph
@pytest.mark.malaysia
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.fr
@pytest.mark.za
@pytest.mark.lv
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.jp
@pytest.mark.pt
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.tw
@pytest.mark.it
@pytest.mark.ar
@pytest.mark.hk
@pytest.mark.fi
@pytest.mark.kr
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ie
@pytest.mark.gr
@pytest.mark.dk
@pytest.mark.no
@pytest.mark.cz
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.tr
@pytest.mark.rs
@pytest.mark.ee
@pytest.mark.ro
@pytest.mark.il
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.campus
@pytest.mark.bg
@pytest.mark.ve
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.ru
@pytest.mark.pl
@pytest.mark.lt
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.be
@pytest.mark.au
@pytest.mark.sandozcn
class Test_HeaderSearch(BaseTest):


    def test_ARC_2493_HeaderSearch_url_validation(self):

        """
        Checks the passing env and the current url is same or not.
        """

        
        self.driver.get(self.env)
        currentUrl = self.driver.current_url
        assert self.env == currentUrl

    def test_ARC_2493_HeaderSearch_searchbar(self):

        """
        Checks search bar has "#221f1f" color border and search box is there.
        """

        # global page_title
        self.driver.get(self.env)
        # page_title = self.driver.title
        self.homePage.click_search_icon()
        hex_code, search = self.homePage.verify_search_window()
        assert "#221f1f" in hex_code
        assert len(search) > 0
       
    def test_ARC_2493_HeaderSearch_searchIcon(self):

        """
        Checks search icon is there.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()

        search_icon = self.homePage.search_icon()
        assert "icon-search.svg" in search_icon

    def test_ARC_2493_HeaderSearch_global_search_display_status(self):

        """
        Checks global search is displayed.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()

        global_search_status = self.homePage.global_search_display_status()
        assert global_search_status == True

    def test_ARC_2493_HeaderSearch_verify_search(self):

        """
        Checks searched keyword is coming in the search box and in the url after clicking on the search button.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()

        search_txt, search_txt_url = self.homePage.search_text(self.homePage.search_keyword, self.searchPage.search_result_xpath)
        assert self.homePage.search_keyword in search_txt
        assert self.homePage.search_keyword in search_txt_url


    def test_ARC_2493_HeaderSearch_verify_globalSearch(self):

        """
        Checks for elements under global search dropdown and clear all button.
        """

        self.driver.get(self.env)        
        self.searchPage.cookie_handler()
        self.homePage.click_search_icon()
        self.searchPage.click_global_search()

        global_search_window_list, clear_all = self.searchPage.verify_global_search_window()
        for global_search_window in global_search_window_list:
            assert global_search_window == True
        assert clear_all == True


    def test_ARC_2493_HeaderSearch_filter_global_search(self):

        """
        Checks the number of element selected in the dropdown, are coming after global search text.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()

        len_selected_filter, global_search_after_select= self.searchPage.select_filter_global_search()
        assert str(len_selected_filter) in global_search_after_select


    def test_ARC_2493_HeaderSearch_verify_clearAll(self):

        """
        Checks clear all button is working as expected.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()
        self.basePage.press_button(self.searchPage.search_button_xpath)
        global_search_without_number, global_search_text, clear_all_status  = self.searchPage.clear_all()
        assert global_search_without_number == global_search_text
        for status in clear_all_status:
            assert status == False

    
    def test_ARC_2493_HeaderSearch_verify_closeOption(self):

        """
        Checks close option is navigating to previous button.
        """

        self.driver.get(self.env)
        page_title = str(self.driver.title.encode("utf-8"))[1:].replace("'", "")
        self.homePage.click_search_icon()
        self.basePage.press_button(self.searchPage.search_button_xpath)

        home_page_url = self.searchPage.close_search()
        assert page_title == str(self.driver.title.encode("utf-8"))[1:].replace("'", "")
        
    def test_ARC_2493_HeaderSearch_tags(self):

        """
        Checks tags are getting filtered out correctly.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()
        self.basePage.press_button(self.homePage.search_button_id)

        self.searchPage.cookie_handler()
        assert self.basePage.is_displayed(self.searchPage.tags_css) == True
        tag_txt_before, tag_txt_after, tags_number_list, tag_filter_list, tag_filter_set = self.searchPage.tags_ele()
        for tag_filter in tag_filter_set:
            assert tag_filter in tag_filter_list
        tag_counter = 1
        for tag_number in tags_number_list:
            assert str(tag_counter) in tag_number
            tag_counter = tag_counter + 1
        # assert tags_bold_font_family == "VoltaModernDisplay-75, arial"
        assert tag_txt_before == tag_txt_after

    def test_ARC_2493_HeaderSearch_auto_suggestion(self):

        """
        Checks auto sugg is working.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()
        auto_suggestion_list = self.searchPage.auto_suggestion("nov")
        for auto_sugg in auto_suggestion_list:
            assert "nov" in auto_sugg.lower()

    def test_ARC_2493_HeaderSearch_get_result(self):

        """
        Checks 3 letter keyword search is working or not.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()
        content_len, result_txt_display = self.searchPage.get_result(self.searchPage.search_values)
        assert result_txt_display == True
        assert content_len > 0

    def test_ARC_2493_HeaderSearch_all_grey(self):

        """
        Checks all is getting greyed out or not by default.
        """
        self.driver.get(self.env)
        self.homePage.click_search_icon()
        self.basePage.press_button(self.searchPage.search_button_xpath)
        assert "#f1f1f1" == self.basePage.get_css_color(self.searchPage.all_css, "background-color")

    def test_ARC_2493_HeaderSearch_tabs_grey(self):

        """
        Checks tabs are grtting greyed out or not.
        """
        self.driver.get(self.env)
        self.homePage.click_search_icon()
        self.basePage.press_button(self.searchPage.search_button_xpath)

        grey_bg_list = self.searchPage.tabs_grey_bg()
        for grey_bg in grey_bg_list:
            assert "#f1f1f1" == grey_bg

    def test_ARC_2493_HeaderSearch_text_present_inputfield_tab_change(self):

        """
        Checks searched text is there in the search field while changing the tabs.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()
        text_list = self.searchPage.text_display_inputfield_tab_change("nov")
        for txt in text_list:
            assert "nov" in txt

    def test_ARC_2493_HeaderSearch_default_results(self):

        """
        Checks that jobs are not coming in 1-4 pages.
        """

        self.driver.get(self.env)
        self.homePage.click_search_icon()
        self.basePage.press_button(self.homePage.search_button_id)

        search_url_list = self.searchPage.search_results()
        for search_url in search_url_list:
            assert "/careers/career-search/" not in search_url





    # def test_ARC_2493_HeaderSearch_relevance(self):

    # self.driver.get(self.env)
    # self.homePage.click_search_icon()
    # self.basePage.press_button(self.homePage.search_button_id)

    # assert self.driver.find_elements(*self.searchPage.relevance_css)[1].is_displayed() == True

    # self.driver.execute_script("arguments[0].click()", self.driver.find_elements(*self.searchPage.relevance_css)[1])

    # relevance_dropdown = self.driver.find_elements(By.XPATH, "//ul[contains(@class, 'select-options')]")[1]
    # relevance_dropdown_options = relevance_dropdown.find_elements(By.XPATH, "//li[contains(@rel, 'created')]")

    # index = 0
    # for relevance_dropdown_option in relevance_dropdown_options:
    #     self.driver.execute_script("arguments[0].click()", self.driver.find_elements(*self.searchPage.relevance_css)[1])
    #     relevance_dropdown = self.driver.find_elements(By.XPATH, "//ul[contains(@class, 'select-options')]")[1]
    #     relevance_dropdown_options = relevance_dropdown.find_elements(By.XPATH, "//li[contains(@rel, 'created')]")
    #     self.driver.execute_script("arguments[0].click()", relevance_dropdown_options[index])
    #     index = index + 1
    #     if index == 2:
    #         break