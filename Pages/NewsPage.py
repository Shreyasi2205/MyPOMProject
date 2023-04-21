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
from datetime import datetime
from Utilities.config import Utilities
import random
import platform

class NewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    banner_img_css = (By.CSS_SELECTOR, ".carousel_img_video > div.field > img")
    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    search_bar_id = (By.XPATH, "//input[starts-with(@id, 'edit-search-api-fulltext')]")
    search_btn_id = (By.XPATH, "//input[starts-with(@id, 'edit-submit-news-archive')]")
    search_txt = "Search"
    news_page_view_css = (By.CSS_SELECTOR, ".view.view-news-archive")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li")
    breadcrumb_lists_anchor_tag_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    anchor_tag_loc = (By.TAG_NAME, "a")
    news_archive_last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child > a")
    from_date_xpath = (By.XPATH, "//label[@for='edit-field-date--2']")
    to_date_xpath = (By.XPATH, "//label[@for='edit-field-date-1--2']")
    content_pages_css = (By.CSS_SELECTOR, "ul.whole-item > li")
    pagination_numbers_css = (By.CSS_SELECTOR, "ul.pagination > li")
    pagination_links_css = (By.CSS_SELECTOR, ".page-link")
    all_topics_css = (By.XPATH,"//ul[(@id='block-newsarchivenavigation')]/li/a[(contains(@class, 'news-archive') or contains(@class, 'noticias-arquivo-de-noticias') or contains(@class, 'ultimas-noticias')) and not(contains(@class, 'type'))]")
    news_archive_url_txt = "news/news-archive"
    tab_elements_css = (By.CSS_SELECTOR, "#block-newsarchivenavigation > li.nav-item")
    key_releases_css = (By.CSS_SELECTOR, "a.key-releases-language")
    media_release_css = (By.CSS_SELECTOR, "a.media-releases-language")
    media_release_secondary_xpath = (By.XPATH, "//a[contains(@class, 'media-release')]")
    lang_tab_css = (By.CSS_SELECTOR, ".media-release-language-filter > label")
    media_release_content_css = (By.CSS_SELECTOR, "ul.whole-item > li")
    card_wrapper_id = (By.ID, "list-card-wrapper")
    card_date_css = (By.CSS_SELECTOR, "span.views-field-field-date > span")
    toggle_text_css = (By.CSS_SELECTOR, ".toggle_text")
    view_css = (By.CSS_SELECTOR,"div.view.view-news-archive")
    view_toggle_icon = (By.CSS_SELECTOR, ".toggle_icon")
    empty_css = (By.CSS_SELECTOR, ".view-empty")
    pagination_heading_xpath = (By.XPATH, "//nav[@aria-label='pagination-heading']")
    next_page_arrow_xpath = (By.XPATH, "//a[@rel='next']")
    prev_page_arrow_xpath = (By.XPATH, "//a[@rel='prev']")
    right_hand_rail_xpath = (By.XPATH,"//div[contains(@id,'right-hand-rail-block')]")
    pagination_pages_css = (By.CSS_SELECTOR, "ul.pagination > li")
    page_link_css = (By.CSS_SELECTOR, ".page-link")
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    mega_menu_news_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]//parent::li/p[@class='we-icon']")
    mega_menu_news_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]")
    mega_menu_news_archive_xapth= (By.XPATH, "//a[contains(@href,'/news/news-archive') and not(contains(@href, '?'))]")
    # mega_menu_news_archive_sandoz_xapth= (By.XPATH, "//a[contains(@href,'/news/news-archive') and not(contains(@href, 'media_release'))]")
    arctic_list_grid_view_css = (By.CSS_SELECTOR, "div.view.view-news-archive")
    search_input_field_xpath = (By.XPATH, "//*[starts-with(@id,'edit-search-api-fulltext')]")
    test_data = "Test"
    test_data_novartis = "Novartis"
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    card_label_css = (By.CSS_SELECTOR,'.views-field-type > span.field-content')
    featured_news_tab_xpath = (By.XPATH,"//li[contains(@class,'nav-item')]/a[contains(@href,'type=news') and not(contains(@href,'&news'))]")
    # featured_news_tab_xpath = (By.XPATH, "//a[(contains(@class, 'archivetypenews') or contains(@class, 'medien-pressemitteilungentypenews') or contains(@class, 'ajankohtaista-uutiset') or contains(@class, 'news-archivio-newstypenews')) and not(contains(@class, 'newsnews'))]")
    news_contents_css = (By.CSS_SELECTOR, "div.item-list > ul.whole-item > li > a")
    mediaRelease_last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3) > a")

    newsArchive_images_css = (By.CSS_SELECTOR,'.whole-item >.each-item > a >.views-field>span>img')
    images_css = (By.CSS_SELECTOR,'.field>img')
    banner_text_css = (By.CSS_SELECTOR,'.stripe_title')
    key_releases_text_xpath = (By.XPATH,'//*[@class="section"]/div[1]')
    ellipses_xpath = (By.XPATH,"//*[contains(@class,'show-hides')]")
    non_visible_ellipses_xpath = (By.XPATH,"//li[contains(@class,'nonvisibleelement')]/a")
    visible_element_xpath = (By.XPATH,"//li[contains(@class,'visibleelement')] [not(contains(@class,'nonvisibleelement'))]")
    link_btn_css = (By.CSS_SELECTOR, "a.link_button.button_text")

    def launch_newsArchive(self,env_name):

        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_news_arrow_xpath)
            else:
                self.move_to_element(self.mega_menu_news_xpath)
            # if env_name == "sandoz":
            #     self.press_button(self.mega_menu_news_archive_sandoz_xapth)
            # else:
            self.press_button(self.mega_menu_news_archive_xapth)
        except:
            menu = Utilities.multi_language[env_name]['news']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['news-archive']
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))

    def search_bar_and_btn(self):

        search_bar = self.is_displayed(self.search_input_field_xpath)
        search_btn = self.is_displayed(self.search_btn_id)

        return search_bar, search_btn

    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)


    def breadcrumb_ele(self):

        breadcrumb_items = []
        breadcrumb_lists = self.driver.find_elements(self.breadcrumb_lists_css[0], self.breadcrumb_lists_css[1])
        for breadcrumb_list in breadcrumb_lists:
            breadcrumb_items.append(breadcrumb_list.find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).text)


        breadcrumb_first_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').getPropertyValue('content')";
        breadcrumb_first_arrow_element = self.driver.execute_script(breadcrumb_first_arrow_script);

        breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3)'),'::before').getPropertyValue('content')";
        breadcrumb_second_arrow_element = self.driver.execute_script(breadcrumb_second_arrow_script);

        return breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element


    def all_topics_grey_color(self):

        all_topics_text_status = self.is_displayed(self.all_topics_css)
        hex_code = self.get_css_color(self.all_topics_css,"background-color")
        
        return all_topics_text_status, hex_code


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


    def grey_menu_verify(self):

        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        count = 0
        hex_color_list = []
        empty_list = []

        while tab_elements_len > 0:

            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            if self.driver.find_elements(self.empty_css[0], self.empty_css[1]):
                empty_list.append(self.get_elemet_attribute(self.empty_css, "class"))
            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            color = tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property("background-color")
            hex = Color.from_string(color).hex
            # rgb = int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[0]), int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[1]), int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[2])
            # hex_code = self.rgb_to_hex(rgb)
            # assert "#f1f1f1" in hex_code
            hex_color_list.append(hex)
            count = count + 1
            tab_elements_len = tab_elements_len - 1

        return hex_color_list, empty_list

    def media_release(self, env_name):

        if self.driver.find_elements(self.media_release_css[0], self.media_release_css[1]):
            self.press_button(self.media_release_css)
        elif self.driver.find_elements(self.media_release_secondary_xpath[0], self.media_release_secondary_xpath[1]):
            self.press_button(self.media_release_secondary_xpath)
            
        # language_tab_txt = ''
        # if env_name == "global":
        #     language_tab_txt = self.get_element_text(self.lang_tab_css)

        elements = self.driver.find_elements(self.media_release_content_css[0], self.media_release_content_css[1])
        ele_list = []
        ele_list_sorted = []
        ch_date_format_list = []
        desc_sort = False

        for element in elements:
            a = element.find_element(self.card_wrapper_id[0], self.card_wrapper_id[1])

            if "switzerland-fr" in env_name:
                ele_list.append(a.find_element(self.card_date_css[0], self.card_date_css[1]).text)
            elif "switzerland" in env_name:
                ele_list.append(a.find_element(self.card_date_css[0], self.card_date_css[1]).text.replace(".",""))
            elif "china" in env_name:
                ele_list.append(str(a.find_element(self.card_date_css[0], self.card_date_css[1]).text.encode("utf-8"))[1:].replace("'","").replace("\\xe6\\x9c\\x88", "").replace(",", ""))
            elif "taiwan" in env_name:
                ele_list.append(str(a.find_element(self.card_date_css[0], self.card_date_css[1]).text.encode("utf-8"))[1:].replace("'","").replace("\\xe6\\x9c\\x88", "").replace(",", ""))
            elif "global" == env_name:
                ele_list.append(a.find_element(self.card_date_css[0], self.card_date_css[1]).text.replace(",", ""))
            else:
                ele_list.append(str(a.find_element(self.card_date_css[0], self.card_date_css[1]).text.encode("utf-8"))[1:].replace("'",""))

        if "switzerland-fr" in env_name:
            ch_date_format_list = self.french_months(ele_list)
            ele_list_sorted = ch_date_format_list[:]
            ele_list_sorted.sort(key = lambda date: datetime.strptime(date, '%d %B %Y'), reverse=True)
            if ele_list_sorted == ch_date_format_list:
                desc_sort = True
        elif "switzerland" in env_name:
            ch_date_format_list = self.german_months(ele_list)
            ele_list_sorted = ch_date_format_list[:]
            ele_list_sorted.sort(key = lambda date: datetime.strptime(date, '%d %B %Y'), reverse=True)
            if ele_list_sorted == ch_date_format_list:
                desc_sort = True
        elif "china" in env_name:
            chinese_date_format_list = self.chinese_months(ele_list)
            ele_list_sorted = chinese_date_format_list[:]
            ele_list_sorted.sort(key = lambda date: datetime.strptime(date, '%b %d %Y'), reverse=True)
            if ele_list_sorted == chinese_date_format_list:
                desc_sort = True
        elif "taiwan" in env_name:
            chinese_date_format_list = self.chinese_months(ele_list)
            ele_list_sorted = chinese_date_format_list[:]
            ele_list_sorted.sort(key = lambda date: datetime.strptime(date, '%b %d %Y'), reverse=True)
            if ele_list_sorted == chinese_date_format_list:
                desc_sort = True
        else:
            ele_list_sorted = ele_list[:]
            ele_list_sorted.sort(key = lambda date: datetime.strptime(date, '%b %d %Y'), reverse=True)
            if ele_list_sorted == ele_list:
                desc_sort = True
            
        
        
        return desc_sort


    def german_months(self, date_list):

        german_date_list = []
        for date in date_list:
            if "Februar" in date:
                german_date_list.append(date.replace("Februar", "February"))
            elif "Januar" in date:
                german_date_list.append(date.replace("Januar", "January"))
            elif "März" in date:
                german_date_list.append(date.replace("März", "March"))
            elif "Oktober" in date:
                german_date_list.append(date.replace("Oktober", "October"))
            elif "Juli" in date:
                german_date_list.append(date.replace("Juli", "July"))
            elif "Juni" in date:
                german_date_list.append(date.replace("Juni", "June"))
            elif "Mai" in date:
                german_date_list.append(date.replace("Mai", "May"))
            elif "Dezember" in date:
                german_date_list.append(date.replace("Dezember", "December"))
            else:
                german_date_list.append(date)
        return german_date_list


    def french_months(self, date_list):

        french_date_list = []
        for date in date_list:
            if "avril" in date:
                french_date_list.append(date.replace("avril", "April"))
            elif "février" in date:
                french_date_list.append(date.replace("février", "February"))
            elif "mars" in date:
                french_date_list.append(date.replace("mars", "March"))
            elif "octobre" in date:
                french_date_list.append(date.replace("octobre", "October"))
            elif "juillet" in date:
                french_date_list.append(date.replace("juillet", "July"))
            elif "juin" in date:
                french_date_list.append(date.replace("juin", "June"))
            elif "mai" in date:
                french_date_list.append(date.replace("mai", "May"))
            elif "septembre" in date:
                french_date_list.append(date.replace("septembre", "September"))
            elif "décembre" in date:
                french_date_list.append(date.replace("décembre", "December"))
            elif "novembre" in date:
                french_date_list.append(date.replace("novembre", "November"))
            elif "août" in date:
                french_date_list.append(date.replace("août", "August"))
            elif "janvier" in date:
                french_date_list.append(date.replace("janvier", "January"))
            else:
                french_date_list.append(date)
        return french_date_list

    def chinese_months(self, date_list):

        chinese_date_list = []
        d = ''
        m = ''
        y = ''
        for date in date_list:
            if "1" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("1", "Jan")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "2" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("2", "Feb")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "3" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("3", "Mar")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "4" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("4", "Apr")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "5" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("5", "May")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "6" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("6", "Jun")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "7" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("7", "Jul")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "8" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("8", "Aug")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "9" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("9", "Sep")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "10" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("10", "Oct")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "11" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("11", "Nov")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            elif "12" in date.split(" ")[0]:
                m = date.split(" ")[0].replace("12", "Dec")
                d = date.split(" ")[1]
                y = date.split(" ")[2]
                chinese_date_list.append(m + " " + d + " " + y)
            else:
                chinese_date_list.append(date)
        return chinese_date_list


    def key_releases(self, env_name):

        self.press_button(self.key_releases_css)
        language_tab_txt = ''
        if env_name == "global":
            language_tab_txt = self.get_element_text(self.lang_tab_css)

        return language_tab_txt

    def toggle_view(self):

        self.press_button(self.toggle_text_css)
        toggle_btn_txt = self.get_element_text(self.toggle_text_css)
        current_view_txt = self.get_elemet_attribute(self.view_css, "class")
        view_icon = self.get_css_property(self.view_toggle_icon, "background")

        return toggle_btn_txt, current_view_txt, view_icon

    def pagination_number(self):

        num_content_page = len(self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1]))
        pagination_num = len(self.driver.find_elements(self.pagination_numbers_css[0], self.pagination_numbers_css[1]))
        current_page_num = []
        page_num = []

        if num_content_page == 12 and pagination_num > 0:

            pagination = self.driver.find_elements(self.pagination_numbers_css[0], self.pagination_numbers_css[1])
            pagination_len = len(pagination)
            count = 0
            

            for i in range(1,pagination_len-1):
                if pagination[count].find_element(self.pagination_links_css[0], self.pagination_links_css[1]).text == i :
                    current_page_num.append(pagination[count].find_element(self.pagination_links_css[0], self.pagination_links_css[1]).text)
                    page_num.append(i)
                count = count + 1

        return current_page_num, page_num

    def pagination_validation(self):

       
        num_content_page = len(self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1]))
        pagination_heading = len(self.driver.find_elements(self.pagination_heading_xpath[0], self.pagination_heading_xpath[1]))
        pagination_count = 0
        page_content_list = []
        while pagination_count <= 3:

            pagination_pages = self.driver.find_elements(self.pagination_pages_css[0], self.pagination_pages_css[1])
            if len(pagination_pages[pagination_count].find_elements(self.page_link_css[0], self.page_link_css[1])) > 0 and "1" != pagination_pages[pagination_count].find_element(self.page_link_css[0], self.page_link_css[1]).text:
                self.driver.execute_script("arguments[0].click()", pagination_pages[pagination_count].find_element(self.page_link_css[0], self.page_link_css[1]))
                page_content_list.append(self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1]))
                
            pagination_count = pagination_count + 1
            pagination_pages = self.driver.find_elements(self.pagination_pages_css[0], self.pagination_pages_css[1])
            try:
                pagination_pages[pagination_count].find_element(self.page_link_css[0], self.page_link_css[1]).text
            except: 
                break

        return num_content_page,pagination_heading, page_content_list



    def pagination_front_arrow_back_arrow_validation(self):

        num_content_page = len(self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1]))
        pagination_heading = len(self.driver.find_elements(self.pagination_heading_xpath[0], self.pagination_heading_xpath[1]))
        self.press_button(self.next_page_arrow_xpath)
        page_one_contents = self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1])
        self.press_button(self.prev_page_arrow_xpath)
        page_zero_contents = self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1])

        return num_content_page,pagination_heading,page_one_contents, page_zero_contents


    def grid_view(self):

        self.press_button(self.toggle_text_css)
        grid_icon = self.get_css_property(self.view_toggle_icon, "background")
        grid_view_btn = self.is_displayed(self.toggle_text_css)
        list_view = self.get_elemet_attribute(self.arctic_list_grid_view_css, "class")

        return grid_icon,grid_view_btn,list_view 

    def list_view(self):

        list_icon = self.get_css_property(self.view_toggle_icon, "background")
        list_view_btn = self.is_displayed(self.toggle_text_css)
        # self.press_button(self.toggle_text_css)
        grid_view = self.get_elemet_attribute(self.arctic_list_grid_view_css, "class")

        return list_icon,list_view_btn,grid_view 

    def verify_search_result(self):

        self.send_keys(self.search_input_field_xpath, self.test_data)
        self.press_button(self.search_btn_id)

        searched_keyword = self.get_elemet_attribute(self.search_input_field_xpath,"value")

        return searched_keyword


    def grey_menu_verify_with_Tabs(self):

        self.send_keys(self.search_input_field_xpath, self.test_data)
        self.press_button(self.search_btn_id)
        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        count = 0
        hex_color_list = []

        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            color = tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property("background-color")
            hex = Color.from_string(color).hex
            hex_color_list.append(hex)
            count = count + 1
            tab_elements_len = tab_elements_len - 1

        return hex_color_list

    def verify_searchText_with_Tabs(self):

        self.send_keys(self.search_input_field_xpath, self.test_data)
        self.press_button(self.search_btn_id)
        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        count = 0
        searched_keyword_status = []
        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            searched_keyword_status.append(self.get_elemet_attribute(self.search_input_field_xpath,"value"))

            count = count + 1
            tab_elements_len = tab_elements_len - 1

        return searched_keyword_status


    def verify_menuTab_url(self):

        count = 0
        href = []
        tab_href_list = []
        selected_tab_url_list = []
        self.send_keys(self.search_input_field_xpath, self.test_data)
        self.press_button(self.search_btn_id)
        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        
        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            element = tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1])
            ele_href = element.get_attribute("href")
            if "type" in ele_href:
                tab_href = element.get_attribute("href")
                href = tab_href.split("type")
                tab_href_list.append(href[1])

            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            if count > 0 :
                selected_tab_url_list.append(self.driver.current_url)
            
            count = count + 1
            tab_elements_len = tab_elements_len - 1

        return tab_href_list, selected_tab_url_list

 
    def verify_searchText_with_url(self):

        selected_tab_url_list = []
        self.send_keys(self.search_input_field_xpath, self.test_data)
        self.press_button(self.search_btn_id)
        searched_keyword = self.get_elemet_attribute(self.search_input_field_xpath,"value")
        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        count = 0
        searched_keyword_status = []
        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            selected_tab_url_list.append(self.driver.current_url)

            count = count + 1
            tab_elements_len = tab_elements_len - 1

        return searched_keyword,selected_tab_url_list


    def search_results(self):

        count = 0
        content_title = [] 
        self.send_keys(self.search_input_field_xpath, self.test_data_novartis)
        self.press_button(self.search_btn_id)
        contents = self.get_elements(self.content_pages_css)

        for content in contents:
            contents = self.get_elements(self.content_pages_css)
            element = contents[count].find_element(By.CSS_SELECTOR,'a .views-field-title>span')
            content_title.append(element.text)

        return (content_title)


    def verify_filters(self):

        count = 0
        index = 0 
        card_label_set = set()
        filter_name_list = []
        lower_filter_name_list = []
        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        tabs_len = tab_elements_len-1
        tab_label_list = []
        menu_tab_list = []
        for i in range(tabs_len):
                 
            i = set()
            tab_label_list.append(i)
                  
        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            element = tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1])
            ele_href = element.get_attribute("href")
            if "type" in ele_href:
            
                self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
                active_tab = self.driver.find_element(By.CSS_SELECTOR,".active-tab")
                filter_name_list.append(str(active_tab.text.encode('utf-8'))[1:].replace("'",""))
                card_labels = self.driver.find_elements(*self.card_label_css)
                for label in card_labels:
                    tab_label_list[index].add((str(label.text.encode('utf-8'))[1:].replace("'","")).lower())
                index = index + 1
            count = count + 1
            tab_elements_len = tab_elements_len - 1

        for filter_name in filter_name_list:  
            lower_filter_name_list.append(filter_name.lower())

        for filter_name in lower_filter_name_list:
            if "stories" in filter_name:
                menu_tab_list.append(filter_name.replace("stories", "story"))
            else :
                menu_tab_list.append(filter_name)


        return menu_tab_list , tab_label_list


    def featured_news_details_breadcrumb_display(self):

        featured_news_contents = self.driver.find_elements(self.news_contents_css[0], self.news_contents_css[1])
        featured_news_contents_len = len(featured_news_contents)
        random_content_number = random.randint(0,featured_news_contents_len-1)
        index = 0

        breadcrumb_items_len_list = []
        breadcrumb_items_list = []
        breadcrumb_first_arrow_element_list = []
        breadcrumb_second_arrow_element_list = []
        color_list =[]

        for featured_news in featured_news_contents:

            random_content_number = random.randint(0,featured_news_contents_len-1)

            featured_news_contents = self.driver.find_elements(self.news_contents_css[0], self.news_contents_css[1])

            self.driver.execute_script("arguments[0].click()", featured_news_contents[random_content_number])

            breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element = self.breadcrumb_ele()


            breadcrumb_items_len_list.append(len(breadcrumb_items))
            breadcrumb_items_list.append(breadcrumb_items)
            breadcrumb_first_arrow_element_list.append(breadcrumb_first_arrow_element)
            breadcrumb_second_arrow_element_list.append(breadcrumb_second_arrow_element)
            color_list.append(self.get_css_color(self.mediaRelease_last_child_breadcrumb_color_css, "color"))
            


            index = index + 1

            if index == 4:
                break

            self.driver.back()

        return breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list, breadcrumb_items_list,color_list


    def news_details_breadcrumb_display(self):

        news_contents = self.driver.find_elements(self.news_contents_css[0], self.news_contents_css[1])
        news_contents_len = len(news_contents)
        random_content_number = random.randint(0,news_contents_len-1)
        index = 0

        breadcrumb_items_len_list = []
        breadcrumb_items_list = []
        breadcrumb_first_arrow_element_list = []
        breadcrumb_second_arrow_element_list = []
        color_list = []

        for news in news_contents:

            random_content_number = random.randint(0,news_contents_len-1)

            news_contents = self.driver.find_elements(self.news_contents_css[0], self.news_contents_css[1])

            self.driver.execute_script("arguments[0].click()", news_contents[random_content_number])

            if self.driver.find_elements(By.CSS_SELECTOR, ".ui-dialog-buttonset"):
                self.press_button((By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(2)"))
            else:
                breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element = self.breadcrumb_ele()

                breadcrumb_items_len_list.append(len(breadcrumb_items))
                breadcrumb_items_list.append(breadcrumb_items)
                breadcrumb_first_arrow_element_list.append(breadcrumb_first_arrow_element)
                breadcrumb_second_arrow_element_list.append(breadcrumb_second_arrow_element)
                color_list.append(self.get_css_color(self.mediaRelease_last_child_breadcrumb_color_css, "color"))
                self.driver.back()


            index = index + 1

            if index == 4:
                break

            

        return breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list, breadcrumb_items_list,color_list


    
    def media_release_details_breadcrumb_display(self):

        media_release_contents = self.driver.find_elements(self.news_contents_css[0], self.news_contents_css[1])
        media_release_contents_len = len(media_release_contents)
        random_content_number = random.randint(0,media_release_contents_len-1)
        index = 0

        breadcrumb_items_len_list = []
        breadcrumb_first_arrow_element_list = []
        breadcrumb_second_arrow_element_list = []
        color_list = []

        for media_release in media_release_contents:

            random_content_number = random.randint(0,media_release_contents_len-1)

            media_release_contents = self.driver.find_elements(self.news_contents_css[0], self.news_contents_css[1])

            self.driver.execute_script("arguments[0].click()", media_release_contents[random_content_number])

            breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element = self.breadcrumb_ele()


            breadcrumb_items_len_list.append(len(breadcrumb_items))
            breadcrumb_first_arrow_element_list.append(breadcrumb_first_arrow_element)
            breadcrumb_second_arrow_element_list.append(breadcrumb_second_arrow_element)
            color_list.append(self.get_css_color(self.mediaRelease_last_child_breadcrumb_color_css, "color"))

            index = index + 1

            if index == 4:
                break

            self.driver.back()

        return breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, breadcrumb_items_len_list,color_list
    def newsArchive_images_validation(self):

        display_list = []
        alt_list = []
        title_list = []
        natural_width_list =[]
        href_images = []
        index = 0 
        image_index = 0
        newsArchive_images = self.driver.find_elements(*self.newsArchive_images_css)
        if len(newsArchive_images) > 0 :
            for image in newsArchive_images:

                newsArchive_images = self.driver.find_elements(*self.newsArchive_images_css)
                href_images.append(index)
                
                self.driver.execute_script("arguments[0].click()", newsArchive_images[index])
                image_count = 0
                images = self.driver.find_elements(*self.images_css)
                for image in images :
                    images = self.driver.find_elements(*self.images_css)
                    display_list.append(images[image_count].get_attribute("src"))
                    alt_list.append(images[image_count].get_attribute("alt"))
                    title_list.append(images[image_count].get_attribute("title"))
                    natural_width_list.append(images[image_count].get_attribute("naturalWidth"))
                    image_count = image_count + 1
                index = index + 1
                time.sleep(4)
                self.driver.back()
                
        return display_list, alt_list, title_list,natural_width_list, href_images


    def menu_tab_one_grey_bg(self):

        tab_elements_len = len(self.driver.find_elements(*self.tab_elements_css))
        count = 0
        tab_elements = self.driver.find_elements(*self.tab_elements_css)
        first_tab_color = ''
        second_tab_color = ''

        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(*self.tab_elements_css)
            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            tab_elements = self.driver.find_elements(*self.tab_elements_css)

            if count > 0:
                second_tab_color = Color.from_string(tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property('background-color')).hex
                first_tab_color = Color.from_string(tab_elements[count-1].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property('background-color')).hex

            count = count + 1
            tab_elements_len = tab_elements_len - 1
            if count == 2:
                break

        return first_tab_color, second_tab_color
        
