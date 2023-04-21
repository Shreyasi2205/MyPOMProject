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
from Utilities.config import Utilities

class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    search_input_field_xpath = (By.XPATH, "//*[starts-with(@id,'edit-search-api-fulltext')]")
    search_btn_field_xpath = (By.XPATH, "//*[starts-with(@id,'edit-submit-products-overview')]")
    next_page_arrow_xpath = (By.XPATH, "//a[@rel='next']")
    prev_page_arrow_xpath = (By.XPATH, "//a[@rel='prev']")
    empty_css = (By.CSS_SELECTOR, "div.view-empty")
    product_title_css = (By.CSS_SELECTOR, "ul > li > div.row > div > div.product-title > h3")
    a_z_toggle_view_css = (By.CSS_SELECTOR, "div.toggle_over_view > a")
    pop_up_logo_css = (By.CSS_SELECTOR, ".ui-dialog-titlebar > .img-fluid.d-inline-block.align-top.novartis-logo")
    pop_up_title_css = (By.CSS_SELECTOR, ".ui-dialog-title")
    pop_up_body_css = (By.CSS_SELECTOR, ".external-link-popup-body > p")
    continue_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)")
    cancel_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(2)")
    continue_button_txt = "Continue"
    cancel_button_txt = "Cancel"
    page_title_css = (By.CSS_SELECTOR, "div.content > div.clearfix > h1")
    page_intro_text_css = (By.CSS_SELECTOR, "div.content > div.clearfix > p")
    product_list_css = (By.CSS_SELECTOR, "ul > li > div.row > div.left-portfolio")
    total_row_css = (By.CSS_SELECTOR, "ul > li > div.row")
    available_in_css = (By.CSS_SELECTOR, "ul > li > div.row > div.right-portfolio > div > span")
    filter_tabs_css = (By.CSS_SELECTOR, "ul.pop-list > li > a")
    hyperlink_css = (By.CSS_SELECTOR, "ul > li > div.row > div.right-portfolio > div.countries > div > a")
    download_btn_css = (By.CSS_SELECTOR, "ul > li > div.row > div.right-portfolio > div.downloads > div.dropdown")
    anchor_tag_css = (By.CSS_SELECTOR, "a")
    menu_tabs_css = (By.CSS_SELECTOR, "div.item-list > ul > li > a.content-type")
    mega_menu_about_arrow_xpath = (By.XPATH, "//li[contains(@class, 'dropdown-menu')]/a[contains(@href, 'about')  and not(contains(@href,'about/'))]//parent::li/p")
    mega_menu_patient_caregivers_arrow_xpath = (By.XPATH,"//li[contains(@class, 'dropdown-menu')]/a[contains(@href, '/patients-and-caregivers')  and not(contains(@href,'about/'))]//parent::li/p")
    mega_menu_about_xpath = (By.XPATH, "//li[contains(@class, 'dropdown-menu')]/a[contains(@href, '/about') and not(contains(@href,'about/'))]")
    mega_menu_patient_caregivers_xpath = (By.XPATH,"//li[contains(@class, 'dropdown-menu')]/a[contains(@href, '/patients-and-caregivers') and not(contains(@href,'about/'))]")
    mega_menu_product_xpath = (By.XPATH, "//li[contains(@class, 'we-mega-menu-li')]/a[contains(@href, '/about/products')]")
    patient_caregivers_product_xpath = (By.XPATH,"//li[contains(@class, 'we-mega-menu-li')]/a[contains(@href, '/products-list')]")
    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    filter_tab_css = (By.CSS_SELECTOR, "ul.pop-list > li")
    anchor_tag_loc = (By.TAG_NAME, "a")
    description_css = (By.CSS_SELECTOR,'[class="content"]>div>p')
    duplicate_product_desc_xpath = (By.XPATH, "//div[contains(@id, 'block-global-product-portfolio')]")
    right_portfolio_xpath = (By.XPATH,"//div[contains(@class,'right-portfolio')]")
    accordion_xpath = (By.XPATH,"//button[contains(@class,'accordion-title')]")
    other_right_portfolio_xpath = (By.XPATH,"//div[contains(@class,'doc_product_cat')]")
    file_css = (By.CSS_SELECTOR,"a.btm-download")
    download_icon_css = (By.XPATH,"//a[contains(@class,'btm-download')]/span[contains(@class,'download-icon')]")
    pagination_numbers_css = (By.CSS_SELECTOR, "ul.pagination > li")
    page_link_css = (By.CSS_SELECTOR, ".page-link")
    product_name_xpath = (By.XPATH,"parent::a/ancestor::div[contains(@class,'right-portfolio')]/preceding-sibling::div/div")
    products_css = (By.CSS_SELECTOR, ".product-portfolio")
    download_link_as_button_css = (By.CSS_SELECTOR,"[class='btm-download apply_btn']")
    

    def launch_productPage(self,env_name):

        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_about_arrow_xpath)
                # self.press_button(self.mega_menu_patient_caregivers_arrow_xpath)

            else:
                 self.move_to_element(self.mega_menu_about_xpath)
            #    self.move_to_element(self.mega_menu_patient_caregivers_xpath)

            self.press_button(self.mega_menu_product_xpath)
            # self.press_button(self.patient_caregivers_product_xpath)
        except:
            menu = Utilities.multi_language[env_name]['about']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['product']
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))

    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)

    def available_in_ele(self):

        total_available_in = self.driver.find_elements(self.available_in_css[0], self.available_in_css[1])
        available_in_list = []

        for available_in in total_available_in:

           available_in_list.append(self.is_displayed_ele(available_in))

        return available_in_list


    def filter_tabs_presence(self):

        filter_tab_list = []

        total_filter_tabs = self.driver.find_elements(self.filter_tabs_css[0], self.filter_tabs_css[1])

        for filter_tab in total_filter_tabs:

            filter_tab_list.append(self.is_displayed_ele(filter_tab))
            # filter_tab_list.append(filter_tab.text)

        return filter_tab_list


    def pagination_check(self):

        self.press_button(self.next_page_arrow_xpath)
        next_page_url = self.driver.current_url
        self.press_button(self.prev_page_arrow_xpath)
        prev_page_url = self.driver.current_url

        return next_page_url, prev_page_url


    def no_result_check(self):

        self.send_keys(self.search_input_field_xpath, "Drug")
        self.press_button(self.search_btn_field_xpath)


    def verify_search_result(self):

        self.send_keys(self.search_input_field_xpath, "Afinitor")
        self.press_button(self.search_btn_field_xpath)

        search_result_list = []

        total_product_titles = self.driver.find_elements(self.product_title_css[0], self.product_title_css[1])
        
        for product_title in total_product_titles:

            search_result_list.append(product_title.text)

        return search_result_list


    def toggle_view(self):

        self.press_button(self.a_z_toggle_view_css)
        a_z_view = self.get_element_text(self.a_z_toggle_view_css)
        self.press_button(self.a_z_toggle_view_css)
        z_a_view = self.get_element_text(self.a_z_toggle_view_css)

        return a_z_view, z_a_view


    def internal_hyperlink_check(self):

        hyperlinks = self.driver.find_elements(self.hyperlink_css[0], self.hyperlink_css[1])
        domain_url = ""
        domain_current_url = ""
        for hyperlink in hyperlinks:
            
            if "www.novartis" in hyperlink.get_attribute("href"):

                domain_url = hyperlink.get_attribute("href")
                self.driver.execute_script("arguments[0].click()", hyperlink)
                domain_current_url = self.driver.current_url
                self.driver.back()
                break

                
        return domain_url, domain_current_url


    def external_hyperlink_check(self):

        hyperlinks = self.driver.find_elements(self.hyperlink_css[0], self.hyperlink_css[1])
        external_domain_url = ""
        external_domain_current_url = ""
        pop_up_logo = ""
        pop_up_title = ""
        pop_up_desc = ""
        continue_btn = ""
        cancel_btn = ""
        current_page_title = ""

        for hyperlink in hyperlinks:
            
            if hyperlink.get_attribute("class") == "ext":

                external_domain_url = hyperlink.get_attribute("href")
                self.driver.execute_script("arguments[0].click()", hyperlink)
                pop_up_logo = self.get_elemet_attribute(self.pop_up_logo_css, "src")
                pop_up_title = self.get_element_text(self.pop_up_title_css)
                pop_up_desc = self.get_element_text(self.pop_up_body_css)
                continue_btn =  self.get_element_text(self.continue_button_css)
                cancel_btn = self.get_element_text(self.cancel_button_css)
                self.press_button(self.cancel_button_css)
                current_page_title = self.driver.title

                self.driver.execute_script("arguments[0].click()", hyperlink)
                self.press_button(self.continue_button_css)
                child = self.driver.window_handles[1]
                parent = self.driver.window_handles[0]
                self.driver.switch_to.window(child)

                external_domain_current_url = self.driver.current_url

                self.driver.close()
                self.driver.switch_to.window(parent)

                break

                
        return external_domain_url, external_domain_current_url, pop_up_logo, pop_up_title, pop_up_desc, continue_btn, cancel_btn, current_page_title



    def download_btn_ele(self):

        download_buttons = self.driver.find_elements(self.download_btn_css[0], self.download_btn_css[1])
    
                  
        for download_btn in download_buttons:

            download_btn_txt = download_btn.find_element(self.anchor_tag_css[0], self.anchor_tag_css[1]).text
            download_btn_clickable = bool(WebDriverWait(download_btn, 10).until(ec.element_to_be_clickable(self.anchor_tag_css)))
            flag = 1
            break

        return download_btn_txt, download_btn_clickable, flag


    def check_greyColor(self):



        grey_color_list = []
        menu_tabs = self.driver.find_elements(self.menu_tabs_css[0], self.menu_tabs_css[1])
        menu_tab_index = 0
        
        for menu in menu_tabs:
            menu_tabs = self.driver.find_elements(self.menu_tabs_css[0], self.menu_tabs_css[1])
            self.driver.execute_script("arguments[0].click()", menu_tabs[menu_tab_index])
            menu_tabs = self.driver.find_elements(self.menu_tabs_css[0], self.menu_tabs_css[1])
            value_of_css = menu_tabs[menu_tab_index].value_of_css_property("background-color")
            hex = Color.from_string(value_of_css).hex
            grey_color_list.append(hex)
            menu_tab_index = menu_tab_index + 1
            

        return  grey_color_list

    def check_alphabetical_order(self):


        alphabetical_order_list = []
        menu_tabs = self.driver.find_elements(self.menu_tabs_css[0], self.menu_tabs_css[1])
        menu_tab_index = 0
        
        for menu in menu_tabs:
            menu_tabs = self.driver.find_elements(self.menu_tabs_css[0], self.menu_tabs_css[1])
            self.driver.execute_script("arguments[0].click()", menu_tabs[menu_tab_index])
            alphabetical_order_list.append(self.get_element_text(self.a_z_toggle_view_css))
            menu_tab_index = menu_tab_index + 1

        return alphabetical_order_list


    def duplicate_description(self):

        description_list = []
        flag = 0
        # duplicate_description_id_list = []

        total_filter_tabs = self.driver.find_elements(self.filter_tab_css [0], self.filter_tab_css [1])
        total_filter_tabs_len = len(total_filter_tabs)
        count = 0
        while total_filter_tabs_len > 0:
            
            total_filter_tabs = self.driver.find_elements(self.filter_tab_css [0], self.filter_tab_css [1])
            self.driver.execute_script("arguments[0].click()", total_filter_tabs[count].find_element(self.anchor_tag_loc[0], self.anchor_tag_loc[1]))
            descriptions = self.driver.find_elements(*self.description_css)
            for desc in descriptions:
                description_list.append(desc.text.split(".")[0])
            if len(description_list) != len(set(description_list)):
                flag = 1
                break
            # duplicate_description_id_list.append(len(self.driver.find_elements(*self.duplicate_product_desc_xpath)))

            # description_list.append(description_len)
            count = count + 1
            total_filter_tabs_len = total_filter_tabs_len - 1
            description_list.clear()

        return flag


    def file_download_button(self):

        file = 0 
        accordion = 0
        accordion_len = 0
        other_right_portfolio = 0
        download_icon_len = 0
        display_status = []
        pagination_count = 0
        product_name = []
        while pagination_count <= 3:

            next_button = self.driver.find_elements(self.next_page_arrow_xpath[0], self.next_page_arrow_xpath[1])
            if next_button or pagination_count == 0:
                accordion = len(self.driver.find_elements(self.accordion_xpath[0], self.accordion_xpath[1]))
                if accordion > 0 :
                    accordion = self.driver.find_elements(self.accordion_xpath[0], self.accordion_xpath[1])
                    accordion_len = len(self.driver.find_elements(self.accordion_xpath[0], self.accordion_xpath[1]))
                    
                    for accord in accordion:
                        self.driver.execute_script("arguments[0].click()", accord)
                    file = len(self.driver.find_elements(self.file_css[0], self.file_css[1]))
                    download_icon_len = len(self.driver.find_elements(self.download_icon_css[0], self.download_icon_css[1]))
                    download_icon = self.driver.find_elements(self.download_icon_css[0], self.download_icon_css[1])
                    count = 0
                    for icon in download_icon:
                        download_icon = self.driver.find_elements(self.download_icon_css[0], self.download_icon_css[1])
                        display_status.append(self.is_displayed_ele(icon))
                        if not self.is_displayed_ele(download_icon[count]):
                            product_name.append(download_icon[count].find_element(self.product_name_xpath[0], self.product_name_xpath[1]).text)

                        count += 1
                            

                else :
                    other_right_portfolio = len(self.driver.find_elements(self.other_right_portfolio_xpath[0], self.other_right_portfolio_xpath[1]))
                    if other_right_portfolio > 0 :
                        file = len(self.driver.find_elements(self.file_css[0], self.file_css[1]))
                        download_icon_len = len(self.driver.find_elements(self.download_icon_css[0], self.download_icon_css[1]))
                        download_icon = self.driver.find_elements(self.download_icon_css[0], self.download_icon_css[1])
                        count = 0
                        for icon in download_icon:
                            download_icon = self.driver.find_elements(self.download_icon_css[0], self.download_icon_css[1])
                            display_status.append(self.is_displayed_ele(icon))
                            if not self.is_displayed_ele(download_icon[count]):
                                product_name.append(download_icon[count].find_element(self.product_name_xpath[0], self.product_name_xpath[1]).text)

                            count += 1
            if next_button:
                self.press_button(self.next_page_arrow_xpath)
            pagination_count = pagination_count + 1


        return accordion_len, other_right_portfolio , file, download_icon_len , display_status, product_name



    def products_count(self):


        num_products_list = []
        pagination_count = 0
        num_products_list.append(len(self.driver.find_elements(self.products_css[0], self.products_css[1])))
        next_button = len(self.driver.find_elements(self.next_page_arrow_xpath[0], self.next_page_arrow_xpath[1]))
        
        while pagination_count <= 3:

            pagination_num = len(self.driver.find_elements(self.pagination_numbers_css[0], self.pagination_numbers_css[1]))
            next_button = len(self.driver.find_elements(self.next_page_arrow_xpath[0], self.next_page_arrow_xpath[1]))
            if pagination_num > 0 and next_button > 0:
                
                self.press_button(self.next_page_arrow_xpath)
                num_products_list.append(len(self.driver.find_elements(self.products_css[0], self.products_css[1])))

            pagination_count = pagination_count + 1
            if next_button == 0 :
                break
        return num_products_list, next_button


    def download_link_as_button(self):

        link_as_buttons = self.driver.find_elements(*self.download_link_as_button_css)
        len_buttons = len(link_as_buttons)
        return len_buttons
        




    # def check_filter_tab(self):


    #     alphabetical_order_list = []
    #     grey_color_list = []
    #     menu_tabs = self.driver.find_elements(self.menu_tabs_css[0], self.menu_tabs_css[1])
    #     menu_tab_index = 0
        
    #     for menu in menu_tabs:
    #         menu_tabs = self.driver.find_elements(self.menu_tabs_css[0], self.menu_tabs_css[1])
    #         self.driver.execute_script("arguments[0].click()", menu_tabs[menu_tab_index])
    #         menu_tabs = self.driver.find_elements(self.menu_tabs_css[0], self.menu_tabs_css[1])
    #         value_of_css = menu_tabs[menu_tab_index].value_of_css_property("background-color")
    #         hex = Color.from_string(value_of_css).hex
    #         grey_color_list.append(hex)
    #         menu_tab_index = menu_tab_index + 1
    #         alphabetical_order_list.append(self.get_element_text(self.a_z_toggle_view_css))

    #     return alphabetical_order_list, grey_color_list