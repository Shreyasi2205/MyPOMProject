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
from selenium.webdriver.support.color import Color

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
@pytest.mark.ph
@pytest.mark.malaysia
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.fr
@pytest.mark.it
@pytest.mark.za
@pytest.mark.lv
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.th
@pytest.mark.jp
@pytest.mark.pt
@pytest.mark.kr
@pytest.mark.tw
@pytest.mark.ar
@pytest.mark.fi
@pytest.mark.hk
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.ie
@pytest.mark.gr
@pytest.mark.dk
@pytest.mark.no
@pytest.mark.cz
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.tr
@pytest.mark.rs
@pytest.mark.ro
@pytest.mark.il
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.ru
@pytest.mark.bg
@pytest.mark.ve
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.lt
@pytest.mark.be
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.ee
@pytest.mark.au
@pytest.mark.pl
class Test_CareerSearch(BaseTest):

    def test_ARC_2585_CareerSearch_get_careerSearch(self):

        """
        Launch the career search page
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)


    def test_ARC_2585_CareerSearch_table_headers(self):

        """
        Checks the table header titles are displayed or not
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        header_name_status = self.careerSearchPage.table_headers_title()
        for header_name in header_name_status:
            assert header_name == True
             

    def test_ARC_2585_CareerSearch_table_headers_sorting(self):

        """
        Checks Table header sorting functionality is working or not
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        table_headers,sort_ascending_list, sort_descending_list = self.careerSearchPage.table_headers_sorting()
        table_header_index = 0
        for header in table_headers:

            assert "asc" in sort_ascending_list[table_header_index]
            assert "desc" in sort_descending_list[table_header_index]

            table_header_index = table_header_index + 1


    def test_ARC_2585_CareerSearch_pagination(self):

        """
        Checks Pagination is working or not and Totals Job results in each page.
        Total Jobs in each page should be 10.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        total_row_per_page_list, pagination_page_row_list_len = self.careerSearchPage.pagination_validation()

        for pagination_page_len, total_row_per_page in zip(pagination_page_row_list_len, total_row_per_page_list):

            assert pagination_page_len > 0
            assert total_row_per_page == 10


    # Alreadt covered in test_breadcrumb
    # def test_ARC_2585_CareerSearch_get_breadcrumbs(self):

    #     self.driver.get(self.env)
    #     self.careerSearchPage.launch_careerSearch(self.env_name)
    #     breadcrumb_items_status, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.careerSearchPage.breadcrumb_ele()
    #     assert len(breadcrumb_items_status) == 3
    #     for breadcrumb in breadcrumb_items_status:
    #         breadcrumb == True

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element


    def test_ARC_2585_CareerSearch_disclaimer(self):

        """
        Checks disclaimer title and description is there or not(Optional)
        """
        
        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        if len(self.driver.find_elements(self.careerSearchPage.disclaimer_id[0], self.careerSearchPage.disclaimer_id[1])) > 0:
            assert self.basePage.is_displayed(self.careerSearchPage.disclaimer_title_css) == True
            assert self.basePage.is_displayed(self.careerSearchPage.disclaimer_desc_css) == True
           

    def test_ARC_2585_CareerSearch_filters(self):

        """
        Checks career search filters are displayed or not.
        Filters - function, location, search button, division, date posted, search input field.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        assert self.basePage.is_displayed(self.careerSearchPage.function_txt_css) == True
        assert self.basePage.is_displayed(self.careerSearchPage.location_txt_css) == True
        assert self.basePage.is_displayed(self.careerSearchPage.search_btn_xpath) == True
        assert self.basePage.is_displayed(self.careerSearchPage.division_txt_css) == True
        assert self.basePage.is_displayed(self.careerSearchPage.date_posted_css) == True
        assert self.basePage.is_displayed(self.careerSearchPage.search_input_field_xpath) == True
        
    
    def test_ARC_2585_CareerSearch_location_filter(self):

        """
        Checks location filter is working or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        filtered_location_list,filterd_attributes_list,after_location_search_text,location_count,location_font = self.careerSearchPage.filter_location()
        for filtered_location,filterd_attributes in zip(filtered_location_list,filterd_attributes_list):
             assert filtered_location == filterd_attributes
        assert str(location_count) in after_location_search_text
        assert "volta_modern_display75_bold" in location_font

    def test_ARC_2585_CareerSearch_function_filter(self):

        """
        Checks function filter is working or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        filtered_function_list,filterd_attributes_list,after_function_search_text ,function_count, function_font  = self.careerSearchPage.filter_function()
        for filtered_function,filterd_attributes in zip(filtered_function_list,filterd_attributes_list):
             assert filtered_function == filterd_attributes
        assert str(function_count) in after_function_search_text
        assert "volta_modern_display75_bold" in function_font 

    # def test_ARC_2585_CareerSearch_search_filter(self):

    # """
    # After Searching some job role for e.g. "Manager", It checks that "Manager" text is coming in the url or not.
    # """

    #     job_title_prev_list = []
    #     job_title_next_list = []
    #     self.driver.get(self.env)
    #     self.careerSearchPage.launch_careerSearch(self.env_name)
    #     if self.driver.find_elements(*self.careerSearchPage.clear_all_css):
    #         self.careerSearchPage.clear_all()
    #     self.basePage.send_keys(self.careerSearchPage.search_input_field_xpath, "Manager")

    #     job_title_prev = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr > td > a")
    #     job_title_prev_index = 0
    #     for prev in job_title_prev:
    #         job_title_prev = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr > td > a")
    #         job_title_prev_list.append(job_title_prev[job_title_prev_index].get_attribute("href"))
    #         job_title_prev_index += 1

    #     self.basePage.press_button(self.careerSearchPage.search_btn_xpath)

    #     job_title_next = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr > td > a")
    #     job_title_next_index = 0
    #     for next in job_title_next:
    #         job_title_next = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr > td > a")
    #         job_title_next_list.append(job_title_next[job_title_next_index].get_attribute("href"))
    #         job_title_next_index += 1

    #     # job_title_next = self.basePage.get_elemet_attribute((By.CSS_SELECTOR, "tbody > tr > td > a"), "href")
    #     while True:
    #         if job_title_prev_list != job_title_next_list:
    #             break
    #         job_title_next = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr > td > a")
    #         job_title_next_index = 0
    #         for next in job_title_next:
    #             job_title_next = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr > td > a")
    #             job_title_next_list.append(job_title_next[job_title_next_index].get_attribute("href"))
    #             job_title_next_index += 1
    #     filtered_url = self.driver.current_url
    #     assert "Manager" in filtered_url

    def test_ARC_2585_CareerSearch_division_filter(self):

        """
        Checks division filter is working or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        filtered_division_list,filterd_attributes_list,after_division_search_text,division_count,division_font = self.careerSearchPage.filter_division()
        for filtered_division,filterd_attributes in zip(filtered_division_list,filterd_attributes_list):
             assert filtered_division == filterd_attributes
        assert str(division_count) in after_division_search_text
        assert "volta_modern_display75_bold" in division_font 


    def test_ARC_2585_CareerSearch_data_posted_filter(self):

        """
        Checks date posted filter is working or not.
        """
        if self.env_name == "global":
            self.driver.get(self.env)
            self.careerSearchPage.launch_careerSearch(self.env_name)
            date_posted_url_list, today_date, yesterday_date, job_latest_date,date_posted_count_list = self.careerSearchPage.date_posted_validations(self.env_name)
            for date_posted_count, date_posted_url in zip(date_posted_count_list , date_posted_url_list):
                assert str(date_posted_count) in date_posted_url 
            assert job_latest_date in [today_date,yesterday_date]

       

    def test_ARC_2585_CareerSearch_search_result(self):

        """
        Checks "Search Reults" text is displaying or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        assert self.basePage.is_displayed(self.careerSearchPage.search_result_css) == True
        
    def test_ARC_2585_CareerSearch_job_page(self):

        """
        Checks the random job url(href) and after clicking on the job, the current url is same or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        random_job_title_url = self.careerSearchPage.random_job_click()
        assert random_job_title_url == self.driver.current_url
        self.driver.back()
       
    def test_ARC_2585_CareerSearch_filter_usa(self):

        """
        Checks after filtering USA location, download button is coming or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        if self.env_name == "usa":
            assert self.basePage.is_displayed(self.careerSearchPage.download_css)
            assert self.basePage.element_clickable(self.careerSearchPage.download_css) == True
            self.careerSearchPage.clear_all()
        else:
            self.careerSearchPage.filter_usa()
            assert self.basePage.is_displayed(self.careerSearchPage.download_css)
            assert self.basePage.element_clickable(self.careerSearchPage.download_css) == True
            self.careerSearchPage.clear_all()

    def test_ARC_2585_CareerSearch_alternative_locationCountry(self):

        """
        Checks alternate location is displaying or not.
        Here we are filtering Ireland location to get the aliternate location text easily.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        self.careerSearchPage.filter_alternative_location()
        alt_flag = 0
        index = 0
        alt_index = 0
        alt_locs = self.driver.find_elements(*self.careerSearchPage.alternative_location_css)
        for alt_loc in alt_locs:
            alt_locs = self.driver.find_elements(*self.careerSearchPage.alternative_location_css)
            if "+" in alt_locs[index].text:
                alt_flag = 1
                break
            index += 1
        if alt_flag == 1:
            alternate_location = self.driver.find_elements(*self.careerSearchPage.alternative_location_css)
            for alt in alternate_location:
                if len(alternate_location[alt_index].text) > 0:
                    assert len(alternate_location[index].text) > 0
                    break
                alt_index += 1


    def test_ARC_2585_CareerSearch_jobUrl_validation(self):

        """
        Checks the job url is matching with the current environment name or not.
        The job url should consist the current environment name.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        jobpage_url_list = self.careerSearchPage.jobUrl_verification()
        for url in jobpage_url_list:
            try :
                assert self.env in url
            except :
                assert self.env.split("@")[1] in url

    def test_ARC_2585_CareerSearch_search_results(self):

        """
        Checks the searched text is coming in the auto suggestion or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        job_title_list,auto_suggestions_text_list= self.careerSearchPage.search_results()
        for suggestion_text in auto_suggestions_text_list:
            assert self.careerSearchPage.search_keyword.lower() in suggestion_text.lower()
        for job_title in job_title_list:
            assert self.careerSearchPage.search_keyword.lower() in job_title.lower()

    def test_ARC_2585_CareerSearch_footer_search_box_color(self):

        """
        Checks the footer search box color is matching with the pattern color or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        
        if 'carmine' in self.basePage.get_css_property(self.careerSearchPage.pattern_css, 'background-image'):
            assert "#8d1f1b" == self.basePage.get_css_color(self.careerSearchPage.footer_search_xpath, 'background-color')
        elif 'blue' in self.basePage.get_css_property(self.careerSearchPage.pattern_css, 'background-image'):
            assert "#0460a9" == self.basePage.get_css_color(self.careerSearchPage.footer_search_xpath, 'background-color')
        elif 'apricot' in self.basePage.get_css_property(self.careerSearchPage.pattern_css, 'background-image'):
            assert "#ec9a1e" == self.basePage.get_css_color(self.careerSearchPage.footer_search_xpath, 'background-color')
        elif 'siena' in self.basePage.get_css_property(self.careerSearchPage.pattern_css, 'background-image'):
            assert "#e74a21" == self.basePage.get_css_color(self.careerSearchPage.footer_search_xpath, 'background-color')

    def test_ARC_2585_CareerSearch_table_color(self):

        """
        Checks the table header color is matching with the pattern color or not.
        """        

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)

        if self.driver.find_elements(*self.careerSearchPage.clear_all_css):
            self.careerSearchPage.clear_all()
        if 'carmine' in self.basePage.get_css_property(self.careerSearchPage.pattern_css, 'background-image'):
            assert "#8d1f1b" == self.basePage.get_css_color(self.careerSearchPage.table_header_css, 'background-color')
        elif 'blue' in self.basePage.get_css_property(self.careerSearchPage.pattern_css, 'background-image'):
            assert "#0460a9" == self.basePage.get_css_color(self.careerSearchPage.table_header_css, 'background-color')
        elif 'apricot' in self.basePage.get_css_property(self.careerSearchPage.pattern_css, 'background-image'):
            assert "#ec9a1e" == self.basePage.get_css_color(self.careerSearchPage.table_header_css, 'background-color')
        elif 'siena' in self.basePage.get_css_property(self.careerSearchPage.pattern_css, 'background-image'):
            assert "#e74a21" == self.basePage.get_css_color(self.careerSearchPage.table_header_css, 'background-color')


    def test_ARC_2585_CareerSearch_career_block(self):

        """
        Checks Careers Title and description is available or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.careerSearchPage.career_block_present_css))
        assert "block-careersearchtitle" in self.basePage.get_elemet_attribute(self.careerSearchPage.career_block_css, 'id')
        assert len(self.basePage.get_element_text(self.careerSearchPage.career_title_css)) > 0
        career_descs = self.driver.find_elements(*self.careerSearchPage.career_desc_css)
        assert len(career_descs[0].text) > 0
        for desc in career_descs:
            assert len(desc.text) > 0

    def test_ARC_2585_CareerSearch_th_font_color(self):

        """
        Checks the Table header title font color is "#fff(white)" or not.
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)

        th_fonts = self.driver.find_elements(*self.careerSearchPage.table_header_font_css)
        for th_font in th_fonts:
            assert "#fff" in Color.from_string(th_font.value_of_css_property('color')).hex
            
    def test_ARC_2585_CareerSearch_get_result(self):

        """
        Checks after searching with a specific keyword for e.g. "associate",
        It's showing any job result or not. If it doesn't, then it should display
        "No Result Found".
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)

        self.basePage.send_keys(self.careerSearchPage.search_input_field_xpath, 'associate')
        self.basePage.press_button(self.careerSearchPage.search_btn_xpath)
        if self.driver.find_elements(*self.careerSearchPage.total_row_css):
            assert len(self.driver.find_elements(*self.careerSearchPage.total_row_css)) > 0
        else:
            assert len(self.basePage.get_element_text(self.careerSearchPage.empty_css)) > 0



    

        

        
