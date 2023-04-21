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
import random

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
@pytest.mark.global_site
@pytest.mark.de
@pytest.mark.lv
@pytest.mark.at
@pytest.mark.ph
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.fr
@pytest.mark.za
@pytest.mark.malaysia
@pytest.mark.jp
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.pt
@pytest.mark.tw
@pytest.mark.it
@pytest.mark.hk
@pytest.mark.fi
@pytest.mark.ar
@pytest.mark.kr
@pytest.mark.ru
@pytest.mark.cn
@pytest.mark.br
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
@pytest.mark.ee
@pytest.mark.il
@pytest.mark.co
@pytest.mark.sk
@pytest.mark.bg
@pytest.mark.ve
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.lt
@pytest.mark.candean
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.ua
@pytest.mark.th
@pytest.mark.be
@pytest.mark.au
@pytest.mark.pl
class Test_JobDetails(BaseTest):

    def test_ARC_2736_JobDetails_get_jobDetails(self):

        """
        launches the job details page
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)

    def test_ARC_2736_JobDetails_pattern(self):

        """
        Checks pattern is there not in job details page.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        row_index, pattern_stripe_paths = self.jobDetailsPage.pattern_verify()
        index = 0
        assert row_index > 0
        for row in range(row_index):
            assert "patterns" in pattern_stripe_paths[index]

    # Already covered in test_breadcrumb
    # def test_ARC_2736_JobDetails_breadcrumbs(self):

    #     self.driver.get(self.env)
    #     self.jobDetailsPage.launch_jobDetails(self.env_name)
    #     row_index ,breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_third_arrow_element, breadcrumb_fourthLevel_color=self.jobDetailsPage.breadcrumb_elements()
    #     index = 0
    #     assert row_index > 0
    #     for row in range(row_index):
            
    #         assert breadcrumb_items[index] == 4
    #         assert "#656565" == breadcrumb_fourthLevel_color[index]

    #         assert ">" in breadcrumb_first_arrow_element[index]
    #         assert ">" in breadcrumb_second_arrow_element[index]
    #         assert ">" in breadcrumb_third_arrow_element[index]

    #         index += 1

    def test_ARC_2736_JobDetail_job_details_content(self):

        """
        Checks the following are displaying or not -
        1. job title
        2. job id
        3. job date
        4. job location
        5. last 2 char of jobID - 'BR'
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        row_index,job_titles,jobs_page_title,job_id_status, job_date_status, job_location_status, job_id_last_char  = self.jobDetailsPage.job_details_content()
        index = 0
        assert row_index > 0
        for row in range(row_index):
            
            assert job_titles[index] == jobs_page_title[index]
            assert job_id_status[index] == True
            assert job_date_status[index] == True
            assert job_location_status[index] == True
            assert job_id_last_char[index][-2] == "B"
            assert job_id_last_char[index][-1] == "R"

            index += 1

    def  test_ARC_2736_JobDetail_job_details_content_right(self):

       """
       checks the following in the right side of job details page -
       1. job image
       2. job title
       3. job id
       """

       self.driver.get(self.env)
       self.jobDetailsPage.launch_jobDetails(self.env_name)
       row_index, job_titles,jobs_page_title,job_img_status,job_id_status  = self.jobDetailsPage.job_details_content_right()
       index = 0
       assert row_index > 0
       for row in range(row_index):
            
            if self.driver.get_window_size().get("width") > 1050:
                assert job_img_status[index] == True
                assert job_titles[index] == jobs_page_title[index]
                assert job_id_status[index] == True

            index += 1

    # Already covered in test_breadcrumb
    # def test_ARC_2736_JobDetails_first_second_third_level_breadcrumbs(self):

    #     self.driver.get(self.env)
    #     self.jobDetailsPage.launch_jobDetails(self.env_name)
    #     row_index,home_url, home_current_url, careers_url, careers_current_url, careers_search_url, careers_current_search_url = self.jobDetailsPage.breadcrumbs_firstLevel_secondLevel_thirdLevel()
    #     index = 0
    #     assert row_index > 0
    #     for row in range(row_index):
            
    #         assert home_current_url[index] ==  home_url[index]
    #         assert careers_current_url[index] ==  careers_url[index]
    #         assert careers_current_search_url[index] ==  careers_search_url[index]

    #         index += 1

    
    # def  test_ARC_2736_JobDetail_job_details_link_button(self):

    #     """
    #     checks the link buttons present in the right side, are working or not.
    #     """

    #     self.driver.get(self.env)
    #     self.jobDetailsPage.launch_jobDetails(self.env_name)
    #     row_index,jobs_button_status,popup_logo_list,popup_title_list,popup_desc_title,popup_continue_list,continue_btn_clickable_status,cancel_button_list,cancel_btn_clickable_status,current_page_url_list,page_url_list,job_url_list,apply_access_job_page_url_list = self.jobDetailsPage.jobs_link_button()
    #     index = 0
    #     assert row_index > 0
    #     for row in range(row_index):

    #         assert jobs_button_status[index] == True
    #         assert self.homePage.novartis_logo in popup_logo_list[index]
    #         assert popup_title_list[index] > 0
    #         assert len(popup_desc_title[index]) > 0
    #         assert len(popup_continue_list[index]) > 0
    #         assert continue_btn_clickable_status[index] == True
    #         assert len(cancel_button_list[index]) > 0
    #         assert cancel_btn_clickable_status[index]== True
    #         assert current_page_url_list[index] == page_url_list[index]
    #         assert len(job_url_list) > 0
    #         assert apply_access_job_page_url_list[index] > 0


    #         index += 1

    def  test_ARC_2736_JobDetail_print_button(self):

        """
        checks the following for print button -
        1. button is available
        2. clickable
        3. print icon
        4. navigating to correct page
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        row_index,print_btn_list, print_btn_clickable_status, print_icon_list,print_url_list,print_page_url_list = self.jobDetailsPage.print_btn_ele()
        index = 0
        assert row_index > 0
        for row in range(row_index):

            assert print_btn_list[index] == True
            assert print_btn_clickable_status[index] == True
            assert "print" in print_icon_list[index]
            assert print_url_list[index] == print_page_url_list[index]
            index += 1

    def  test_ARC_2736_JobDetail_save_button(self):

        """
        checks the following for save button -
        1. button is available
        2. clickable
        3. save icon
        4. href is there in <a> tag
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        row_index,save_btn_list,save_btn_clickable_status,save_icon_list,save_href_list = self.jobDetailsPage.save_btn_ele()
        index = 0
        assert row_index > 0
        for row in range(row_index):

            assert save_btn_list[index] == True
            assert save_btn_clickable_status[index] == True
            assert "save" in save_icon_list[index]
            assert len(save_href_list[index]) > 0

            index += 1

    def  test_ARC_2736_JobDetail_share_button(self):

        """
        checks the following for share button -
        1. button is available
        2. clickable
        3. share icon
        4. twitter, whatsapp, facebook, linkedin, email icons
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        row_index , share_btn_icon_list,share_btn_list, twitter_icon_list,facebook_icon_list,whatsapp_icon_list,linkedin_icon_list,email_icon_list = self.jobDetailsPage.share_btn_ele()
        index = 0
        assert row_index > 0
        for row in range(row_index):

            assert "share" in share_btn_icon_list[index]
            assert share_btn_list[index] == True
            assert "twitter" in twitter_icon_list[index]
            assert "facebook" in facebook_icon_list[index]
            assert "whatsapp" in whatsapp_icon_list[index]
            assert "linkedin" in linkedin_icon_list[index]
            assert "email" in email_icon_list[index]

            index += 1

    def  test_ARC_2736_JobDetail_tag_elements(self):

        """
        Checks tags are available or not.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        row_index ,tag_len , tag_elements_list_status, tag_elements_url_list, tag_elements_page_url_list = self.jobDetailsPage.tag_ele()
        index = 0
        assert row_index > 0
        for row in range(row_index):

            assert tag_len > 0
            assert tag_elements_list_status[index] == True
            for  tag_element_url, tag_element_page_url in zip(tag_elements_url_list[index], tag_elements_page_url_list[index]):

                assert tag_element_url == tag_element_page_url


            index += 1

    def test_ARC_2736_JobDetail_jobs_content(self):

        """
        Checks for exposed job structure.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        row_index,job_content_class_list = self.jobDetailsPage.jobs_content()
        index = 0
        assert row_index > 0
        for row in range(row_index):

            assert job_content_class_list[index] == "jobs-content"
            index += 1

    def test_ARC_2736_JobDetail_label_name_value(self):

        """
        Checks for job label and values.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        index = 0
        row_index, job_detail_label_list, job_detail_value_list = self.jobDetailsPage.label_name_value_ele()
        assert row_index > 0
        for row in range(row_index):

            for job_detail_label, job_detail_value in zip(job_detail_label_list[index], job_detail_value_list[index]):
                
                assert len(job_detail_label) > 0
                assert len(job_detail_value) > 0

            index += 1

    def test_ARC_2736_JobDetail_job_info_single_row(self):

        """
        Checks job id, date and location are in single row.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        
        job_info_class_list, job_info_each_div_class_list = self.jobDetailsPage.job_info_single_row()
        assert len(job_info_class_list) == 4
        assert len(job_info_each_div_class_list) == 12
        for job_info_class in job_info_class_list:
            assert "d-sm-flex" in job_info_class
        for job_info_each_div_class in job_info_each_div_class_list:
            assert "d-sm-inline-block" in job_info_each_div_class

    def test_ARC_2736_JobDetail_job_desc(self):

        """
        Checks job description is available or not and it's in <h3> tag or not.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)

        job_desc_list, job_desc_tag_list = self.jobDetailsPage.job_description()
        assert len(job_desc_list) == 4
        assert len(job_desc_tag_list) == 4
        for job_desc, job_desc_tag in zip(job_desc_list, job_desc_tag_list):
            assert len(job_desc) > 0
            assert job_desc_tag == "h3"


    def test_ARC_2736_JobDetail_right_hand_rail(self):

        """
        Checks right hand rail is not there in job details page.
        """

        self.driver.get(self.env)
        self.jobDetailsPage.launch_jobDetails(self.env_name)
        row_index,right_hand_rail_list = self.jobDetailsPage.right_hand_rail()
        index = 0
        assert row_index > 0
        for row in range(row_index):

            assert right_hand_rail_list[index] == 0
            index += 1



    def test_ARC_2736_JobDetail_alternative_locationCountry(self):

        """
        check alternate location country in job detail page
        """

        self.driver.get(self.env)
        self.careerSearchPage.launch_careerSearch(self.env_name)
        self.careerSearchPage.filter_alternative_location()
        alt_index = 0
        
        alternate_location = self.driver.find_elements(*self.careerSearchPage.alternative_location_css)
        for alt in alternate_location:
            alternate_location = self.driver.find_elements(*self.careerSearchPage.alternative_location_css)
            self.driver.execute_script("arguments[0].click()", alternate_location[alt_index].find_element(*self.careerSearchPage.alternate_job_title_xpath))
            detail_page_alternate_country = self.driver.find_elements(*self.jobDetailsPage.job_detail_alternate_country_xpath)
            assert len(detail_page_alternate_country) >= 1
            self.driver.back()
            alt_index += 1

        
                        
                        
           
                    
                    
                
       
    
