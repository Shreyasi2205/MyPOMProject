import time
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

class AddMapElement(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    paragraph_dropdown_btn_first_time_xpath = (By.XPATH, "//select[contains(@id, 'edit-field-body-add-more-add-more-select')]")
    add_paragraph_btn_xpath = (By.XPATH, "//input[contains(@id, 'edit-field-body-add-more-add-more-button')]")
    map_name_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-map-0-name') and contains (@for, 'edit-field-body-0')]")
    map_name_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-map-0-name') and contains (@id, 'edit-field-body-0')]")
    latitude_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-map-0-lat') and contains (@for, 'edit-field-body-0')]")
    latitude_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-map-0-lat') and contains (@id, 'edit-field-body-0')]")
    longitude_label_xpath = (By.XPATH, "//label[contains(@for, 'subform-field-map-0-lon') and contains (@for, 'edit-field-body-0')]")
    longitude_input_xpath = (By.XPATH, "//input[contains(@id, 'subform-field-map-0-lon') and contains (@id, 'edit-field-body-0')]")
    set_map_btn_xpath = (By.XPATH, "//input[contains(@id, 'map_setter_field_map-0-1')]")
    google_map_field_xpath = (By.XPATH, "//div[contains (@id, 'google_map_field_dialog')]")
    map_zoom_label_xpath = (By.XPATH, "//label[contains (@for, 'edit-zoom')]")
    map_zoom_input_xpath = (By.XPATH, "//select[contains (@id, 'edit-zoom')]")
    map_type_label_xpath = (By.XPATH, "//label[contains (@for, 'edit-type')]")
    map_type_input_xpath = (By.XPATH, "//select[contains (@id, 'edit-type')]")
    map_width_label_xpath = (By.XPATH, "//label[contains (@for, 'edit-width')]")
    map_width_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-width') and contains (@value, '100%')]")
    map_height_label_xpath = (By.XPATH, "//label[contains (@for, 'edit-height')]")
    map_height_input_xpath = (By.XPATH, "//input[contains(@id, 'edit-height') and contains (@value, '450px')]")
    enable_controls_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-controls')]")
    enable_controls_checkbox_xpath = (By.XPATH, "//input[contains(@id, 'edit-controls')]")
    traffic_layer_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-traffic')]")
    traffic_layer_checkbox_xpath = (By.XPATH, "//input[contains(@id, 'edit-traffic')]")
    enable_marker_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-marker')]")
    enable_marker_checkbox_xpath = (By.XPATH, "//input[contains(@id, 'edit-marker')]")
    custom_marker_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-marker-icon')]")
    custom_marker_helper_text_xpath = (By.XPATH, "//p[contains(@class, 'marker-text')]")
    address_label_name_xpath = (By.XPATH, "//label[text()='Enter an address/town/postcode, etc., to center the map on:']")
    enter_address_input_xpath = (By.XPATH, "//input[contains(@id, 'centre_map_on')]")
    find_button_xpath = (By.XPATH, "//button[contains(@class, 'ui-button-text-only button')]")
    result_found_text_xpath = (By.XPATH, "//div[contains(@id, 'centre_map_results')]")
    infowindow_label_xpath = (By.XPATH, "//label[contains(@for, 'edit-infowindow')]")
    infowindow_input_xpath = (By.XPATH, "//textarea[contains(@id, 'edit-infowindow')]")
    insert_map_btn_xpath = (By.XPATH, "//button[contains(.,'Insert map')]")
    cancel_btn_xpath = (By.XPATH, "//button[contains(.,'Cancel')]")
    paragraph_drp_dwn_value = 'map_element'
    # map_zoom_value = "2"
    # map_type_value = "roadmap"
    map_name = "India"
    default_lat_value = "45"
    default_lon_value = "0.01"
    address = "530043"
    info_window_text = "Pointer"
    checkbox_selected = "disabled"
   





    
    def click_paragraph_dropdown(self,input_loc,value):
        BasePage.select_dropdown_by_value(self, input_loc, value)


    def add_paragraph_btn(self,btn_loc):
        BasePage.press_button(self, btn_loc)

    def map_name_ele(self,label_loc, input_loc, map_name):

        heading_title = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self,input_loc)
        BasePage.send_keys(self, input_loc, map_name)
        return heading_title

    def latitude_and_longitude(self,lat_label_loc, lon_label_loc, lat_value_loc, lon_value_loc):

        lat_heading_title = BasePage.get_element_text(self,lat_label_loc)
        lon_heading_title = BasePage.get_element_text(self,lon_label_loc)
        default_lat_value = BasePage.get_elemet_attribute(self, lat_value_loc, 'value')
        default_lon_value = BasePage.get_elemet_attribute(self, lon_value_loc, 'value')
        return lat_heading_title,lon_heading_title, default_lat_value, default_lon_value


    def set_map_ele(self, btn_loc):
        BasePage.press_button(self,btn_loc )

    def map_zoom_or_map_type_ele(self,label_loc, input_loc):

        heading_title = BasePage.get_element_text(self,label_loc)
        map_zoom_type_len = len(self.driver.find_elements(*input_loc))
        return heading_title, map_zoom_type_len


    def map_width_or_height_ele(self, label_loc, input_text):
        heading_title = BasePage.get_element_text(self,label_loc)
        input = BasePage.get_elemet_attribute(self, input_text,'value')
        return heading_title, input


    def enable_controls_or_traffic_layer_or_enable_marker(self, label_loc,input_loc, value ):
        heading_title = BasePage.get_element_text(self,label_loc)
        check_box = BasePage.get_elemet_attribute(self,input_loc,value)
        print(check_box)
        checkbox_selected = BasePage.is_selected(self, input_loc)
        return heading_title, check_box, checkbox_selected

    def cutom_marker_ele(self, label_loc, helper_text):
        label = BasePage.get_element_text(self,label_loc)
        custom_marker_helper_text = BasePage.get_element_text(self,helper_text)
        return label, custom_marker_helper_text

    def enter_address_ele(self, label_loc, input_loc , address, find_btn, result_loc):
        label = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self, input_loc )
        BasePage.send_keys(self, input_loc,  address )
        BasePage.press_button(self, find_btn )
        result_text = BasePage.get_element_text(self,result_loc)
        return label,result_text

    def infowindow_ele(self, label_loc,input_loc, info_window_text):
        label = BasePage.get_element_text(self,label_loc)
        BasePage.press_button(self, input_loc)
        BasePage.send_keys(self, input_loc , info_window_text)
        return label

    def cancel_ele(self, btn_loc):
        BasePage.press_button(self,btn_loc )
        return len(self.driver.find_elements(*self.google_map_field_xpath))
        

        
    def insert_map(self, btn_loc, new_lat_value_loc, new_lon_value_loc):
        BasePage.press_button(self, btn_loc)
        updated_lat_value = BasePage.get_elemet_attribute(self, new_lat_value_loc, 'value')
        updated_lon_value = BasePage.get_elemet_attribute(self, new_lon_value_loc, 'value')
        return updated_lat_value , updated_lon_value




    
        

    




    

    


    

    
    

    


    

    

    


    



    

    


