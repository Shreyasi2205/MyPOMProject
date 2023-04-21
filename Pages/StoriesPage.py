import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from Utilities.config import Utilities
import random
from selenium.webdriver.support.color import Color
import platform

class StoriesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    novartis_logo_xpath = (By.XPATH, "//img[contains(@class, 'logo')]")
    mega_menu_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    all_topics_xpath = (By.XPATH, "//ul[(@id='block-storynavigation')]/li/a[contains(@data-drupal-link-system-path, 'stories') and not(contains(@class, 'news'))]")
    menus_list = ["All Topics", "Discovery", "From Our Labs", "Patient Perspectives", "Access to Healthcare", "People & Culture"]
    menus_items_css = (By.CSS_SELECTOR, "#block-storynavigation > .nav-item")
    anchor_tag_loc = (By.TAG_NAME, "a")
    anchor_tag_css = (By.CSS_SELECTOR, "a")
    toggle_text_css = (By.CSS_SELECTOR, ".toggle_text")
    view_css = (By.CSS_SELECTOR,"div.view.view-stories-overview-page")
    second_menu_item_css = (By.CSS_SELECTOR, "#block-storynavigation > li:nth-child(2)")
    content_pages_css = (By.CSS_SELECTOR, "div.item-list > ul.whole-item > li")
    # div.item-list > ul.whole-item > li
    pagination_heading_xpath = (By.XPATH, "//nav[@aria-label='pagination-heading']")
    pagination_heading_txt_xpath = (By.XPATH, "//nav[@aria-label='pagination-heading']/h4")
    next_page_arrow_xpath = (By.XPATH, "//a[@rel='next']")
    prev_page_arrow_xpath = (By.XPATH, "//a[@rel='prev']")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "ol.breadcrumb > li")
    breadcrumb_lists_anchor_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    # ol.breadcrumb > li

    random_content_title_css = (By.CSS_SELECTOR, "a > div.views-field.views-field-title > span")
    first_content_title_css = (By.CSS_SELECTOR, "ul.whole-item > li:nth-child(1) > a > div.views-field.views-field-title > span")
    # ul.whole-item > li:nth-child(1) > a > div.views-field.views-field-title > span
    first_content_css = (By.CSS_SELECTOR, "ul.whole-item > li:nth-child(1)")
    story_contents_css = (By.CSS_SELECTOR, "ul.whole-item > li")
    print_css = (By.CSS_SELECTOR, ".print > a")
    save_css = (By.CSS_SELECTOR, ".pdf > a")
    view_toggle_icon = (By.CSS_SELECTOR, ".toggle_icon")
    twitter_txt_css = (By.CSS_SELECTOR, ".a2a_button_twitter")
    fb_txt_css = (By.CSS_SELECTOR, ".a2a_button_facebook")
    whatsapp_txt_css = (By.CSS_SELECTOR, ".a2a_button_whatsapp")
    linkedin_txt_css = (By.CSS_SELECTOR, ".a2a_button_linkedin")
    email_txt_css = (By.CSS_SELECTOR, ".a2a_button_email")
    content_title_css = (By.CSS_SELECTOR,'.views-field-title >  span.field-content')
    stories_images_css = (By.CSS_SELECTOR,'.whole-item >.each-item > a >.views-field-field-story-image >div >img')

    

    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    mega_menu_stories_xpath= (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'/stories') and not(contains(@href, 'news')) and not(contains(@href, 'education'))]")
    mega_menu_news_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]//parent::li/p[@class='we-icon']")
    mega_menu_news_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]")
    page_title_css = (By.CSS_SELECTOR,'.page_title')
    tab_elements_css = (By.CSS_SELECTOR, "#block-storynavigation> li.nav-item")
    card_label_css = (By.CSS_SELECTOR,'.arctic-over-view-category')
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    breadcrumb_lists_anchor_tag_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    stories_last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3) > a")
    images_tag_name = (By.TAG_NAME,'img')
    images_css = (By.CSS_SELECTOR,'.field>img')
    menu_tabs_css = (By.CSS_SELECTOR, "#block-storynavigation > .nav-item")
    tabs_ellipse_css = (By.XPATH, "//li[contains(@class, 'visible')]")
    ellipse_css = (By.CSS_SELECTOR, ".show-hides")
    non_visible_ellipses_xpath = (By.XPATH,"//li[contains(@class,'nonvisibleelement')]/a")
    visible_element_xpath = (By.XPATH,"//li[contains(@class,'visibleelement')] [not(contains(@class,'nonvisibleelement'))]")
    search_icon_css = (By.CSS_SELECTOR, "li.nav-item.search > button img.icon-search")


    def launch_story_page(self,env_name):
        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_news_arrow_xpath)
            else:
                self.move_to_element(self.mega_menu_news_xpath)

            self.press_button(self.mega_menu_stories_xpath)
        except:
            menu = Utilities.multi_language[env_name]['news']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['stories']
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))

    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

    def search_icon_ele(self):

        search_icon = self.get_elemet_attribute(self.search_icon_css, "src")

        return search_icon


    def all_topics_grey_color(self):

        all_topics_txt = self.get_element_text(self.all_topics_xpath)
        hex_code = self.get_css_color(self.all_topics_xpath, "background-color")

        return all_topics_txt, hex_code


    def verify_menu_names(self):

        menu_items = self.driver.find_elements(self.menus_items_css[0], self.menus_items_css[1])

        return menu_items


    def default_view(self):

        view_icon = self.get_css_property(self.view_toggle_icon, "background")
        toggle_btn_txt = self.get_element_text(self.toggle_text_css)
        current_view_txt = self.get_elemet_attribute(self.view_css, "class")

        return toggle_btn_txt, current_view_txt, view_icon

    def check_breadcrumb(self):

        self.press_button(self.second_menu_item_css)
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


    def toggle_view(self):

        self.press_button(self.toggle_text_css)
        view_icon = self.get_css_property(self.view_toggle_icon, "background")
        toggle_btn_txt = self.get_element_text(self.toggle_text_css)
        current_view_txt = self.get_elemet_attribute(self.view_css, "class")

        return toggle_btn_txt, current_view_txt, view_icon


    def menu_items(self):

        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
        # That's why we are pressing on mega menu two times to ignore the issue.
        self.press_button(self.mega_menu_btn_css)
        self.press_button(self.mega_menu_btn_css)

        tab_elements_len = len(self.driver.find_elements(By.CSS_SELECTOR, "#block-storynavigation > .nav-item"))
        count = 0
        tab_elements = self.driver.find_elements(By.CSS_SELECTOR, "#block-storynavigation > .nav-item")
        hex_color_list = []
        page_src_list = []

        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(By.CSS_SELECTOR, "#block-storynavigation > .nav-item")
            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            tab_elements = self.driver.find_elements(By.CSS_SELECTOR, "#block-storynavigation > .nav-item")
            color = tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property("background-color")
            hex = Color.from_string(color).hex
            # rgb = int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[0]), int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[1]), int(color.split(" none")[0].split('(')[1].split(')')[0].split(', ')[2])
            # hex_code = self.rgb_to_hex(rgb)
            # assert "#f1f1f1" in hex_code
            hex_color_list.append(hex)
            if count > 0:
                page_src_list.append(self.driver.page_source)
                # assert "breadcrumb-item" in self.driver.page_source
            count = count + 1
            tab_elements_len = tab_elements_len - 1


        return hex_color_list, page_src_list

    def menu_items_url(self):

        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
        # That's why we are pressing on mega menu two times to ignore the issue.
        self.press_button(self.mega_menu_btn_css)
        self.press_button(self.mega_menu_btn_css)

        tab_elements_len = len(self.driver.find_elements(*self.menu_tabs_css))
        count = 0
        tab_elements = self.driver.find_elements(*self.menu_tabs_css)
        tab_name_list = []
        current_url_list = []

        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(*self.menu_tabs_css)
            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            tab_elements = self.driver.find_elements(*self.menu_tabs_css)

            if count > 0:
                if "&" in tab_elements[count].find_element(*self.anchor_tag_loc).text:
                    tab_name_list.append(tab_elements[count].find_element(*self.anchor_tag_loc).text.lower().replace(" ", "-").replace('&', 'and'))
                elif " " in tab_elements[count].find_element(*self.anchor_tag_loc).text:
                    tab_name_list.append(tab_elements[count].find_element(*self.anchor_tag_loc).text.lower().replace(" ", "-"))
                else:
                    tab_name_list.append(tab_elements[count].find_element(*self.anchor_tag_loc).text.lower().replace(" ", "-"))
                current_url_list.append(self.driver.current_url)

            count = count + 1
            tab_elements_len = tab_elements_len - 1

        return tab_name_list, current_url_list

    def menu_tab_one_grey_bg(self):

        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
        # That's why we are pressing on mega menu two times to ignore the issue.
        self.press_button(self.mega_menu_btn_css)
        self.press_button(self.mega_menu_btn_css)

        tab_elements_len = len(self.driver.find_elements(*self.menu_tabs_css))
        count = 0
        tab_elements = self.driver.find_elements(*self.menu_tabs_css)
        first_tab_color = ''
        second_tab_color = ''

        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(*self.menu_tabs_css)
            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            tab_elements = self.driver.find_elements(*self.menu_tabs_css)

            if count > 0:
                second_tab_color = Color.from_string(tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property('background-color')).hex
                first_tab_color = Color.from_string(tab_elements[count-1].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property('background-color')).hex

            count = count + 1
            tab_elements_len = tab_elements_len - 1
            if count == 2:
                break

        return first_tab_color, second_tab_color



    def pagination_front_arrow_back_arrow_validation(self):

        self.press_button(self.next_page_arrow_xpath)
        page_one_content_len = len(self.driver.find_elements(By.CSS_SELECTOR, ".view-content > div.item-list > ul > li"))
        self.press_button(self.prev_page_arrow_xpath)
        page_zero_content_len = len(self.driver.find_elements(By.CSS_SELECTOR, ".view-content > div.item-list > ul > li"))

        return page_one_content_len, page_zero_content_len


    def content_breadcrumb_ele(self):

        breadcrumb_items = []
        breadcrumb_lists = self.driver.find_elements(self.breadcrumb_lists_css[0], self.breadcrumb_lists_css[1])
        for breadcrumb_list in breadcrumb_lists:
            breadcrumb_items.append(str(breadcrumb_list.find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).text.encode('utf-8'))[1:].replace("'",""))


        breadcrumb_first_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').getPropertyValue('content')";
        breadcrumb_first_arrow_element = self.driver.execute_script(breadcrumb_first_arrow_script);

        breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3)'),'::before').getPropertyValue('content')";
        breadcrumb_second_arrow_element = self.driver.execute_script(breadcrumb_second_arrow_script);

        return breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element



    def social_media_icons(self):

        twitter_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_twitter'),'::before').getPropertyValue('background')";
        twitter_icon_element = self.driver.execute_script(twitter_icon_script);
        twitter_clickable = self.element_clickable(self.twitter_txt_css)
        twitter_txt_element = self.get_element_text(self.twitter_txt_css)

        facebook_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_facebook'),'::before').getPropertyValue('background')";
        facebook_icon_element = self.driver.execute_script(facebook_icon_script);
        facebook_clickable = self.element_clickable(self.fb_txt_css)
        facebook_txt_element = self.get_element_text(self.fb_txt_css)

        whatsapp_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_whatsapp'),'::before').getPropertyValue('background')";
        whatsapp_icon_element = self.driver.execute_script(whatsapp_icon_script);
        whatsapp_clickable = self.element_clickable(self.whatsapp_txt_css)

        linkedin_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_linkedin'),'::before').getPropertyValue('background')";
        linkedin_icon_element = self.driver.execute_script(linkedin_icon_script);
        linkedin_clickable = self.element_clickable(self.linkedin_txt_css)

        email_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_email'),'::before').getPropertyValue('background')";
        email_icon_element = self.driver.execute_script(email_icon_script);
        email_clickable = self.element_clickable(self.email_txt_css)


        return twitter_icon_element, twitter_txt_element, twitter_clickable, facebook_icon_element, facebook_txt_element, facebook_clickable, whatsapp_icon_element, whatsapp_clickable, linkedin_icon_element, linkedin_clickable, email_icon_element, email_clickable

    def twitter_icon(self):

        twitter_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_twitter'),'::before').getPropertyValue('background')";
        twitter_icon_element = self.driver.execute_script(twitter_icon_script);
        twitter_clickable = self.element_clickable(self.twitter_txt_css)
        twitter_txt_element = self.get_element_text(self.twitter_txt_css)

        return twitter_icon_element, twitter_txt_element, twitter_clickable

    def facebook_icon(self):

        facebook_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_facebook'),'::before').getPropertyValue('background')";
        facebook_icon_element = self.driver.execute_script(facebook_icon_script);
        facebook_clickable = self.element_clickable(self.fb_txt_css)
        facebook_txt_element = self.get_element_text(self.fb_txt_css)

        return facebook_icon_element, facebook_txt_element, facebook_clickable

    def whatsapp_icon(self):

        whatsapp_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_whatsapp'),'::before').getPropertyValue('background')";
        whatsapp_icon_element = self.driver.execute_script(whatsapp_icon_script);
        whatsapp_clickable = self.element_clickable(self.whatsapp_txt_css)

        return whatsapp_icon_element, whatsapp_clickable

    def linkedin_icon(self):

        linkedin_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_linkedin'),'::before').getPropertyValue('background')";
        linkedin_icon_element = self.driver.execute_script(linkedin_icon_script);
        linkedin_clickable = self.element_clickable(self.linkedin_txt_css)

        return linkedin_icon_element, linkedin_clickable

    def email_icon(self):

        email_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_email'),'::before').getPropertyValue('background')";
        email_icon_element = self.driver.execute_script(email_icon_script);
        email_clickable = self.element_clickable(self.email_txt_css)

        return email_icon_element, email_clickable


    def print_and_save_btn(self):

        print_script = "return window.getComputedStyle(document.querySelector('.print > a'),'::before').getPropertyValue('background')";
        print_icon = self.driver.execute_script(print_script);
        print_txt = self.get_element_text(self.print_css)

        pdf_script = "return window.getComputedStyle(document.querySelector('.pdf > a'),'::before').getPropertyValue('background')";
        pdf_icon = self.driver.execute_script(pdf_script);
        pdf_txt = self.get_element_text(self.save_css)

        return print_icon, print_txt, pdf_icon, pdf_txt


    def print_btn(self):
        
        print_script = "return window.getComputedStyle(document.querySelector('.print > a'),'::before').getPropertyValue('background')";
        print_icon = self.driver.execute_script(print_script);
        print_txt = self.get_element_text(self.print_css)

        return print_icon, print_txt

    def save_btn(self):

        pdf_script = "return window.getComputedStyle(document.querySelector('.pdf > a'),'::before').getPropertyValue('background')";
        pdf_icon = self.driver.execute_script(pdf_script);
        pdf_txt = self.get_element_text(self.save_css)

        return pdf_icon, pdf_txt

    def duplicate_contents(self):

        content_title_list = []
        content_title_set = set()
        for i in range(3):
            content_titles = self.driver.find_elements(*self.content_title_css)
            for title in content_titles:
                content_title_list.append(title.text)
                content_title_set.add(title.text)
            if len(self.driver.find_elements(*self.next_page_arrow_xpath)) > 0:
                self.press_button(self.next_page_arrow_xpath) 
            else :
                 break
        
        return content_title_list, content_title_set


    def verify_filters(self):

        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
        # That's why we are pressing on mega menu two times to ignore the issue.
        self.press_button(self.mega_menu_btn_css)
        self.press_button(self.mega_menu_btn_css)

        count = 0
        card_label_set = set()
        filter_name_list = []
        menu_tab_list = []
        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        
        while tab_elements_len > 0:

            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            element = tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1])
            ele_href = element.get_attribute("href")
            if "stories/" in ele_href:
                self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
                active_tab = self.driver.find_element(By.CSS_SELECTOR,".active-tab")
                
                card_labels = self.driver.find_elements(*self.card_label_css)
                if len(card_labels) > 0:
                    filter_name_list.append(str(active_tab.text.encode('utf-8'))[1:].replace("'",""))
                for label in card_labels:
                    card_label_set.add(str(label.text.encode('utf-8'))[1:].replace("'",""))
            
            count = count + 1
            tab_elements_len = tab_elements_len - 1
        
        for filter_name in filter_name_list:
            if "&" in filter_name:
                menu_tab_list.append(filter_name.replace("&", "and"))
            else :
                menu_tab_list.append(filter_name)

        return  menu_tab_list ,card_label_set



    def story_details_breadcrumb_display(self):

        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        breadcrumb_items_len_list = []
        content_title_list = []
        breadcrumb_items_list = []
        breadcrumb_first_arrow_element_list = []
        breadcrumb_second_arrow_element_list = []
        color_list = []

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            content_title = str(story_contents[random_content_number].find_element(self.random_content_title_css[0], self.random_content_title_css[1]).text.encode('utf-8'))

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element = self.content_breadcrumb_ele()
            print(breadcrumb_items)


            breadcrumb_items_len_list.append(len(breadcrumb_items))
            content_title_list.append(content_title[1:].replace("'",""))
            breadcrumb_items_list.append(breadcrumb_items)
            breadcrumb_first_arrow_element_list.append(breadcrumb_first_arrow_element)
            breadcrumb_second_arrow_element_list.append(breadcrumb_second_arrow_element)
            color_list.append(self.get_css_color(self.stories_last_child_breadcrumb_color_css, "color"))

            index = index + 1

            if index == 4:
                break

            self.driver.back()

        return breadcrumb_first_arrow_element_list, breadcrumb_second_arrow_element_list, content_title_list, breadcrumb_items_len_list, breadcrumb_items_list, color_list



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
        
    def stories_images_validation(self):

        display_list = []
        alt_list = []
        title_list = []
        natural_width_list =[]
        index = 0 
        stories_images = self.driver.find_elements(*self.stories_images_css)
        if len(stories_images) > 0 :
            for image in stories_images:

                stories_images = self.driver.find_elements(*self.stories_images_css)
                self.driver.execute_script("arguments[0].click()", stories_images[index])
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
                self.driver.back()
                
        return display_list, alt_list, title_list,natural_width_list
           


    def multiple_tab_greyed_out(self):

        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
        # That's why we are pressing on mega menu two times to ignore the issue.
        self.press_button(self.mega_menu_btn_css)
        self.press_button(self.mega_menu_btn_css)
       
        tab_grey_before_pagination_list = []
        tab_grey_after_pagination_list = []
       
        tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
        tab_elements_len = len(tab_elements)
        count = 0
        while tab_elements_len > 0 and self.driver.find_elements(*self.next_page_arrow_xpath):
           
            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            self.driver.execute_script("arguments[0].click()", tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            bg_color = Color.from_string(tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property('background-color')).hex
            tab_grey_before_pagination_list.append(bg_color)
            if self.driver.find_elements(*self.next_page_arrow_xpath):
                self.press_button(self.next_page_arrow_xpath)
            tab_elements = self.driver.find_elements(self.tab_elements_css[0], self.tab_elements_css[1])
            background_color = Color.from_string(tab_elements[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).value_of_css_property('background-color')).hex
            tab_grey_after_pagination_list.append(background_color)
            self.driver.back()
            
            count = count + 1
            tab_elements_len = tab_elements_len - 1


        return tab_grey_before_pagination_list , tab_grey_after_pagination_list


    def story_title_no_paragraph_tag(self):

        toggle_icon = self.get_css_property(self.view_toggle_icon, "background")
        if "list.svg" in toggle_icon:
            self.press_button(self.toggle_text_css)
        
        content_titles_list = []

        content_titles = self.driver.find_elements(*self.random_content_title_css)

        for title in content_titles:
            content_titles_list.append(title.text)

        return content_titles_list


