from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.color import Color





class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_icon_css = (By.CSS_SELECTOR, "li.nav-item.search > span")
    search_input_id = (By.XPATH, '//*[starts-with(@id,"edit-keyword")]')
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    # search_result_stg1_id = (By.ID, 'edit-keyword--4')
    search_result_xpath = (By.XPATH, "//input[contains(@id, 'edit-keyword')]")
    search_input_footer_id = (By.XPATH, '//input[contains(@id, "edit-keys")]')
    global_search_css = (By.CSS_SELECTOR, "#ms-list-1 > button > span")
    search_button_xpath = (By.XPATH, "//*[starts-with(@id, 'edit-submit-global-search')]")
    search_button_footer_id = (By.ID, "edit-submit")
    global_search_names = ["Global", "Digital", "ESG", "Media Center", "Careers"]
    clear_all_button_id = (By.ID, "section-uncheck-all")
    clear_all_button_css =(By.CSS_SELECTOR,".section-uncheck-all > input")
    # checks = 5
    close_search_css = (By.CSS_SELECTOR, "li.search > .nav-link.nav-link-")
    global_search_filter_css = (By.CSS_SELECTOR, "#ms-list-1 > div > ul > li > label")
    input_css = (By.CSS_SELECTOR, "input")
    tags_css = (By.CSS_SELECTOR, "#ms-list-3 > button > span")
    tags_btn_css = (By.CSS_SELECTOR, "#ms-list-3 > button")
    tag_elements_css = (By.CSS_SELECTOR, "#ms-list-3 > div > ul > li > label")
    pagination_css = (By.CSS_SELECTOR, "#pagination-heading")
    next_btn_xpath = (By.XPATH, "//a[contains(@rel, 'next')]")
    tag_filter_label_css = (By.CSS_SELECTOR, ".views-field-field-category > .field-content > a")
    tag_clear_xpath = (By.XPATH, "//input[contains(@id, 'tags-uncheck-all')]")
    suggestion_css = (By.CSS_SELECTOR, "ul#ui-id-1 > li")
    show_result_css = (By.CSS_SELECTOR, ".view-header")
    all_css = (By.XPATH, "//a[contains(@class, 'searchkeywordtypeall')]")
    tabs_css = (By.CSS_SELECTOR, "ul#block-globalsearchnavigation > li > a")
    relevance_css = (By.CSS_SELECTOR, "div.select-styled")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    search_page_urls_css = (By.CSS_SELECTOR, ".views-field-nid > span.field-content")
    no_result_xpath = (By.XPATH, "//div[@class = 'view-empty']")
    search_values = ["nov", "hub","news","new"]




    

    def click_global_search(self):

        self.press_button(self.global_search_css)

    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

    def verify_global_search_window(self):

        global_search_window_list = []
        index = 0
        global_search_lists = self.get_elements(self.global_search_filter_css)
        for search_list in global_search_lists:
            global_search_lists = self.get_elements(self.global_search_filter_css)
            global_search_window_list.append(global_search_lists[index].is_displayed())
            index += 1
            # assert name in self.get_element_text((By.CSS_SELECTOR, f"#ms-list-1 > div > ul > li:nth-child({count}) > label"))
        clear_all_status = self.is_displayed(self.clear_all_button_css)
        # assert "Clear All" in self.get_elemet_attribute(self.clear_all_button_id, "value")

        return global_search_window_list, clear_all_status

    def select_filter_global_search(self):


        filtered_search_list = []
        search_count = 0
        global_search_option = self.get_elements(self.global_search_filter_css)
        self.press_button(self.search_button_xpath)
        self.press_button(self.mega_menu_btn_css)
        self.press_button(self.mega_menu_btn_css)
        
        for option in global_search_option:

            global_search_option = self.get_elements(self.global_search_filter_css)
            self.driver.execute_script("arguments[0].click()", global_search_option[search_count].find_element(self.input_css[0], self.input_css[1]))
            global_search_option = self.get_elements(self.global_search_filter_css)
            filtered_search_list.append(global_search_option[search_count].text)
            search_count = search_count + 1
            if search_count == 2:
                break

        len_selected_filter = len(filtered_search_list)
        global_search_after_select = self.get_element_text(self.global_search_css)

        return len_selected_filter, global_search_after_select

    def clear_all(self):

        clear_all_status = []
        # self.click_global_search()
        # self.press_button(self.search_button_xpath)
        self.press_button(self.clear_all_button_id)
        global_search_without_number = self.get_element_text(self.global_search_css)
        global_search_option = self.get_elements(self.global_search_filter_css)
        for option in global_search_option:
            clear_all_status.append(option.find_element(self.input_css[0], self.input_css[1]).is_selected())
        global_search_text = self.get_element_text(self.global_search_css)

        return global_search_without_number, global_search_text,clear_all_status

    def close_search(self):

        self.press_button(self.close_search_css)
        return self.driver.current_url


    def tags_ele(self):

        counter = 0
        tags_number_list = []
        tag_filter_list = []
        tag_filter_set = set()
        tag_txt_before = str(self.driver.find_element(self.tags_css[0], self.tags_css[1]).text.encode("utf-8"))[1:].replace("'", "")
        self.press_button(self.tags_css)
        tag_elements = self.driver.find_elements(*self.tag_elements_css)
        tag_elements_len = len(tag_elements)
        for tag in tag_elements:
            tag_elements = self.driver.find_elements(*self.tag_elements_css)
            self.driver.execute_script("arguments[0].click()", tag_elements[counter])
            tag_filter_list.append(str(tag_elements[counter].text.encode("utf-8"))[1:].replace("'", ""))
            tags_number_list.append(str(self.driver.find_element(self.tags_css[0], self.tags_css[1]).text.encode("utf-8"))[1:].replace("'", ""))
            counter = counter + 1
            if tag_elements_len <= 5 and counter == tag_elements_len:
                break
            if tag_elements_len > 5 and counter == 5:
                break

        self.press_button(self.search_button_xpath)
        # tags_bold_font_family = self.get_css_property(self.tags_btn_css, "font-family")

        for i in range(2):
            
            tag_filters = self.driver.find_elements(*self.tag_filter_label_css)
            for tag_filter in tag_filters:
                tag_filter_set.add(str(tag_filter.text.encode("utf-8"))[1:].replace("'", ""))
            if self.driver.find_elements(*self.next_btn_xpath):
                self.press_button(self.next_btn_xpath)
            else:
                break
        self.press_button(self.tag_clear_xpath)
        tag_txt_after = str(self.driver.find_element(self.tags_css[0], self.tags_css[1]).text.encode("utf-8"))[1:].replace("'", "")

        return tag_txt_before, tag_txt_after, tags_number_list, tag_filter_list, tag_filter_set

    def auto_suggestion(self, text):

        auto_suggestion_list = []
        self.send_keys(self.search_input_id, text)
        self.driver.find_element(*self.search_input_id).clear()
        self.send_keys(self.search_input_id, text)
        auto_suggestions = self.driver.find_elements(*self.suggestion_css)
        self.get_element_text(self.suggestion_css)
        for sugg in auto_suggestions:
            auto_suggestion_list.append(sugg.text)
        # print(auto_suggestion_list)

        return auto_suggestion_list


    def get_result(self, search_text):
        content_len = 0 
        result_txt_display = False
        for text in search_text:
                self.send_keys(self.search_input_id, text)
                self.press_button(self.search_button_xpath)
                
                #if  "No Results found" == self.get_element_text(self.no_result_xpath):
                if self.driver.find_elements(*self.no_result_xpath):
                    self.driver.find_element(*self.search_input_id).clear()
                else:
                    result_txt = str(self.driver.find_element(self.show_result_css[0], self.show_result_css[1]).text.encode("utf-8"))[1:].replace("'", "")
                    result_txt_display = self.is_displayed(self.show_result_css)
                    result_txt_num = int(result_txt.split(" ")[1])
                    if result_txt_num > 0:
                        content_len = len(self.driver.find_elements(By.CSS_SELECTOR, "ul.each-result > li"))
                    break
        return content_len, result_txt_display

    
    

    def tabs_grey_bg(self):

        index = 0
        grey_bg_list = []
        tabs_ele = self.driver.find_elements(*self.tabs_css)
        for tab in tabs_ele:
            tabs_ele = self.driver.find_elements(*self.tabs_css)
            self.driver.execute_script("arguments[0].click()", tabs_ele[index])
            tabs_ele = self.driver.find_elements(*self.tabs_css)
            grey_bg_list.append(Color.from_string(tabs_ele[index].value_of_css_property("background-color")).hex)
            index = index + 1
        return grey_bg_list

    def text_display_inputfield_tab_change(self, text):

        index = 0
        text_list = []
        self.send_keys(self.search_input_id, text)
        self.press_button(self.search_button_xpath)

        tabs_ele = self.driver.find_elements(*self.tabs_css)
        for tab in tabs_ele:
            tabs_ele = self.driver.find_elements(*self.tabs_css)
            self.driver.execute_script("arguments[0].click()", tabs_ele[index])
            text_list.append(self.get_elemet_attribute(self.search_input_id, "value"))
            index = index + 1

        return text_list



    def search_results(self):

        search_url_list = []
        search_urls = self.driver.find_elements(*self.search_page_urls_css)
        search_url_index = 0

        for i in range(4):
            search_url_index = 0
            search_urls = self.driver.find_elements(*self.search_page_urls_css)
            for search_url in search_urls:

                search_urls = self.driver.find_elements(*self.search_page_urls_css)
                search_url_list.append(search_urls[search_url_index].text)

                search_url_index = search_url_index + 1

            if self.driver.find_elements(*self.next_btn_xpath):
                self.press_button(self.next_btn_xpath)
            else:
                break

        return search_url_list


    def footer_search_icon(self):

        search_icon_script = "return window.getComputedStyle(document.querySelector('#block-searchform > div > div > form > div > div'),'::after').getPropertyValue('background-image')";
        search_icon_element = self.driver.execute_script(search_icon_script);

        return search_icon_element



        


    
    # def select_filter_global_search(self):

    #     for check in range(self.checks):
    #         self.press_button((By.ID, f"ms-opt-{check+1}"))

    #     global_search_number = self.get_element_text(self.global_search_css)
    #     # assert f"Global Search ({self.checks})" in self.get_element_text(self.global_search_css)
        
    #     return global_search_number;