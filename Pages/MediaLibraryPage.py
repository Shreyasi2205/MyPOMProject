import time
import pytest
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.color import Color
from Utilities.config import Utilities



class MediaLibraryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    arctic_list_grid_view_css = (By.CSS_SELECTOR, "div.view.view-media-library1")
    media_library_breadcrumb_color_css = (By.CSS_SELECTOR, "ol.breadcrumb >li:last-child > a")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "ol.breadcrumb > li")
    # ol.breadcrumb > li
    anchor_tag_loc = (By.TAG_NAME, "a")
    content_pages_css = (By.CSS_SELECTOR, "div.item-list > ul.whole-item > li")
    # div.item-list > ul.whole-item > li
    pagination_heading_xpath = (By.XPATH, "//nav[@aria-label='pagination-heading']")
    pagination_pages_css = (By.CSS_SELECTOR, "ul.pagination > li")
    # ul.pagination > li
    page_link_css = (By.CSS_SELECTOR, ".page-link")
    next_page_arrow_xpath = (By.XPATH, "//a[@title='Go to next page']")
    prev_page_arrow_xpath = (By.XPATH, "//a[@title='Go to previous page']")
    toggle_text_css = (By.CSS_SELECTOR, ".toggle_text")
    tab_elements_css = (By.CSS_SELECTOR, "div > ul > li.list-group-item")
    view_toggle_icon = (By.CSS_SELECTOR, ".toggle_icon")
    protected_items_css = (By.CSS_SELECTOR, "ul.whole-item > li.protected-item")
    lock_icon_css = (By.CSS_SELECTOR, "div.document-asset-lock > div")
    lock_icon_no_img_css = (By.CSS_SELECTOR, "div > div.document-asset-lock > div")
    image_tab_xpath = (By.XPATH, "//ul[contains(@class,'pop-list')]/li/a[contains(@href,'/image')]")
    doc_tab_xpath = (By.XPATH, "//ul[contains(@class,'pop-list')]/li/a[contains(@href,'/document')]")
    video_tab_xpath = (By.XPATH, "//ul[contains(@class,'pop-list')]/li/a[contains(@href,'/video')]")
    contents_css = (By.CSS_SELECTOR, "ul.whole-item > li")
    data_id_css = (By.CSS_SELECTOR, ".media-row-click")
    content_card_css = (By.CSS_SELECTOR, ".media-row-click > div.views-field > span > div > div.arctic-over-view-img")
    kaltura_video_frame_css = (By.CSS_SELECTOR, "div.kWidgetIframeContainer > iframe")
    youtube_video_frame_css = (By.CSS_SELECTOR, "div.video-embed-field-provider-youtube > iframe")
    content_deatils_txt_css = (By.CSS_SELECTOR, "div.clearfix.text-formatted.field.field--label-inline")
    content_title_txt_css = (By.CSS_SELECTOR, ".field__label")
    content_desc_txt_css = (By.CSS_SELECTOR, ".field__item")
    unprotected_download_btn_css = (By.CSS_SELECTOR, "a.btm-download")
    protected_download_btn_css = (By.CSS_SELECTOR, "div.col-sm-6.media_content > .media_usage_right > .field > .field__item > div.paragraph > div.lockbtnwrap > a")
    protected_content_img_css = (By.CSS_SELECTOR, ".col-sm-6.media_img > .field > .field__item > .paragraph > div.lockimagewrap.opt > a.use-ajax > img")
    unprotected_img_css = (By.CSS_SELECTOR, "div.col-sm-6.media_img > img")
    breadcrumb_lists_anchor_tag_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    yes_btn_xpath = (By.XPATH, "//a[starts-with(@id, 'edit-yes')]")
    no_btn_xpath = (By.XPATH, "//a[starts-with(@id, 'edit-no')]")
    all_menu_xpath = (By.XPATH,"(//ul[@class='pop-list list-group']/li/a)[1]")
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    mega_menu_media_library_xpath= (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'/media-library')]")
    mega_menu_news_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]//parent::li/p[@class='we-icon']")
    mega_menu_news_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]")
    media_content_css = (By.CSS_SELECTOR, ".views-field-title")
    
    lock_icon_overview_img_css = (By.CSS_SELECTOR, "#media-row-click > div > span > div > div.arctic-over-view-img")
    label_list = ["Description", "Usage Rights & Restrictions"]
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    mediaLibrary_images_css = (By.CSS_SELECTOR,'.arctic-over-view-img>img')
    images_css = (By.CSS_SELECTOR,'.img')
    search_bar = (By.CSS_SELECTOR,'[id="edit-title"]')
    search_button = (By.XPATH,'//input[contains(@id,"edit-submit-media-library")]')
    related_items_css = (By.CSS_SELECTOR,"[class='whole-item']>.each-item")
    related_items_anchor_css = (By.CSS_SELECTOR,'a')
    related_itmes_title_css = (By.CSS_SELECTOR,'.field--name-title')
    reset_button = (By.XPATH,"//*[contains(@id,'reset')]")
    related_items_title_xpath = (By.XPATH,"//*[contains(@id,'media-library-related-items')]/h2")
    labels_css = (By.CSS_SELECTOR,'div>div>span>div>div.arctic-over-view-content>div.arctic-over-view-category')
    fact_sheet_tab_xpath = (By.XPATH, "//ul[contains(@class,'pop-list')]/li/a[contains(@href,'/fact-sheet')]")


    def launch_mediaLibrary(self,env_name):

        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_news_arrow_xpath)
            else:
                self.move_to_element(self.mega_menu_news_xpath)

            self.press_button(self.mega_menu_media_library_xpath)
        except:
            menu = Utilities.multi_language[env_name]['news']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['media-library']
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))
            

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

        breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child'),'::before').getPropertyValue('content')";
        breadcrumb_second_arrow_element = self.driver.execute_script(breadcrumb_second_arrow_script);


        return breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element


    def breadcrumbs_firstLevel_secondLevel(self):

        breadcumb_anchor_url_list = []
        breadcumb_anchor_current_url_list = []
        breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_tag_css[0], self.breadcrumb_lists_anchor_tag_css[1])
        breadcumb_index = 0
        for breadcumb_anchor in breadcumb_anchor_elements:

            breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_tag_css[0], self.breadcrumb_lists_anchor_tag_css[1])
            breadcumb_anchor_url_list.append(breadcumb_anchor_elements[breadcumb_index].get_attribute("href"))
            self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
            breadcumb_anchor_current_url_list.append(self.driver.current_url)
            self.driver.back()

            breadcumb_index = breadcumb_index + 1

            if breadcumb_index == 2:
                break

        return breadcumb_anchor_url_list, breadcumb_anchor_current_url_list

    def pagination_validation(self):

        num_content_page = len(self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1]))
        pagination_heading = len(self.driver.find_elements(self.pagination_heading_xpath[0], self.pagination_heading_xpath[1]))
        pagination_count = 0
        # current_page_url = []
        page_content_list = []
        while pagination_count <= 2:

            pagination_pages = self.driver.find_elements(self.pagination_pages_css[0], self.pagination_pages_css[1])
            if len(pagination_pages[pagination_count].find_elements(self.page_link_css[0], self.page_link_css[1])) > 0 and "1" != pagination_pages[pagination_count].find_element(self.page_link_css[0], self.page_link_css[1]).text:
                self.driver.execute_script("arguments[0].click()", pagination_pages[pagination_count].find_element(self.page_link_css[0], self.page_link_css[1]))
                # assert f"page={pagination_count}" in self.driver.current_url
                # current_page_url.append(self.driver.current_url)
                # page_content_list.append(len(self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1])))
                page_content_list.append(self.driver.find_elements(self.content_pages_css[0], self.content_pages_css[1]))
                # self.driver.back()
                
            pagination_count = pagination_count + 1

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
        grid_view_btn = self.get_element_text(self.toggle_text_css)
        list_view = self.get_elemet_attribute(self.arctic_list_grid_view_css, "class")

        return grid_icon,grid_view_btn,list_view 

    def list_view(self):

        list_icon = self.get_css_property(self.view_toggle_icon, "background")
        list_view_btn = self.get_element_text(self.toggle_text_css)
        # self.press_button(self.toggle_text_css)
        grid_view = self.get_elemet_attribute(self.arctic_list_grid_view_css, "class")

        return list_icon,list_view_btn,grid_view 


    def media_title_no_paragraph_tag(self):

        toggle_icon = self.get_css_property(self.view_toggle_icon, "background")
        if "list.svg" in toggle_icon:
            self.press_button(self.toggle_text_css)
        
        content_titles_list = []

        content_titles = self.driver.find_elements(*self.media_content_css)

        for title in content_titles:
            content_titles_list.append(title.text)

        return content_titles_list


    def grey_menu_verify(self):

        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        count = 0
        hex_color_list = []

        while tab_elements_len > 0:

            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            color = tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property("background-color")
            hex = Color.from_string(color).hex
            # rgb = int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[0]), int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[1]), int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[2])
            # hex_code = self.rgb_to_hex(rgb)
            # assert "#f1f1f1" in hex_code
            hex_color_list.append(hex)
            count = count + 1
            tab_elements_len = tab_elements_len - 1

        return hex_color_list

    def lock_icon_verify(self):

        content_pages_locked = self.driver.find_elements(self.protected_items_css[0], self.protected_items_css[1])

        index = 0
        pages = 2
        hex_color_list = []
        document_type_locked= []
        document_type_locked_1 = []

        for p in range(pages):
            index = 0
            content_pages_locked = self.driver.find_elements(self.protected_items_css[0], self.protected_items_css[1])
            for i in content_pages_locked:
                content_pages_locked = self.driver.find_elements(self.protected_items_css[0], self.protected_items_css[1])
                color = content_pages_locked[index].value_of_css_property("background-color")
                hex = Color.from_string(color).hex
                hex_color_list.append(hex)

                if len(content_pages_locked[index].find_elements(self.lock_icon_overview_img_css[0], self.lock_icon_overview_img_css[1])) > 0:

                    lock_img_ele = content_pages_locked[index].find_element(self.lock_icon_overview_img_css[0], self.lock_icon_overview_img_css[1])
                    lock_img_attr = content_pages_locked[index].find_element(self.lock_icon_overview_img_css[0], self.lock_icon_overview_img_css[1]).get_attribute("class")
                    
                    if "no-img" in lock_img_attr:
                        document_type_locked.append(lock_img_ele.find_element(self.lock_icon_no_img_css[0], self.lock_icon_no_img_css[1]).get_attribute("class"))
                    else:
                        document_type_locked_1.append(lock_img_ele.find_element(self.lock_icon_css[0], self.lock_icon_css[1]).get_attribute("class"))


                index = index + 1
            self.press_button(self.next_page_arrow_xpath)
            # if "No results found" in self.driver.page_source:
            #     break
        
        self.press_button(self.media_library_breadcrumb_color_css)
        return hex_color_list,document_type_locked,document_type_locked_1

       
    def video(self):

        contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

        content_index = 0
        index = 0
        # flag = 0
        video_page_label_list = []
        video_desc_page_label_list = []
        flag_list = []
        video_frame_len_list = []
        video_page_url_list = []
        current_page_url_list = []


        for content in contents:

            contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

            if len(contents) > 0:

                video_page_url_list.append(contents[content_index].find_element(self.data_id_css[0], self.data_id_css[1]).get_attribute("data-id"))
                self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
                current_page_url_list.append(self.driver.current_url)

                if len(self.driver.find_elements(self.kaltura_video_frame_css[0], self.kaltura_video_frame_css[1])) > 0:
                    video_frame_len_list.append(len(self.driver.find_elements(self.kaltura_video_frame_css[0], self.kaltura_video_frame_css[1])))
                    flag_list.append(1)
                elif len(self.driver.find_elements(self.youtube_video_frame_css[0], self.youtube_video_frame_css[1])) > 0:
                    video_frame_len_list.append(len(self.driver.find_elements(self.youtube_video_frame_css[0], self.youtube_video_frame_css[1])))
                    flag_list.append(1)
                
                labels = self.driver.find_elements(self.content_deatils_txt_css[0], self.content_deatils_txt_css[1])
                for label in labels:
                    if len(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text) > 0:
                        video_page_label_list.append(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text)
                        video_desc_page_label_list.append(label.find_element(self.content_desc_txt_css[0], self.content_desc_txt_css[1]).text)

                self.driver.back()

                index = index + 1
            content_index = content_index + 1

            if index == 4:
                break
        return index, video_page_label_list, video_desc_page_label_list, video_frame_len_list, flag_list, video_page_url_list, current_page_url_list

        
    def unprotected_doc(self):

        contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

        content_index = 0
        index = 0
        # img_src_list = []
        btn_clickable_list = []
        unprotected_doc_page_label_list = []
        unprotected_doc_desc_page_label_list = []
        unprotected_doc_page_url_list = []
        current_page_url_list = []


        for content in contents:

            contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

            if "protected-item" not in contents[content_index].get_attribute("class"):

                unprotected_doc_page_url_list.append(contents[content_index].find_element(self.data_id_css[0], self.data_id_css[1]).get_attribute("data-id"))
                self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
                current_page_url_list.append(self.driver.current_url)
    
                btn_clickable_list.append(self.element_clickable(self.unprotected_download_btn_css))

                
                
                labels = self.driver.find_elements(self.content_deatils_txt_css[0], self.content_deatils_txt_css[1])
                for label in labels:
                    if len(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text) > 0:
                        unprotected_doc_page_label_list.append(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text)
                        unprotected_doc_desc_page_label_list.append(label.find_element(self.content_desc_txt_css[0], self.content_desc_txt_css[1]).text)

                self.driver.back()

                index = index + 1
            content_index = content_index + 1

            if index == 4:
                break
        return index, btn_clickable_list, unprotected_doc_page_label_list, unprotected_doc_desc_page_label_list, unprotected_doc_page_url_list, current_page_url_list



    def protected_doc(self):

        contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

        content_index = 0
        index = 0
        img_src_list = []
        btn_clickable_list = []
        pop_up_window_list = []
        yes_btn_clickable_list = []
        current_page_url_list = []
        current_page_url_one_list = []
        protected_doc_page_label_list = []
        protected_doc_desc_page_label_list = []
        protected_doc_page_url_list = []
        protected_doc_current_page_url_list = []


        for content in contents:

            contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

            if "protected-item" in contents[content_index].get_attribute("class"):

                protected_doc_page_url_list.append(contents[content_index].find_element(self.data_id_css[0], self.data_id_css[1]).get_attribute("data-id"))
                self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
                protected_doc_current_page_url_list.append(self.driver.current_url)

                img_src_list.append(self.get_elemet_attribute(self.protected_content_img_css, "src"))
                btn_clickable_list.append(self.element_clickable(self.protected_download_btn_css))

                
                
                labels = self.driver.find_elements(self.content_deatils_txt_css[0], self.content_deatils_txt_css[1])
                for label in labels:
                    if len(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text) > 0:
                        protected_doc_page_label_list.append(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text)
                        protected_doc_desc_page_label_list.append(label.find_element(self.content_desc_txt_css[0], self.content_desc_txt_css[1]).text)


                self.press_button(self.protected_download_btn_css)
                pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one = self.pop_up_window()
                pop_up_window_list.append(pop_up_window)
                yes_btn_clickable_list.append(yes_btn_clickable)
                current_page_url_list.append(current_page_url)
                current_page_url_one_list.append(current_page_url_one)

                self.driver.back()

                index = index + 1
            content_index = content_index + 1

            if index == 4:
                break
        return index, img_src_list, btn_clickable_list, protected_doc_page_label_list, protected_doc_desc_page_label_list, pop_up_window_list, yes_btn_clickable_list, current_page_url_list, current_page_url_one_list, protected_doc_page_url_list, protected_doc_current_page_url_list



    def unprotected_img(self):

        contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

        content_index = 0
        index = 0
        img_src_list = []
        btn_clickable_list = []
        unprotected_img_page_label_list = []
        unprotected_img_desc_page_label_list = []
        unprotected_img_page_url_list = []
        unprotected_img_current_page_url_list = []


        for content in contents:


            contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

            if "protected-item" not in contents[content_index].get_attribute("class"):

                unprotected_img_page_url_list.append(contents[content_index].find_element(self.data_id_css[0], self.data_id_css[1]).get_attribute("data-id"))
                self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
                unprotected_img_current_page_url_list.append(self.driver.current_url)
                img_src_list.append(self.get_elemet_attribute(self.unprotected_img_css, "src"))
                btn_clickable_list.append(self.element_clickable(self.unprotected_download_btn_css))

                
                
                labels = self.driver.find_elements(self.content_deatils_txt_css[0], self.content_deatils_txt_css[1])
                for label in labels:
                    if len(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text) > 0:
                        unprotected_img_page_label_list.append(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text)
                        unprotected_img_desc_page_label_list.append(label.find_element(self.content_desc_txt_css[0], self.content_desc_txt_css[1]).text)

                self.driver.back()

                index = index + 1
            content_index = content_index + 1

            if index == 4:
                break
        return index, img_src_list, btn_clickable_list, unprotected_img_page_label_list, unprotected_img_desc_page_label_list, unprotected_img_page_url_list, unprotected_img_current_page_url_list


    def protected_img(self):

        contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

        content_index = 0
        index = 0
        img_src_list = []
        btn_clickable_list = []
        pop_up_window_list = []
        yes_btn_clickable_list = []
        current_page_url_list = []
        current_page_url_one_list = []
        protected_img_page_label_list = []
        protected_img_desc_page_label_list = []
        protected_img_page_url_list = []
        protected_img_current_page_url_list = []


        for content in contents:

            contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

            if "protected-item" in contents[content_index].get_attribute("class"):

                protected_img_page_url_list.append(contents[content_index].find_element(self.data_id_css[0], self.data_id_css[1]).get_attribute("data-id"))
                self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
                protected_img_current_page_url_list.append(self.driver.current_url)

                img_src_list.append(self.get_elemet_attribute(self.protected_content_img_css, "src"))

                btn_clickable_list.append(self.element_clickable(self.protected_download_btn_css))

                
                
                labels = self.driver.find_elements(self.content_deatils_txt_css[0], self.content_deatils_txt_css[1])
                for label in labels:
                    if len(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text) > 0:
                        protected_img_page_label_list.append(label.find_element(self.content_title_txt_css[0], self.content_title_txt_css[1]).text)
                        protected_img_desc_page_label_list.append(label.find_element(self.content_desc_txt_css[0], self.content_desc_txt_css[1]).text)


                self.press_button(self.protected_content_img_css)
                pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one = self.pop_up_window()
                pop_up_window_list.append(pop_up_window)
                yes_btn_clickable_list.append(yes_btn_clickable)
                current_page_url_list.append(current_page_url)
                current_page_url_one_list.append(current_page_url_one)

                self.driver.back()

                index = index + 1
            content_index = content_index + 1

            if index == 4:
                break
        return index, img_src_list, btn_clickable_list, protected_img_page_label_list, protected_img_desc_page_label_list, pop_up_window_list, yes_btn_clickable_list, current_page_url_list, current_page_url_one_list, protected_img_page_url_list, protected_img_current_page_url_list


    def pop_up_window(self):

        # the following line now fails in STG1 on ARC-2.4.4 - 5-JAN-2022
        pop_up_window = self.get_elemet_attribute((By.CSS_SELECTOR, "div.ui-dialog"), "role")
        yes_btn_clickable = self.element_clickable(self.yes_btn_xpath)
        current_page_url = self.driver.current_url
        self.press_button(self.no_btn_xpath)
        current_page_url_one = self.driver.current_url

        return pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one


    def mediaLibrary_images_validation(self):

        display_list = []
        alt_list = []
        title_list = []
        natural_width_list =[]
        index = 0 
        image_index = 0
        mediaLirary_images = self.driver.find_elements(*self.mediaLibrary_images_css)
        if len(mediaLirary_images) > 0 :
            for image in mediaLirary_images:

                mediaLirary_images = self.driver.find_elements(*self.mediaLibrary_images_css)
                self.driver.execute_script("arguments[0].click()", mediaLirary_images[index])
                images = self.driver.find_elements(*self.images_css)
                for image in images :
                    images = self.driver.find_elements(*self.images_css)
                    display_list.append(images[image_index].get_attribute("src"))
                    alt_list.append(images[image_index].get_attribute("alt"))
                    title_list.append(images[image_index].get_attribute("title"))
                    natural_width_list.append(images[image_index].get_attribute("naturalWidth"))
                index = index + 1
                self.driver.back()
                
        return display_list, alt_list, title_list,natural_width_list


    def related_items(self):

        contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])

        content_index = 0

        related_items_len = []
        related_items_title_len = []
        index = 0
        related_items_href_list = []
        current_page_url_list = []
        label_list = []

        for content in contents:

            contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])


            label_len = len(contents[content_index].find_element(self.labels_css[0], self.labels_css[1]).text)
            
            if label_len > 0:
                
                self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
                related_items = self.driver.find_elements(*self.related_items_css)
                related_items_len.append(len(related_items))
                related_items_title = self.driver.find_elements(self.related_items_title_xpath[0], self.related_items_title_xpath[1])
                related_items_title_len.append(len(related_items_title))

                related_items_index = 0
                for items in related_items:
                    related_items = self.driver.find_elements(*self.related_items_css)
                    related_items_href_list.append(related_items[related_items_index].find_element(self.related_items_anchor_css[0],self.related_items_anchor_css[1]).get_attribute('href'))
                    self.driver.execute_script("arguments[0].click()", related_items[related_items_index].find_element(self.related_items_anchor_css[0],self.related_items_anchor_css[1]))
                    self.is_visible(self.related_itmes_title_css)
                    current_page_url_list.append(self.driver.current_url)
                    related_items_index += 1
                    self.driver.back()

                self.driver.back()

                index = index + 1
                content_index = content_index + 1

                if index == 4:
                    break
        return index,related_items_len, related_items_href_list ,current_page_url_list,related_items_title_len




    # def unprotected_img_click(self):

    #     contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])
    #     content_index = 0
    #     for content in contents:

    #         contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])
    #         if "protected-item" not in contents[content_index].get_attribute("class"):

    #             img_url = contents[content_index].find_element(By.ID, "media-row-click").get_attribute("data-id")
    #             self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
    #             return img_url

    #         content_index = content_index + 1
        

    # def check_unprotected_img(self):

        
    #     self.press_button(self.image_tab_link_txt)

    #     pages = 3
    #     flag = 0
    #     d = dict()

    #     if "pagination" in self.driver.page_source:
    #         for page in range(pages):

    #             img_url = self.unprotected_img_click()
    #             if img_url:
    #                 flag = 1
    #                 break
    #             if len(self.driver.find_elements(By.XPATH, "//a[contains(@title, 'Go to next page')]")) > 0:
    #                 self.press_button((By.XPATH, "//a[contains(@title, 'Go to next page')]"))

    #     else:
    #         img_url = self.unprotected_img_click()
    #         if img_url:
    #             flag = 1

    #     if flag == 1:
    #         d['page_url'] = self.driver.current_url
    #         d['img_url'] = img_url

    #         d['img_src'] = self.get_elemet_attribute((By.CSS_SELECTOR, "div.col-sm-6.media_img > img"), "src")

    #         d['btn_clickable'] = self.element_clickable((By.CSS_SELECTOR, "a.apply_btn"))
    #         unprotected_img_page_label_list = []
    #         unprotected_img_desc_page_label_list = []
    #         # index = 0
    #         labels = self.driver.find_elements(By.CSS_SELECTOR, "div.clearfix.text-formatted")
    #         for label in labels:
    #             if len(label.find_element(By.CSS_SELECTOR, ".field__label").text) > 0:
    #                 unprotected_img_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__label").text)
    #                 unprotected_img_desc_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__item > p").text)

    #         d['unprotected_img_page_label_list'] = unprotected_img_page_label_list
    #         d['unprotected_img_desc_page_label_list'] = unprotected_img_desc_page_label_list

    #         return d
    #     else:
    #         return d



    # def protected_img_click(self):

    #     contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])
    #     content_index = 0
    #     for content in contents:

    #         contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])
    #         if "protected-item" in contents[content_index].get_attribute("class"):

    #             img_url = contents[content_index].find_element(By.ID, "media-row-click").get_attribute("data-id")
    #             self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
    #             return img_url

    #         content_index = content_index + 1



    # def check_protected_img(self):

        
    #     self.press_button(self.image_tab_link_txt)
    #     pages = 3
    #     flag = 0
    #     d = dict()

    #     if "pagination" in self.driver.page_source:
    #         for page in range(pages):

    #             img_url = self.protected_img_click()
    #             if img_url:
    #                 flag = 1
    #                 break
    #             if len(self.driver.find_elements(By.XPATH, "//a[contains(@title, 'Go to next page')]")) > 0:
    #                 self.press_button((By.XPATH, "//a[contains(@title, 'Go to next page')]"))

    #     else:
    #         img_url = self.protected_img_click()
    #         if img_url:
    #             flag = 1

    #     if flag == 1:
    #         d['page_url'] = self.driver.current_url
    #         d['img_url'] = img_url
    #         d['img_src'] = self.get_elemet_attribute((By.CSS_SELECTOR, ".col-sm-6.media_img > .field > .field__item > .paragraph > div.lockimagewrap.opt > a.use-ajax > img"), "src")

    #         self.press_button((By.CSS_SELECTOR, ".col-sm-6.media_img > .field > .field__item > .paragraph > div.lockimagewrap.opt > a.use-ajax > img"))

    #         pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one = self.pop_up_window()
    #         d['pop_up_window'] = pop_up_window
    #         d['yes_btn_clickable'] = yes_btn_clickable
    #         d['current_page_url'] = current_page_url
    #         d['current_page_url_one'] = current_page_url_one


    #         d['download_btn'] = self.get_element_text((By.CSS_SELECTOR, "div.col-sm-6.media_content > .media_usage_right > .field > .field__item > div.paragraph > div.lockbtnwrap > a.link_button"))
    #         self.press_button((By.CSS_SELECTOR, "div.col-sm-6.media_content > .media_usage_right > .field > .field__item > div.paragraph > div.lockbtnwrap > a.link_button"))

    #         pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one = self.pop_up_window()
    #         d['pop_up_window'] = pop_up_window
    #         d['yes_btn_clickable'] = yes_btn_clickable
    #         d['current_page_url'] = current_page_url
    #         d['current_page_url_one'] = current_page_url_one
    #         protected_img_page_label_list = []
    #         protected_img_desc_page_label_list = []
    #         # index = 0
    #         labels = self.driver.find_elements(By.CSS_SELECTOR, "div.clearfix.text-formatted")
    #         for label in labels:
    #             if len(label.find_element(By.CSS_SELECTOR, ".field__label").text) > 0:
    #                 protected_img_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__label").text)
    #                 protected_img_desc_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__item > p").text)
    #         d['protected_img_page_label_list'] = protected_img_page_label_list
    #         d['protected_img_desc_page_label_list'] = protected_img_desc_page_label_list


    #         return d
    #     else:
    #         return d



    # def unprotected_doc_click(self):

    #     contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])
    #     content_index = 0
    #     for content in contents:

    #         contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])
    #         if "protected-item" not in contents[content_index].get_attribute("class"):

    #             doc_url = contents[content_index].find_element(By.ID, "media-row-click").get_attribute("data-id")
    #             self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
    #             return doc_url

    #         content_index = content_index + 1


    # def check_unprotected_doc(self):

        
    #     self.press_button(self.doc_tab_link_txt)
    #     pages = 3
    #     flag = 0
    #     d = dict()

    #     if "pagination" in self.driver.page_source:
    #         for page in range(pages):

    #             img_url = self.unprotected_doc_click()
    #             if img_url:
    #                 flag = 1
    #                 break
    #             if len(self.driver.find_elements(By.XPATH, "//a[contains(@title, 'Go to next page')]")) > 0:
    #                 self.press_button((By.XPATH, "//a[contains(@title, 'Go to next page')]"))

    #     else:
    #         img_url = self.unprotected_doc_click()
    #         if img_url:
    #             flag = 1

    #     if flag == 1:
    #         d['page_url'] = self.driver.current_url
    #         d['img_url'] = img_url
    #         d['btn_clickable'] = self.element_clickable((By.CSS_SELECTOR, "a.apply_btn"))
    #         d['btn'] = self.get_element_text((By.CSS_SELECTOR, "a.apply_btn"))
    #         unprotected_doc_page_label_list = []
    #         unprotected_doc_desc_page_label_list = []
    #         # index = 0
    #         labels = self.driver.find_elements(By.CSS_SELECTOR, "div.clearfix.text-formatted")
    #         for label in labels:
    #             if len(label.find_element(By.CSS_SELECTOR, ".field__label").text) > 0:
    #                 unprotected_doc_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__label").text)
    #                 unprotected_doc_desc_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__item > p").text)
    #         d['unprotected_doc_page_label_list'] = unprotected_doc_page_label_list
    #         d['unprotected_doc_desc_page_label_list'] = unprotected_doc_desc_page_label_list

    #         return d
    #     else:
    #         return d


    # def protected_doc_click(self):

    #     contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])
    #     content_index = 0
    #     for content in contents:

    #         contents = self.driver.find_elements(self.contents_css[0], self.contents_css[1])
    #         if "protected-item" in contents[content_index].get_attribute("class"):

    #             img_url = contents[content_index].find_element(By.ID, "media-row-click").get_attribute("data-id")
    #             self.driver.execute_script("arguments[0].click()", contents[content_index].find_element(self.content_card_css[0], self.content_card_css[1]))
    #             return img_url

    #         content_index = content_index + 1



    # def check_protected_doc(self):

        
    #     self.press_button(self.doc_tab_link_txt)
    #     pages = 3
    #     flag = 0
    #     d = dict()

    #     if "pagination" in self.driver.page_source:
    #         for page in range(pages):

    #             img_url = self.protected_doc_click()
    #             if img_url:
    #                 flag = 1
    #                 break
    #             if len(self.driver.find_elements(By.XPATH, "//a[contains(@title, 'Go to next page')]")) > 0:
    #                 self.press_button((By.XPATH, "//a[contains(@title, 'Go to next page')]"))

    #     else:
    #         img_url = self.protected_doc_click()
    #         if img_url:
    #             flag = 1

    #     if flag == 1:
    #         d['page_url'] = self.driver.current_url
    #         d['img_url'] = img_url
    #         d['img_src'] = self.get_elemet_attribute((By.CSS_SELECTOR, ".col-sm-6.media_img > .field > .field__item > .paragraph > div.lockimagewrap.opt > a.use-ajax > img"), "src")

    #         self.press_button((By.CSS_SELECTOR, ".col-sm-6.media_img > .field > .field__item > .paragraph > div.lockimagewrap.opt > a.use-ajax > img"))

    #         pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one = self.pop_up_window()
    #         d['pop_up_window'] = pop_up_window
    #         d['yes_btn_clickable'] = yes_btn_clickable
    #         d['current_page_url'] = current_page_url
    #         d['current_page_url_one'] = current_page_url_one


    #         d['download_btn'] = self.get_element_text((By.CSS_SELECTOR, "div.col-sm-6.media_content > .media_usage_right > .field > .field__item > div.paragraph > div.lockbtnwrap > a.link_button"))
    #         self.press_button((By.CSS_SELECTOR, "div.col-sm-6.media_content > .media_usage_right > .field > .field__item > div.paragraph > div.lockbtnwrap > a.link_button"))

    #         pop_up_window, yes_btn_clickable, current_page_url, current_page_url_one = self.pop_up_window()
    #         d['pop_up_window'] = pop_up_window
    #         d['yes_btn_clickable'] = yes_btn_clickable
    #         d['current_page_url'] = current_page_url
    #         d['current_page_url_one'] = current_page_url_one

    #         protected_doc_page_label_list = []
    #         protected_doc_desc_page_label_list = []
    #         # index = 0
    #         labels = self.driver.find_elements(By.CSS_SELECTOR, "div.clearfix.text-formatted")
    #         for label in labels:
    #             if len(label.find_element(By.CSS_SELECTOR, ".field__label").text) > 0:
    #                 protected_doc_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__label").text)
    #                 protected_doc_desc_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__item > p").text)
    #         d['protected_doc_page_label_list'] = protected_doc_page_label_list
    #         d['protected_doc_desc_page_label_list'] = protected_doc_desc_page_label_list

    #         return d
    #     else:
    #         return d

            


 


    # def check_video_page(self):

    #     flag = 0
        
    #     self.press_button(self.video_tab_link_txt)
    
    #     video_page_url = self.get_elemet_attribute((By.CSS_SELECTOR, "#media-row-click"), "data-id")
    #     self.press_button((By.CSS_SELECTOR, "#media-row-click > div > span > div > div.arctic-over-view-img > img"))

    #     assert video_page_url in self.driver.current_url

    #     if len(self.driver.find_elements(By.CSS_SELECTOR, "div.kWidgetIframeContainer > iframe")) > 0:
    #         video_frame_len = len(self.driver.find_elements(By.CSS_SELECTOR, "div.kWidgetIframeContainer > iframe"))
    #         flag = 1
    #     elif len(self.driver.find_elements(By.CSS_SELECTOR, "div.video-embed-field-provider-youtube > iframe")) > 0:
    #         video_frame_len = self.driver.find_elements(By.CSS_SELECTOR, "div.video-embed-field-provider-youtube > iframe")
    #         flag = 1


    #     video_page_label_list = []
    #     video_page_desc_label_list = []
    #     # index = 0
    #     labels = self.driver.find_elements(By.CSS_SELECTOR, "div.clearfix.text-formatted")
    #     for label in labels:
    #         if len(label.find_element(By.CSS_SELECTOR, ".field__label").text) > 0:
    #                 video_page_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__label").text)
    #                 video_page_desc_label_list.append(label.find_element(By.CSS_SELECTOR, ".field__item > p").text)
    #         # index = index + 1

    #     return video_page_label_list, video_page_desc_label_list, flag, video_frame_len




    



    