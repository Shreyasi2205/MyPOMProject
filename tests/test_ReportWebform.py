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
class Test_ReportWebform(BaseTest):

    def test_ARC_9113_ReportWebform_radioButton(self):

        """
        Checks default language is english in radio button.
        """

        self.driver.get(self.env + "report-webform")
        assert self.basePage.is_selected(self.webformPage.english_radio_button_css) == True

    def test_ARC_9113_ReportWebform_location(self):

        """
        Checks after selecting the location dropdown, locations are displaying or not.
        """

        self.driver.get(self.env + "report-webform")
        display_status_list = self.webformPage.filter_location()
        
        for status in display_status_list:

            assert status == True


    def test_ARC_9113_ReportWebform_country_content(self):

        """
        Clicks on one random country and checks country related contents are coming or not.
        """

        self.driver.get(self.env + "report-webform")
        if self.driver.find_elements(*self.webformPage.cookie_id):
            self.basePage.press_button(self.webformPage.cookie_id)
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")        
        content_status = self.webformPage.location_content()

        assert content_status == True

    def test_ARC_9113_ReportWebform_other_language(self):

        """
        Checks that after selecting different language radio button, the title is getting changed.
        """

        self.driver.get(self.env + "report-webform")
        eng_title = self.basePage.get_element_text(self.webformPage.eng_title_css)
        self.basePage.press_button(self.webformPage.france_radio_button_css)
        france_title = self.basePage.get_element_text(self.webformPage.fr_title_css)
        assert eng_title != france_title

    def test_ARC_9113_ReportWebform_image(self):

        """
        Checks image is displaying.
        """

        self.driver.get(self.env + "report-webform")
        assert self.basePage.is_displayed(self.webformPage.image_css) == True


       

    