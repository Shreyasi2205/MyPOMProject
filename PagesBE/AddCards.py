
import time
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException
from datetime import datetime
from Utilities.config import Utilities
import random
from datetime import date
from datetime import datetime, timedelta

class AddCards(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    landing_page_xpath = (By.XPATH, "//li[contains(@class, 'clearfix')]/a[contains(@href, 'landing_page')]")
    body_dropdown_btn_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    body_dropdown_btn_after_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-body-add-more-wrapper')]/div/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    add_cards_xpath = (By.XPATH, "//input[contains(@value, 'Add Cards')]")
    various_cards_dropdown_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-card-type')]/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    various_cards_dropdown_after_first_time_xpath = (By.XPATH, "//div[contains(@id, 'field-card-type')]/div/div/div/div/ul/li[contains(@class, 'dropbutton-toggle')]/button")
    img_css = (By.CSS_SELECTOR, 'img')
    submit_button_iframe_xpath = (By.XPATH, "//input[contains(@id, 'edit-submit') and not(contains(@id, 'media'))]")
    image_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_image_browser')]")
    video_iframe_xpath = (By.XPATH, "//iframe[contains(@id, 'entity_browser_iframe_media_browser')]")

    # THREE COL CARDS SELECTORS
    three_col_card_xpath = (By.XPATH, "//input[contains(@value, 'Add 3 columns equal size card stripe')]")
    # three_col_card_add_items_label_xpath = (By.XPATH, "//label[contains(@for, 'field-card-type-4') and contains(@for, 'subform-field-column')]")
    # three_col_card_add_item_xpath = (By.XPATH, "//select[contains(@id, 'subform-field-column-potrait') and contains(@id, 'field-card-type-4')]")

    # Add 2 columns 2/3 and 1/3 size card stripe
    two_col_two_three_card_xpath = (By.XPATH, "//input[contains(@value, 'Add 2 columns 2/3 and 1/3 size card stripe')]")

    # Add 2 columns 1/3 and 2/3 size card stripe
    two_col_one_three_card_xpath = (By.XPATH, "//input[contains(@value, 'Add 2 columns 1/3 and 2/3 size card stripe')]")

    # Add 2 columns 1/2 and 1/2 card stripe
    two_col_one_two_card_xpath = (By.XPATH, "//input[contains(@value, 'Add 2 columns 1/2 and 1/2 card stripe')]")

    # Add 1 column full width size card stripe
    one_col_card_xpath = (By.XPATH, "//input[contains(@value, 'Add 1 column full width size card stripe')]")

    card_title_label_xpath = (By.XPATH, "//label[contains(@for, 'field-card-type-0') and contains(@for, 'subform-field-title') and contains(@for, 'edit-field-body-0')]")
    card_desc_label_xpath = (By.XPATH, "//label[contains(@for, 'field-card-type-0') and contains(@for, 'subform-field-card-desc') and contains(@for, 'edit-field-body-0')]")
    card_content_column_label_xpath = (By.XPATH, "//label[contains(@for, 'field-card-type-0') and contains(@for, 'subform-field-content-column') and contains(@for, 'edit-field-body-0')]")
    card_image_label_xpath = (By.XPATH, "//div[contains(@id, 'field-card-type-0') and contains(@id, 'subform-field-image-wrapper') and contains(@id, 'edit-field-body-0')]/details/summary/span[not(contains(@class, 'summary'))]")
    card_external_url_label_xpath = (By.XPATH, "//label[contains(@for, 'field-card-type-0') and contains(@for, 'subform-field-url') and contains(@for, 'edit-field-body-0')]")
    card_video_label_xpath = (By.XPATH, "//div[contains(@id, 'field-card-type-0') and contains(@id, 'subform-field-document') and contains(@id, 'edit-field-body-0')]/details/summary")

    card_title_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-title') and contains(@id, 'field-card-type-0') and contains(@id, 'edit-field-body-0')]")
    card_description_xpath = (By.XPATH, "//div[contains(@id, 'field-card-type-0') and contains(@id, 'subform-field-card-description') and contains(@id, 'edit-field-body-0')]/div/div/textarea")
    card_content_column_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-content-column') and contains(@id, 'field-card-type-0') and contains(@id, 'edit-field-body-0')]")
    card_external_url_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-url') and contains(@id, 'field-card-type-0') and contains(@id, 'edit-field-body-0')]")

    card_image_col1_xpath = (By.XPATH, "//div[contains(@id, 'col1') and contains(@id, 'field-card-type-0') and contains(@id, 'subform-field-image-wrapper') and contains(@id, 'edit-field-body-0')]/details/summary")
    card_select_image_col1_xpath = (By.XPATH, "//input[contains(@id, 'col1') and contains(@id, 'field-card-type-0') and contains(@id, 'subform-field-image-entity') and not(contains(@id, 'target')) and contains(@id, 'edit-field-body-0')]")
    card_image_col1_remove_btn_xpath = (By.XPATH, "//input[contains(@data-drupal-selector, 'col1') and contains(@data-drupal-selector, 'field-card-type-0') and contains(@id, 'edit-field-body-0') and contains(@data-drupal-selector, 'subform-field-image-current') and contains(@id, 'remove-button')]")

    card_upload_vdo_col1_xpath = (By.XPATH, "//input[contains(@id, 'col1') and contains(@id, 'field-card-type-0') and contains(@id, 'subform-field-document') and not(contains(@id, 'target')) and contains(@id, 'edit-field-body-0')]")
    card_video_col1_remove_btn_xpath = (By.XPATH, "//input[contains(@data-drupal-selector, 'col1') and contains(@data-drupal-selector, 'field-card-type-0') and contains(@data-drupal-selector, 'subform-field-document') and contains(@id, 'remove-button') and contains(@id, 'edit-field-body-0')]")

    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    cards_stripe_value = "cards"

    add_items_label_xpath = (By.XPATH,"//label[contains(@for,'subform-field-card-col1') and contains(@for,'subform-field-card-type-0') and contains(@for,'subform-field-column-portrait-type')]")
    add_items_dropdown_xpath = (By.XPATH, "//select[contains(@id,'subform-field-card-col1') and contains(@id,'subform-field-card-type-0') and contains(@id,'subform-field-column-portrait-type')]")
    drp_dwn_value = "node"
    drp_dwn_value1 = "twitter_text"
    drp_dwn_value2 = "twitter_text_img"
    

    card_tweet_tag_label_xpath = (By.XPATH,"//label[contains(@for,'subform-field-card-col1') and contains(@for,'subform-field-card-type-0') and contains(@for,'subform-field-card-tweet-tag')]")
    card_tweet_tag_input_xpath = (By.XPATH,"//input[contains(@id,'subform-field-card-col1') and contains(@id,'subform-field-card-tweet-tag') and contains(@id,'edit-field-body-0') and contains(@id,'subform-field-card-type-0')]")
    card_tweet_number_label_xpath = (By.XPATH, "//label[contains(@for,'subform-field-card-col1') and contains(@for,'subform-field-card-type-0') and contains(@for,'subform-field-card-tweet-number')]")
    crad_tweet_number_input_xpath = (By.XPATH, "//input[contains(@id,'subform-field-card-col1') and contains(@id,'subform-field-card-tweet-number') and contains(@id,'edit-field-body-0') and contains(@id,'subform-field-card-type-0')]")

    tweet_tag_text = "example@twitter.com"


    one_col_card_title = "One Columns Card Title "
    one_col_card_desc = "One Columns Card Description "
    two_col_two_three_one_three_card_title = "Two Column 2/3 and 1/3 Card Title "
    two_col_two_three_one_three_card_desc = "Two Column 2/3 and 1/3 Card Description "
    two_col_one_three_two_three_card_title = "Two Column 1/3 and 2/3 Card Title "
    two_col_one_three_two_three_card_desc = "Two Column 1/3 and 2/3 Card Description "
    two_col_one_two_card_title = "Two Column 1/2 and 1/2 Card Title "
    two_col_one_two_card_desc = "Two Column 1/2 and 1/2 Card Description "
    three_col_card_title = "Three Column Card Title "
    three_col_card_desc = "Three Column Card Description "
    second_three_col_card_title = "Second Three Column Card Title"
    second_three_col_card_desc = "Second Three Column Card Description"

    add_items_label_xpath = (By.XPATH, "//label[contains(@for,'field-card-type-0') and contains(@for, 'field-card-col1') and contains(@for, 'field-column-portrait-type') and contains(@for,'edit-field-body-0')]")
    add_items_input_xpath = (By.XPATH, "//select[contains(@id, 'field-card-type-0') and contains(@id, 'field-card-col1') and contains(@id, 'field-column-portrait-type') and contains(@id, 'edit-field-body-0')]")
    card_tweet_tag_label_xpath = (By.XPATH, "//label[contains(@for, 'field-card-type-0') and contains(@for, 'field-card-col1') and contains(@for, 'field-card-tweet-tag') and contains(@for,'edit-field-body-0')]")
    card_tweet_tag_input_xpath = (By.XPATH, "//input[contains(@id, 'field-card-type-0') and contains(@id, 'field-card-col1') and contains(@id, 'field-card-tweet-tag') and contains(@id,'edit-field-body-0')]")
    card_tweet_number_label_xpath = (By.XPATH, "//label[contains(@for, 'field-card-type-0') and contains(@for, 'field-card-col1') and contains(@for, 'field-card-tweet-number') and contains(@for,'edit-field-body-0)]")
    card_tweet_number_input_xpath = (By.XPATH, "//input[contains(@id, 'field-card-type-0') and contains(@id, 'field-card-col1') and contains(@id, 'field-card-tweet-number') and contains(@id,'edit-field-body-0')]")



    card_title1= "Stories"
    card_desc1 = "Our research redefines the way we understand disease and develop medicines. Discover the people and stories that make it possible."

    two_col_one_two_card_title_sample = "Innovative Medicines"
    two_col_one_two_card_desc_sample = "Innovative Medicines, made up of two separate commercial organizations, Innovative Medicines International and Innovative Medicines US, commercializes innovative patented medicines to enhance health outcomes."
    
    drp_dwn_value1 = "node"
    drp_dwn_value2 = "twitter_text"
    drp_dwn_value3 = "twitter_text_img"
    tweet_tag_text = "NovartisNews"


    def click_body_dropdown(self, body_dropdown_flag):

        if body_dropdown_flag == 0:
            BasePage.press_button(self, self.body_dropdown_btn_first_time_xpath)
        else:
            BasePage.press_button(self, self.body_dropdown_btn_after_first_time_xpath)

    # def card_stripe(self):

    #     BasePage.is_visible(self, self.accordion_xpath )
    #     BasePage.select_dropdown_by_value(self, self.accordion_xpath ,'cards')
    #     BasePage.press_button(self, self.add_new_paragraph_btn_xpath)

    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)


    def click_card_dropdown(self, card_dropdown_flag):

        if card_dropdown_flag == 0:
            BasePage.press_button(self, self.various_cards_dropdown_first_time_xpath)
        else:
            BasePage.press_button(self, self.various_cards_dropdown_after_first_time_xpath)

    def add_cards(self):

        BasePage.press_button(self, self.add_cards_xpath)
        if len(self.driver.find_elements(*self.three_col_card_xpath)) == 0:
            BasePage.press_button(self, self.add_cards_xpath)

    def three_col_card_add_item(self):

        three_card_add_item_list = []
        add_item_labels = self.driver.find_elements(*self.three_col_card_add_items_label_xpath)
        add_items = self.driver.find_elements(*self.three_col_card_add_item_xpath)
        for add_item, add_item_label in zip(add_items, add_item_labels):
            Select(add_item).select_by_value("node")
            three_card_add_item_list.append(add_item_label.text)

        return three_card_add_item_list

    def click_card_type(self, input_loc):

        BasePage.press_button(self, input_loc)

    def card_title(self, input_loc, label_loc, txt):

        card_title_list = []
        title_labels = self.driver.find_elements(*label_loc)
        count = 1
        card_titles = self.driver.find_elements(*input_loc)
        i=0
        for title, title_label in zip(card_titles, title_labels):
            self.driver.execute_script("arguments[0].click()", title)
            title.send_keys(f"{txt}{count}")
            card_title_list.append(title_label.text)
            count += 1
        return card_title_list


    def card_description(self, input_loc, label_loc, txt):

        card_desc_list = []
        desc_labels = self.driver.find_elements(*label_loc)
        count = 1
        card_descriptions = self.driver.find_elements(*input_loc)
        i=0
        for desc, desc_label in zip(card_descriptions, desc_labels):
            desc.send_keys(f"{txt}{count}")
            card_desc_list.append(desc_label.text)
            count += 1
        return card_desc_list

    def card_content_column(self, input_loc, label_loc):

        card_content_column_list = []
        content_column_labels = self.driver.find_elements(*label_loc)
        card_content_column = self.driver.find_elements(*input_loc)
        for content_column, content_column_label in zip(card_content_column, content_column_labels):
            content_column.send_keys("Test (1096)")
            card_content_column_list.append(content_column_label.text)

        return card_content_column_list


    def card_img(self, img_summary_loc, select_img_loc, remove_btn_loc):

        BasePage.press_button(self, img_summary_loc)
        BasePage.press_button(self, select_img_loc)
        if len(self.driver.find_elements(*self.image_iframe_xpath)) == 0:
            BasePage.press_button(self, select_img_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.image_iframe_xpath))
        images = self.driver.find_elements(*self.img_css)
        random_img_index = random.randint(0, len(images) - 1)
        for img in images:
            self.driver.execute_script("arguments[0].click()", images[random_img_index])
            break
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()

        remove_btn = BasePage.is_visible(self, remove_btn_loc)

        return remove_btn


    def card_external_url(self, input_loc, label_loc):

        card_external_url_list = []
        external_url_labels = self.driver.find_elements(*label_loc)
        card_external_url = self.driver.find_elements(*input_loc)
        for external_url, external_url_label in zip(card_external_url, external_url_labels):
            self.driver.execute_script("arguments[0].click()", external_url)
            self.driver.execute_script("arguments[0].click()", external_url)
            external_url.send_keys("https://www.google.com/")
            card_external_url_list.append(external_url_label.text)

        return card_external_url_list


    def card_videos(self, upload_vdo_loc, remove_btn_loc):

        BasePage.press_button(self, upload_vdo_loc)
        if len(self.driver.find_elements(*self.video_iframe_xpath)) == 0:
            BasePage.press_button(self, upload_vdo_loc)
        self.driver.switch_to.frame(self.driver.find_element(*self.video_iframe_xpath))
        BasePage.press_button(self, self.img_css)
        BasePage.press_button(self, self.submit_button_iframe_xpath)
        self.driver.switch_to.default_content()
        remove_btn = BasePage.is_visible(self, remove_btn_loc)

        return remove_btn

    def add_items(self,label_loc, input_loc, drp_dwn_value):
        BasePage.select_dropdown_by_value(self, input_loc, drp_dwn_value)
        add_items_label = BasePage.get_element_text(self, label_loc)
        return add_items_label

    def card_tweet_tag_ele(self,label_loc,input_loc,label_text):

        tag_label = self.get_element_text(label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc,label_text )
        return  tag_label

    def click_card_tweet_num_ele(self,num_loc):

       
        BasePage.press_button(self, num_loc)
        min_value = int(BasePage.get_elemet_attribute(self,num_loc,'min'))
        max_value = int(BasePage.get_elemet_attribute(self,num_loc,'max'))
        num = random.randint(min_value,max_value)
        self.driver.find_elements(*num_loc).clear()
        BasePage.send_keys(self, num_loc, num)
        num_result = int(BasePage.get_elemet_attribute(self,num_loc,'value'))
        return min_value, max_value


    def three_column_twitter_card_title(self, input_loc, label_loc, txt):

        card_title_list = []
        title_labels = self.driver.find_elements(*label_loc)
        count = 1
        card_titles = self.driver.find_elements(*input_loc)
    
        for title, title_label in zip(card_titles, title_labels):
            self.driver.execute_script("arguments[0].click()", title)
            title.send_keys(f"{(txt)}{count}")
            card_title_list.append(title_label.text)
            count += 1
            if count == 3:
                break
        return card_title_list

    def three_column_twitter_card_description(self, input_loc, label_loc, txt):

        card_desc_list = []
        desc_labels = self.driver.find_elements(*label_loc)
        count = 1
        card_descriptions = self.driver.find_elements(*input_loc)
        for desc, desc_label in zip(card_descriptions, desc_labels):
            desc.send_keys(f"{(txt)}{count}")
            card_desc_list.append(desc_label.text)
            count += 1
            if count == 3:
                break
        return card_desc_list

    def three_column_twitter_card_external_url(self, input_loc, label_loc):

        card_external_url_list = []
        external_url_labels = self.driver.find_elements(*label_loc)
        count = 1
        card_external_url = self.driver.find_elements(*input_loc)
        for external_url, external_url_label in zip(card_external_url, external_url_labels):
            self.driver.execute_script("arguments[0].click()", external_url)
            self.driver.execute_script("arguments[0].click()", external_url)
            external_url.send_keys("https://www.google.com/")
            card_external_url_list.append(external_url_label.text)
            count += 1
            if count == 3:
                break
        return card_external_url_list
        add_item_label = BasePage.get_element_text(self, label_loc)
        return add_item_label

    def card_tweet_tag(self, label_loc, input_loc, txt):

        BasePage.send_keys(self, input_loc, txt)
        label = BasePage.get_element_text(self, label_loc)
        return label

    # def card_tweet_tag(self, input_loc, label_loc, txt):

    #     card_tweet_tag_list = []
    #     card_tweet_tag_labels = self.driver.find_elements(*label_loc)
    #     count = 1
    #     card_tweet_tag = self.driver.find_elements(*input_loc)
    #     i=0
    #     for card_tweet_input, card_tweet_label in zip(card_tweet_tag, card_tweet_tag_labels):
    #         self.driver.execute_script("arguments[0].click()", card_tweet_input)
    #         card_tweet_input.send_keys(f"{(txt[i])}{count}")
    #         i += 1  
    #         card_tweet_tag_list.append(card_tweet_label.text)
    #         count += 1
    #     return card_tweet_tag_list

    

    




    

