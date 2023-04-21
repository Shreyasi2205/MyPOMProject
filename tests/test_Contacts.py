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
class Test_Contacts(BaseTest):

    
    def test_ARC_3940_Contacts_pattern(self):

        """
        Checks for pattern in contacts page.
        """

        self.driver.get(self.env)
        self.ContactsPage.launch_contactsPage()
        assert "patterns" in self.basePage.get_css_property(self.newsPage.pattern_css, "background-image")


    def test_ARC_3940_Contacts_title(self):

        """
        Checks for title in contacts page.
        """

        self.driver.get(self.env)
        self.ContactsPage.launch_contactsPage()
        assert True == self.basePage.is_displayed(self.ContactsPage.contacts_title_css)


    def test_ARC_3940_Contacts_first_column(self):

        """
        Checks for first column and validate data is present in first column.
        """

        self.driver.get(self.env)
        self.ContactsPage.launch_contactsPage()
        assert True == self.basePage.is_displayed(self.ContactsPage.first_col_css)
        assert len(self.basePage.get_element_text(self.ContactsPage.first_col_data_css)) > 0

    
    def test_ARC_3940_Contacts_last_column(self):

        """
        Checks for last columnand validate data is present in last column .
        """

        self.driver.get(self.env)
        self.ContactsPage.launch_contactsPage()
        assert True == self.basePage.is_displayed(self.ContactsPage.last_col_css)
        assert len(self.basePage.get_element_text(self.ContactsPage.last_col_data_css)) > 0


    def test_ARC_3940_Contacts_share_button(self):

        """
        Checks for share column.
        """

        self.driver.get(self.env)
        self.ContactsPage.launch_contactsPage()
        share_btn_status = self.ContactsPage.share_button()
        assert share_btn_status == True

    def test_ARC_3940_Contacts_print_button(self):

        """
        Checks for printt column.
        """

        self.driver.get(self.env)
        self.ContactsPage.launch_contactsPage()
        print_btn_status = self.ContactsPage.print_button()
        assert print_btn_status == True

    def test_ARC_3940_Contacts_save_button(self):

        """
        Checks for save column.
        """

        self.driver.get(self.env)
        self.ContactsPage.launch_contactsPage()
        save_btn_status   = self.ContactsPage.save_button()
        assert save_btn_status  == True

    
