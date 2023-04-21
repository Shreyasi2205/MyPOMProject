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
@pytest.mark.sandoz
@pytest.mark.eg
@pytest.mark.global_site
@pytest.mark.de
@pytest.mark.at
@pytest.mark.it
@pytest.mark.ph
# @pytest.mark.ch
# @pytest.mark.ch_fr
# @pytest.mark.malaysia
@pytest.mark.kr
@pytest.mark.fr
@pytest.mark.lv
@pytest.mark.za
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.pt
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.jp
@pytest.mark.tw
@pytest.mark.hk
@pytest.mark.fi
@pytest.mark.ar
@pytest.mark.br
@pytest.mark.no
@pytest.mark.cn
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.ie
@pytest.mark.gr
@pytest.mark.dk
@pytest.mark.cz
@pytest.mark.ca
@pytest.mark.ru
@pytest.mark.se
@pytest.mark.tr
@pytest.mark.rs
@pytest.mark.th
@pytest.mark.ro
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.il
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.bg
@pytest.mark.ve
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.pl
@pytest.mark.lt
@pytest.mark.be
@pytest.mark.ee
@pytest.mark.au
class Test_CareerLandingPage(BaseTest):

    @pytest.mark.malaysia
    def test_ARC_2673_CareerLandingPage_get_careerLandingPage(self):

        """
        Opens the career landing page
        """

        self.driver.get(self.env)
        self.careerLandingPage.launch_careerLandingPage(self.env_name)

    @pytest.mark.malaysia
    def test_ARC_2673_CareerLandingPage_hero_banner(self):

        """
        Checks the hero banner image and hero text is displayed or not
        """

        self.driver.get(self.env)
        self.careerLandingPage.launch_careerLandingPage(self.env_name)
        hero_img_display_status, hero_txt_display_status = self.careerLandingPage.hero_ele()
        assert hero_img_display_status == True
        assert hero_txt_display_status == True

    @pytest.mark.malaysia
    def test_ARC_2673_CareerLandingPage_stripes(self):

        """
        Checks Stripes are available or not
        """

        self.driver.get(self.env)
        self.careerLandingPage.launch_careerLandingPage(self.env_name)

        if self.driver.find_elements(self.careerLandingPage.careers_txt_css[0], self.careerLandingPage.careers_txt_css[1]):
            assert self.basePage.is_displayed(self.careerLandingPage.careers_txt_css) == True

        stripe_list = self.careerLandingPage.stripe_ele()

        for stripe in stripe_list:
            assert "stripe" in stripe

    def test_ARC_2673_CareerLandingPage_search_input_field(self):

        """
        Checks input field and placeholder inside input field is available or not
        """

        self.driver.get(self.env)
        self.careerLandingPage.launch_careerLandingPage(self.env_name)
        assert len(self.basePage.get_elemet_attribute(self.careerLandingPage.search_input_field_xpath, "placeholder")) > 0
        assert self.basePage.is_displayed(self.careerLandingPage.search_input_field_xpath) == True

    def test_ARC_2673_CareerLandingPage_search_btn(self):

        """
        Checks Search Button is availble or not
        """

        self.driver.get(self.env)
        self.careerLandingPage.launch_careerLandingPage(self.env_name)
        assert len(self.basePage.get_elemet_attribute(self.careerLandingPage.search_btn_xpath, "value")) > 0
        assert self.basePage.is_displayed(self.careerLandingPage.search_btn_xpath) == True

    def test_ARC_2673_CareerLandingPage_function_filter(self):

        """
        Checks function filter is availble or not
        """

        self.driver.get(self.env)
        self.careerLandingPage.launch_careerLandingPage(self.env_name)
        assert self.basePage.is_displayed(self.careerLandingPage.function_txt_css) == True

    def test_ARC_2673_CareerLandingPage_location_filter(self):

        """
        Checks location filter is available or not and It's working or not
        """

        self.driver.get(self.env)
        self.careerLandingPage.launch_careerLandingPage(self.env_name)
        assert self.basePage.is_displayed(self.careerLandingPage.location_txt_css) == True
        filtered_elements_list, filterd_attributes_list = self.careerLandingPage.filter_location()
        for filtered_attr, filtered_ele in zip(filterd_attributes_list,filtered_elements_list):
            assert filtered_attr in filtered_ele
    
    def test_ARC_2673_CareerLandingPage_career_label(self):

        """
        Checks if "Career" Label is displayed or not(Optional)
        """

        self.driver.get(self.env)
        self.careerLandingPage.launch_careerLandingPage(self.env_name)
        if self.driver.find_elements(self.careerLandingPage.careers_txt_css[0], self.careerLandingPage.careers_txt_css[1]):
            assert self.basePage.is_displayed(self.careerLandingPage.careers_txt_css) == True




