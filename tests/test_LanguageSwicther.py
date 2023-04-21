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
class Test_LanguageSwitcher(BaseTest):

    def test_ARC_5858_Language_switcher_click_langswitcher(self):

        """
        Opens the language switcher.
        """

        self.driver.get(self.env)
        self.basePage.press_button(self.homePage.lang_selector_css)

    def test_ARC_5858_Language_switcher_choose_location_displayed(self):

        """
        Checks the country name is displayed or not.
        """

        assert self.basePage.is_displayed(self.homePage.lang_selector_css) == True

    def test_ARC_5858_Language_switcher_country_displayed(self):

        """
        Checks all the regions are displayed or not.
        """

        assert self.basePage.is_displayed(self.homePage.country_name_css) == True

    def test_ARC_5858_Language_switcher_blue_color(self):

        """
        Checks the current country name is in blue color.
        """

        blue_color_list = self.homePage.verify_language_selector_color()

        for blue in blue_color_list:
            assert "#0460a9" == blue

    def test_ARC_5858_Language_switcher_url_check(self):

        """
        Checks the country url is correct or not.
        """

        url_list, country_code_list = self.homePage.check_url()
        print(country_code_list)
        for url, country_code in zip(url_list, country_code_list):
            assert country_code in url

    
