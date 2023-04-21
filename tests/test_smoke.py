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


now = datetime.now() 



# If any more library is needed import it here.

# Holds down the alt key

@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
@pytest.mark.global_site
@pytest.mark.ca
@pytest.mark.ro
@pytest.mark.il
@pytest.mark.co
@pytest.mark.sk
# @pytest.mark.campus
@pytest.mark.bg
@pytest.mark.lv
@pytest.mark.id
@pytest.mark.ve
@pytest.mark.bd
@pytest.mark.pl
@pytest.mark.ru
@pytest.mark.candean
@pytest.mark.ua
@pytest.mark.ee
@pytest.mark.lt
@pytest.mark.sa
@pytest.mark.cl
@pytest.mark.th
@pytest.mark.au
@pytest.mark.sandozcn
class TestSmoke(BaseTest):
    

    @pytest.mark.migration
    @pytest.mark.singapore
    @pytest.mark.pakistan
    @pytest.mark.usa
    @pytest.mark.uk
    @pytest.mark.eg
    @pytest.mark.sandoz
    @pytest.mark.de
    @pytest.mark.at
    @pytest.mark.ph
    # @pytest.mark.ch
    # @pytest.mark.ch_fr
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.es
    @pytest.mark.malaysia
    @pytest.mark.fi
    @pytest.mark.it
    @pytest.mark.nl
    @pytest.mark.pt
    @pytest.mark.jp
    @pytest.mark.tw
    # @pytest.mark.hk
    @pytest.mark.ar
    @pytest.mark.kr
    @pytest.mark.scn
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.biome
    @pytest.mark.no
    @pytest.mark.foundation
    @pytest.mark.ie
    # @pytest.mark.gr
    @pytest.mark.dk
    # @pytest.mark.cz
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.rs
    @pytest.mark.be
    def test_ARC_2408_NovartisLogoHeroBannerPatternVerify(self):

        """
        Checks for hero banner, hero text and Novartis logo in homepage.
         /en shouldn’t be display on the global sites url.
        """

        self.driver.get(self.env)

        if self.env_name == "global":
            current_url =self.driver.current_url
            assert '/en' not in current_url

        novartis_logo_href = self.basePage.get_elemet_attribute(self.homePage.novartisLogo_css,'href') 
        assert len(self.basePage.get_elemet_attribute(self.homePage.novartis_logo_css, "src")) > 0

        self.basePage.press_button(self.homePage.novartis_logo_css)
        current_url = self.driver.current_url
        try:
            assert self.env in current_url
        except:
            assert self.env.split("@")[1] in self.driver.current_url

        assert len(self.driver.find_elements(*self.homePage.top_hero_img_css)) > 0
        
        # text1, text2, css_text = self.homePage.hero_banner(self.homePage.top_hero_img_css, self.homePage.top_hero_title_css, self.homePage.hero_desc_css, self.homePage.hero_blue_box_css, "background")
        # # assert len(img) > 0
        # assert len(text1) > 0
        # if self.driver.find_elements(*self.homePage.hero_desc_css):
        #     assert len(text2) > 0
            
        # assert self.homePage.hero_blue_rgb in css_text

        if self.env_name != "campus":
            pattern = self.basePage.get_css_property(self.homePage.pattern_css, "background-image")
            assert len(pattern) > 0

        #second hero banner:
        # if self.env_name == "global":
        #     img, text1, text2, css_text = self.homePage.hero_banner(self.homePage.bottom_hero_img_css, self.homePage.bottom_hero_title_css, self.homePage.bottom_hero_desc_css, self.homePage.bottom_hero_blue_box_xpath, "background")
        #     assert len(img) > 0
        #     assert len(text1) > 0
        #     assert len(text2) > 0
        #     assert self.homePage.hero_blue_rgb in css_text

       

        if 'carmine' in self.basePage.get_css_property(self.homePage.pattern_css, 'background-image'):
            assert "#8d1f1b" == self.basePage.get_css_color(self.homePage.footer_search_xpath, 'background-color')
            assert "#8d1f1b" == self.basePage.get_css_color(self.homePage.hero_box_css, 'background-color')
        elif 'blue' in self.basePage.get_css_property(self.homePage.pattern_css, 'background-image'):
            assert "#0460a9" == self.basePage.get_css_color(self.homePage.footer_search_xpath, 'background-color')
            assert "#0460a9" == self.basePage.get_css_color(self.homePage.hero_box_css, 'background-color')
        elif 'apricot' in self.basePage.get_css_property(self.homePage.pattern_css, 'background-image'):
            assert "#ec9a1e" == self.basePage.get_css_color(self.homePage.footer_search_xpath, 'background-color')
            assert "#ec9a1e" == self.basePage.get_css_color(self.homePage.hero_box_css, 'background-color')
        elif 'siena' in self.basePage.get_css_property(self.homePage.pattern_css, 'background-image'):
            assert "#e74a21" == self.basePage.get_css_color(self.homePage.footer_search_xpath, 'background-color')
            assert "#e74a21" == self.basePage.get_css_color(self.homePage.hero_box_css, 'background-color')

        # if "pakistan" not in self.env_name:
        #     self.newsPage.launch_newsArchive(self.env_name)
        #     self.basePage.press_button(self.homePage.novartisLogo_css)
        #     current_novartisLogo_url = self.driver.current_url
        #     assert current_novartisLogo_url == novartis_logo_href
        


    @pytest.mark.migration
    @pytest.mark.singapore
    @pytest.mark.pakistan
    @pytest.mark.jp
    @pytest.mark.usa
    @pytest.mark.uk
    @pytest.mark.eg
    @pytest.mark.sandoz
    @pytest.mark.de
    @pytest.mark.at
    @pytest.mark.ph
    @pytest.mark.it
    @pytest.mark.ch
    @pytest.mark.fr
    @pytest.mark.fi
    @pytest.mark.za
    @pytest.mark.malaysia
    @pytest.mark.es
    @pytest.mark.nl
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.no
    @pytest.mark.hk
    @pytest.mark.ar
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.cn
    @pytest.mark.scn
    @pytest.mark.hu
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.gr
    @pytest.mark.dk
    @pytest.mark.cz
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.rs
    def test_ARC_2410_ImageVerify(self):

        """
        Checks for images present in homepage and they are navigating to correct page or not.
        """
        
        self.driver.get(self.env)
        
        card_full_type = self.driver.find_elements(*self.homePage.card_type_full_css)
        img_elements = self.driver.find_elements(self.homePage.image_elements_xpath[0], self.homePage.image_elements_xpath[1])
        # card_content = self.driver.find_elements(*self.homePage.card_content_css)
        assert len(card_full_type) == len(img_elements)
        index=0
        for img_ele in range(len(img_elements)):

            img_elements = self.driver.find_elements(self.homePage.image_elements_xpath[0], self.homePage.image_elements_xpath[1])
            card_href = img_elements[index].find_element(self.homePage.card_img_parent_anchor_tag_xpath[0], self.homePage.card_img_parent_anchor_tag_xpath[1]).get_attribute("href")
            assert len(img_elements[index].find_element(By.CSS_SELECTOR, "img").get_attribute("title")) > 0
            assert len(img_elements[index].find_element(By.CSS_SELECTOR, "img").get_attribute("alt")) > 0
            self.driver.execute_script("arguments[0].click()", img_elements[index].find_element(By.CSS_SELECTOR, "img"))
            if card_href in self.driver.current_url:
                assert card_href in self.driver.current_url
                self.driver.back()
            else:
                if self.driver.find_elements(self.homePage.continue_button_css[0], self.homePage.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.homePage.continue_button_css[0], self.homePage.continue_button_css[1]))
                if card_href in self.driver.current_url:
                    assert card_href in self.driver.current_url
                    self.driver.back()
                else:
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    assert card_href in self.driver.current_url
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
            index=index+1

    # Modification needed
    @pytest.mark.migration
    @pytest.mark.singapore
    @pytest.mark.pakistan
    @pytest.mark.usa
    @pytest.mark.uk
    @pytest.mark.eg
    @pytest.mark.fi
    @pytest.mark.sandoz
    @pytest.mark.de
    @pytest.mark.at
    @pytest.mark.ph
    @pytest.mark.no
    @pytest.mark.ch
    @pytest.mark.jp
    @pytest.mark.fr
    @pytest.mark.za
    @pytest.mark.malaysia
    @pytest.mark.it
    @pytest.mark.es
    @pytest.mark.nl
    @pytest.mark.pt
    @pytest.mark.tw
    @pytest.mark.hk
    @pytest.mark.ar
    @pytest.mark.kr
    @pytest.mark.br
    @pytest.mark.scn
    @pytest.mark.cn
    @pytest.mark.hu
    @pytest.mark.biome
    @pytest.mark.foundation
    @pytest.mark.ie
    @pytest.mark.gr
    @pytest.mark.dk
    @pytest.mark.cz
    @pytest.mark.se
    @pytest.mark.tr
    @pytest.mark.rs
    def test_ARC_2413_HeaderCarousel(self):

        """
        Checks that carousel is working as expected or not in the homepage.
        """

        self.driver.get(self.env)

        if self.env_name == "global":
            carousel_elements = self.driver.find_elements(self.homePage.carousel_elements_css[0], self.homePage.carousel_elements_css[1])
        else:
            carousel_elements = self.driver.find_elements(self.homePage.carousel_elements_migration_css[0], self.homePage.carousel_elements_migration_css[1])

        # Checking if carousel is available
        if len(carousel_elements) == 0:
            assert len(carousel_elements) == 0, "Passing test case because Carousel is not currently available"
        else:

            assert len(carousel_elements) >= 1
            # assert 1!=1

            banner_links, active_dot_color_list, inactive_dot_color_list, active_carousel_list = self.homePage.carousel_ele(self.env_name)

            for active_dot_color, inactive_dot_color, active_carousel in zip(active_dot_color_list, inactive_dot_color_list, active_carousel_list):
            
            # checking color code       
                assert "#fff" in active_dot_color
                # assert "rgba(255, 255, 255, 1)" in active_dot_color
                assert "#221f1f" in inactive_dot_color
                # assert "rgba(34, 31, 31, 1)" in inactive_dot_color
                assert "active" in active_carousel


            for banner_link in banner_links:

                if len(banner_link) == 0:
                    banner_link = self.env
                    self.driver.get(banner_link)
                else:
                    self.driver.get(banner_link)

                assert self.driver.current_url.split("//")[1] in banner_link
        

    


   




                ################################## DON'T DELETE THIS COMMENTS ####################################



    # def test_ARC_9087_brow(self):

    #     self.driver.get("https://www.novartis.com.my/stories/education-awareness/keep-it-pumping-dont-fail-your-heart-or-it-may-fail-you")
    #     self.basePage.press_button((By.LINK_TEXT, 'Save'))
    #     time.sleep(2.5)
    #     # print(len(os.listdir(os.getcwd() + "\\download")))
    #     # print(os.listdir(os.getcwd() + "\\download")[0])
    #     assert len(os.listdir(os.getcwd() + "\\download")) > 0
    #     if "download" in os.listdir():
    #         shutil.rmtree("download")


    # def test_ARC_999_hello(self):

    #     # <ul>
    #     # <li></li>
    #     # <li></li>
    #     # <li></li>
    #     # <li></li>
    #     # </ul>

    #     self.driver.get(self.env + "news/news-archive")
    #     self.basePage.press_button((By.LINK_TEXT, "Media Releases"))
    #     list = []
    #     flag=0
    #     elements = self.driver.find_elements(By.XPATH, "//*[@id='block-views-block-news-archive-block-1']/div/div/div/div/div[1]/ul/li")
    #     for element in elements:
    #         a = element.find_element(By.ID, "list-card-wrapper")
    #         list.append(int(a.find_element(By.CSS_SELECTOR, "span.views-field-field-date > span").text.split(" ")[1].split(",")[0]))

    #     list1 = list[:]
    #     list1.sort(reverse = True)
    #     if (list1 == list):
	#         flag = 1

    #     assert flag == 1

    #      script = "return window.getComputedStyle(document.querySelector('#block-nvs-arctic-breadcrumbs > div > nav > ol > li:nth-child(2)'),'::before').              getPropertyValue('content')";
    #      element = self.driver.execute_script(script);
    #      print(element)
    #      assert 1!=1


  


    # def test_ARC_1010_demo(self):

    #     self.driver.get(self.env + "careers/career-search")
    #     self.basePage.send_keys((By.ID, "edit-search-api-fulltext--2"), "sales")
    #     assert "(Senior) Sales Executive" in self.basePage.get_element_text((By.CSS_SELECTOR, "#ui-id-3 > div > span"))




    # def test_ARC_2317_MegaMenuVerify(self):


    #     self.driver.get(self.env)
    #     self.basePage.click_button((By.ID, "onetrust-accept-btn-handler"))
    #     self.megaMenuPage.clickMegaMenuButton()
    #     # self.megaMenuPage.rightSideImgEle()
    #     self.megaMenuPage.aboutEle()
    #     self.megaMenuPage.healthCareProfessionalEle()

    # def test_ARC_1212_footer(self):

    #     self.driver.get(self.env)
    #     self.basePage.press_button(self.twitter)
    #     self.basePage.press_button((By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)"))
    #     assert "Twitter" in self.driver.page_source
    #     self.driver.switch_to.window(self.driver.window_handles[0])

    #     time.sleep(5)

    #     self.basePage.press_button(self.linkedin)
    #     self.basePage.press_button((By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)"))
    #     assert "LinkedIn" in self.driver.page_source
    #     self.driver.switch_to.window(self.driver.window_handles[0])

    #     time.sleep(5)



    # def multi_language():
            # For Content Migration
        # href=   "/about"- Novartis.com
        # href=   "/about" - Malaysia
        # href=   "/de/about-switzerland-de-german-version” - ch
        # try:
            
            #From megamenu route to news-archive 
        # FirstLevelHref_list = []
        # NewsHref_List = []

        # self.basePage.click_button(self.homePage.megamenu_css)
        # firstLevelHref = self.driver.find_elements(*self.homePage.megamenu_href_xpath)
        # for i in firstLevelHref:
        #     href = i.get_attribute('href')
        #     FirstLevelHref_list.append(href)
        # for menu in FirstLevelHref_list:
        #     if 'news' in menu:
        #         print(menu)
        #         actions = ActionChains(self.driver)
        #         # actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR,"[href="+menu+"]")).perform()
        #         actions.move_to_element(self.driver.find_element(By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]")).perform()

        #         break


        # newsHref = self.driver.find_elements(*self.homePage.news_href_xpath)
        # for i in newsHref:
        #     href = i.get_attribute('href')
        #     NewsHref_List.append(href)
        # for menu in NewsHref_List:
        #     if 'news-archive' in menu:
        #         self.basePage.click_button(self.homePage.mega_menu_news_archive_xapth)
        #         break

        # except:
        #     menu = Utilities.ch['news']
        #     actions = ActionChains(self.driver)
        #     actions.move_to_element(self.driver.find_element(By.CSS_SELECTOR,"[href="+menu+"]")).perform()
        #     submenu = Utilities.ch['news-archieve']
        #     self.driver.find_element(By.CSS_SELECTOR,"[href="+ menu +"]").click()




                                    #################################### END #########################################