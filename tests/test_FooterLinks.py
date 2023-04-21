import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from BaseTest import BaseTest
from Helper import Helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException, ElementNotSelectableException
import random
from Utilities.config import Utilities
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.alert import Alert


now = datetime.now() 



# If any more library is needed import it here.

# Holds down the alt key

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.migration
@pytest.mark.singapore
@pytest.mark.pakistan
@pytest.mark.usa
@pytest.mark.it
@pytest.mark.uk
@pytest.mark.sandoz
@pytest.mark.de
@pytest.mark.lv
@pytest.mark.at
@pytest.mark.malaysia
@pytest.mark.ph
@pytest.mark.fi
@pytest.mark.jp
@pytest.mark.global_site
@pytest.mark.ch
@pytest.mark.ch_fr
@pytest.mark.fr
@pytest.mark.za
@pytest.mark.th
@pytest.mark.es
@pytest.mark.nl
@pytest.mark.pt
@pytest.mark.tw
@pytest.mark.kr
@pytest.mark.ar
# @pytest.mark.campus
@pytest.mark.hk
@pytest.mark.br
@pytest.mark.cn
@pytest.mark.scn
@pytest.mark.hu
@pytest.mark.biome
@pytest.mark.foundation
@pytest.mark.ie
@pytest.mark.ca
@pytest.mark.se
@pytest.mark.tr
@pytest.mark.ru
@pytest.mark.ro
@pytest.mark.il
@pytest.mark.ee
@pytest.mark.co
@pytest.mark.bg
@pytest.mark.ve
@pytest.mark.id
@pytest.mark.bd
@pytest.mark.pl
@pytest.mark.lt
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.be
@pytest.mark.au
@pytest.mark.eg
@pytest.mark.cz
@pytest.mark.rs
@pytest.mark.gr
@pytest.mark.dk
@pytest.mark.no
class TestFooterLinks(BaseTest):

    
    def test_ARC_2499_FooterLinks_title(self):

        """
        Checks Title is there or not in Footer Section.
        For BIOME and FOUNDATION site, it checks the particulars titles are displaying or not.
        """

        self.driver.get(self.env)
        assert self.basePage.is_displayed(self.homePage.footer_title_css) == True
        if self.env_name == "biome":
            self.basePage.get_element_text(self.homePage.footer_title_css) == "Novartis Biome"
        elif self.env_name == "foundation":
            self.basePage.get_element_text(self.homePage.footer_title_css) == "Novartis Foundation"

    def test_ARC_2499_FooterLinks_submenu_links(self):

        """
        Checks if footer links are navigating to correct url or not.
        """

        self.driver.get(self.env) 
        alert = Alert(self.driver)
        footer_sub_menu_list = self.driver.find_elements(*self.homePage.footerLinks_xpath)
        footer_sub_menu_index = 0
        for footer_sub_menu in footer_sub_menu_list:
            footer_sub_menu_list = self.driver.find_elements(*self.homePage.footerLinks_xpath)
            footer_sub_menu_href = footer_sub_menu_list[footer_sub_menu_index].get_attribute("href")
            footer_sub_menu_text = str(footer_sub_menu_list[footer_sub_menu_index].text.encode('UTF-8'))[1:].replace("'","")
            if not 'https://www.novartis.com/' == footer_sub_menu_href or self.env_name == "global":
                self.driver.execute_script("arguments[0].click()", footer_sub_menu_list[footer_sub_menu_index])

                
                    
                try :
                    if len(alert.text) > 0:
                        alert.accept()
                        self.driver.refresh()
                        self.driver.switch_to.window(self.driver.window_handles[1])
                        assert footer_sub_menu_href in self.driver.current_url
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])
                except:
                    print('Alert pop up is not coming')
                    if footer_sub_menu_href in self.driver.current_url:
                            
                        assert footer_sub_menu_href in self.driver.current_url
                        if self.env_name == "switzerland":
                            if ("media-library" or "live.novartis" or "campus.novartis")  in footer_sub_menu_href :

                                assert len(self.driver.current_url) > 0
                            else :

                                assert self.env.split("@")[1] in self.driver.current_url


                        else :

                            try:
                                assert self.env in self.driver.current_url
                            except:
                                assert self.env.split("@")[1] in self.driver.current_url
        
                        
                    else:
                        if self.env_name == "switzerland":
                            if ("live.novartis" or "campus.novartis")  in footer_sub_menu_href :
                                # try :
                                #     if len(alert.text) > 0:
                                #         alert.accept()
                                #         self.driver.refresh()
                                # except:
                                #     print('Alert pop up is not coming')
                                self.driver.switch_to.window(self.driver.window_handles[1])
                                assert footer_sub_menu_href in self.driver.current_url
                                self.driver.close()
                                self.driver.switch_to.window(self.driver.window_handles[0])
                                
                        else:
                            # try :
                            #     if len(alert.text) > 0:
                            #     alert.accept()
                            #     self.driver.refresh()
                            # except:
                            #     print('Alert pop up is not coming')
                            if self.driver.find_elements(self.homePage.continue_button_css[0], self.homePage.continue_button_css[1]):
                                self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.homePage.continue_button_css[0], self.homePage.continue_button_css[1]))
                            if footer_sub_menu_href in self.driver.current_url:
                                assert footer_sub_menu_href in self.driver.current_url
                            else:
                                self.driver.switch_to.window(self.driver.window_handles[1])
                                # assert "Page Not Found" not in self.driver.page_source
                                assert footer_sub_menu_href in self.driver.current_url
                                self.driver.close()
                                self.driver.switch_to.window(self.driver.window_handles[0])
                    self.driver.get(self.env) 
                    # self.driver.back()
                    footer_sub_menu_index = footer_sub_menu_index + 1


    def test_ARC_2499_FooterLinks_portfolio_links(self):

        """
        Checks if footer portfolio links are navigating to correct url or not.
        """

        self.driver.get(self.env)
        alert = Alert(self.driver)
        portfolio_urls = self.driver.find_elements(*self.homePage.footer_link_portfolio_css)
        portfolio_index = 0
        for portfolio_link in portfolio_urls:
            portfolio_urls = self.driver.find_elements(*self.homePage.footer_link_portfolio_css)
            portfolio_sub_menu_href = portfolio_urls[portfolio_index].get_attribute("href")
            portfolio_sub_menu_target = portfolio_urls[portfolio_index].get_attribute("target")
            self.driver.execute_script("arguments[0].click()", portfolio_urls[portfolio_index])
            if portfolio_sub_menu_href in self.driver.current_url:
                 assert portfolio_sub_menu_href in self.driver.current_url
            elif portfolio_sub_menu_target == "_blank":
                try :
                    if len(alert.text) > 0:
                        alert.accept()
                        self.driver.refresh()
                except:
                        print('Alert pop up is not coming')
                child = self.driver.window_handles[1]
                parent = self.driver.window_handles[0]
                self.driver.switch_to.window(child)
                assert portfolio_sub_menu_href in self.driver.current_url
                self.driver.close()
                self.driver.switch_to.window(parent) 
            elif self.driver.find_elements((self.homePage.continue_button_css[0], self.homePage.continue_button_css[1])):
                self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.homePage.continue_button_css[0], self.homePage.continue_button_css[1]))
                assert portfolio_sub_menu_href in self.driver.current_url
            self.driver.back()
            portfolio_index += 1


        if self.env_name == "uk" or self.env_name == "usa" or self.env_name == "singapore" or self.env_name == "austria":
            footer_sub_menu_list = self.driver.find_elements(*self.homePage.footer_link_portfolio_css)
            footer_sub_menu_index = 0
            for footer_sub_menu in footer_sub_menu_list:
                footer_sub_menu_list = self.driver.find_elements(*self.homePage.footer_link_portfolio_css)
                footer_sub_menu_href = footer_sub_menu_list[footer_sub_menu_index].get_attribute("href")
                if "products" in footer_sub_menu_href:
                    self.driver.execute_script("arguments[0].click()", footer_sub_menu_list[footer_sub_menu_index])
                    try:
                        assert self.env in self.driver.current_url
                    except:
                        assert self.env.split("@")[1] in self.driver.current_url
                    self.driver.back()
                footer_sub_menu_index = footer_sub_menu_index + 1

    
    # def test_ARC_2499_FooterLinks_sitemap(self):

    #     """
    #     Checks if sitemap is navigating to correct url or not.
    #     Checks if content is there or not in sitemap.xml.
    #     Checks sitemap urls consist the particular env.
    #     """


    #     self.driver.get(self.env)

    #     link_txt,primary_url,site_url,right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.site_map_xpath)
    #     assert len(link_txt) > 0
    #     assert site_url in primary_url

    #     site_map_urls = self.homePage.sitemap_validation()
    #     assert len(site_map_urls) > 0
    #     for url in site_map_urls:
    #         try:
    #             assert self.env in url
    #         except:
    #             assert self.env.split("@")[1]  in url

    
    def test_ARC_2499_FooterLinks_sitemap_nodeUrl_validation(self):

        """
        Checks if sitemap is having node url or not.
    
        """
        self.driver.get(self.env) 

        site_map_href = self.homePage.sitemap_node_url()
        for url in site_map_href:

            assert not "/node/" in url
        
    
    def test_ARC_2499_FooterLinks_privacy_policy(self):

        """
        Checks if privacy policy is navigating to correct url or not.
        """

        self.driver.get(self.env)

        try:
            if self.env_name == 'france':
                link_txt,primary_url,site_url, right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_france_xpath)
            elif self.env_name == 'italy':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.privacy_italy_xpath)
            elif self.env_name == 'spain':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.privacy_spain_xpath)
            elif self.env_name == 'japan':
                link_txt,primary_url,site_url, right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_spain_xpath)
            elif 'switzerland-fr' in self.env_name:
                link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_ch_fr_xpath)
            elif 'switzerland' in self.env_name:
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.privacy_ch_xpath)
            elif self.env_name == 'austria':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.privacy_austria_xpath)
            elif self.env_name == 'portugal':
                link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_portugal_xpath)
            elif self.env_name == 'german' or self.env_name == 'austria':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.privacy_german_xpath)
            elif self.env_name == 'cz-cs':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.privacy_cz_cs_xpath)
            elif self.env_name == 'canada-fr':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.privacy_canada_fr_xpath)
            elif self.env_name == 'netherland':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.privacy_nl_xpath)
            elif self.env_name == 'finland':
                link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_finland_xpath)
            elif self.env_name == 'slovakia':
                link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_slovakia_xpath)
            elif self.env_name == 'serbia':
                link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_serbia_xpath)
            elif self.env_name == 'norway':
                link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_norway_xpath)
            elif self.env_name == 'denmark':
                link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_dk_xpath)


            assert len(link_txt) > 0
            assert primary_url in site_url
            assert right_hand_rail == 0
            
        except:
            link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.privacy_xpath)
            assert len(link_txt) > 0
            assert primary_url in site_url
            assert right_hand_rail == 0

    
    def test_ARC_2499_FooterLinks_terms_of_use(self):

        """
        Checks if terms of use is navigating to correct url or not.
        """
    
        self.driver.get(self.env)

        try:
            if self.env_name == 'france':
                link_txt,primary_url,site_url,right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_france_xpath)
            elif self.env_name == 'italy':
                link_txt,primary_url,site_url,right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_italy_xpath)
            elif self.env_name == 'spain':
                link_txt,primary_url,site_url,right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_spain_xpath)
            elif self.env_name == 'japan':
                link_txt,primary_url,site_url,right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_spain_xpath)
            elif 'switzerland-fr' in self.env_name:
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_ch_fr_xpath)
            elif 'switzerland' in self.env_name:
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_ch_xpath)
            elif self.env_name == 'austria':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_austria_xpath)
            elif self.env_name == 'portugal':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_portugal_xpath)
            elif self.env_name == 'german' or self.env_name == 'austria':
                link_txt,primary_url,site_url , right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_german_xpath)
            elif self.env_name == 'cz-cs':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_cz_cs_xpath)
            elif self.env_name == 'canada-fr':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_canada_fr_xpath)
            elif self.env_name == 'netherland':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_nl_xpath)
            elif self.env_name == 'finland':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_finland_xpath)
            elif self.env_name == 'slovakia':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_slovakia_xpath)
            elif self.env_name == 'serbia':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_serbia_xpath)
            elif self.env_name == 'norway':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_norway_xpath)
            elif self.env_name == 'denmark':
                link_txt,primary_url,site_url , right_hand_rail= self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_dk_xpath)


            assert len(link_txt) > 0
            assert primary_url in site_url
            assert right_hand_rail == 0


        except:
            link_txt,primary_url,site_url,right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.terms_of_use_xpath)
            assert len(link_txt) > 0
            assert primary_url in site_url
            assert right_hand_rail == 0


   
        

    
    # def test_ARC_2499_FooterLinks_site_directory(self):

    #     """
    #     Checks if site directory is navigating to correct url or not.
    #     """

    #     self.driver.get(self.env)
    #     if "china" not in self.env_name:
    #         link_txt,primary_url,site_url,right_hand_rail = self.homePage.footer_links_under_copyright(self.homePage.site_directory_css)
    #         assert len(link_txt) > 0    
    #         if "biome" in self.env_name:
    #             assert site_url in primary_url.replace("-site","")
    #         else:
    #             assert site_url in primary_url

            

    
    def test_ARC_2499_FooterLinks_total_menu_regions(self):

        """
        Checks the following :-
        1. In Global Site Footer Section 4 columns are there.
        2. In Biome Site Footer Section 3 columns are there.
        3. In Foundation Site Footer Section 3 columns are there.
        """

        if self.env_name == 'global':
            self.driver.get(self.env)
            assert len(self.driver.find_elements(*self.homePage.footer_regions_xpath)) == 4
        elif self.env_name == 'biome':
            self.driver.get(self.env)
            assert len(self.driver.find_elements(*self.homePage.footer_regions_xpath)) == 2
        elif self.env_name == 'foundation':
            self.driver.get(self.env)
            assert len(self.driver.find_elements(*self.homePage.footer_regions_xpath)) == 3

    
    def test_ARC_2499_FooterLinks_social_icon_title(self):

        """
        Checks if title attribute is there in <a> tag of social icons.
        """

        self.driver.get(self.env)
        social_media_titles = self.driver.find_elements(*self.homePage.social_media_icons_xpath)
        assert len(social_media_titles) > 0
        for title in social_media_titles:
            assert len(title.get_attribute("title")) > 0

    
    def test_ARC_2499_FooterLinks_copyright(self):

        """
        Checks if 1)© 2023 Sandoz is there for sandoz and 2)© 2023 Novartis is there for rest of the sites.
        """

        self.driver.get(self.env)
        if self.env_name == "sandoz":
            assert "© 2023 Sandoz" in self.basePage.get_element_text(self.homePage.copyright_css)
        elif self.env_name == "hk":
            assert "\\xc2\\xa9 2023" in str(self.driver.find_element(*self.homePage.copyright_css).text.encode("utf-8"))[1:].replace("'","")
        elif self.env_name == "japan":
            assert len(self.driver.find_elements(*self.homePage.copyright_css)) > 0
        else:
            assert "© 2023 Novartis" in self.basePage.get_element_text(self.homePage.copyright_css)


    def test_ARC_2499_FooterLinks_seven_menu(self):

        """
        Checks if the followings are there in the footer section of root site :-
        1. Terms of Use
        2. Privacy
        3. Site Map
        4. Contacts
        5. Cookie Settings
        6. Open Source
        7. Web Accessibility
        """

        if self.env_name == 'global':
            self.driver.get(self.env)
            assert self.basePage.get_element_text(self.homePage.terms_of_use_xpath) == "Terms of Use" 
            assert self.basePage.get_element_text(self.homePage.privacy_xpath) == "Privacy" 
            assert self.basePage.get_element_text(self.homePage.site_map_xpath) == "Site Map" 
            assert self.basePage.get_element_text(self.homePage.contacts_xpath) == "Contacts" 
            assert self.basePage.get_element_text(self.homePage.cookie_setting_id) == "Cookie Settings" 
            assert self.basePage.get_element_text(self.homePage.open_source_xpath) == "Open Source" 
            assert self.basePage.get_element_text(self.homePage.accessibility_xpath) == "Web Accessibility" 

    
    def test_ARC_2499_FooterLinks_menu_titles(self):

        """
        Checks the menu title are in particular order or not for Global, Biome and Foundation site
        """

        self.driver.get(self.env)
        if self.env_name == 'global':
            menu_titles = self.driver.find_elements(*self.homePage.footer_menu_titles_css)
            assert menu_titles[0].text == "Navigate Novartis" 
            assert menu_titles[1].text == "Topics" 
            assert menu_titles[2].text == "Explore" 
            assert menu_titles[3].text == "Novartis companies"
        elif self.env_name == 'biome':
            menu_titles = self.driver.find_elements(*self.homePage.footer_menu_titles_css)
            assert menu_titles[0].text == "Navigate Biome" 
            assert menu_titles[1].text == "Media Center" 
        elif self.env_name == 'foundation':
            menu_titles = self.driver.find_elements(*self.homePage.footer_menu_titles_css)
            assert menu_titles[0].text == "Navigate Novartis Foundation" 
            assert menu_titles[1].text == "About the Novartis Foundation" 
            assert menu_titles[2].text == "Media Center" 

    
    def test_ARC_2499_FooterLinks_not_bold(self):

        """
        Checks that Footer links under copyright scetion are not in bold.
        """

        self.driver.get(self.env)

        assert self.basePage.get_css_property(self.homePage.footer_links_under_copyright_ul_xpath, "font-weight") == "400"
