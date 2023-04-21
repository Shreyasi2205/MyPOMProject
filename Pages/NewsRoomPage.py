import time
from Pages.BasePage import BasePage
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException


class NewsRoomPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    hero_img_css = (By.CSS_SELECTOR, "div.carousel_img_video > div > img")
    hero_txt_css = (By.CSS_SELECTOR, "div.carousel-caption > div.container > div.carousel_inner--wrapper > h1.stripe_title")
    stripe_xpath = (By.XPATH,"//div[@class='field__item']/div[contains(@class,'card-stripe')]")
    card_image_css = (By.CSS_SELECTOR,".card_img")
    card_title_css = (By.CSS_SELECTOR,".card_title")
    card_desc_css = (By.CSS_SELECTOR,".card_content >.basic_paragraph")
    tweeter_id = (By.ID, "tweeter_show")
    tweeter_css = (By.CSS_SELECTOR,'.card_wrapper  > #tweeter_show > div >div >div >.carousel-item')
    media_release_xpath = (By.XPATH,'//div[@class="media-releases-list row"]')
    media_cards_css = (By.CSS_SELECTOR,'div.media-releases-list > a')
    media_label_css = (By.CSS_SELECTOR,'ul.meta_content')
    media_date_css = (By.CSS_SELECTOR,'p.meta_content')
    link_button_css = (By.CSS_SELECTOR, "a.link_button")
    media_stripe_img_css= (By.CSS_SELECTOR,'.media_stripe_img')
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    table_header_css = (By.CSS_SELECTOR, "th")
    footer_search_xpath = (By.XPATH, "//input[contains(@id, 'edit-keys')]")
    twitter_icon_css = (By.CSS_SELECTOR,'.twitter_line_icon')
    twitter_time_css = (By.CSS_SELECTOR,'.tweeter_time')
    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    hero_box_css = (By.CSS_SELECTOR,".container>.carousel_inner--wrapper  ")
    twitter = (By.CSS_SELECTOR, ".social-media-link-icon--twitter")
    pop_up_logo_css = (By.CSS_SELECTOR, ".ui-dialog-titlebar > .img-fluid.d-inline-block.align-top")
    pop_up_title_css = (By.CSS_SELECTOR, ".ui-dialog-title")
    pop_up_body_css = (By.CSS_SELECTOR, ".external-link-popup-body > p")
    continue_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)")
    cancel_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(2)")
    carousel_items_css = (By.CSS_SELECTOR,'.carousel-indicators > li')
    continue_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)")
    link_btn_css = (By.CSS_SELECTOR, "a.link_button.button_text")

    def hero_image_text(self):

        hero_img_len = len(self.get_elemet_attribute(self.hero_img_css, "src")) 
        hero_txt_len = len(self.get_element_text(self.hero_txt_css)) 

        return hero_img_len, hero_txt_len
        
    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)
        

    def stripe_ele(self):

        stripe_elements = self.driver.find_elements(self.stripe_xpath[0], self.stripe_xpath[1])
        stripe_list = []
        index = 0

        for stripe_element in stripe_elements:

            stripe_elements = self.driver.find_elements(self.stripe_xpath[0], self.stripe_xpath[1])
            stripe_list.append(stripe_elements[index].get_attribute("class"))
            index += 1

        return stripe_list


    def stripe_card_val(self,image,text,desc):

        
        cards_length =[]
        elements = [image,text,desc]
        tweeter = 0
        
        for ele in elements:
            card_elements = self.driver.find_elements(*ele)
            card_ele_len = len(card_elements)
            cards_length.append(card_ele_len)

        if self.driver.find_elements(self.tweeter_id[0], self.tweeter_id[1]):
            tweeter = len(self.get_elemet_attribute(self.tweeter_css, "class")) 

        return cards_length,tweeter

    def media_release_label(self):

        displayed_status = False
        media_card = 0
        media_label = 0

        if self.driver.find_elements(*self.media_release_xpath):
            
            displayed_status = True
            media_card = len(self.driver.find_elements(*self.media_cards_css))
            media_label = len(self.driver.find_elements(*self.media_label_css))
        
        return displayed_status, media_card ,media_label

    

    def media_date_val(self, env_name):
        
        original_date = []
        sorted_date = []
        original_date_sorted = []
        desc_sort = False

        mediadate = self.driver.find_elements(*self.media_date_css)
        for date in mediadate:
            # original_date.append(date.text)

            if "switzerland-fr" in env_name:
                original_date.append(date.text)
            elif "switzerland" in env_name:
                original_date.append(date.text.replace(".",""))
            else:
                original_date.append(date.text.replace(",",""))

        # sorted_date =  original_date[:]

        # sorted_date.sort(key=lambda date: datetime.strptime(date, '%b %d, %Y'),reverse=True)

        if "switzerland-fr" in env_name:
            ch_date_format_list = self.french_months(original_date)
            original_date_sorted = ch_date_format_list[:]
            original_date_sorted.sort(key = lambda date: datetime.strptime(date, '%d %B %Y'), reverse=True)
            if original_date_sorted == ch_date_format_list:
                desc_sort = True
        elif "switzerland" in env_name:
            ch_date_format_list = self.german_months(original_date)
            original_date_sorted = ch_date_format_list[:]
            original_date_sorted.sort(key = lambda date: datetime.strptime(date, '%d %B %Y'), reverse=True)
            if original_date_sorted == ch_date_format_list:
                desc_sort = True
        else:
            original_date_sorted = original_date[:]
            original_date_sorted.sort(key = lambda date: datetime.strptime(date, '%b %d %Y'), reverse=True)
            if original_date_sorted == original_date:
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


    def links_button(self):

        links_button = self.driver.find_elements(*self.link_button_css)
        links_button_index = 0
        links_button_url_list = []
        links_button_ext_url_list = []
        links_button_current_url_list = []
        links_button_ext_current_url_list = []

        for btn in links_button:
            
            links_button = self.driver.find_elements(*self.link_button_css)
            ext_available = links_button[links_button_index].get_attribute("class").split(" ")
            if "_blank" not in links_button[links_button_index].get_attribute("target") and "live.novartis.com" not in links_button[links_button_index].get_attribute("href") :
                links_button = self.driver.find_elements(*self.link_button_css)
                links_button_url_list.append(links_button[links_button_index].get_attribute("href"))
                self.driver.execute_script("arguments[0].click()", links_button[links_button_index])
                if self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                links_button_current_url_list.append(self.driver.current_url)
                self.driver.back()
            
            links_button_index += 1
        
        links_button_index = 0
        for btn in links_button:
            
            links_button = self.driver.find_elements(*self.link_button_css)
            ext_available = links_button[links_button_index].get_attribute("class").split(" ")
            
            if "ext" in ext_available and links_button[links_button_index].get_attribute("target") == "_blank":
                links_button = self.driver.find_elements(*self.link_button_css)
                links_button_ext_url_list.append(links_button[links_button_index].get_attribute("href"))
                self.driver.execute_script("arguments[0].click()", links_button[links_button_index])
                self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                child = self.driver.window_handles[1]
                parent = self.driver.window_handles[0]
                self.driver.switch_to.window(child)
                links_button_ext_current_url_list.append(self.driver.current_url)
                self.driver.close()
                self.driver.switch_to.window(parent)
            links_button_index += 1
            
        links_button_index = 0
        for btn in links_button:
            
            links_button = self.driver.find_elements(*self.link_button_css)
            href_ext = links_button[links_button_index].get_attribute("href")
            
            if "live.novartis.com" in href_ext and "_blank" not in links_button[links_button_index].get_attribute("target"):
                links_button = self.driver.find_elements(*self.link_button_css)
                links_button_ext_url_list.append(links_button[links_button_index].get_attribute("href"))
                self.driver.execute_script("arguments[0].click()", links_button[links_button_index])
                self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                links_button_ext_current_url_list.append(self.driver.current_url)
                self.driver.back()
            elif "live.novartis.com" in href_ext and "_blank" in links_button[links_button_index].get_attribute("target"):
                links_button = self.driver.find_elements(*self.link_button_css)
                links_button_ext_url_list.append(links_button[links_button_index].get_attribute("href"))
                self.driver.execute_script("arguments[0].click()", links_button[links_button_index])
                self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                child = self.driver.window_handles[1]
                parent = self.driver.window_handles[0]
                self.driver.switch_to.window(child)
                links_button_ext_current_url_list.append(self.driver.current_url)
                self.driver.close()
                self.driver.switch_to.window(parent)
            links_button_index += 1

        return links_button_url_list, links_button_current_url_list, links_button_ext_url_list, links_button_ext_current_url_list

    def stripe_img(self):

        images = self.driver.find_elements(*self.media_stripe_img_css)
        displayed_status = False
        index = 0

        for img in images:

            images = self.driver.find_elements(*self.media_stripe_img_css)
            displayed_status = images[index].is_displayed()
            index += 1
        return displayed_status

        


    

         



            


        




