import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from BaseTest import BaseTest
from Helper import Helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Utilities.config import Utilities

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.global_site
class Test_FormService(BaseTest):

    """
    Checks Pattern is available or not.
    """

    def test_ARC_2702_FormService_pattern(self):

        self.driver.get(self.env + "news/stay-up-to-date")    

        assert "patterns" in self.basePage.get_css_property(self.subscribePage.pattern_css, "background-image")

    """
    Checks Title is availble or not.
    """

    def test_ARC_2702_FormService_title(self):

        self.driver.get(self.env + "news/stay-up-to-date")
        assert "Stay Up-to-Date" in self.basePage.get_element_text(self.subscribePage.subscribe_page_title_css)

    # def test_ARC_2702_FormService_breadcrumb(self):

    #     self.driver.get(self.env + "news/stay-up-to-date")
    #     breadcrumb_items, breadcrumb_first_arrow_element, breadcrumb_second_arrow_element= self.subscribePage.breadcrumb_ele()

    #     assert "Home" in breadcrumb_items
    #     assert "News" in breadcrumb_items
    #     assert "Stay Up To Date" in breadcrumb_items

    #     assert ">" in breadcrumb_first_arrow_element
    #     assert ">" in breadcrumb_second_arrow_element

    #     assert "#656565" == self.basePage.get_css_color(self.globalPipelinePage.pipeline_last_child_breadcrumb_color_css, "color")

    def test_ARC_2702_FormService_labels(self):

        """
        Checks The Following labels and attributes are there or not -
        1. First Name
        2. Last Name
        3. Email
        4. Phone
        5. Employer
        6. Occupation
        7. Location
        8. I agree
        9. checkbox
        10. Submit
        """

        self.driver.get(self.env + "news/stay-up-to-date")

        assert self.basePage.get_element_text(self.subscribePage.first_name_label_xpath) == "First Name"
        assert self.basePage.get_element_text(self.subscribePage.last_name_label_xpath) == "Last Name"
        assert self.basePage.get_element_text(self.subscribePage.email_label_xpath) == "Email"
        assert self.basePage.get_element_text(self.subscribePage.phone_label_xpath) == "Phone"
        assert self.basePage.get_element_text(self.subscribePage.employer_label_xpath) == "Employer"
        assert self.basePage.get_element_text(self.subscribePage.occupation_label_xpath) == "Occupation"
        assert self.basePage.get_element_text(self.subscribePage.location_label_xpath) == "Location"
        assert "I agree" in self.basePage.get_element_text(self.subscribePage.agree_id)
        assert self.basePage.get_elemet_attribute(self.subscribePage.agree_checkbox_id, "type") == "checkbox"
        assert self.basePage.get_elemet_attribute(self.subscribePage.submit_btn_id, "value") == "Submit"

    def test_ARC_2702_FormService_subscribe(self):

        """
        Action :

            Click on the subscribe checkbox

            Enter below details:

                First Name(mandatory)
                Last Name (mandatory)
                Email (mandatory)
                Click on I agree checkbox
                Click on the submit button.

        Expected Result : 

            Unsubscribe Checkbox should be disable
            Publication Order Form Checkbox should be enable
            Language field should be display and Default 'English' should be selected.

            Users should be registered successfully
            A successful registration message should display.

        """

        self.driver.get(self.env + "news/stay-up-to-date")    

        self.subscribePage.click_subscribe()
        assert "true" == self.basePage.get_elemet_attribute(self.subscribePage.edit_unsubscribe_id, "disabled")
        assert None == self.basePage.get_elemet_attribute(self.subscribePage.publication_order_form_id, "disabled")
        assert self.basePage.get_element_text(self.subscribePage.lang_label_css) == "Language"
       
        lang_checkboxes = self.driver.find_elements(self.subscribePage.lang_checkbox_css[0], self.subscribePage.lang_checkbox_css[1])
        for lang_checkbox in lang_checkboxes:

            if "English" in lang_checkbox.find_element(self.subscribePage.label_tag_css[0], self.subscribePage.label_tag_css[1]).text:
                is_checked = lang_checkbox.find_element(self.subscribePage.input_tag_css[0], self.subscribePage.input_tag_css[1]).get_attribute("checked")
                break
        assert is_checked == "true"


        self.subscribePage.fill_mandatory_fields()
        self.subscribePage.agree_checkbox_ele()
        self.subscribePage.click_submit_btn()

        alert_txt = self.subscribePage.alert_danger()
        assert self.subscribePage.captcha_warning_txt in alert_txt

    def test_ARC_2702_FormService_subscribe_fill_all_the_fields(self):

        """
        Action:

            Enter below details:

            First Name(mandatory) - Last Name (mandatory)
            Email (mandatory)
            Phone(optional)
            Employer(optional)
            Occupation(optional)
            Location(optional)
            Click on I agree checkbox
            Click on the submit button.

        Expected Result:

            Users should be registered successfully.
            A successful registration message should display

        """

        self.driver.get(self.env + "news/stay-up-to-date")    

        # self.basePage.press_button(self.subscribePage.stay_up_to_date_css)

        self.subscribePage.click_subscribe()
        self.subscribePage.fill_mandatory_fields()
        self.subscribePage.fill_optional_fields()
        self.subscribePage.agree_checkbox_ele()
        self.subscribePage.click_submit_btn()

        alert_txt = self.subscribePage.alert_danger()
        assert self.subscribePage.captcha_warning_txt in alert_txt

    def test_ARC_2702_FormService_unsubscribe(self):

        """
        Action:

            Click on the Unsubscribe checkbox

            Enter Email details(mandatory)

            Click on I agree checkbox
            Click on the submit button.

        Expected result:

            Verify below should display:

            Email, I agree checkbox, submit button when clicked on Unsubscribe checkbox.
            Should be disable:
            Subscribe Check box should be disable
            Publication Order should be disable

            Users 'Unsubscribed successfully' Message should be display.

        """

        self.driver.get(self.env + "news/stay-up-to-date")

        # self.basePage.press_button(self.subscribePage.stay_up_to_date_css)
        self.subscribePage.click_unsubscribe()
        assert "true" == self.basePage.get_elemet_attribute(self.subscribePage.edit_subscribe_id, "disabled")
        assert "true" == self.basePage.get_elemet_attribute(self.subscribePage.publication_order_form_id, "disabled")
        
        assert self.basePage.get_element_text(self.subscribePage.email_label_xpath) == "Email"
        assert "I agree" in self.basePage.get_element_text(self.subscribePage.agree_id)

        self.subscribePage.fill_mandatory_fields_unsubscribe()
        self.subscribePage.agree_checkbox_ele()
        self.subscribePage.click_submit_btn()
        alert_txt = self.subscribePage.alert_danger()
        assert self.subscribePage.captcha_warning_txt in alert_txt

    def test_ARC_2702_FormService_publication_order(self):

        """
        Action:

            Click on Publication Order Form checkbox

            Enter below details:

            First Name(mandatory)
            Last Name (mandatory)
            Email (mandatory)
            Click on I agree checkbox
            Click on the submit button.

            Select Publication(mandatory)
            Quantity(mandatory)
            Street Address(mandatory)
            City/Town (mandatory)
            ZIP/Postal Code(mandatory)
            Country(mandatory)
            Click on I agree checkbox

            Click all the checkboxes and the Location dropdown

            Checkboxes should be clickable properly as per selection.
            Dropdown should be display properly.

        Expected Result:

            verify Below should be present:

            Select publication dropdown, Quantity dropdown
            Remove button,,Add another publications button, submit button
            Street Address, City/Town, ZIP/Postal Code, Country

            Users 'Ordered successfully' the Message should be display.
        """

        self.driver.get(self.env + "news/stay-up-to-date")    

        # self.basePage.press_button(self.subscribePage.stay_up_to_date_css)

        self.subscribePage.click_publication_order_form()
        assert "Select Publication" == self.basePage.get_element_text(self.subscribePage.publication_label_css)
        assert "Quantity" == self.basePage.get_element_text(self.subscribePage.quantity_label_css)
        assert "Remove" in self.basePage.get_elemet_attribute(self.subscribePage.remove_btn_xpath, "title")
        assert "Add another Publication" == self.basePage.get_elemet_attribute(self.subscribePage.add_publication_btn, "value")
        assert "Street Address" in self.basePage.get_element_text(self.subscribePage.street_address_xpath)
        assert "City/Town" in self.basePage.get_element_text(self.subscribePage.city_town_xpath)
        assert "ZIP/Postal Code" in self.basePage.get_element_text(self.subscribePage.zip_xpath)
        assert "Country" in self.basePage.get_element_text(self.subscribePage.country_xpath)

        self.subscribePage.fill_mandatory_fields()
        self.subscribePage.publication_mandatory_fields()
        self.subscribePage.agree_checkbox_ele()
        self.subscribePage.click_submit_btn()
        alert_txt = self.subscribePage.alert_danger()
        assert self.subscribePage.captcha_warning_txt in alert_txt

        self.basePage.press_button(self.subscribePage.stay_up_to_date_css)

        self.basePage.element_clickable(self.subscribePage.edit_subscribe_id)
        self.basePage.element_clickable(self.subscribePage.edit_unsubscribe_id)
        self.basePage.element_clickable(self.subscribePage.publication_order_form_id)
        assert self.driver.find_element(self.subscribePage.location_id[0], self.subscribePage.location_id[1]).tag_name == "select"