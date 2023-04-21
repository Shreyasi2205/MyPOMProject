import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from datetime import datetime
from Utilities.config import Utilities
import random
from datetime import date
from datetime import datetime, timedelta
import platform

class CareerSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    breadcrumb_lists_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li")
    search_btn_xpath = (By.XPATH, "//*[starts-with(@id,'edit-submit-career-search')]")
    download_css = (By.CSS_SELECTOR, "div.download-wrapper > a")
    career_title_css = (By.CSS_SELECTOR, ".clearfix > h1")
    career_desc_css = (By.CSS_SELECTOR, ".clearfix > p")
    anchor_tag_loc = (By.TAG_NAME, "a")
    table_header_names = ["Job Title", "Business", "Location", "Site", "Date Posted"]
    career_search_css = (By.CSS_SELECTOR, "ol.breadcrumb > li:last-child > a")
    clear_all_css = (By.CSS_SELECTOR, "a.clear-button")
    table_header_elements_css = (By.CSS_SELECTOR, "tr > th > a")
    date_posted_css = (By.CSS_SELECTOR, "label.date_posted")
    date_posted_elements_css = (By.CSS_SELECTOR, "div.item-list > div.count-filters > ul > li > a")
    search_input_field_xpath = (By.XPATH, "//*[starts-with(@id,'edit-search-api-fulltext')]")
    function_btn_css = (By.CSS_SELECTOR, "#ms-list-3 > button")
    location_btn_css = (By.CSS_SELECTOR, "#ms-list-2 > button")
    division_btn_css = (By.CSS_SELECTOR, "#ms-list-4 > button")
    function_txt_css = (By.CSS_SELECTOR, "#ms-list-3 > button > span")
    location_txt_css = (By.CSS_SELECTOR, "#ms-list-2 > button > span")
    division_txt_css = (By.CSS_SELECTOR, "#ms-list-4 > button > span")
    function_labels_css = (By.CSS_SELECTOR, "#ms-list-3 > div > ul > li > label")
    location_labels_css = (By.CSS_SELECTOR, "#ms-list-2 > div > ul > li > label")
    division_labels_css = (By.CSS_SELECTOR, "#ms-list-4 > div > ul > li > label")
    input_css = (By.CSS_SELECTOR, "input")
    filter_attr_css = (By.CSS_SELECTOR, "div.exposed-filters-wrapper > div")
    total_row_css = (By.CSS_SELECTOR, "tbody > tr")
    pagination_ele_css = (By.CSS_SELECTOR, "ul.pagination > li")
    page_link_css = (By.CSS_SELECTOR, ".page-link")
    rand_num = random.randint(1,10)
    random_job_title_css = (By.CSS_SELECTOR, f"table > tbody > tr:nth-child({rand_num}) > td:nth-child(1) > a")
    usa_checkbox_xpath = (By.XPATH, "//input[starts-with(@value, 'LOC_US') and contains(@type, 'checkbox')]")
    ireland_checkbox_xpath = (By.XPATH, "//input[starts-with(@value, 'LOC_IE') and contains(@type, 'checkbox')]")
    disclaimer_id = (By.ID, "block-disclaimerglobalcontent")
    disclaimer_title_css = (By.CSS_SELECTOR, "#block-disclaimerglobalcontent > div > div.field.field--name-field-title")
    disclaimer_desc_css = (By.CSS_SELECTOR, "#block-disclaimerglobalcontent > div > div.clearfix")
    search_result_css = (By.CSS_SELECTOR, "div.view-header") 
    alternative_location_css = (By.XPATH, "//span[text()='+Alternative Locations']")
    alternate_job_title_xpath = (By.XPATH,"parent::td/preceding-sibling::td[contains(@class,'job-title')]/a") 
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    mega_menu_career_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/careers') and not(contains(@target,'_self'))]//parent::li/p[@class='we-icon']")
    mega_menu_career_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/careers') and not(contains(@target,'_self'))]")
    mega_menu_career_search_xpath= (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'/career-search')]")
    job_title_css = (By.CSS_SELECTOR, "td > a")
    search_keyword = "Novartis"
    auto_suggestions_css = (By.CSS_SELECTOR,".search-api-autocomplete-suggestion")
    job_page_title_css = (By.CSS_SELECTOR, "h1.title > span")
    today_xpath = (By.XPATH,"(//tbody/tr/td[contains(@class,'views-field-field-job-posted-date')]/time)[1]")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    breadcrumb_lists_anchor_tag_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    career_last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child > a")
    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    footer_search_xpath = (By.XPATH, "//input[contains(@id, 'edit-keys')]")
    career_block_css = (By.CSS_SELECTOR, "section.section > div:nth-child(1)")
    career_block_present_css = (By.CSS_SELECTOR, "section.section > #block-careersearchtitle") 
    table_header_css = (By.CSS_SELECTOR, "th")
    table_header_font_css = (By.CSS_SELECTOR, "th > a")
    empty_css = (By.CSS_SELECTOR, ".view-empty")

    def launch_careerSearch(self,env_name):

        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_career_arrow_xpath)
            else:
                self.move_to_element(self.mega_menu_career_xpath)

            self.press_button(self.mega_menu_career_search_xpath)
        except:
            menu = Utilities.multi_language[env_name]['careers']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}') and not(contains(@target,'_self'))]"))
            submenu = Utilities.multi_language[env_name]['career-search']
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))


    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

            
    def click_career_search(self):

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.career_search_css)

    def clear_all(self):

        self.press_button(self.clear_all_css)

    def table_headers_title(self):

        table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])
        table_header_index = 0
        header_name_status = []

        for th in table_headers:

            table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])
            header_name_status.append(self.is_displayed_ele(table_headers[table_header_index]))
           
            table_header_index = table_header_index + 1

        return header_name_status

    def table_headers_sorting(self):

        table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])
        table_header_index = 0
        sort_ascending_list = []
        sort_descending_list = []

        for th in table_headers:

            table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])

            self.driver.execute_script("arguments[0].click()", table_headers[table_header_index])
            table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])
            sort_descending_list.append(table_headers[table_header_index].find_element(By.CSS_SELECTOR, "span").get_attribute("class"))


            self.driver.execute_script("arguments[0].click()", table_headers[table_header_index])
            table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])
            sort_ascending_list.append(table_headers[table_header_index].find_element(By.CSS_SELECTOR, "span").get_attribute("class"))

            table_header_index = table_header_index + 1

        return table_headers,sort_ascending_list, sort_descending_list

    def breadcrumb_ele(self):

        breadcrumb_items_status = []
        breadcrumb_lists = self.driver.find_elements(self.breadcrumb_lists_css[0], self.breadcrumb_lists_css[1])
        for breadcrumb_list in breadcrumb_lists:
            breadcrumb_items_status.append(self.is_displayed_ele(breadcrumb_list.find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1])))
            

        breadcrumb_first_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').getPropertyValue('content')";
        breadcrumb_first_arrow_element = self.driver.execute_script(breadcrumb_first_arrow_script);

        breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child'),'::before').getPropertyValue('content')";
        breadcrumb_second_arrow_element = self.driver.execute_script(breadcrumb_second_arrow_script);

        return breadcrumb_items_status, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element

    def check_all_breadcrumb_url(self):

        breadcumb_anchor_url_list = []
        breadcumb_anchor_current_url_list = []
        breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_tag_css[0], self.breadcrumb_lists_anchor_tag_css[1])
        breadcumb_index = 0
        for breadcumb_anchor in breadcumb_anchor_elements:

            breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_tag_css[0], self.breadcrumb_lists_anchor_tag_css[1])
            breadcumb_anchor_url_list.append(breadcumb_anchor_elements[breadcumb_index].get_attribute("href"))
            # self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
            try:
                if 'Windows' in platform.system():
                    ActionChains(self.driver).key_down(Keys.CONTROL).click(breadcumb_anchor_elements[breadcumb_index]).key_up(Keys.CONTROL).perform()
                elif 'Darwin' in platform.system():
                    ActionChains(self.driver).key_down(Keys.COMMAND).click(breadcumb_anchor_elements[breadcumb_index]).key_up(Keys.COMMAND).perform()
                self.driver.switch_to.window(self.driver.window_handles[1])

                # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
                # That's why we are pressing on mega menu two times to ignore the issue.
                self.press_button(self.mega_menu_btn_css)
                self.press_button(self.mega_menu_btn_css)
                
                breadcumb_anchor_current_url_list.append(self.driver.current_url)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            except:
                self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
                breadcumb_anchor_current_url_list.append(self.driver.current_url)
                self.driver.back()

            breadcumb_index = breadcumb_index + 1

            if breadcumb_index == 2:
                break

        return breadcumb_anchor_url_list, breadcumb_anchor_current_url_list 


    def date_posted_filter(self):

        active_date_list = []
        self.press_button(self.date_posted_css)
        date_elements = self.driver.find_elements(self.date_posted_elements_css[0], self.date_posted_elements_css[1])
        date_index = 0
        for date_ele in date_elements:

            date_elements = self.driver.find_elements(self.date_posted_elements_css[0], self.date_posted_elements_css[1])
            self.driver.execute_script("arguments[0].click()", date_elements[date_index])
            date_elements = self.driver.find_elements(self.date_posted_elements_css[0], self.date_posted_elements_css[1])
            active_date_list.append(date_elements[date_index].get_attribute("class"))

            date_index = date_index + 1

        return active_date_list

    def filter_location(self):

        filtered_location_list = []
        filterd_attributes_list = []
        location_count = 0

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)
        self.press_button(self.location_btn_css)
        location_elements = self.driver.find_elements(self.location_labels_css[0], self.location_labels_css[1])
        
        for ele in location_elements:

            self.driver.execute_script("arguments[0].click()", ele.find_element(self.input_css[0], self.input_css[1]))
            element = ele.find_element(self.input_css[0], self.input_css[1])
            selected_location_label = element.get_attribute("title")
            filtered_location_list.append(selected_location_label)
            location_count = location_count + 1
            if location_count == 5:
                break
        
        self.press_button(self.search_btn_xpath)

        filterd_attributes = self.driver.find_elements(self.filter_attr_css[0], self.filter_attr_css[1])
        for filtered_attr in filterd_attributes:

            if filtered_attr.text[-1] == "X":
                filterd_attributes_list.append(filtered_attr.text[:-1])
            else:
                filterd_attributes_list.append(filtered_attr.text)

        after_location_search_text = self.get_element_text(self.location_txt_css)
        location_font = self.get_css_property(self.location_txt_css,'font-family')
        

        return filtered_location_list,filterd_attributes_list,after_location_search_text,location_count,location_font

    def filter_function(self):

        filtered_function_list = []
        filterd_attributes_list = []
        function_count = 0

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)
        self.press_button(self.function_btn_css)
        function_elements = self.driver.find_elements(self.function_labels_css[0], self.function_labels_css[1])
        
        for ele in function_elements:

            self.driver.execute_script("arguments[0].click()", ele.find_element(self.input_css[0], self.input_css[1]))
            element = ele.find_element(self.input_css[0], self.input_css[1])
            selected_function_label = element.get_attribute("title")
            filtered_function_list.append(selected_function_label)
            function_count = function_count + 1
            if function_count == 5:
                break
        
        self.press_button(self.search_btn_xpath)

        filterd_attributes = self.driver.find_elements(self.filter_attr_css[0], self.filter_attr_css[1])
        for filtered_attr in filterd_attributes:

            if filtered_attr.text[-1] == "X":
                filterd_attributes_list.append(filtered_attr.text[:-1])
            else:
                filterd_attributes_list.append(filtered_attr.text)

        after_function_search_text = self.get_element_text(self.function_txt_css)
        function_font = self.get_css_property(self.function_txt_css,'font-family')

        return filtered_function_list,filterd_attributes_list,after_function_search_text ,function_count,function_font 

    def filter_division(self):

        filtered_division_list = []
        filterd_attributes_list = []
        division_count = 0

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)
        self.press_button(self.division_btn_css)
        division_elements = self.driver.find_elements(self.division_labels_css[0], self.division_labels_css[1])
        division_count = 0
        for ele in division_elements:

            self.driver.execute_script("arguments[0].click()", ele.find_element(self.input_css[0], self.input_css[1]))
            filtered_division_list.append(ele.find_element(By.CSS_SELECTOR, "input").get_attribute("title").split("(")[0])
            division_count = division_count + 1
            if division_count == 4:
                break

        
        self.press_button(self.search_btn_xpath)

        filterd_attributes = self.driver.find_elements(self.filter_attr_css[0], self.filter_attr_css[1])
        for filtered_attr in filterd_attributes:

            if filtered_attr.text[-1] == "X":
                filterd_attributes_list.append(filtered_attr.text[:-1])
            else:
                filterd_attributes_list.append(filtered_attr.text)
        
        after_division_search_text = self.get_element_text(self.division_txt_css)
        division_font = self.get_css_property(self.division_txt_css,'font-family')

        return filtered_division_list,filterd_attributes_list,after_division_search_text,division_count,division_font

   
    def pagination_validation(self):

        total_table_row_per_page = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])

        pagination_elements = self.driver.find_elements(self.pagination_ele_css[0], self.pagination_ele_css[1])
        print(len(pagination_elements))

        page_index = 0
        pagination_page_row_list_len = []
        total_row_per_page_list = []

        for pagination_element in pagination_elements:
            # page_index = 0
            # assert len(total_table_row_per_page) == 10
            total_row_per_page_list.append(len(total_table_row_per_page))

            pagination_elements = self.driver.find_elements(self.pagination_ele_css[0], self.pagination_ele_css[1])

            if page_index > 0 and page_index != 2:
                self.driver.execute_script("arguments[0].click()", pagination_elements[page_index].find_element(self.page_link_css[0], self.page_link_css[1]))
                pagination_page_row_list_len.append(len(self.driver.find_elements(self.pagination_ele_css[0], self.pagination_ele_css[1])))

                # if page_index > 1:
                #     assert f"page={page_index - 1}" in self.driver.current_url
                # else:
                #     assert f"page={page_index}" in self.driver.current_url

            page_index = page_index + 1
            if page_index == 6:
                break

        return total_row_per_page_list, pagination_page_row_list_len


    def random_job_click(self):

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)
        random_job_title_url = self.get_elemet_attribute(self.random_job_title_css, "href")
        self.press_button(self.random_job_title_css)

        return random_job_title_url

    

    def filter_usa(self):

        self.press_button(self.location_btn_css)
        self.press_button(self.usa_checkbox_xpath)
        self.press_button(self.search_btn_xpath)



    def filter_alternative_location(self):

        self.press_button(self.location_btn_css)
        self.press_button(self.ireland_checkbox_xpath)
        self.press_button(self.search_btn_xpath)


    def jobUrl_verification(self):

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        row_index = 0
        jobpage_url_list = []


        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))

            jobpage_url_list.append(self.driver.current_url)
            self.driver.back()
            
            row_index = row_index + 1
            if row_index == 4:
                break
        
        return jobpage_url_list


    def search_results(self):

        job_title_list = []
        count = 0
        auto_suggestions_text_list = []

        for i in range(2):

            self.send_keys(self.search_input_field_xpath, self.search_keyword)
            self.driver.find_element(*self.search_input_field_xpath).clear()
            self.send_keys(self.search_input_field_xpath, self.search_keyword)
            self.is_visible(self.auto_suggestions_css)
            auto_suggestions = self.driver.find_elements(*self.auto_suggestions_css)
            if count == 0:
                for suggestion in auto_suggestions:
                    auto_suggestions_text_list.append(suggestion.text)
            self.driver.execute_script("arguments[0].click()",auto_suggestions[count])
            job_title_text = self.get_element_text(self.job_page_title_css)
            job_title_list.append(job_title_text)
            count += 1
            self.driver.back()

        return job_title_list,auto_suggestions_text_list


    def date_posted_validations(self, env_name):

        date_posted_href_list = []
        date_posted_url_list = []
        count = 0
        date_posted_count_list = []
        job_date = ""
        job_latest_date = ""
        today_date = ""
        yesterday_date =""
        self.press_button(self.date_posted_css)
        date_elements = self.driver.find_elements(self.date_posted_elements_css[0], self.date_posted_elements_css[1])
        date_index = 0
        for date_ele in date_elements:

            date_elements = self.driver.find_elements(self.date_posted_elements_css[0], self.date_posted_elements_css[1])
            href = date_elements[date_index].get_attribute("href")
            date_posted_href_list.append(href)
            self.driver.execute_script("arguments[0].click()", date_elements[date_index])
            print(href)
            if date_index > 0:
                date_posted_count_list.append(count)
                date_posted_url_list.append(self.driver.current_url)
                if "job_posted_date=1" in self.driver.current_url and self.driver.find_elements(*self.total_row_css):
                    job_date = self.get_element_text(self.today_xpath)
                    if "switzerland" in env_name and "fr" not in env_name:
                        job_date = job_date.replace(".","")
                        job_latest_date = self.german_months(job_date)
                        job_latest_date = str(datetime.strptime(job_latest_date, '%d %B %Y')).split(" ")[0]
                        current_date = date.today()
                        today_date = current_date.strftime("%Y-%m-%d")
                        # today_date = current_date.strftime("%b %d, %Y")
                        yesterday_date = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
                        # yesterday_date = (datetime.now() - timedelta(1)).strftime("%b %d, %Y")
                    elif "switzerland-fr" in env_name:
                        job_latest_date = self.french_months(job_date)
                        job_latest_date = str(datetime.strptime(job_latest_date, '%d %B %Y')).split(" ")[0]
                        current_date = date.today()
                        today_date = current_date.strftime("%Y-%m-%d")
                        # today_date = current_date.strftime("%b %d, %Y")
                        yesterday_date = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
                        # yesterday_date = (datetime.now() - timedelta(1)).strftime("%b %d, %Y")
                    else:
                        current_date = date.today()
                        today_date = current_date.strftime("%b %d, %Y")
                        yesterday_date = (datetime.now() - timedelta(1)).strftime("%b %d, %Y")
                        job_latest_date = job_date
            date_index = date_index + 1
            count += 1

        return date_posted_url_list, today_date, yesterday_date, job_latest_date,date_posted_count_list


    def german_months(self, job_date):

        updated_job_date = ''
        if "Februar" in job_date:
            updated_job_date = job_date.replace("Februar", "February")
        elif "Januar" in job_date:
            updated_job_date = job_date.replace("Januar", "January")
        elif "März" in job_date:
            updated_job_date = job_date.replace("März", "March")
        elif "Oktober" in job_date:
            updated_job_date = job_date.replace("Oktober", "October")
        elif "Juli" in job_date:
            updated_job_date = job_date.replace("Juli", "July")
        elif "Juni" in job_date:
            updated_job_date = job_date.replace("Juni", "June")
        elif "Mai" in job_date:
            updated_job_date = job_date.replace("Mai", "May")
        elif "Dezember" in job_date:
            updated_job_date = job_date.replace("Dezember", "December")
        
        return updated_job_date


    def french_months(self, job_date):

        updated_job_date = ''
        if "avril" in job_date:
            updated_job_date = job_date.replace("avril", "April")
        elif "février" in job_date:
            updated_job_date = job_date.replace("février", "February")
        elif "mars" in job_date:
            updated_job_date = job_date.replace("mars", "March")
        elif "octobre" in job_date:
            updated_job_date = job_date.replace("octobre", "October")
        elif "juillet" in job_date:
            updated_job_date = job_date.replace("juillet", "July")
        elif "juin" in job_date:
            updated_job_date = job_date.replace("juin", "June")
        elif "mai" in job_date:
            updated_job_date = job_date.replace("mai", "May")
        elif "septembre" in job_date:
            updated_job_date = job_date.replace("septembre", "September")
        elif "décembre" in job_date:
            updated_job_date = job_date.replace("décembre", "December")
        elif "novembre" in job_date:
            updated_job_date = job_date.replace("novembre", "November")
        elif "août" in job_date:
            updated_job_date = job_date.replace("août", "August")
        elif "janvier" in job_date:
            updated_job_date = job_date.replace("janvier", "January")

        return updated_job_date

     # def table_headers(self):

    #     table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])

    #     table_header_index = 0
    #     header_name_list = []
    #     sort_ascending_list = []
    #     sort_descending_list = []

    #     for th in table_headers:

    #         table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])
    #         header_name_list.append(table_headers[table_header_index].text)

    #         self.driver.execute_script("arguments[0].click()", table_headers[table_header_index])
    #         table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])
    #         sort_descending_list.append(table_headers[table_header_index].find_element(By.CSS_SELECTOR, "span").get_attribute("class"))


    #         self.driver.execute_script("arguments[0].click()", table_headers[table_header_index])
    #         table_headers = self.driver.find_elements(self.table_header_elements_css[0], self.table_header_elements_css[1])
    #         sort_ascending_list.append(table_headers[table_header_index].find_element(By.CSS_SELECTOR, "span").get_attribute("class"))

    #         table_header_index = table_header_index + 1

    #     return header_name_list, sort_ascending_list, sort_descending_list


    # def filter_elements(self, search_txt):

    #     self.send_keys(self.search_input_field_xpath, search_txt)

    #     filtered_elements_list = []

    #     self.press_button(self.function_btn_css)
    #     function_elements = self.driver.find_elements(self.function_labels_css[0], self.function_labels_css[1])
    #     function_count = 0
    #     for ele in function_elements:

    #         self.driver.execute_script("arguments[0].click()", ele.find_element(self.input_css[0], self.input_css[1]))
    #         filtered_elements_list.append(ele.text)
    #         function_count = function_count + 1
    #         if function_count == 4:
    #             break

    #     self.press_button(self.location_btn_css)
    #     location_elements = self.driver.find_elements(self.location_labels_css[0], self.location_labels_css[1])
    #     location_count = 0
    #     for ele in location_elements:

    #         self.driver.execute_script("arguments[0].click()", ele.find_element(self.input_css[0], self.input_css[1]))
    #         filtered_elements_list.append(ele.text)
    #         location_count = location_count + 1
    #         if location_count == 4:
    #             break

    #     self.press_button(self.division_btn_css)
    #     division_elements = self.driver.find_elements(self.division_labels_css[0], self.division_labels_css[1])
    #     division_count = 0
    #     for ele in division_elements:

    #         self.driver.execute_script("arguments[0].click()", ele.find_element(self.input_css[0], self.input_css[1]))
    #         filtered_elements_list.append(ele.find_element(By.CSS_SELECTOR, "input").get_attribute("title").split("(")[0])
    #         division_count = division_count + 1
    #         if division_count == 4:
    #             break

    #     self.press_button(self.search_btn_xpath)

    #     filterd_attributes = self.driver.find_elements(self.filter_attr_css[0], self.filter_attr_css[1])

    #     filterd_attributes_list = []
    #     for filtered_attr in filterd_attributes:

    #         if filtered_attr.text[-1] == "X":
    #             filterd_attributes_list.append(filtered_attr.text[:-1])
    #         else:
    #             filterd_attributes_list.append(filtered_attr.text)
    #     filtered_url = self.driver.current_url


    #     self.clear_all()

    #     return filterd_attributes_list, filtered_elements_list, filtered_url



    



        