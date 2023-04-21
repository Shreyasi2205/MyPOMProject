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
@pytest.mark.singapore
@pytest.mark.usa
@pytest.mark.uk
@pytest.mark.global_site
@pytest.mark.at
@pytest.mark.ca
@pytest.mark.tr
@pytest.mark.kr
@pytest.mark.bd
@pytest.mark.ru
@pytest.mark.be
@pytest.mark.ee
@pytest.mark.au
# @pytest.mark.rs
class Test_ProductOverviewPage(BaseTest):

    # def test_ARC_2723_ProductOverviewPage_get_productOverviewPage(self):

    #     self.driver.get(self.env)
    #     self.driver.get(self.env)
    #     self.productPage.launch_productPage(self.env_name)

    def test_ARC_2723_ProductOverviewPage_title(self):

         """
         Checks Title is displaying or not in product overview page.
         """

         self.driver.get(self.env)
         self.productPage.launch_productPage(self.env_name)
         assert self.basePage.is_displayed(self.productPage.page_title_css) == True
        
    def test_ARC_2723_ProductOverviewPage_introText(self):

        """
         Checks intro text is displaying or not in product overview page.
         """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        assert self.basePage.is_displayed(self.productPage.page_intro_text_css) == True
       
    def test_ARC_2723_ProductOverviewPage_product_list(self):

        """
         Checks products are displaying or not in product overview page.
         """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        product_list = self.basePage.get_elements(self.productPage.product_list_css)
        for list in product_list:

            assert self.basePage.is_displayed_ele(list) == True
       
    
    def test_ARC_2723_ProductOverviewPage_search_textBox(self):

        """
         Checks search bar is displaying or not in product overview page.
         """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        assert self.basePage.is_displayed(self.productPage.search_input_field_xpath) == True

    def test_ARC_2723_ProductOverviewPage_search_button(self):

        """
         Checks search button is displaying or not in product overview page.
         """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        assert self.basePage.is_displayed(self.productPage.search_btn_field_xpath) == True
         
    def test_ARC_2723_ProductOverviewPage_filterTags(self):

        """
        Checks filter tabs are displaying or not.
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        filter_tab_list = self.productPage.filter_tabs_presence()
        assert len(filter_tab_list) > 0
        for filter_tab in filter_tab_list:

            assert filter_tab == True

    def test_ARC_2723_ProductOverviewPage_pagination(self):

         """
         Checks Pagination is working or not and if there is more than 10 products, pagination is there or not.
         """
         
         self.driver.get(self.env)
         self.productPage.launch_productPage(self.env_name)
         total_row = self.basePage.get_elements(self.productPage.total_row_css)
         len_total_row = len(total_row)
         if len_total_row == 10 and self.driver.find_elements(By.CSS_SELECTOR, "h4#pagination-heading"):

            assert len(self.driver.find_elements(By.CSS_SELECTOR, "h4#pagination-heading")) > 0

            next_page_url, prev_page_url = self.productPage.pagination_check()
            assert "page=1" in next_page_url
            assert "page=0" in prev_page_url

         else:
            
            assert len(self.driver.find_elements(By.CSS_SELECTOR, "h4#pagination-heading")) == 0


    def test_ARC_2723_ProductOverviewPage_no_search_result(self):

         """
         Checks if there is No Result for the searched text, It should display
         No Result Found.
         """

         self.driver.get(self.env)
         self.productPage.launch_productPage(self.env_name)
         self.productPage.no_result_check()
         assert self.basePage.is_displayed(self.productPage.empty_css)  == True

        
    def test_ARC_2723_ProductOverviewPage_search_result(self):

        """
        Checks if searched text is coming in the results.
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        self.basePage.press_button(self.productPage.mega_menu_btn_css)
        self.basePage.press_button(self.productPage.mega_menu_btn_css)
        search_result_list = self.productPage.verify_search_result()

        for search_result in search_result_list:
            assert "afinitor" in search_result.lower()


    def test_ARC_2723_ProductOverviewPage_filters_greyColor(self):

        """
        Checks Tabs are getting greyed out or not.
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        grey_color_list = self.productPage.check_greyColor()
        for  grey_color in grey_color_list:
            assert "#f1f1f1" in grey_color

    def test_ARC_2723_ProductOverviewPage_filters_alphabetical_order(self):

        """
        Checks the alphabetical order is coming from A-Z while changing tabs.
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        alphabetical_order_listt = self.productPage.check_alphabetical_order()
        for alphabetical_order in alphabetical_order_listt:
            assert "A-Z" in alphabetical_order
           
    def test_ARC_2723_ProductOverviewPage_filters_toggle_view(self):

        """
        Checks "A-Z" and "Z-A" toggle is working or not.
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        a_z_view, z_a_view = self.productPage.toggle_view()
        assert "Z-A" in z_a_view
        assert "A-Z" in a_z_view

    def test_ARC_2723_ProductOverviewPage_availableIn(self):

        """
        Checks available in is displaying or not.
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        available_in_list = self.productPage.available_in_ele()

        for available_in in available_in_list:

            assert available_in == True

    def test_ARC_2723_ProductOverviewPage_download_button(self):

        """
        Checks for download btn is there or not and if it is there, it's clickable or not.
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        total_row = self.basePage.get_elements(self.productPage.total_row_css)
        len_total_row = len(total_row)
        if len_total_row == 10 and self.driver.find_elements(By.CSS_SELECTOR, "h4#pagination-heading"):

            pagination_index = 3
            flag = 0
            while pagination_index > 0:
                if len(self.driver.find_elements(self.productPage.download_btn_css[0], self.productPage.download_btn_css[1])) > 0:

                    download_btn_txt, download_btn_clickable, flag = self.productPage.download_btn_ele()
                    assert len(download_btn_txt) > 0
                    assert download_btn_clickable == True

                pagination_index = pagination_index - 1
                if flag == 1:
                    break
                self.basePage.press_button(self.productPage.next_page_arrow_xpath)

        else:

            if len(self.driver.find_elements(self.productPage.download_btn_css[0], self.productPage.download_btn_css[1])) > 0:

                    download_btn_txt, download_btn_clickable, flag = self.productPage.download_btn_ele()
                    assert len(download_btn_txt) > 0
                    assert download_btn_clickable == True



    def test_ARC_2723_ProductOverviewPage_duplicate_description(self):

        """
        Checks for duplicate description while changing menu tabs.
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        
        flag = self.productPage.duplicate_description()
        assert flag == 0
        


    def test_ARC_2723_ProductOverviewPage_file_download_button(self):

        """
        check for product download icon for all kind of files and 
        if the download icon is missing for any file then we will get the particular product name in the logs
        """

        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        accordion_len, other_right_portfolio , file, download_icon_len , display_status, product_name = self.productPage.file_download_button()
        
        if accordion_len > 0 or other_right_portfolio > 0 :
            assert file == download_icon_len
            for status in display_status :
                assert status == True ,f"Products which don't have download button {product_name}" 


    def test_ARC_2723_ProductOverviewPage_product_count(self):

        """
        check for product count in the page and product count should be 10
        If pagination is there , check the count for the next page also
        """
        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        num_products_list, next_button = self.productPage.products_count()
        assert len(num_products_list) > 0
        for products in num_products_list:
            if next_button > 0:
                assert products == 10
            else:
                assert products > 0


    def test_ARC_2723_ProductOverviewPage_download_link_as_button(self):

        """
        check the Download links shouldn’t display as button 
        """
        self.driver.get(self.env)
        self.productPage.launch_productPage(self.env_name)
        len_buttons = self.productPage.download_link_as_button()
        assert len_buttons == 0 ,f"{len_buttons} download links showing as button"

