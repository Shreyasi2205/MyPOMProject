import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.color import Color

class GlobalPipelinePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    indication_name_color_list = ['border-color: rgb(141, 31, 27); background-color: rgb(141, 31, 27);', 'border-color: rgb(236, 154, 30); background-color: rgb(236, 154, 30);', 'border-color: rgb(231, 74, 33); background-color: rgb(231, 74, 33);']
    indication_tag_border_color = ["border-color: rgb(141, 31, 27);", "border-color: rgb(236, 154, 30);", "border-color: rgb(231, 74, 33);"]
    

    search_input_field_xpath = (By.XPATH, "//*[starts-with(@id,'edit-search-api-fulltext')]")
    search_btn_field_xpath = (By.XPATH, "//*[starts-with(@id,'edit-submit-compounds-list')]")
    page_title_css = (By.CSS_SELECTOR, "#block-novartispipeline > div.content > div.clearfix > h1")
    page_intro_css = (By.CSS_SELECTOR, "#block-novartispipeline > div.content > div.clearfix > p")
    pipeline_last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child > a")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li")
    anchor_tag_loc = (By.TAG_NAME, "a")
    next_page_arrow_xpath = (By.XPATH, "//a[@title='Go to next page']")
    prev_page_arrow_xpath = (By.XPATH, "//a[@title='Go to previous page']")
    content_elements_css = (By.CSS_SELECTOR, "div.item-list > ul")
    filter_elements_css = (By.CSS_SELECTOR, "div.form-row > fieldset.js-form-item.js-form-type-select  > div > div.ms-options-wrap > button > span")
    indication_css = (By.CSS_SELECTOR, ".main-indication")
    content_elements_list_css = (By.CSS_SELECTOR, "div.item-list > ul > li")
    pagination_txt = "pagination"
    clear_all_css = (By.CSS_SELECTOR, ".clear-button")
    pagination_links_css = (By.CSS_SELECTOR, "ul.pagination > li.page-item > a")
    novartis_pipeline_css = (By.CSS_SELECTOR, "ol.breadcrumb > li:last-child > a")
    legend_title_xpath = (By.XPATH, "//div[starts-with(@id, 'block-pipelinelegendglobal')]/div[@class = 'content']/div[contains(@class, 'field field--name-field-title')]")
    disclaimer_title_xpath = (By.XPATH, "//div[starts-with(@id, 'block-pipelinedisclaimerglobal')]/div[@class = 'content']/div[contains(@class, 'field field--name-field-title')]")
    dev_phase_checkbox_css = (By.CSS_SELECTOR, "#ms-list-3 > div > ul > li > label > input")
    dev_phase_filter_css = (By.CSS_SELECTOR, "#ms-list-3 > button > span")
    dev_phase_btn_css = (By.CSS_SELECTOR, "#ms-list-3 > button")
    quert_attr_css = (By.CSS_SELECTOR, ".query-attribute")
    dev_phase_res_css = (By.CSS_SELECTOR, "div.main-second > span:nth-child(2)")
    filling_date_checkbox_css = (By.CSS_SELECTOR, "#ms-list-5 > div > ul > li > label > input")
    filling_date_filter_css = (By.CSS_SELECTOR, "#ms-list-5 > button > span")
    filling_date_btn_css = (By.CSS_SELECTOR, "#ms-list-5 > button")
    filling_date_res_css = (By.CSS_SELECTOR, "div.main-second > span:nth-child(3)")
    therapeutic_area_checkbox_css = (By.CSS_SELECTOR, "#ms-list-2 > div > ul > li > label > input")
    therapeutic_area_filter_css = (By.CSS_SELECTOR, "#ms-list-2 > button > span")
    therapeutic_area_btn_css = (By.CSS_SELECTOR, "#ms-list-2 > button")
    therapeutic_area_res_css = (By.CSS_SELECTOR, "div.main-second > span:nth-child(1)")
    indication_name_checkbox_css = (By.CSS_SELECTOR, "#ms-list-4 > div > ul > li > label > input")
    indication_name_filter_css = (By.CSS_SELECTOR, "#ms-list-4 > button > span")
    indication_name_btn_css = (By.CSS_SELECTOR, "#ms-list-4 > button")
    indication_res_css = (By.CSS_SELECTOR, "div.view-content.row > div > ul > li > div.pipeline-main-wrapper > .main-indication")
    filter_tag_len_css = (By.CSS_SELECTOR, ".exposed-filters-wrapper")
    empty_css = (By.CSS_SELECTOR, ".view-empty")
    search_res_css = (By.CSS_SELECTOR, ".compound-name")
    breadcrumb_lists_anchor_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    


    def breadcrumb_ele(self):

        breadcrumb_items = []
        breadcrumb_lists = self.driver.find_elements(self.breadcrumb_lists_css[0], self.breadcrumb_lists_css[1])
        for breadcrumb_list in breadcrumb_lists:
            breadcrumb_items.append(breadcrumb_list.find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).text)


        breadcrumb_first_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').getPropertyValue('content')";
        breadcrumb_first_arrow_element = self.driver.execute_script(breadcrumb_first_arrow_script);

        breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child'),'::before').getPropertyValue('content')";
        breadcrumb_second_arrow_element = self.driver.execute_script(breadcrumb_second_arrow_script);

        return breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element

    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

    def breadcrumb_url(self):

        breadcumb_anchor_url_list = []
        breadcumb_anchor_current_url_list = []
        breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
        breadcumb_index = 0
        for breadcumb_anchor in breadcumb_anchor_elements:

            breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
            breadcumb_anchor_url_list.append(breadcumb_anchor_elements[breadcumb_index].get_attribute("href"))
            self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
            breadcumb_anchor_current_url_list.append(self.driver.current_url)
            self.driver.back()

            breadcumb_index = breadcumb_index + 1

            if breadcumb_index == 2:
                break


        return breadcumb_anchor_url_list, breadcumb_anchor_current_url_list


    def development_phase_ele(self):

        phase_total_checkbox = self.driver.find_elements(self.dev_phase_checkbox_css[0], self.dev_phase_checkbox_css[1])
        phase_index = 0
        phase_title_list = []
        phase_filter_tag_list = []
        phase_checkbox_color_list = []
        phase_result_list = []

        for phase in phase_total_checkbox:

            self.press_button(self.dev_phase_filter_css)
            phase_total_checkbox = self.driver.find_elements(self.dev_phase_checkbox_css[0], self.dev_phase_checkbox_css[1])
            phase_title_list.append(phase_total_checkbox[phase_index].get_attribute("title"))
            self.driver.execute_script("arguments[0].click()", phase_total_checkbox[phase_index])
            
            phase_index = phase_index + 1

            if phase_index == 2:
                break

        phase_index = 0
        for phase in phase_total_checkbox:

            phase_total_checkbox = self.driver.find_elements(self.dev_phase_checkbox_css[0], self.dev_phase_checkbox_css[1])
            value_of_css = phase_total_checkbox[phase_index].value_of_css_property("background-color")
            hex = Color.from_string(value_of_css).hex
            phase_checkbox_color_list.append(hex)
            
            phase_index = phase_index + 1
            
            if phase_index == 2:
                break

        development_phase_txt = self.get_element_text(self.dev_phase_filter_css)
        development_phase_font_weight = self.get_css_property(self.dev_phase_btn_css, "font-family")
        
    
        phase_filter_tags = self.driver.find_elements(self.quert_attr_css[0], self.quert_attr_css[1])

        for phase_filter in phase_filter_tags:

            phase_filter_tag_list.append(phase_filter.text)


        phase_results = self.driver.find_elements(self.dev_phase_res_css[0], self.dev_phase_res_css[1])
        for phase_result in phase_results:
            phase_result_list.append(phase_result.text)

        return phase_index, phase_title_list, phase_filter_tag_list, phase_checkbox_color_list, phase_result_list, development_phase_txt, development_phase_font_weight



    def filling_date_ele(self):

        filling_date_total_checkbox = self.driver.find_elements(self.filling_date_checkbox_css[0], self.filling_date_checkbox_css[1])
        filling_date_index = 0
        filling_date_title_list = []
        filling_date_filter_tag_list = []
        filling_date_checkbox_color_list = []
        filling_date_result_list = []

        for filling_date in filling_date_total_checkbox:

            self.press_button(self.filling_date_filter_css)
            filling_date_total_checkbox = self.driver.find_elements(self.filling_date_checkbox_css[0], self.filling_date_checkbox_css[1])
            filling_date_title_list.append(filling_date_total_checkbox[filling_date_index].get_attribute("title"))
            self.driver.execute_script("arguments[0].click()", filling_date_total_checkbox[filling_date_index])
            
            filling_date_index = filling_date_index + 1

            if filling_date_index == 2:
                break

        filling_date_index = 0
        for filling_date in filling_date_total_checkbox:

            filling_date_total_checkbox = self.driver.find_elements(self.filling_date_checkbox_css[0], self.filling_date_checkbox_css[1])
            value_of_css = filling_date_total_checkbox[filling_date_index].value_of_css_property("background-color")
            hex = Color.from_string(value_of_css).hex
            filling_date_checkbox_color_list.append(hex)
            
            filling_date_index = filling_date_index + 1
            
            if filling_date_index == 2:
                break

        filling_date_txt = self.get_element_text(self.filling_date_filter_css)
        filling_date_font_weight = self.get_css_property(self.filling_date_btn_css, "font-family")
        
    
        filling_date_filter_tags = self.driver.find_elements(self.quert_attr_css[0], self.quert_attr_css[1])

        for filling_date_filter in filling_date_filter_tags:

            filling_date_filter_tag_list.append(filling_date_filter.text)

        filling_date_results = self.driver.find_elements(self.filling_date_res_css[0], self.filling_date_res_css[1])
        for filling_date_result in filling_date_results:
            filling_date_result_list.append(filling_date_result.text)


        return filling_date_index, filling_date_title_list, filling_date_filter_tag_list, filling_date_checkbox_color_list, filling_date_txt, filling_date_font_weight, filling_date_result_list



    def therapeutic_area_ele(self):

        therapeutic_area_total_checkbox = self.driver.find_elements(self.therapeutic_area_checkbox_css[0], self.therapeutic_area_checkbox_css[1])
        therapeutic_area_index = 0
        therapeutic_area_title_list = []
        therapeutic_area_filter_tag_list = []
        therapeutic_area_checkbox_color_list = []
        therapeutic_area_result_list = []

        for therapeutic_area in therapeutic_area_total_checkbox:

            self.press_button(self.therapeutic_area_filter_css)
            therapeutic_area_total_checkbox = self.driver.find_elements(self.therapeutic_area_checkbox_css[0], self.therapeutic_area_checkbox_css[1])
            therapeutic_area_title_list.append(therapeutic_area_total_checkbox[therapeutic_area_index].get_attribute("title"))
            self.driver.execute_script("arguments[0].click()", therapeutic_area_total_checkbox[therapeutic_area_index])
            
            therapeutic_area_index = therapeutic_area_index + 1

            if therapeutic_area_index == 2:
                break

        therapeutic_area_index = 0
        for therapeutic_area in therapeutic_area_total_checkbox:

            therapeutic_area_total_checkbox = self.driver.find_elements(self.therapeutic_area_checkbox_css[0], self.therapeutic_area_checkbox_css[1])
            value_of_css = therapeutic_area_total_checkbox[therapeutic_area_index].value_of_css_property("background-color")
            hex = Color.from_string(value_of_css).hex
            therapeutic_area_checkbox_color_list.append(hex)
            
            
            therapeutic_area_index = therapeutic_area_index + 1
            
            if therapeutic_area_index == 2:
                break

        therapeutic_area_txt = self.get_element_text(self.therapeutic_area_filter_css)
        therapeutic_area_font_weight = self.get_css_property(self.therapeutic_area_btn_css, "font-family")
        
    
        therapeutic_area_filter_tags = self.driver.find_elements(self.quert_attr_css[0], self.quert_attr_css[1])

        for therapeutic_area_filter in therapeutic_area_filter_tags:

            therapeutic_area_filter_tag_list.append(therapeutic_area_filter.text)


        therapeutic_area_results = self.driver.find_elements(self.therapeutic_area_res_css[0], self.therapeutic_area_res_css[1])
        for therapeutic_area_result in therapeutic_area_results:
            therapeutic_area_result_list.append(therapeutic_area_result.text)

        return therapeutic_area_index, therapeutic_area_title_list, therapeutic_area_filter_tag_list, therapeutic_area_checkbox_color_list, therapeutic_area_result_list, therapeutic_area_txt, therapeutic_area_font_weight


    def indication_name_ele(self):

        indication_name_total_checkbox = self.driver.find_elements(self.indication_name_checkbox_css[0], self.indication_name_checkbox_css[1])
        indication_name_index = 0
        indication_name_title_list = []
        indication_name_filter_tag_list = []
        indication_name_checkbox_color_list = []
        indication_name_result_list = []

        for indication_name in indication_name_total_checkbox:

            self.press_button(self.indication_name_filter_css)
            indication_name_total_checkbox = self.driver.find_elements(self.indication_name_checkbox_css[0], self.indication_name_checkbox_css[1])
            indication_name_title_list.append(indication_name_total_checkbox[indication_name_index].get_attribute("title"))
            self.driver.execute_script("arguments[0].click()", indication_name_total_checkbox[indication_name_index])
            
            indication_name_index = indication_name_index + 1


        indication_name_index = 0
        for indication_name in indication_name_total_checkbox:

            indication_name_total_checkbox = self.driver.find_elements(self.indication_name_checkbox_css[0], self.indication_name_checkbox_css[1])
            indication_name_checkbox_color_list.append(indication_name_total_checkbox[indication_name_index].get_attribute("style"))
            
            indication_name_index = indication_name_index + 1
            

        indication_name_txt = self.get_element_text(self.indication_name_filter_css)
        indication_name_font_weight = self.get_css_property(self.indication_name_btn_css, "font-family")
        
    
        indication_name_filter_tags = self.driver.find_elements(self.quert_attr_css[0], self.quert_attr_css[1])

        for indication_name_filter in indication_name_filter_tags:

            indication_name_filter_tag_list.append(indication_name_filter.text)


        indication_name_results = self.driver.find_elements(self.indication_res_css[0], self.indication_res_css[1])
        for indication_name_result in indication_name_results:
            indication_name_result_list.append(indication_name_result.text)

        return indication_name_index, indication_name_title_list, indication_name_filter_tag_list, indication_name_checkbox_color_list, indication_name_result_list, indication_name_txt, indication_name_font_weight


    def clear_all_ele(self):

        self.press_button(self.clear_all_css)

        filter_tag_len = len(self.driver.find_elements(self.filter_tag_len_css[0], self.filter_tag_len_css[1]))

        return filter_tag_len


    def check_no_result(self, text):

        self.send_keys(self.search_input_field_xpath, text)
        self.press_button(self.search_btn_field_xpath)

        empty_txt = self.get_element_text(self.empty_css)

        return empty_txt

    def check_search_result(self, text):

        content_title_list = []
        self.send_keys(self.search_input_field_xpath, text)
        self.press_button(self.search_btn_field_xpath)

        contents = self.driver.find_elements(self.search_res_css[0], self.search_res_css[1])
        for content in contents:
            content_title_list.append(content.text)

        return content_title_list


    def pagination_front_arrow_back_arrow_validation(self):

        self.press_button(self.next_page_arrow_xpath)
        page_one_url = self.driver.current_url
        self.press_button(self.prev_page_arrow_xpath)
        page_zero_url = self.driver.current_url

        return page_one_url, page_zero_url