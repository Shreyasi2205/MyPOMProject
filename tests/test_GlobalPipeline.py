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
import random

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.global_site
class Test_GlobalPipeline(BaseTest):


    def test_ARC_2724_NovartisPipeline_get_pipeline(self):

        """
        Launches the Global Pipeline Page.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()


    def test_ARC_2724_NovartisPipeline_title(self):

        """
        Checks Title is available or not.
        """
        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        assert len(self.basePage.get_element_text(self.globalPipelinePage.page_title_css)) > 0

    def test_ARC_2724_NovartisPipeline_intro(self):

        """
        Checks intro text is available or not.
        """
        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        assert len(self.basePage.get_element_text(self.globalPipelinePage.page_intro_css)) > 0

    def test_ARC_2724_NovartisPipeline_compounds_view(self):

        """
        Checks List of compounds displaying in 2 columns
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        assert self.basePage.get_css_property(self.globalPipelinePage.content_elements_css, "display") == "grid"
        assert self.basePage.get_css_property(self.globalPipelinePage.content_elements_css, "grid-template-columns").split(" ")[0] == self.basePage.get_css_property(self.globalPipelinePage.content_elements_css, "grid-template-columns").split(" ")[1]


    def test_ARC_2724_NovartisPipeline_search_bar_button(self):

        """
        Checks search bar and button is available or not.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        assert len(self.basePage.get_elemet_attribute(self.globalPipelinePage.search_input_field_xpath, "placeholder")) > 0
        assert self.basePage.get_elemet_attribute(self.globalPipelinePage.search_btn_field_xpath, "value") == "Search"


    def test_ARC_2724_NovartisPipeline_filter_tags(self):

        """
        Checks the availability of filter tags.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        for filter in self.driver.find_elements(self.globalPipelinePage.filter_elements_css[0], self.globalPipelinePage.filter_elements_css[1]):

            assert len(filter.text) > 0


    def test_ARC_2724_NovartisPipeline_filter_indication(self):

        """
        Checks filter indication colors are correct or not.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        for indication in self.driver.find_elements(self.globalPipelinePage.indication_css[0], self.globalPipelinePage.indication_css[1]):

            assert len(indication.text) > 0
            assert indication.get_attribute("style") in self.globalPipelinePage.indication_tag_border_color
            value_of_css = indication.value_of_css_property("color")
            hex = Color.from_string(value_of_css).hex
            assert "#221f1f" == hex

    # Already covered in test_breadcrumb
    # def test_ARC_2724_NovartisPipeline_breadcrumbs(self):

    #     self.driver.get(self.env)
    #     self.homePage.about_pipeline_mega_menu()
    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.globalPipelinePage.breadcrumb_ele()

    #     assert "Home" in breadcrumb_items
    #     assert "Research & Development" in breadcrumb_items
    #     assert "Novartis Pipeline" in breadcrumb_items

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    #     assert "#656565" == self.basePage.get_css_color(self.globalPipelinePage.pipeline_last_child_breadcrumb_color_css, "color")

    # Already covered in test_breadcrumb
    # def test_ARC_2724_NovartisPipeline_first_second_level_breadcrumbs(self):

    #     self.driver.get(self.env)
    #     self.homePage.about_pipeline_mega_menu()
    #     breadcumb_anchor_url_list, breadcumb_anchor_current_url_list = self.globalPipelinePage.breadcrumb_url()
    #     for breadcumb_anchor_url, breadcumb_anchor_current_url in zip(breadcumb_anchor_url_list, breadcumb_anchor_current_url_list):
    #         assert breadcumb_anchor_url in breadcumb_anchor_current_url


    def test_ARC_2724_NovartisPipeline_content_elements(self):

        """
        Checks Pagination functionality.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        if  self.globalPipelinePage.pagination_txt in self.driver.page_source:

            assert len(self.driver.find_elements(*self.globalPipelinePage.content_elements_list_css)) == 20
            assert self.globalPipelinePage.pagination_txt in self.driver.page_source

            page_one_url, page_zero_url = self.globalPipelinePage.pagination_front_arrow_back_arrow_validation()
            assert "page=1" in page_one_url
            assert "page=0" in page_zero_url

            pages = self.driver.find_elements(self.globalPipelinePage.pagination_links_css[0], self.globalPipelinePage.pagination_links_css[1])
            random_page_number = random.randint(2, len(pages))
            self.driver.execute_script("arguments[0].click()", pages[random_page_number-1])
            assert "page=" in self.driver.current_url

        else:

            assert self.globalPipelinePage.pagination_txt not in self.driver.page_source


    def test_ARC_2724_NovartisPipeline_check_no_results(self):

        """
        If no result is there, It should display "NO RESULT FOUND"
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        empty_txt = self.globalPipelinePage.check_no_result("Test")
        assert len(empty_txt) > 0


    def test_ARC_2724_NovartisPipeline_check_results(self):

        """
        If we search for a specific keyword, that keyword should be there in the result. 
        Otherwise it should display no result found.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        self.basePage.press_button(self.globalPipelinePage.novartis_pipeline_css)

        content_title_list = self.globalPipelinePage.check_search_result("AAA")
        if len(content_title_list) > 0:
            for content_title in content_title_list:
                assert "AAA" in content_title
        else:
            assert self.basePage.get_element_text(self.globalPipelinePage.empty_css) > 0


    def test_ARC_2724_NovartisPipeline_development_phase_filter(self):

        """
        Action:

            Verify Development Phase filter functionality

            "1.In Global Pipeline overview page--Click on Development Phase filter OR

            In Search Results screen--Click on Development Phase filter

            2.Select one or more multiple check boxes & Check the results displaying based on the selection"

        Expected result:

            1. When Clicked on ARROW - It should display with list of check boxes & allow user to select one or multiple boxes. [Arrow Should toggle when clicked]

            2. a.The check box will fill with the relevant colour when checked

            b. The Development Phase filter tag should get highlighted in Bold & displays the number of selected filters in brackets next to filter name & also displays the selected name under Filter Tags

            c. It should automatically displays the search results based on the selected Development Phase"

        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()
        phase_index, phase_title_list, phase_filter_tag_list, phase_checkbox_color_list, phase_result_list, development_phase_txt, development_phase_font_weight = self.globalPipelinePage.development_phase_ele()

        for phase_checkbox_color in phase_checkbox_color_list:
            assert "#221f1f" in phase_checkbox_color

        assert f"Development Phase ({phase_index})" == development_phase_txt
        assert "75" in development_phase_font_weight

        assert f"Development Phase ({phase_index})" == development_phase_txt
        assert "75" in development_phase_font_weight

        for phase_title, phase_filter_tag in zip(phase_title_list, phase_filter_tag_list):
            assert phase_title in phase_filter_tag

        for phase_result in phase_result_list:
            assert phase_result in phase_title_list

        filter_tag_len = self.globalPipelinePage.clear_all_ele()
        assert filter_tag_len == 0


    def test_ARC_2724_NovartisPipeline_development_filling_date_filter(self):

        """
        Action:

            Verify Filling date filter functionality

            "1.In Global Pipeline overview page--Click on Filling date filter OR

            In Search Results screen--Click on Filling date filter

            2.Select one or more multiple check boxes & Check the results displaying based on the selection"

        Expected result:

            "1.It should display box with list of check boxes & allow user to select one or multiple boxes.

            2. a.The check box will fill with the relevant colour when checked

            b. The Filling date filter tag should get highlighted in Bold & displays the number of selected filters in brackets next to filter name & also displays the selected name under Filter Tags

            c. It should automatically displays the search results based on the selected Filling date"
            
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()

        filling_date_index, filling_date_title_list, filling_date_filter_tag_list, filling_date_checkbox_color_list, filling_date_txt, filling_date_font_weight, filling_date_result_list = self.globalPipelinePage.filling_date_ele()

        for filling_date_checkbox_color in filling_date_checkbox_color_list:
            assert "#221f1f" in filling_date_checkbox_color

        assert f"Filing Date ({filling_date_index})" == filling_date_txt
        assert "75" in filling_date_font_weight

        for filling_date_title, filling_date_filter_tag in zip(filling_date_title_list, filling_date_filter_tag_list):
            assert filling_date_title in filling_date_filter_tag

        for filling_date_result in filling_date_result_list:
            assert filling_date_result in filling_date_title_list

        

        filter_tag_len = self.globalPipelinePage.clear_all_ele()
        assert filter_tag_len == 0


    def test_ARC_2724_NovartisPipeline_therapeutic_area_filter(self):

        """
        Action:

            Verify Therapeutic Area filter functionality

            "1.In Global Pipeline overview page--Click on Therapeutic area filter OR

            In Search Results screen--Click on Therapeutic area filter

            2.Select one or more multiple check boxes & Check the results displaying based on the selection"

        Expected result:

            "1.It should display box with list of check boxes & allow user to select one or multiple boxes.

            2. a.The check box will fill with the relevant colour when checked

            b. The Therapeutic area filter tag should get highlighted in Bold & displays the number of selected filters in brackets next to filter name & also displays the selected name under Filter Tags

            c. It should automatically displays the search results based on the selected therapeutic areas."
            
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()

        therapeutic_area_index, therapeutic_area_title_list, therapeutic_area_filter_tag_list, therapeutic_area_checkbox_color_list, therapeutic_area_result_list, therapeutic_area_txt, therapeutic_area_font_weight = self.globalPipelinePage.therapeutic_area_ele()

        for therapeutic_area_checkbox_color in therapeutic_area_checkbox_color_list:
            assert "#221f1f" in therapeutic_area_checkbox_color

        assert f"Therapeutic Area ({therapeutic_area_index})" == therapeutic_area_txt
        assert "75" in therapeutic_area_font_weight

        for phase_title, phase_filter_tag in zip(therapeutic_area_title_list, therapeutic_area_filter_tag_list):
            assert phase_title in phase_filter_tag

        for therapeutic_area_result in therapeutic_area_result_list:
            assert therapeutic_area_result in therapeutic_area_title_list

        filter_tag_len = self.globalPipelinePage.clear_all_ele()
        assert filter_tag_len == 0


    def test_ARC_2724_NovartisPipeline_indication_name_filter(self):

        """
        Action:

            Verify Indication Name filter functionality

            "1.In Global Pipeline overview page--Click on Indication Name filter OR

            In Search Results screen--Click on Indication Name filter

            2.Select one or more multiple check boxes & Check the results displaying based on the selection"

            Note: Lead Indication- #8d1f1b, New Indication-#ec9a1e, Supplementary Indication- #e74a21 these indication colours can be changed in BE

        Expected result:

            "1.It should display box with list of check boxes & allow user to select one or multiple boxes.

            2. a.The check box will fill with the relevant colour when checked

            b. The Indication Name filter Tag should get highlighted in Bold & displays the number of selected filters in brackets next to filter name & also displays the selected name under Filter Tags

            c. It should automatically displays the search results based on the selected Indication Name"

            Note:

            Lead Indication- #8d1f1b, New Indication- #ec9a1e, Supplementary Indication- #e74a21 these indication colours can be changed in BE
            
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()

        indication_name_index, indication_name_title_list, indication_name_filter_tag_list, indication_name_checkbox_color_list, indication_name_result_list, indication_name_txt, indication_name_font_weight = self.globalPipelinePage.indication_name_ele()

        for indication_name_checkbox_color, indication_name_color in zip(indication_name_checkbox_color_list, self.globalPipelinePage.indication_name_color_list):
            assert indication_name_checkbox_color == indication_name_color

        assert f"Indication Name ({indication_name_index})" == indication_name_txt
        assert "75" in indication_name_font_weight

        for indication_name_title, indication_name_filter_tag in zip(indication_name_title_list, indication_name_filter_tag_list):
            assert indication_name_title in indication_name_filter_tag

        for indication_name_result in indication_name_result_list:
            assert indication_name_result in indication_name_title_list
        
        filter_tag_len = self.globalPipelinePage.clear_all_ele()
        assert filter_tag_len == 0


    def test_ARC_2724_NovartisPipeline_legend(self):

        """
        Checks legend is there or not.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()

        assert self.basePage.get_element_text(self.globalPipelinePage.legend_title_xpath) == "Legend"


    def test_ARC_2724_NovartisPipeline_disclaimer(self):

        """
        Checks disclaimer is there or not.
        """

        self.driver.get(self.env)
        self.homePage.about_pipeline_mega_menu()

        assert self.basePage.get_element_text(self.globalPipelinePage.disclaimer_title_xpath) == "Disclaimer"







       
    
    