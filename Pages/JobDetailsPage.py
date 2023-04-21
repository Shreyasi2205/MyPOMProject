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
import platform

class JobDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    pop_up_logo_css = (By.CSS_SELECTOR, ".ui-dialog-titlebar > img")
    pop_up_title_css = (By.CSS_SELECTOR, ".ui-dialog-title")
    pop_up_body_css = (By.CSS_SELECTOR, ".external-link-popup-body > p")
    continue_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)")
    cancel_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(2)")
    apply_to_job_css = (By.CSS_SELECTOR, "div.field_job_snapshot > a:nth-child(3)")
    access_job_account_css = (By.CSS_SELECTOR, "div.field_job_snapshot > a:nth-child(4)")
    breadcrumb_lists_css = (By.CSS_SELECTOR, "ol.breadcrumb > li")
    breadcrumb_lists_anchor_css = (By.CSS_SELECTOR, "ol.breadcrumb > li > a")
    anchor_tag_loc = (By.TAG_NAME, "a")
    # box_color = "rgba(199, 199, 199, 1)"
    tage_elements_css = (By.CSS_SELECTOR, "span.field-content > a")
    share_btn_css = (By.CSS_SELECTOR, ".addtoany_share")
    print_css = (By.CSS_SELECTOR, "li.print > a")
    clear_all_css = (By.CSS_SELECTOR, "a.clear-button")
    save_css = (By.CSS_SELECTOR, "li.pdf > a")
    job_details_css = (By.CSS_SELECTOR, "div.job_details_content_bottom > div.row")
    jobs_content_css = (By.CSS_SELECTOR, "div#block-careerssection > div.content > div")
    job_detail_label_css = (By.CSS_SELECTOR, "label")
    job_detail_value_css = (By.CSS_SELECTOR, "div")
    total_row_css = (By.CSS_SELECTOR, "table > tbody > tr")
    job_title_css = (By.CSS_SELECTOR, "td > a")
    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    job_page_title_css = (By.CSS_SELECTOR, "h1.title > span")
    job_id_css = (By.CSS_SELECTOR, ".d-sm-inline-block.field_job_id")
    job_date_css = (By.CSS_SELECTOR, ".d-sm-inline-block.field_job_last_updated")
    job_location_css = (By.CSS_SELECTOR, ".d-sm-inline-block.field_job_country")
    job_img_css = (By.CSS_SELECTOR,".job_details_content_right > .field_job_image > img")
    frame_css = (By.CSS_SELECTOR,".job_details_content_right > div.field_job_snapshot")
    frame_job_id_css = (By.CSS_SELECTOR,'.job_details_content_right > .field_job_snapshot >div > div[class="d-inline-block field_job_id"]')
    frame_job_title_css = (By.CSS_SELECTOR,".job_details_content_right > .field_job_snapshot > h3.field_job_title ")
    apply_access_job_mobile_css = (By.CSS_SELECTOR, ".cta-links-mobile > a")
    apply_access_job_desktop_css = (By.CSS_SELECTOR, "div.field_job_snapshot > a")
    share_btn_txt_css = (By.CSS_SELECTOR, ".addtoany_share")
    apply_access_job_txt_list = ["Apply to Job", "Access Job Account"]
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    mega_menu_career_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/careers') and not(contains(@target,'_self'))]")
    mega_menu_career_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/careers') and not(contains(@target,'_self'))]//parent::li/p[@class='we-icon']")
    mega_menu_career_search_xpath= (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'/career-search')]")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    share_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(2)")
    print_save_block_css = (By.CSS_SELECTOR,".region-featured-bottom-first > div:nth-last-child(1)")
    anchor_tag_css = (By.CSS_SELECTOR,'a')
    job_info_single_row_css = (By.CSS_SELECTOR, ".job_details_content_top > .title-info")
    job_info_single_row_each_div_css = (By.CSS_SELECTOR, ".job_details_content_top > .title-info > div")
    job_desc_css = (By.CSS_SELECTOR, ".field_job_description ")
    right_hand_rail_xpath = (By.XPATH,"//div[contains(@id,'right-hand-rail-block')]")
    alternate_country_job_xpath = (By.XPATH,"//span[@class='alternative-locations']/parent::td/preceding-sibling::td/a")
    job_detail_alternate_country_xpath = (By.XPATH,"//label[contains(text(),'Alternative Location')]")
    

    def launch_jobDetails(self,env_name):

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
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['career-search']
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))

    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

    def tag_ele(self):

        row_index = 0
        tag_elements_list_status = []
        tag_elements_url_list = []
        tag_elements_page_url_list = []
        tag_element_index = 0

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))

            tag_elements = self.driver.find_elements(self.tage_elements_css[0], self.tage_elements_css[1])
            tag_len = len(tag_elements)
            for tag_element in tag_elements:

                tag_elements = self.driver.find_elements(self.tage_elements_css[0], self.tage_elements_css[1])
                tag_elements_list_status.append(self.is_displayed_ele(tag_elements[tag_element_index]))
                tag_elements_url_list.append(tag_elements[tag_element_index].get_attribute("href"))
                self.driver.execute_script("arguments[0].click()", tag_elements[tag_element_index])
                tag_elements_page_url_list.append(self.driver.current_url)
                self.driver.back()
                tag_element_index = tag_element_index + 1
                if tag_element_index == tag_len:
                    tag_element_index = 0
            self.driver.back()
            
            row_index = row_index + 1
            if row_index == 4:
                break
        
        return row_index ,tag_len , tag_elements_list_status, tag_elements_url_list, tag_elements_page_url_list


    def job_info_single_row(self):

        row_index = 0
        job_info_class_list = []
        job_info_each_div_class_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))

            job_info_class_list.append(self.get_elemet_attribute(self.job_info_single_row_css, 'class'))
            job_info_each_div_classes = self.driver.find_elements(*self.job_info_single_row_each_div_css)
            for job_info_each_div_class in job_info_each_div_classes:
                job_info_each_div_class_list.append(job_info_each_div_class.get_attribute("class"))

            self.driver.back()
            
            row_index = row_index + 1
            if row_index == 4:
                break

        return job_info_class_list, job_info_each_div_class_list
    

    def share_btn_ele(self):


        row_index = 0
        share_btn_icon_list = []
        share_btn_list = []
        twitter_icon_list = []
        facebook_icon_list = []
        whatsapp_icon_list = []
        linkedin_icon_list = []
        email_icon_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))

            share_btn_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.addtoany_share'),'::before').getPropertyValue('background')");
            share_btn_icon_list.append(share_btn_icon)
            share_btn_list.append(self.is_displayed(self.share_btn_css))
            self.press_button(self.share_btn_css)

            twitter_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_twitter'),'::before').getPropertyValue('background')");
            twitter_icon_list.append(twitter_icon)
            facebook_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_facebook'),'::before').getPropertyValue('background')");
            facebook_icon_list.append(facebook_icon)
            whatsapp_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_whatsapp'),'::before').getPropertyValue('background')");
            whatsapp_icon_list.append(whatsapp_icon)
            linkedin_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_linkedin'),'::before').getPropertyValue('background')");
            linkedin_icon_list.append(linkedin_icon)
            email_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_email'),'::before').getPropertyValue('background')");
            email_icon_list.append(email_icon)
            self.driver.back()

            row_index = row_index + 1
            if row_index == 4:
                break

        return row_index , share_btn_icon_list,share_btn_list, twitter_icon_list,facebook_icon_list,whatsapp_icon_list,linkedin_icon_list,email_icon_list

    def print_block_ele(self):

        row_index = 0
        print_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)
       

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            print_list.append(len(self.driver.find_elements(*self.print_css)))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
        
        return row_index, print_list


    def share_block_ele(self):

        row_index = 0
        save_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            save_list.append(len(self.driver.find_elements(*self.share_btn_css)))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
            
        return row_index, save_list

    def save_block_ele(self):


        row_index = 0
        save_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]))
            save_list.append(len(self.driver.find_elements(*self.save_css)))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 5:
                break
            
        return row_index, save_list

    def print_share_misalignment(self):

        row_index = 0
        share_block = []
        print_save_block = []

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))

            share_block.append(self.get_elemet_attribute(self.share_block_css, "id"))
            print_save_block.append(self.get_elemet_attribute(self.print_save_block_css, "id"))

            self.driver.back()

            row_index = row_index + 1
            if row_index == 4:
                break

        return row_index, share_block, print_save_block

    def print_btn_ele(self):

        row_index = 0
        print_btn_list = []
        print_btn_clickable_status = []
        print_icon_list = []
        print_url_list = []
        print_page_url_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            print_btn_list.append(self.is_displayed(self.print_css))
            print_btn_clickable_status.append(self.element_clickable(self.print_css))
            print_url_list.append(self.get_elemet_attribute(self.print_css, "href"))
            print_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('li.print > a'),'::before').getPropertyValue('background')");
            print_icon_list.append(print_icon)
            self.press_button(self.print_css)
            print_page_url_list.append(self.driver.current_url)
            self.driver.back()

            self.driver.back()
            row_index = row_index + 1
            if row_index == 4:
                break
        
        return row_index,print_btn_list, print_btn_clickable_status, print_icon_list,print_url_list,print_page_url_list

    def save_btn_ele(self):


        row_index = 0
        save_btn_list = []
        save_btn_clickable_status = []
        save_icon_list = []
        save_href_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            save_btn_list.append(self.is_displayed(self.save_css))
            save_btn_clickable_status.append(self.element_clickable(self.save_css))
            save_href_list.append(self.get_elemet_attribute(self.save_css, "href"))
            save_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('li.pdf > a'),'::before').getPropertyValue('background')");
            save_icon_list.append(save_icon)
            self.driver.back()

            row_index = row_index + 1
            if row_index == 4:
                break
            
        return row_index,save_btn_list,save_btn_clickable_status,save_icon_list,save_href_list


    def label_name_value_ele(self):

        row_index = 0
        job_detail_label_list = []
        job_detail_value_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            job_details_table = self.driver.find_elements(self.job_details_css[0], self.job_details_css[1])

            for job_detail in job_details_table:

                job_detail_label_list.append(job_detail.find_element(self.job_detail_label_css[0], self.job_detail_label_css[1]).text)
                job_detail_value_list.append(job_detail.find_element(self.job_detail_value_css[0], self.job_detail_value_css[1]).text)
    
            self.driver.back()

            row_index = row_index + 1
            if row_index == 4:
                break

        return row_index , job_detail_label_list, job_detail_value_list



    def external_link(self, by_locator_one):

        self.driver.execute_script("arguments[0].click()", by_locator_one)
        pop_up_logo = self.get_elemet_attribute(self.pop_up_logo_css, "src")
        pop_up_title = self.get_element_text(self.pop_up_title_css)
        pop_up_desc = self.get_element_text(self.pop_up_body_css)
        continue_btn =  self.get_element_text(self.continue_button_css)
        continue_btn_clickable = self.element_clickable(self.continue_button_css)
        cancel_btn = self.get_element_text(self.cancel_button_css)
        cancel_btn_clickable = self.element_clickable(self.cancel_button_css)
        self.press_button(self.cancel_button_css)
        page_url = self.driver.current_url

        return pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_url;

    def apply_access_job_page(self, by_locator, class_name):

        job_url = by_locator.get_attribute("href")
        self.driver.execute_script("arguments[0].click()", by_locator)
        self.press_button(self.continue_button_css)
        if "ext" in class_name.split(' '):
            child = self.driver.window_handles[1]
            parent = self.driver.window_handles[0]
            self.driver.switch_to.window(child)
            apply_access_job_page_url = self.driver.current_url
            self.driver.close()
            self.driver.switch_to.window(parent)
        else:
            apply_access_job_page_url = self.driver.current_url
            self.driver.back()

        return job_url, apply_access_job_page_url

    def apple_access_job_by_screen_size(self):

        if self.driver.get_window_size().get("width") <= 1050:
            jobs = self.driver.find_elements(self.apply_access_job_mobile_css[0], self.apply_access_job_mobile_css[1])
        else:
            jobs = self.driver.find_elements(self.apply_access_job_desktop_css[0], self.apply_access_job_desktop_css[1])
        
        return jobs


    
    def pattern_verify(self):

        row_index = 0
        pattern_stripe_paths = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            pattern_stripe_paths.append(self.get_css_property(self.pattern_css, "background-image"))
            self.driver.back()

            row_index = row_index + 1
            if row_index == 4:
                break
        
        return row_index , pattern_stripe_paths

    def breadcrumb_elements(self):

        row_index = 0
        breadcrumb_items = []
        breadcrumb_text =[]
        breadcrumb_first_arrow_element = []
        breadcrumb_second_arrow_element =[]
        breadcrumb_third_arrow_element = []
        breadcrumb_fourthLevel_color = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            job_title = str(total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]).text.encode('utf-8'))
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            
            breadcrumb_lists = self.driver.find_elements(self.breadcrumb_lists_css[0], self.breadcrumb_lists_css[1])
            for breadcrumb_list in breadcrumb_lists:
                breadcrumb_text.append(breadcrumb_list.find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).text.encode('utf-8'))
            breadcrumb_items.append(len(breadcrumb_text))
            breadcrumb_text.clear()

            breadcrumb_first_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').getPropertyValue('content')";
            element = self.driver.execute_script(breadcrumb_first_arrow_script);
            breadcrumb_first_arrow_element.append(element)

            breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3)'),'::before').getPropertyValue('content')";
            element = self.driver.execute_script(breadcrumb_second_arrow_script);
            breadcrumb_second_arrow_element.append(element)
          

            breadcrumb_third_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child'),'::before').getPropertyValue('content')";
            element = self.driver.execute_script(breadcrumb_third_arrow_script);
            breadcrumb_third_arrow_element.append(element)
            
            breadcrumb_fourthLevel_color.append(self.get_css_color((By.CSS_SELECTOR, "ol.breadcrumb > li:last-child > a"), "color"))
            self.driver.back()
            row_index = row_index + 1
            if row_index == 4:
                break
        
        return row_index, breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_third_arrow_element,breadcrumb_fourthLevel_color


    def check_all_breadcrumb_url(self):

        breadcumb_anchor_url_list = []
        breadcumb_anchor_current_url_list = []
        breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
        breadcumb_index = 0
        for breadcumb_anchor in breadcumb_anchor_elements:

            breadcumb_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
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

            # if breadcumb_index == 2:
            #     break

        return breadcumb_anchor_url_list, breadcumb_anchor_current_url_list 

    def breadcrumbs_firstLevel_secondLevel_thirdLevel(self):

        home_url = []
        home_current_url = []
        careers_url = []
        careers_current_url = []
        careers_search_url = []
        careers_current_search_url = []
        breadcrumb_index = 0
        row_index = 0
        breadcumb_anchor_url = ''

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
            for breadcrumb in breadcrumb_lists_anchor_elements:
                if breadcrumb_index == 0:
                    breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
                    home_url.append(breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href"))
                    breadcumb_anchor_url = breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href")
                    # self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
                    # self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
                    try:
                        if 'Windows' in platform.system():
                            ActionChains(self.driver).key_down(Keys.CONTROL).click(breadcrumb_lists_anchor_elements[breadcrumb_index]).key_up(Keys.CONTROL).perform()
                        elif 'Darwin' in platform.system():
                            ActionChains(self.driver).key_down(Keys.COMMAND).click(breadcrumb_lists_anchor_elements[breadcrumb_index]).key_up(Keys.COMMAND).perform()
                        self.driver.switch_to.window(self.driver.window_handles[1])

                        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
                        # That's why we are pressing on mega menu two times to ignore the issue.
                        self.press_button(self.mega_menu_btn_css)
                        self.press_button(self.mega_menu_btn_css)
                        
                        careers_current_url.append(self.driver.current_url)
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])
                    except:
                        self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
                        careers_current_url.append(self.driver.current_url)
                        self.driver.back()
                elif breadcrumb_index == 1:
                    breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
                    careers_url.append(breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href"))
                    breadcumb_anchor_url = breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href")
                    # self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
                    try:
                        if 'Windows' in platform.system():
                            ActionChains(self.driver).key_down(Keys.CONTROL).click(breadcrumb_lists_anchor_elements[breadcrumb_index]).key_up(Keys.CONTROL).perform()
                        elif 'Darwin' in platform.system():
                            ActionChains(self.driver).key_down(Keys.COMMAND).click(breadcrumb_lists_anchor_elements[breadcrumb_index]).key_up(Keys.COMMAND).perform()
                        self.driver.switch_to.window(self.driver.window_handles[1])

                        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
                        # That's why we are pressing on mega menu two times to ignore the issue.
                        self.press_button(self.mega_menu_btn_css)
                        self.press_button(self.mega_menu_btn_css)
                        
                        careers_current_url.append(self.driver.current_url)
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])
                    except:
                        self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
                        careers_current_url.append(self.driver.current_url)
                        self.driver.back()
                elif breadcrumb_index == 2:
                    breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
                    careers_search_url.append(breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href"))
                    breadcumb_anchor_url = breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href")
                    # self.driver.execute_script("arguments[0].click()", breadcumb_anchor_elements[breadcumb_index])
                    try:
                        if 'Windows' in platform.system():
                            ActionChains(self.driver).key_down(Keys.CONTROL).click(breadcrumb_lists_anchor_elements[breadcrumb_index]).key_up(Keys.CONTROL).perform()
                        elif 'Darwin' in platform.system():
                            ActionChains(self.driver).key_down(Keys.COMMAND).click(breadcrumb_lists_anchor_elements[breadcrumb_index]).key_up(Keys.COMMAND).perform()
                        self.driver.switch_to.window(self.driver.window_handles[1])

                        # While the page is loading, the menu tabs are displaying in 2 columns. After loading is complete, it's displaying correctly.
                        # That's why we are pressing on mega menu two times to ignore the issue.
                        self.press_button(self.mega_menu_btn_css)
                        self.press_button(self.mega_menu_btn_css)
                        
                        careers_current_url.append(self.driver.current_url)
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])
                    except:
                        self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
                        careers_current_url.append(self.driver.current_url)
                        self.driver.back()
                else:
                    break
                breadcrumb_index = breadcrumb_index + 1
                # if breadcrumb_index == 3:
                #     breadcrumb_index = 0

            self.driver.back()
            row_index = row_index + 1
            if row_index == 4:
                break
        
        return row_index,home_url, home_current_url, careers_url, careers_current_url, careers_search_url, careers_current_search_url


    def job_details_content(self):
    
         jobs_page_title =[]
         job_titles = []
         job_id_status = []
         job_id_last_char = []
         job_date_status = []
         job_location_status = []
         row_index = 0

         if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

         total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
         for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            job_title = total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]).text
            job_titles.append(job_title)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            jobs_page_title.append(self.get_element_text(self.job_page_title_css))
            job_id_status.append(self.is_displayed(self.job_id_css))
            job_id_last_char.append(self.get_element_text(self.job_id_css))
            job_date_status.append(self.is_displayed(self.job_date_css))
            job_location_status.append(self.is_displayed(self.job_location_css))
        
            self.driver.back()
            row_index = row_index + 1
            if row_index == 4:
                break

         return row_index,job_titles,jobs_page_title,job_id_status, job_date_status, job_location_status, job_id_last_char

    def job_description(self):
    
        row_index = 0
        job_desc_list = []
        job_desc_tag_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            job_title = total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]).text
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))

            job_desc_list.append(self.get_element_text(self.job_desc_css))
            job_desc_tag_list.append(self.get_tag_name(self.job_desc_css))
            
        
            self.driver.back()
            row_index = row_index + 1
            if row_index == 4:
                break  

        return job_desc_list, job_desc_tag_list

        
    def job_details_content_right(self):

        job_titles = []
        jobs_page_title =[]
        job_img_status = []
        job_id_status = []
        row_index = 0

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            job_title = str(total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]).text.encode("utf-8"))[1:].replace("'","")
            job_titles.append(job_title)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            if self.driver.get_window_size().get("width") > 1050:
                job_img_status.append(self.is_displayed(self.job_img_css))
                jobs_page_title.append(str(self.driver.find_element(*self.frame_job_title_css).text.encode("utf-8"))[1:].replace("'",""))
                job_id_status.append(self.is_displayed(self.frame_job_id_css))


            self.driver.back()
            row_index = row_index + 1
            if row_index == 4:
                break

        return row_index, job_titles,jobs_page_title,job_img_status,job_id_status


    def jobs_link_button(self):

        row_index = 0
        job_index = 0
        jobs_button_status = []
        popup_logo_list = []
        popup_title_list = []
        popup_desc_title =[]
        popup_continue_list =[]
        continue_btn_clickable_status =[]
        cancel_button_list =[]
        cancel_btn_clickable_status = []
        current_page_url_list = []
        page_url_list = []
        job_url_list =[]
        apply_access_job_page_url_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            current_page_url = self.driver.current_url

            jobs = self.apple_access_job_by_screen_size()
        

            for job in jobs:
                jobs = self.apple_access_job_by_screen_size()
                jobs_button_status.append(self.is_displayed_ele(jobs[job_index]))
                pop_up_logo, pop_up_title, pop_up_desc, continue_btn, continue_btn_clickable, cancel_btn, cancel_btn_clickable, page_url = self.external_link(jobs[job_index])
                popup_logo_list.append(pop_up_logo)
                popup_title_list.append(len(pop_up_title))
                popup_desc_title.append(pop_up_desc)
                popup_continue_list.append(continue_btn)
                continue_btn_clickable_status.append(continue_btn_clickable)
                cancel_button_list.append(cancel_btn)
                cancel_btn_clickable_status.append(cancel_btn_clickable)
                current_page_url_list.append(current_page_url)
                page_url_list.append(page_url)

                jobs = self.apple_access_job_by_screen_size()
                class_name = jobs[job_index].get_attribute("class")
                job_url, apply_access_job_page_url = self.apply_access_job_page(jobs[job_index], class_name)
                
                job_url_list.append(job_url)
                apply_access_job_page_url_list.append(len(apply_access_job_page_url))

                job_index = job_index + 1
                if job_index == 2:
                    job_index = 0
    
            self.driver.back()
            row_index = row_index + 1
            if row_index == 4:
                break

        
        return row_index,jobs_button_status,popup_logo_list,popup_title_list,popup_desc_title,popup_continue_list,continue_btn_clickable_status,cancel_button_list,cancel_btn_clickable_status,current_page_url_list,page_url_list,job_url_list,apply_access_job_page_url_list

    def jobs_content(self):

        row_index = 0
        job_content_class_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            job_content_class_list.append(self.get_elemet_attribute(self.jobs_content_css, "class"))

            self.driver.back()

            row_index = row_index + 1
            if row_index == 4:
                break
        
        return row_index,job_content_class_list


    def right_hand_rail(self):

        row_index = 0
        right_hand_rail_list = []

        if self.driver.find_elements(*self.clear_all_css):
            self.press_button(self.clear_all_css)

        total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
        for row in total_rows:

            total_rows = self.driver.find_elements(self.total_row_css[0], self.total_row_css[1])
            rand_num = random.randint(0,len(total_rows) - 1)
            self.driver.execute_script("arguments[0].click()", total_rows[rand_num].find_element(self.job_title_css[0], self.job_title_css[1]))
            right_hand_rail_list.append(len(self.driver.find_elements(*self.right_hand_rail_xpath)))

            self.driver.back()

            row_index = row_index + 1
            if row_index == 4:
                break
        
        return row_index,right_hand_rail_list




    # def apply_access_job_page(self, by_locator):

    #     job_url = self.get_elemet_attribute(by_locator, "href")
    #     self.press_button(by_locator)
    #     self.press_button(self.continue_button_css)
    #     apply_access_job_page_url = self.driver.current_url
    #     self.driver.back()

    #     return job_url, apply_access_job_page_url

    
    # def breadcrumb_ele(self):

    #     breadcrumb_items = []
    #     breadcrumb_lists = self.driver.find_elements(self.breadcrumb_lists_css[0], self.breadcrumb_lists_css[1])
    #     for breadcrumb_list in breadcrumb_lists:
    #         breadcrumb_items.append(breadcrumb_list.find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]).text)


    #     breadcrumb_first_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').getPropertyValue('content')";
    #     breadcrumb_first_arrow_element = self.driver.execute_script(breadcrumb_first_arrow_script);

    #     breadcrumb_second_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(3)'),'::before').getPropertyValue('content')";
    #     breadcrumb_second_arrow_element = self.driver.execute_script(breadcrumb_second_arrow_script);

    #     breadcrumb_third_arrow_script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:last-child'),'::before').getPropertyValue('content')";
    #     breadcrumb_third_arrow_element = self.driver.execute_script(breadcrumb_third_arrow_script);


    #     home_url = ''
    #     home_current_url = ''
    #     careers_url = ''
    #     careers_current_url = ''
    #     careers_search_url = ''
    #     careers_current_search_url = ''
    #     breadcrumb_index = 0
    #     breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
    #     for breadcrumb in breadcrumb_lists_anchor_elements:
    #         if breadcrumb_index == 0:
    #             breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
    #             home_url = breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href")
    #             self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
    #             home_current_url = self.driver.current_url
    #             self.driver.back()
    #         elif breadcrumb_index == 1:
    #             breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
    #             careers_url = breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href")
    #             self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
    #             careers_current_url = self.driver.current_url
    #             self.driver.back()
    #         elif breadcrumb_index == 2:
    #             breadcrumb_lists_anchor_elements = self.driver.find_elements(self.breadcrumb_lists_anchor_css[0], self.breadcrumb_lists_anchor_css[1])
    #             careers_search_url = breadcrumb_lists_anchor_elements[breadcrumb_index].get_attribute("href")
    #             self.driver.execute_script("arguments[0].click()", breadcrumb_lists_anchor_elements[breadcrumb_index])
    #             careers_current_search_url = self.driver.current_url
    #             self.driver.back()
    #         else:
    #             break
    #         breadcrumb_index = breadcrumb_index + 1

        

        
    #     return breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element, breadcrumb_third_arrow_element, home_url, home_current_url, careers_url, careers_current_url, careers_search_url, careers_current_search_url

    # def print_btn_ele(self):

    #     print_btn_txt = self.get_element_text(self.print_css)
    #     print_btn_clickable = self.element_clickable(self.print_css)
    #     print_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('li.print > a'),'::before').getPropertyValue('background')");
    #     print_url = self.get_elemet_attribute(self.print_css, "href")
    #     self.press_button(self.print_css)
    #     print_page_url = self.driver.current_url
    #     self.driver.back()
        
    #     return print_btn_txt, print_btn_clickable, print_icon, print_url, print_page_url

    # def share_btn_ele(self):

    #     share_btn_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.addtoany_share'),'::before').getPropertyValue('background')");
    #     share_btn_txt = self.get_element_text(self.share_btn_txt_css)
    #     self.press_button(self.share_btn_css)

    #     twitter_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_twitter'),'::before').getPropertyValue('background')");
    #     facebook_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_facebook'),'::before').getPropertyValue('background')");
    #     whatsapp_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_whatsapp'),'::before').getPropertyValue('background')");
    #     linkedin_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_linkedin'),'::before').getPropertyValue('background')");
    #     email_icon = self.driver.execute_script("return window.getComputedStyle(document.querySelector('.a2a_button_email'),'::before').getPropertyValue('background')");

    #     return share_btn_icon, share_btn_txt, twitter_icon, facebook_icon, whatsapp_icon, linkedin_icon, email_icon


    #   def tag_ele(self):

    #     tag_elements = self.driver.find_elements(self.tage_elements_css[0], self.tage_elements_css[1])
    #     tag_elements_len = len(tag_elements)
    #     tag_elements_list = []
    #     tag_elements_url_list = []
    #     tag_elements_page_url_list = []
    #     tag_element_index = 0

    #     for tag_element in tag_elements:

    #         tag_elements = self.driver.find_elements(self.tage_elements_css[0], self.tage_elements_css[1])
    #         tag_elements_list.append(tag_elements[tag_element_index].text)
    #         tag_elements_url_list.append(tag_elements[tag_element_index].get_attribute("href"))
    #         self.driver.execute_script("arguments[0].click()", tag_elements[tag_element_index])
    #         tag_elements_page_url_list.append(self.driver.current_url)
    #         self.driver.back()
    #         tag_element_index = tag_element_index + 1
    
    #     return tag_elements_len, tag_elements_list, tag_elements_url_list, tag_elements_page_url_list


    # def label_name_value_ele(self):

    #     job_details_table = self.driver.find_elements(self.job_details_css[0], self.job_details_css[1])
    #     job_detail_label_list = []
    #     job_detail_value_list = []

    #     for job_detail in job_details_table:

    #         job_detail_label_list.append(job_detail.find_element(self.job_detail_label_css[0], self.job_detail_label_css[1]).text)
    #         job_detail_value_list.append(job_detail.find_element(self.job_detail_value_css[0], self.job_detail_value_css[1]).text)

    #     return job_detail_label_list, job_detail_value_list
