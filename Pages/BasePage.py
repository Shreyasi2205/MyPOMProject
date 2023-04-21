from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, TimeoutException

"""This class is the parent of all classes"""
"""It contains all the generic methods and utilities for all pages"""


class BasePage:

    hyperlinks = (By.TAG_NAME, 'a')

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()
        except:
            self.driver.execute_script("arguments[0].click()", self.driver.find_element(by_locator[0], by_locator[1]))

    def click_button(self, by_locator):
        try:
            self.driver.find_element(by_locator[0], by_locator[1]).click()
        except:
            self.driver.execute_script("arguments[0].click()", self.driver.find_element(by_locator[0], by_locator[1]))

    def press_button(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator)).click()
        except:
            self.driver.execute_script("arguments[0].click()", self.driver.find_element(by_locator[0], by_locator[1]))

    def get_tag_name(self, by_locator):
        
        element = self.driver.find_element(by_locator[0], by_locator[1])
        return element.tag_name
        
    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator)).send_keys(text)

    def select_dropdown_by_value(self, by_locator, value):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator))
        sel = Select(self.driver.find_element(*by_locator))
        sel.select_by_value(value)


    def select_dropdown_by_index(self, by_locator, index):
        Select(self.driver.find_element(*by_locator)).select_by_index(index)

    def select_dropdown_by_visible_text(self, by_locator, text):
        Select(self.driver.find_element(*by_locator)).select_by_visible_text(text)

    def move_to_element(self, by_locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(by_locator[0], by_locator[1])).perform()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def get_elemet_attribute(self, by_locator, attribute):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute)

    def get_css_property(self, by_locator, css_property):
        
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.value_of_css_property(css_property)
    
    def get_css_property_without_ec(self, by_locator, css_property):
        
        element = self.driver.find_element(*by_locator)
        return element.value_of_css_property(css_property)

    def verify_css_property(self, by_locator, text, css_property):
        
        assert text in self.driver.find_element(by_locator[0], by_locator[1]).value_of_css_property(css_property)

    def reuse(self, name=[], prop=[]):
        count = 0
        for i in zip(name, prop):
            assert i[0] in self.get_element_text(i[1])

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator))
        return bool(element)

    def is_not_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until_not(ec.presence_of_element_located(by_locator))
        return bool(element)

    def element_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator))
        return bool(element)

    def rgb_to_hex(self, rgb):

        return '#%02x%02x%02x' % rgb

    def get_elements(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        return elements

    def get_css_color(self,by_locator,css_property):
        value_of_css = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator)).value_of_css_property(css_property)
        hex_code = Color.from_string(value_of_css).hex
        return hex_code

    def is_displayed(self, locator):
         element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
         return element.is_displayed()

    def is_selected(self, locator):
         element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
         return element.is_selected()

    def is_displayed_ele(self, element):
         return element.is_displayed()

    def is_visible(self,locator):
        
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        return bool(element)
