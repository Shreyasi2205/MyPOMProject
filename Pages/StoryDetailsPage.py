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

class StoryDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    story_contents_css = (By.CSS_SELECTOR, "ul.whole-item > li")
    anchor_tag_css = (By.CSS_SELECTOR, "a")
    banner_img_css = (By.CSS_SELECTOR, "div.carousel_img_video > div > picture > img")
    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    title_css = (By.CSS_SELECTOR, "h1.title")
    random_content_title_css = (By.CSS_SELECTOR, "a > div.views-field.views-field-title > span")
    stories_last_child_breadcrumb_color_css = (By.CSS_SELECTOR, "#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3) > a")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "ol.breadcrumb > li")
    anchor_tag_loc = (By.TAG_NAME, "a")
    breadcrumb_lists_anchor_tag_css = (By.CSS_SELECTOR, "ol.breadcrumb > li.breadcrumb-item > a")
    related_links_xpath = (By.XPATH, "//*[contains(@class, 'right-hand-rail')]")
    images_css = (By.CSS_SELECTOR, ".field > img")
    print_css = (By.CSS_SELECTOR, ".print > a")
    save_css = (By.CSS_SELECTOR, ".pdf > a")
    twitter_txt_css = (By.CSS_SELECTOR, ".a2a_button_twitter")
    fb_txt_css = (By.CSS_SELECTOR, ".a2a_button_facebook")
    whatsapp_txt_css = (By.CSS_SELECTOR, ".a2a_button_whatsapp")
    linkedin_txt_css = (By.CSS_SELECTOR, ".a2a_button_linkedin")
    email_txt_css = (By.CSS_SELECTOR, ".a2a_button_email")
    date_css = (By.CSS_SELECTOR, ".dateBlock")
    novartis_logo_css = (By.CSS_SELECTOR, "#navbar-main > a > img")
    search_css = (By.CSS_SELECTOR, ".search > button")
    menu_css = (By.CSS_SELECTOR, ".menu > button")
    card_css = (By.CSS_SELECTOR, "li.each-item")
    card_anchor_css = (By.CSS_SELECTOR, "li.each-item > a")
    card_label_css = (By.CSS_SELECTOR, "li.each-item > a > .views-field-field-category")
    card_title_css = (By.CSS_SELECTOR, "li.each-item > a > .views-field-title")
    view_all_css = (By.CSS_SELECTOR, ".more-link > a")
    related_stories_title_css = (By.CSS_SELECTOR, ".views-element-container > h2")
    share_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(2)")
    print_save_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(1)")
    anchor_tag_css = (By.CSS_SELECTOR,'a')
    tags_css = (By.CSS_SELECTOR, ".view-content > .views-row")
    share_css = (By.CSS_SELECTOR,'share_block_css')
    blocks_css =(By.CSS_SELECTOR,'[class="pre_links"] >li')
    twitter_alignment_css = (By.CSS_SELECTOR,'.addtoany_list >a:nth-child(2)')
    fshare_alignment_css = (By.CSS_SELECTOR,'.addtoany_list >a:nth-child(3)')
    wattsapp_alignment_css = (By.CSS_SELECTOR,'.addtoany_list >a:nth-child(4)')
    linkedIn_alignment_css = (By.CSS_SELECTOR,'.addtoany_list >a:nth-child(5)')
    email_alignment_css = (By.CSS_SELECTOR,'.addtoany_list >a:nth-child(6)')
    twitter_anchor_tag_xpath = (By.XPATH,"//a[contains(@class,'button_twitter')]")
    facebook_anchor_tag_xpath = (By.XPATH,"//a[contains(@title,'Facebook') and contains(@class,'a2a_button_facebook')]")
    whattsapp_anchor_tag_xpath = (By.XPATH,"//a[contains(@title,'Whatsapp') and contains(@class,'a2a_button_whatsapp')]")
    linkedIn_anchor_tag_xpath = (By.XPATH,"//a[contains(@title,'Linkedin') and contains(@class,'a2a_button_linkedin')]")
    email_anchor_tag_xpath = (By.XPATH,"//a[contains(@title,'Email') and contains(@class,'a2a_button_email')]")
    search_icon_css = (By.CSS_SELECTOR, "li.nav-item.search > button img.icon-search")

    
    def banner_img(self):

        banner_img_list = []
        banner_img_broken_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            banner_img_list.append(self.is_displayed(self.banner_img_css))
            banner_img_broken_list.append(self.get_elemet_attribute(self.banner_img_css, "naturalWidth"))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return banner_img_list, banner_img_broken_list


    def pattern_ele(self):

        pattern_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            pattern_list.append(self.get_css_property(self.pattern_css, "background-image"))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return pattern_list


    def tags_ele(self):

        tags_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            tags_list.append(len(self.driver.find_elements(*self.tags_css)))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return tags_list


    def title_ele(self):

        title_display_list = []
        title_length_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            title_length_list.append(len(self.get_element_text(self.title_css)))
            title_display_list.append(self.is_displayed(self.title_css))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return title_display_list, title_length_list

    def print_block_ele(self):

        total_rows = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        row_index = 0
        print_list = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            print_list.append(len(self.driver.find_elements(*self.print_css)))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
        
        return print_list

    def save_block_ele(self):

        total_rows = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        row_index = 0
        save_list = []

        for row in total_rows:

            total_rows = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            save_list.append(len(self.driver.find_elements(*self.save_css)))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
            
        return save_list


    def date_ele(self):

        date_display_list = []
        date_len_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            date_display_list.append(self.is_displayed(self.date_css))
            date_len_list.append(len(self.get_element_text(self.date_css)))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return date_display_list, date_len_list


    def search_ele(self):

        search_display_list = []
        search_len_list = []
        search_icon_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            search_display_list.append(self.is_displayed(self.search_css))
            search_len_list.append(len(self.get_element_text(self.search_css)))
            search_icon_list.append(self.get_elemet_attribute(self.search_icon_css, "src"))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return search_display_list, search_len_list, search_icon_list

    def menu_ele(self):

        menu_display_list = []
        menu_len_list = []
        menu_icon_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            menu_display_list.append(self.is_displayed(self.menu_css))
            menu_len_list.append(len(self.get_element_text(self.menu_css)))
            menu_icon_script = "return window.getComputedStyle(document.querySelector('.menu > button'),'::before').getPropertyValue('background')";
            menu_icon_list.append(self.driver.execute_script(menu_icon_script))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return menu_display_list, menu_len_list, menu_icon_list

    
    def logo_ele(self):

        menu_display_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            menu_display_list.append(self.is_displayed(self.novartis_logo_css))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return menu_display_list


    def related_links_ele(self):

        related_links_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            related_links_list.append(len(self.driver.find_elements(*self.related_links_xpath)))

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return related_links_list

    def images_ele(self):

        img_ele_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:
            
            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            images_content = self.driver.find_elements(*self.images_css)
            img_index = 0
            for img in images_content:
                images_content = self.driver.find_elements(*self.images_css)
                img_ele_list.append(images_content[img_index].get_attribute("src"))
                img_index += 1

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return img_ele_list
    

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
            self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
            breadcumb_anchor_current_url_list.append(self.driver.current_url)
            time.sleep(4)
            self.driver.back()

            breadcumb_index = breadcumb_index + 1

            if breadcumb_index == 2:
                break

        return breadcumb_anchor_url_list, breadcumb_anchor_current_url_list 


    def twitter_icon(self):

        twitter_icon_list = []
        twitter_clickable_list = []
        twitter_txt_element_list = []
        twitter_href_list = []
        # twitter_redirected_url =[]

        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            twitter_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_twitter'),'::before').getPropertyValue('background')";
            twitter_icon_list.append(self.driver.execute_script(twitter_icon_script))
            twitter_clickable_list.append(self.element_clickable(self.twitter_txt_css))
            twitter_txt_element_list.append(self.get_element_text(self.twitter_txt_css))
            twitter_href_list.append(self.get_elemet_attribute(self.twitter_anchor_tag_xpath,'href'))
            # self.press_button(self.twitter_anchor_tag_xpath)
            # self.driver.switch_to.window(self.driver.window_handles[1])
            # twitter_redirected_url.append(self.driver.current_url)
            # self.driver.switch_to.window(self.driver.window_handles[0])




            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return twitter_icon_list, twitter_clickable_list, twitter_txt_element_list, twitter_href_list


    def facebook_icon(self):

        facebook_icon_list = []
        facebook_clickable_list = []
        facebook_txt_element_list = []
        facebook_href_list = []
        # facebook_redirected_url =[]


        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            facebook_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_facebook'),'::before').getPropertyValue('background')";
            facebook_icon_list.append(self.driver.execute_script(facebook_icon_script))
            facebook_clickable_list.append(self.element_clickable(self.fb_txt_css))
            facebook_txt_element_list.append(self.get_element_text(self.fb_txt_css))
            facebook_href_list.append(self.get_elemet_attribute(self.facebook_anchor_tag_xpath,'href'))
            # self.press_button(self.facebook_anchor_tag_xpath)
            # self.driver.switch_to.window(self.driver.window_handles[1])
            # facebook_redirected_url.append(self.driver.current_url)
            # self.driver.switch_to.window(self.driver.window_handles[0])



            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return facebook_icon_list, facebook_clickable_list, facebook_txt_element_list, facebook_href_list


    def whatsapp_icon(self):

        whatsapp_icon_list = []
        whatsapp_clickable_list = []
        whatsapp_href_list = []
        whatsapp_redirected_url =[]

        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            whatsapp_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_whatsapp'),'::before').getPropertyValue('background')";
            whatsapp_icon_list.append(self.driver.execute_script(whatsapp_icon_script))
            whatsapp_clickable_list.append(self.element_clickable(self.whatsapp_txt_css))
            whatsapp_href_list.append(self.get_elemet_attribute(self.whattsapp_anchor_tag_xpath,'href'))
            # self.press_button(self.whattsapp_anchor_tag_xpath)
            # self.driver.switch_to.window(self.driver.window_handles[1])
            # whatsapp_redirected_url.append(self.driver.current_url)
            # self.driver.switch_to.window(self.driver.window_handles[0])


            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return whatsapp_icon_list, whatsapp_clickable_list,whatsapp_href_list


    def linkedin_icon(self):

        linkedin_icon_list = []
        linkedin_clickable_list = []
        linkedIn_href_list = []
        linkedIn_redirected_url =[]

        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            linkedin_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_linkedin'),'::before').getPropertyValue('background')";
            linkedin_icon_list.append(self.driver.execute_script(linkedin_icon_script))
            linkedin_clickable_list.append(self.element_clickable(self.linkedin_txt_css))
            linkedIn_href_list.append(self.get_elemet_attribute(self.linkedIn_anchor_tag_xpath,'href'))
            # self.press_button(self.linkedIn_anchor_tag_xpath)
            # self.driver.switch_to.window(self.driver.window_handles[1])
            # linkedIn_redirected_url.append(self.driver.current_url)
            # self.driver.switch_to.window(self.driver.window_handles[0])


            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return linkedin_icon_list, linkedin_clickable_list, linkedIn_href_list

    def email_icon(self):

        email_icon_list = []
        email_clickable_list = []
        email_href_list = []

        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            email_icon_script = "return window.getComputedStyle(document.querySelector('.a2a_button_email'),'::before').getPropertyValue('background')";
            email_icon_list.append(self.driver.execute_script(email_icon_script))
            email_clickable_list.append(self.element_clickable(self.email_txt_css))
            email_href_list.append(self.get_elemet_attribute(self.email_anchor_tag_xpath,'href'))


            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return email_icon_list, email_clickable_list, email_href_list


    def print_icon(self):

        print_icon_list = []
        print_txt_list = []
        print_href_url_list = []
        print_current_url_list = []

        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            print_icon_script = "return window.getComputedStyle(document.querySelector('.print > a'),'::before').getPropertyValue('background')";
            print_icon_list.append(self.driver.execute_script(print_icon_script))
            print_txt_list.append(self.get_element_text(self.print_css))
            print_href_url_list.append(self.get_elemet_attribute(self.print_css, "href"))
            self.press_button(self.print_css)
            print_current_url_list.append(self.driver.current_url)
            self.driver.back()

            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return print_icon_list, print_txt_list, print_href_url_list, print_current_url_list

    def save_icon(self):

        save_icon_list = []
        save_txt_list = []

        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            save_icon_script = "return window.getComputedStyle(document.querySelector('.pdf > a'),'::before').getPropertyValue('background')";
            save_icon_list.append(self.driver.execute_script(save_icon_script))
            save_txt_list.append(self.get_element_text(self.save_css))


            index = index + 1
            if index == 4:
                break

            self.driver.back()


        return save_icon_list, save_txt_list


    def related_stories_title(self):

        related_stories_title_display_list = []
        related_stories_title_length_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            related_stories_title_length_list.append(len(self.get_element_text(self.related_stories_title_css)))
            related_stories_title_display_list.append(self.is_displayed(self.related_stories_title_css))

            index = index + 1
            if index == 4:
                break

            self.driver.back()

        return related_stories_title_display_list, related_stories_title_length_list, story_contents_len


    def related_stories_content(self):

        related_stories_content_len_list = []
        card_label_list = []
        card_title_list = []
        card_href_list = []
        card_current_url_list = []
        view_all_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            related_stories_content_len_list.append(len(self.driver.find_elements(*self.card_css)))
            if story_contents_len > 4:
                view_all_list.append(self.is_displayed(self.view_all_css))

            card_labels = self.driver.find_elements(*self.card_label_css)
            card_label_index = 0
            for card_label in card_labels:
                card_label_list.append(self.is_displayed_ele(card_labels[card_label_index]))
                card_label_index = card_label_index + 1

            card_titles = self.driver.find_elements(*self.card_title_css)
            card_title_index = 0
            for card_title in card_titles:
                card_title_list.append(self.is_displayed_ele(card_titles[card_title_index]))
                card_title_index = card_title_index + 1

            cards = self.driver.find_elements(*self.card_anchor_css)
            card_anchor_index = 0
            for card in cards:
                cards = self.driver.find_elements(*self.card_anchor_css)
                card_href_list.append(cards[card_anchor_index].get_attribute("href"))
                cards = self.driver.find_elements(*self.card_anchor_css)
                self.driver.execute_script("arguments[0].click()", cards[card_anchor_index])
                card_current_url_list.append(self.driver.current_url)
                self.driver.back()

            index = index + 1
            if index == 4:
                break

            self.driver.back()

        return related_stories_content_len_list, card_label_list, card_title_list, card_href_list, card_current_url_list, view_all_list, story_contents_len



    def share_block(self):

        share_block_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            share_block_list.append(len(self.driver.find_elements(*self.share_css)))
            
            index = index + 1
            if index == 4:
                break

            self.driver.back()

        return  share_block_list


    def print_save_block_alignment(self):


        print_block_list = []
        save_block_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            blocks = self.driver.find_elements(*self.blocks_css)
            count = 0
            print_block_list.append(blocks[count].get_attribute('class'))
            save_block_list.append(blocks[count+1].get_attribute('class'))
                
            
            index = index + 1
            if index == 4:
                break

            self.driver.back()

        return  print_block_list , save_block_list



    def socail_media_alignment(self):


        twitter_block_list = []
        fshare_block_list = []
        wattsapp_block_list = []
        linkedIn_block_list = []
        email_block_list = []
        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            twitter_block_list.append(self.get_elemet_attribute(self.twitter_alignment_css,'title'))
            fshare_block_list.append(self.get_elemet_attribute(self.fshare_alignment_css,'title'))
            wattsapp_block_list.append(self.get_elemet_attribute(self.wattsapp_alignment_css,'title'))
            linkedIn_block_list.append(self.get_elemet_attribute(self.linkedIn_alignment_css,'title'))
            email_block_list.append(self.get_elemet_attribute(self.email_alignment_css,'title'))
                
            
            index = index + 1
            if index == 4:
                break

            self.driver.back()

        return  twitter_block_list, fshare_block_list , wattsapp_block_list, linkedIn_block_list,  email_block_list



    def view_all_bold(self):

        story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
        story_contents_len = len(story_contents)
        random_content_number = random.randint(0,story_contents_len-1)
        view_all_bold_list = []
        index = 0

        for story in story_contents:

            random_content_number = random.randint(0,story_contents_len-1)

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])

            story_contents = self.driver.find_elements(self.story_contents_css[0], self.story_contents_css[1])
            self.driver.execute_script("arguments[0].click()", story_contents[random_content_number].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))

            if len(self.driver.find_elements(self.view_all_css[0], self.view_all_css[1])) > 0:

                view_all_bold = self.get_css_property(self.view_all_css,'font-weight')
                view_all_bold_list.append(view_all_bold)

            index = index + 1
            if index == 4:
                break

            self.driver.back()

        return view_all_bold_list



    