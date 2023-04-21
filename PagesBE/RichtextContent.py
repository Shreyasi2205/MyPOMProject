import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException
from datetime import datetime
from Utilities.config import Utilities
import random
from datetime import date
from datetime import datetime, timedelta
import platform


class RichtextContent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)



    
    frame_xpath = (By.XPATH,"(//iframe[contains(@title,'Rich Text Editor, Content field')])[1]")
    # source_icon_xpath = (By.XPATH,"(//a[contains(@class,'cke_button__source')]/span)[7]")
    source_icon_xpath = (By.XPATH,"//div[contains(@id,'cke_edit-field-body-1-subform-field-content-0-value-')]/div/span[contains(@id,'top')]/span/span/span/a[contains(@class,'cke_button__source')]/span")
    bold_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__bold_icon")
    italic_icon_css = (By.CSS_SELECTOR,".ajax-new-content >div  span.cke_button__italic_icon")
    strike_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__strike_icon")
    superscript_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__superscript_icon")
    subscript_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__superscript_icon")
    removeformat_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__removeformat_icon")
    link_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__drupallink_icon")
    unlink_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__drupalunlink_icon")
    video_embed_icon_css = (By.CSS_SELECTOR,".ajax-new-content >div  span.cke_button__video_embed_icon")
    tweetable_icon_css = (By.CSS_SELECTOR,".ajax-new-content >div  span.cke_button__tweetabletext_icon")
    media_library_icon_css = (By.CSS_SELECTOR,".ajax-new-content >div  span.cke_button__drupalmedialibrary_icon")
    responsive_area_css = (By.CSS_SELECTOR,".ajax-new-content > div a.cke_button__addresponsivearea")
    show_blocks_css = (By.CSS_SELECTOR,'.ajax-new-content > div span.cke_button__showblocks_icon')
    source_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__source_icon")
    text_css = (By.CSS_SELECTOR,'body p')
    media_browser_css = (By.CSS_SELECTOR,".ajax-new-content >div  span.cke_button__media_browser_icon")
    media_browser_dialog_box_css = (By.CSS_SELECTOR,".ui-dialog")
    media_browser_name_css = (By.CSS_SELECTOR,"input[name='entity_id']")
    media_browser_next_button = (By.CSS_SELECTOR,"button.js-button-next")
    suggestions_css = (By.CSS_SELECTOR,".ui-dialog-content ul>li")
    after_text_pass_css = (By.CSS_SELECTOR,"body p strong")
    align_text_xpath = (By.XPATH,"//p[contains(@class,'text-align')]")
    media_browser_display_as_dropdown_xpath = (By.XPATH,"//select[contains(@id,'embed-display')]")
    media_browser_display_as_xpath= (By.XPATH,"//select[contains(@id,'embed-display')]//preceding-sibling::label")
    media_browser_second_dialog_box_css = (By.CSS_SELECTOR,".ui-dialog")
    media_browser_name_data= "pdf"
    media_browser_align_label_xpath = (By.XPATH,"//div[contains(@id,'embed-display')]//following-sibling::fieldset/legend/span")
    media_browser_align_none_xpath = (By.XPATH,"(//input[contains(@id,'edit-attributes-data-align')])[1]")
    media_browser_embed_button_css = (By.CSS_SELECTOR,".ui-dialog-buttonpane div button.button--primary")
    video_embed_dialog_box_css = (By.CSS_SELECTOR,"div.video-embed-dialog")
    video_embed_url_data = "https://youtu.be/aBdb-Cc5gro"
    video_embed_url_xpath = (By.XPATH,"//input[contains(@id,'edit-video-url')]")
    video_embed_url_label_xpath = (By.XPATH,"//input[contains(@id,'edit-video-url')]//preceding-sibling::label")
    video_embed_responsive_radiobutton_xpath = (By.XPATH,"//input[contains(@id,'edit-responsive')]")
    video_embed_save_button_xpath = (By.XPATH,"//button[contains(@class,'form-submit')]")
    tweetable_text_display_text_label_xpath = (By.XPATH,"//label[text()='Display Text']")
    tweetable_text_display_text_xpath = (By.XPATH,"//label[text()='Display Text']//parent::div//following-sibling::div/div/input")
    tweetable_text_xpath = (By.XPATH,"//label[text()='Tweetable Text']//parent::div//following-sibling::div/div/input")
    tweetable_text_label_xpath = (By.XPATH,"//label[text()='Tweetable Text']")
    tweetable_hastag_xpath = (By.XPATH,"//label[text()='Tweetable Text Hash tags (#sample #news)']//parent::div//following-sibling::div/div/input")
    tweetable_hastag_label_xpath = (By.XPATH,"//label[text()='Tweetable Text Hash tags (#sample #news)']")
    tweetable_dialog_box_css = (By.CSS_SELECTOR,'[class="cke_dialog_body"]')
    tweetable_display_text_data ="twitter"
    tweetable_text_data ="Twitter"
    tweetable_ok_button_css = (By.CSS_SELECTOR,"td > .cke_dialog_ui_button_ok")
    media_library_dialog_css = (By.CSS_SELECTOR,".media-library-widget-modal")
    media_library_image_css = (By.CSS_SELECTOR,'a[data-title="Image"]')
    media_library_document_css = (By.CSS_SELECTOR,'a[data-title="Document"]')
    media_library_tweet_css = (By.CSS_SELECTOR,'a[data-title="Tweet"]')
    media_library_video_css = (By.CSS_SELECTOR,'a[data-title="Video"]')
    media_library_image_input_xpath = (By.XPATH,'//input[@name="media_library_select_form[1]"]')
    media_library_image_button_xpath = (By.XPATH,"//button[contains(@class,'media-library-select')]")
    media_library_edit_media_icon_css = (By.CSS_SELECTOR,".media-library-item__edit")
    media_library_edit_media_dialog_css = (By.CSS_SELECTOR,".ui-dialog")
    media_library_edit_media_align_none_xpath = (By.XPATH,"//input[contains(@id,'edit-attributes-data-align-none')]")
    media_library_edit_media_caption_xpath = (By.XPATH,"//input[contains(@id,'edit-hascaption')]")
    media_library_display_as_dropdown_xpath = (By.XPATH,"//select[contains(@id,'edit-attributes-data-view-mode')]")
    media_library_display_as_xpath= (By.XPATH,"//select[contains(@id,'edit-attributes-data-view-mode')]//preceding-sibling::label")
    media_library_edit_media_save_btn_css = (By.CSS_SELECTOR,".ui-dialog button.js-form-submit")
    media_library_edit_media_caption_text_css = (By.CSS_SELECTOR,"figcaption.cke_widget_editable")
    left_alignment_icon_css = (By.CSS_SELECTOR,".ajax-new-content > div span.cke_button__justifyleft_icon")
    centre_alignment_icon_css = (By.CSS_SELECTOR,'.ajax-new-content > div span.cke_button__justifycenter_icon')
    right_alignment_icon_css = (By.CSS_SELECTOR,'.ajax-new-content > div span.cke_button__justifyright_icon')
    justify_alignment_icon_css = (By.CSS_SELECTOR,'.ajax-new-content > div span.cke_button__justifyblock_icon')
    responsive_area_dialog_box_css = (By.CSS_SELECTOR,'[role="presentation"] >.cke_dialog_body')
    responsive_area_dialog_box_close_btn_xpath = (By.XPATH,"//a[contains(@id,'cke_dialog_close_button')]")
    show_blocks_temp_css = (By.CSS_SELECTOR,"body.cke_show_blocks")
    source_html_format_xpath = (By.XPATH,"//*[contains(@class,'cke_source')]")
    add_new_paragraph_btn_xpath = (By.XPATH,'//input[@value="Add new Paragraph"]')
    accordion_xpath  = (By.XPATH,'//select[@name="field_body[actions][bundle]"]')


    textarea_xpath = (By.XPATH,'//textarea[@title="Rich Text Editor, Content field"]')
    body_dropdown_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    rich_text_content_stripe_value = "rich_text_content"

    """
    Data related to Investors
    """

    stock_ticker_txt = '[<div class="stock-ticker">Stocks</div>]'

    def click_paragraph_dropdown(self,input_loc,paragraph_dropdown_value):
        BasePage.select_dropdown_by_value(self, input_loc, paragraph_dropdown_value)

    def add_paragraph(self,btn_loc):

        BasePage.press_button(self, btn_loc)

    def richtext_content_stripe(self):

        BasePage.is_visible(self, self.accordion_xpath )
        BasePage.select_dropdown_by_value(self, self.accordion_xpath ,'rich_text_content')
        BasePage.press_button(self, self.add_new_paragraph_btn_xpath)


    def media_browser_icon(self):

        display_status_media_browser  = False
        display_as_dropdown_status = False 
        display_label_status = False 
        align_label_status = False 
        align_none_status = False
        display_status_media_browser =  BasePage.is_displayed(self,self.media_browser_css) 
        BasePage.press_button(self, self.media_browser_css)
        BasePage.is_visible(self,self.media_browser_dialog_box_css)
        if len(self.driver.find_elements(*self.media_browser_dialog_box_css)) > 0 :

            BasePage.press_button(self, self.media_browser_name_css)
            BasePage.send_keys(self, self.media_browser_name_css, self.media_browser_name_data)
            if len(BasePage.get_element_text(self,self.media_browser_name_css)) == 0 :
                BasePage.press_button(self, self.media_browser_name_css)
                BasePage.send_keys(self, self.media_browser_name_css, self.media_browser_name_data)
            auto_suggestions = self.driver.find_elements(*self.suggestions_css)
            for sugg in auto_suggestions:
                try:
                     WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(sugg)).click()
                except:
                    self.driver.execute_script("arguments[0].click()", sugg)
            BasePage.press_button(self, self.media_browser_next_button)
            BasePage.is_visible(self,self.media_browser_second_dialog_box_css)
            if len(self.driver.find_elements(*self.media_browser_second_dialog_box_css)) > 0 :

                display_as_dropdown_status = BasePage.is_displayed(self,self.media_browser_display_as_dropdown_xpath)
                display_label_status = BasePage.is_displayed(self,self.media_browser_display_as_xpath)
                align_label_status = BasePage.is_displayed(self,self.media_browser_align_label_xpath)
                align_none_status = BasePage.is_selected(self,self.media_browser_align_none_xpath)
                BasePage.press_button(self, self.media_browser_embed_button_css)
                

        

        return display_status_media_browser, display_as_dropdown_status , display_label_status, align_label_status, align_none_status


    def bold_icon(self,frame):

        display_status_bold = False
        display_status_bold =  BasePage.is_displayed(self,self.bold_icon_css) 
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        BasePage.press_button(self, self.text_css)
        BasePage.send_keys(self,self.text_css,Utilities.RichtextContent_data)
        self.driver.switch_to.default_content()
        BasePage.press_button(self, self.text_css)
        if 'Windows' in platform.system():
            a = ActionChains(self.driver)
            a.key_down(Keys.CONTROL).send_keys('a').perform()
        elif 'Darwin' in platform.system():
            a = ActionChains(self.driver)
            a.key_down(Keys.COMMAND).send_keys('a').perform()
        BasePage.press_button(self, self.bold_icon_css)
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        font_weight = BasePage.get_css_property(self,self.after_text_pass_css,'font-weight')
        self.driver.switch_to.default_content()



        return display_status_bold, font_weight


    def italic_icon(self,frame):

        display_status_italic= False
        display_status_italic=  BasePage.is_displayed(self,self.italic_icon_css) 
        BasePage.press_button(self, self.text_css)
        a = ActionChains(self.driver)
        if 'Windows' in platform.system():
            a.key_down(Keys.CONTROL).send_keys('a').perform()
        elif 'Darwin' in platform.system():
            a.key_down(Keys.COMMAND).send_keys('a').perform()
        BasePage.press_button(self, self.italic_icon_css)
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        font_style = BasePage.get_css_property(self,self.after_text_pass_css,'font-style')
        BasePage.press_button(self, self.text_css)
        self.driver.switch_to.default_content()
        

        return display_status_italic, font_style


    def video_embed(self,frame):

        responsive_status = False
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        BasePage.press_button(self, self.text_css)
        a = ActionChains(self.driver)
        if 'Windows' in platform.system():
            self.driver.find_element(By.CSS_SELECTOR,'body p').send_keys(Keys.ENTER)
        elif 'Darwin' in platform.system():
            self.driver.find_element(By.CSS_SELECTOR,'body p').send_keys(Keys.RETURN)
        self.driver.switch_to.default_content()
        BasePage.press_button(self, self.video_embed_icon_css)
        BasePage.is_visible(self,self.video_embed_dialog_box_css)
        if len(self.driver.find_elements(*self.video_embed_dialog_box_css)) > 0 :

            BasePage.press_button(self, self.video_embed_url_xpath)
            BasePage.send_keys(self,self.video_embed_url_xpath,self.video_embed_url_data)
            url_label = BasePage.get_element_text(self,self.video_embed_url_label_xpath)
            responsive_status = BasePage.is_selected(self,self.video_embed_responsive_radiobutton_xpath)
            BasePage.press_button(self, self.video_embed_save_button_xpath)
            

        return url_label, responsive_status


    def tweetable_icon(self):

        display_text_label_status = False
        tweetable_text_label_status = False
        tweetable_hastag_label_status = False
        BasePage.press_button(self, self.tweetable_icon_css)
        BasePage.is_visible(self,self.tweetable_dialog_box_css)
        if len(self.driver.find_elements(*self.tweetable_dialog_box_css)) > 0 :

            display_text_label_status = BasePage.is_displayed(self,self.tweetable_text_display_text_label_xpath)
            BasePage.send_keys(self,self.tweetable_text_display_text_xpath,self.tweetable_display_text_data)
            tweetable_text_label_status = BasePage.is_displayed(self,self.tweetable_text_label_xpath)
            BasePage.send_keys(self,self.tweetable_text_xpath,self.tweetable_text_data)
            tweetable_hastag_label_status = BasePage.is_displayed(self,self.tweetable_hastag_label_xpath)
            BasePage.send_keys(self,self.tweetable_text_xpath,self.tweetable_hastag_xpath)
            BasePage.press_button(self, self.tweetable_ok_button_css)



        return display_text_label_status, tweetable_text_label_status, tweetable_hastag_label_status


    def media_libarary_icon(self,frame):

         self.driver.switch_to.frame(self.driver.find_element(*frame))
         BasePage.press_button(self, self.text_css)
         a = ActionChains(self.driver)
         if 'Windows' in platform.system():
            self.driver.find_element(By.CSS_SELECTOR,'body p').send_keys(Keys.ENTER)
         elif 'Darwin' in platform.system():
            self.driver.find_element(By.CSS_SELECTOR,'body p').send_keys(Keys.RETURN)
         self.driver.switch_to.default_content()
         BasePage.press_button(self, self.media_library_icon_css)
         BasePage.is_visible(self,self.media_library_dialog_css)
         if len(self.driver.find_elements(*self.media_library_dialog_css)) > 0 :
            image_text = BasePage.get_element_text(self,self.media_library_image_css)
            document_text = BasePage.get_element_text(self,self.media_library_document_css)
            tweet_text = BasePage.get_element_text(self,self.media_library_tweet_css)
            video_text = BasePage.get_element_text(self,self.media_library_video_css)
            BasePage.press_button(self, self.media_library_image_input_xpath)
            BasePage.press_button(self, self.media_library_image_button_xpath)
            if len(self.driver.find_elements(*self.media_library_dialog_css)) > 0 :
                BasePage.press_button(self, self.media_library_image_button_xpath)

         return image_text, document_text , tweet_text , video_text


        


    def edit_media_icon(self,frame):

        edit_media_status = False
        align_icon_status = False
        display_as_dropdown_status = False
        display_label_status = False

        self.driver.switch_to.frame(self.driver.find_element(*frame))
        BasePage.is_visible(self,self.media_library_edit_media_icon_css)
        if len(self.driver.find_elements(*self.media_library_edit_media_icon_css)) > 0 :
            edit_media_status = BasePage.is_displayed(self,self.media_library_edit_media_icon_css)  
            BasePage.press_button(self, self.media_library_edit_media_icon_css) 
            self.driver.switch_to.default_content()
            BasePage.is_visible(self,self.media_library_edit_media_dialog_css)
            if len(self.driver.find_elements(*self.media_library_edit_media_dialog_css)) > 0 :

                align_icon_status = BasePage.is_selected(self,self.media_library_edit_media_align_none_xpath)
                BasePage.press_button(self, self.media_library_edit_media_caption_xpath) 
                display_as_dropdown_status = BasePage.is_displayed(self,self.media_library_display_as_dropdown_xpath)
                display_label_status = BasePage.is_displayed(self,self.media_library_display_as_xpath)
                BasePage.press_button(self, self.media_library_edit_media_save_btn_css) 
                self.driver.switch_to.frame(self.driver.find_element(*frame))
                caption_text = BasePage.get_elemet_attribute(self,self.media_library_edit_media_caption_text_css, 'data-placeholder')
                self.driver.switch_to.default_content()

        return edit_media_status , align_icon_status , display_as_dropdown_status , display_label_status , caption_text



    def alignment_icon(self,frame):

        self.driver.switch_to.frame(self.driver.find_element(*frame))
        BasePage.press_button(self, self.text_css)
        BasePage.send_keys(self,self.text_css,Utilities.RichtextContent_data)
        self.driver.switch_to.default_content()
        BasePage.press_button(self, self.text_css)
        if 'Windows' in platform.system():
            a = ActionChains(self.driver)
            a.key_down(Keys.CONTROL).send_keys('a').perform()
        elif 'Darwin' in platform.system():
            a = ActionChains(self.driver)
            a.key_down(Keys.COMMAND).send_keys('a').perform()
        BasePage.press_button(self, self.centre_alignment_icon_css)
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        center_alignment = BasePage.get_css_property(self,self.align_text_xpath,'text-align')
        self.driver.switch_to.default_content()
        BasePage.press_button(self, self.right_alignment_icon_css)
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        right_alignment = BasePage.get_css_property(self,self.align_text_xpath,'text-align')
        self.driver.switch_to.default_content()
        BasePage.press_button(self, self.justify_alignment_icon_css)
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        justify_alignment = BasePage.get_css_property(self,self.align_text_xpath,'text-align')
        self.driver.switch_to.default_content()


        return center_alignment , right_alignment , justify_alignment
        

    def responsive_area_icon(self):

        dialog_box_status = False
        BasePage.press_button(self, self.responsive_area_css)
        BasePage.is_visible(self,self.responsive_area_dialog_box_css)
        dialog_box_status = BasePage.is_displayed(self,self.responsive_area_dialog_box_css)
        BasePage.press_button(self,self.responsive_area_dialog_box_close_btn_xpath)


        return dialog_box_status


    def show_blocks_icon(self,frame):

        show_blocks_status = False
        BasePage.press_button(self, self.show_blocks_css)
        self.driver.switch_to.frame(self.driver.find_element(*frame))
        show_blocks_status = BasePage.is_displayed(self,self.show_blocks_temp_css)
        self.driver.switch_to.default_content()

        return show_blocks_status



    def source_icon(self):

        
        BasePage.press_button(self,self.source_icon_css)
        BasePage.is_visible(self,self.source_html_format_xpath)
        source_html = len(self.driver.find_elements(*self.source_html_format_xpath))
        
        return source_html


    def stock_ticker(self,data):

        # time.sleep(2)
        BasePage.press_button(self, self.source_icon_xpath)
        BasePage.send_keys(self,self.textarea_xpath,data)
       
        















