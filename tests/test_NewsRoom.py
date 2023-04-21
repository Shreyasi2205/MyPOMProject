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
@pytest.mark.ph
@pytest.mark.fi
@pytest.mark.malaysia
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.fr
@pytest.mark.jp
@pytest.mark.za
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.it
@pytest.mark.lv
@pytest.mark.pt
@pytest.mark.tw
@pytest.mark.kr
@pytest.mark.hk
@pytest.mark.ar
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.ie
@pytest.mark.no
@pytest.mark.gr
@pytest.mark.dk
@pytest.mark.cz
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.tr
@pytest.mark.sa
@pytest.mark.cl
# @pytest.mark.rs
@pytest.mark.ro
@pytest.mark.il
@pytest.mark.co
@pytest.mark.ee
@pytest.mark.bg
@pytest.mark.sk
@pytest.mark.ve
@pytest.mark.th
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.ru
@pytest.mark.pl
@pytest.mark.lt
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.be
@pytest.mark.au
class Test_NewsRoom(BaseTest):

    # @pytest.mark.biome
    # @pytest.mark.foundation
    # def test_ARC_2379_NewsRoom_get_newsRoom(self):

    #     self.driver.get(self.env)
    #     self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')

    @pytest.mark.biome
    @pytest.mark.foundation
    def test_ARC_2379_NewsRoom_bannerImage(self):

        """
        Checks banner image & text is displaying.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        if self.driver.find_elements(*self.newsRoomPage.hero_img_css):
            hero_img_len, hero_txt_len = self.newsRoomPage.hero_image_text()
            assert hero_img_len > 0
            assert hero_txt_len > 0

    @pytest.mark.biome
    @pytest.mark.foundation
    def test_ARC_2379_NewsRoom_pattern(self):

        """
        Checks pattern is displaying or not.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        pattern = self.basePage.get_css_property(self.homePage.pattern_css, "background-image")
        assert len(pattern) > 0


    def test_ARC_2379_NewsRoom_stripes(self):

        """
        Checks stripes are displaying or not.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        stripe_list = self.newsRoomPage.stripe_ele()

        for stripe in stripe_list:
            assert "stripe" in stripe


    def test_ARC_2379_NewsRoom_cards(self):

        """
        Checks cards are displaying or not.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        global twitter
        cards,twitter = self.newsRoomPage.stripe_card_val(self.newsRoomPage.card_image_css,self.newsRoomPage.card_title_css,self.newsRoomPage.card_desc_css)
        for card in cards:
            assert card > 0

    def test_ARC_2379_NewsRoom_twitter(self):

        """
        Checks the following for twitter card :-

        1. Twitter Text in Blue & Heading in Black [Both Clickable]

        2. Twitter Icon - Black, clickable

        3. When Clicked - Pop-up Disclaimer is displayed with Message

        4. twitter Caroussel is displayed [Upto max 5] 

        5. If No Twitter or Card - Should not display Blank Card
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        if self.driver.find_elements(self.newsRoomPage.tweeter_id[0], self.newsRoomPage.tweeter_id[1]):
            assert self.basePage.get_css_color(self.newsRoomPage.tweeter_css,'color') == "#035697"
            assert True == self.basePage.is_displayed(self.newsRoomPage.twitter_icon_css)
            assert True == self.basePage.is_displayed(self.newsRoomPage.twitter_time_css)
            assert self.basePage.get_css_color(self.newsRoomPage.twitter_time_css,'color') == "#221f1f"
            assert True == self.basePage.element_clickable(self.newsRoomPage.twitter_icon_css)
            assert len(self.driver.find_elements(*self.newsRoomPage.carousel_items_css)) <= 5
            self.basePage.press_button(self.newsRoomPage.twitter_icon_css)
            assert  len(self.basePage.get_elemet_attribute(self.newsRoomPage.pop_up_logo_css, "src")) > 0
            assert len(self.basePage.get_element_text(self.newsRoomPage.pop_up_title_css)) > 0
            assert len(self.basePage.get_element_text(self.newsRoomPage.pop_up_body_css)) > 0
            assert len(self.basePage.get_element_text(self.newsRoomPage.continue_button_css)) > 0
            assert True == self.basePage.element_clickable(self.newsRoomPage.continue_button_css)
            assert len(self.basePage.get_element_text(self.newsRoomPage.cancel_button_css)) > 0
            assert True == self.basePage.element_clickable(self.newsRoomPage.cancel_button_css)
            self.basePage.press_button(self.newsRoomPage.cancel_button_css)

    def test_ARC_2379_NewsRoom_mediaRelease(self):

        """
        Checks media release cards are displaying or not.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        global displayed_status
        displayed_status, len_media_card ,len_media_label= self.newsRoomPage.media_release_label()

        if displayed_status == True:

            assert len_media_card == len_media_label


    def test_ARC_2379_NewsRoom_mediaRelease_date(self):

        """
        Checks date is displaying in desc order in media release card.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        displayed_status = False
        displayed_status, len_media_card ,len_media_label= self.newsRoomPage.media_release_label()
        if displayed_status == True:
            desc_sort = self.newsRoomPage.media_date_val(self.env_name)
            assert desc_sort == True

    @pytest.mark.biome
    @pytest.mark.foundation
    def test_ARC_2379_NewsRoom_linkButtons(self):

        """
        Checks link buttons are working as expected.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        if len(self.driver.find_elements(*self.newsRoomPage.link_button_css)) > 0:
        
            links_button_url_list, links_button_current_url_list, links_button_ext_url_list, links_button_ext_current_url_list = self.newsRoomPage.links_button()
            assert links_button_url_list == links_button_current_url_list
            if len(links_button_ext_url_list) > 0:
                assert len(links_button_ext_current_url_list) > 0

    @pytest.mark.biome
    @pytest.mark.foundation
    def test_ARC_2379_NewsRoom_media_stripe_images(self):

        """
        Checks stripe images are displaying.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')
        if len(self.driver.find_elements(*self.newsRoomPage.media_stripe_img_css)) > 0:
            assert self.newsRoomPage.stripe_img() == True

    @pytest.mark.biome
    @pytest.mark.foundation
    def test_ARC_2379_NewsRoom_footer_search_box_color(self):

        """
        Checks footer search box color is matching with pattern color.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')

        if 'carmine' in self.basePage.get_css_property(self.newsRoomPage.pattern_css, 'background-image'):
            assert "#8d1f1b" == self.basePage.get_css_color(self.newsRoomPage.footer_search_xpath, 'background-color')
        elif 'blue' in self.basePage.get_css_property(self.newsRoomPage.pattern_css, 'background-image'):
            assert "#0460a9" == self.basePage.get_css_color(self.newsRoomPage.footer_search_xpath, 'background-color')
        elif 'apricot' in self.basePage.get_css_property(self.newsRoomPage.pattern_css, 'background-image'):
            assert "#ec9a1e" == self.basePage.get_css_color(self.newsRoomPage.footer_search_xpath, 'background-color')
        elif 'siena' in self.basePage.get_css_property(self.newsRoomPage.pattern_css, 'background-image'):
            assert "#e74a21" == self.basePage.get_css_color(self.newsRoomPage.footer_search_xpath, 'background-color')
            
    @pytest.mark.biome
    @pytest.mark.foundation
    def test_ARC_2379_NewsRoom_hero_text_box(self):

        """
        Checks hero text box color is matching with pattern color.
        """

        self.driver.get(self.env)
        self.homePage.mega_menu_landing_page(self.env_name,self.homePage.mega_menu_news_xpath,'news')

        if 'carmine' in self.basePage.get_css_property(self.newsRoomPage.pattern_css, 'background-image'):
            assert "#8d1f1b" == self.basePage.get_css_color(self.newsRoomPage.hero_box_css, 'background-color')
        elif 'blue' in self.basePage.get_css_property(self.newsRoomPage.pattern_css, 'background-image'):
            assert "#0460a9" == self.basePage.get_css_color(self.newsRoomPage.hero_box_css, 'background-color')
        elif 'apricot' in self.basePage.get_css_property(self.newsRoomPage.pattern_css, 'background-image'):
            assert "#ec9a1e" == self.basePage.get_css_color(self.newsRoomPage.hero_box_css, 'background-color')
        elif 'siena' in self.basePage.get_css_property(self.newsRoomPage.pattern_css, 'background-image'):
            assert "#e74a21" == self.basePage.get_css_color(self.newsRoomPage.hero_box_css, 'background-color')





