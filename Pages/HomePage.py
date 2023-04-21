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
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.alert import Alert


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    megamenu_css = (By.CSS_SELECTOR, 'button[class="nav-link nav-link- "]')
    megamenu_href_xpath = (By.XPATH,"//ul[contains(@class,'nav-tabs')]/li[@data-level='0']/a")
    news_href_xpath = (By.XPATH,'//ul[contains(@class,"subul")]/li[@data-level="1"]')


    novartis_logo_css = (By.CSS_SELECTOR, "#navbar-main > a > img")
    pattern_css = (By.CSS_SELECTOR, ".background_stripe")
    pattern_path = "/themes/custom/nvs_arctic/patterns/images/blue_carbon_open_pattern_tile_120.png"
    watch_the_video_external_icon_css = (By.CSS_SELECTOR, "div > a > svg")
    esg_video_xpath = (By.XPATH, "//iframe[contains(@id,'zlz')]")
    research_dev_video_xpath = (By.XPATH, "//iframe[contains(@id,'yxr')]")
    play_pause_btn_css = (By.CSS_SELECTOR, ".playPauseBtn")
    render_state_css = (By.CSS_SELECTOR, ".mwPlayerContainer")
    novartis_video_link_css = (By.CSS_SELECTOR, ".videoDisplay > video")
    
    novartis_finance_result_xpath_wildcard = (By.XPATH, "//img[contains(@title, 'Basel Campus')]")
    novartis_covid19_info_xpath_wildcard = (By.XPATH, "//img[contains(@title, 'COVID')]")
    susanne_schaffert_talks_to_monocle_img = (By.XPATH, "//img[@title='Susanne Schaffert talks to Monocle']")
    kidney_patient_at_camera_img = (By.XPATH, "//img[@title='A kidney patient is smiling at the camera.']")
    top_hero_img_css = (By.CSS_SELECTOR, "div.carousel_img_video > div > picture > img")
    top_hero_img_src = "/sites/novartis_com/files/styles/banner_image_1920/public/2021-10/female-scientist-in-lab-hero.jpg"
    top_hero_title_css = (By.CSS_SELECTOR, ".stripe_title")
    hero_desc_css = (By.CSS_SELECTOR, ".carousel_desc")
    hero_blue_box_css = (By.CSS_SELECTOR, ".carousel_inner--wrapper")
    hero_blue_rgb = "rgb(4, 96, 169)"
    
    hero_learn_more = (By.CSS_SELECTOR, "div.carousel_link_button > a")
    bottom_hero_img_css = (By.CSS_SELECTOR, "#paragraph--37081 > div > div > div.carousel_img_video > div > picture > img")
    bottom_hero_title_css = (By.CSS_SELECTOR, "#paragraph--37081 > div > div > div.carousel-caption.d-md-block.content_box.left > div > div > h1 > a")
    bottom_hero_img_src = "sites/novartis_com/files/styles/banner_image_1920/public/2021-10/chinese-girls-sharing-umbrella.jpg"
    bottom_hero_desc_css = (By.CSS_SELECTOR, "#paragraph--37081 > div > div > div.carousel-caption.d-md-block.left > div > div > p")
    bottom_hero_blue_box_xpath = (By.XPATH, "//*[starts-with(@id,'paragraph')]/div/div/div[2]/div/div")
    learn_more_25year = (By.CSS_SELECTOR, "div.col-lg-6.order-lg-1.media_stripe_text > div > div > div > div > a")
    pop_up_logo_css = (By.CSS_SELECTOR, ".ui-dialog-titlebar > .img-fluid.d-inline-block.align-top")
    pop_up_title_css = (By.CSS_SELECTOR, ".ui-dialog-title")
    pop_up_body_css = (By.CSS_SELECTOR, ".external-link-popup-body > p")
    continue_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(1)")
    cancel_button_css = (By.CSS_SELECTOR, ".ui-dialog-buttonset > button:nth-child(2)")
    large_play_button_css = (By.CSS_SELECTOR, ".largePlayBtn")
    twitter = (By.CSS_SELECTOR, ".social-media-link-icon--twitter")
    linkedin = (By.CSS_SELECTOR, ".social-media-link-icon--linkedin")
    youtube = (By.CSS_SELECTOR, ".social-media-link-icon--youtube")
    facebook = (By.CSS_SELECTOR, ".social-media-link-icon--facebook")
    instagram = (By.CSS_SELECTOR, ".social-media-link-icon--instagram")
    sandoz_css = (By.XPATH, "//a[contains(@class,'sandoz')]")
    advanced_accelerator_applications_xpath = (By.XPATH, "//a[contains(@class,'adacap')]")
    navigate_sub_menu_names = ["Patients and Caregivers", "Healthcare Professionals", "Researchers", "Job Seekers", "Investors", "Partners", "Suppliers"]
    topics_sub_menu_names = ["Clinical Trials", "COVID-19 Info Center", "ESG"]
    explore_sub_menu_names = ["Stories", "Diseases", "Locations"]
    companies_sub_menu_names = ["Sandoz", "Advanced Accelerator Applications"]
    stories_css = (By.CSS_SELECTOR, ".nav-link--stories")
    diseases_css = (By.CSS_SELECTOR, ".nav-link--diseases")
    locations_css = (By.CSS_SELECTOR, ".nav-link--about-locations")
    site_map_xpath = (By.XPATH, "//a[contains(@class, 'sitemapxml')]")
    site_directory_css = (By.CSS_SELECTOR, "div.site_directory > a > span.dir-text")
    site_directory_url_css = (By.CSS_SELECTOR, "#block-footerbottom > div > div > div > div.col-lg-4 > div.site_directory > a")

    terms_of_use_xpath = (By.XPATH, "//a[contains(@class, 'terms-') and contains(@class, '-use')]")
    # have to change when site goes live
    terms_of_use_italy_xpath = (By.XPATH, "//a[contains(@class, 'node-226')]")
    terms_of_use_canada_fr_xpath = (By.XPATH, "//a[contains(@class, 'node-226')]")
    terms_of_use_cz_cs_xpath = (By.XPATH, "//a[contains(@class, 'podminky-pouziti')]")
    terms_of_use_austria_xpath = (By.XPATH, "//a[contains(@class, 'nutzungsbedingungen')]")
    terms_of_use_portugal_xpath = (By.XPATH, "//a[contains(@class, 'termos-de-utilizacao')]")
    terms_of_use_france_xpath = (By.XPATH, "//a[contains(@class, 'conditions-dutilisation')]")
    terms_of_use_norway_xpath = (By.XPATH, "//a[contains(@class, 'brukervilkar-denne-nettsiden')]")
    terms_of_use_spain_xpath = (By.XPATH, "//a[contains(@class, 'terminos-de-uso')]")
    terms_of_use_dk_xpath = (By.XPATH, "//a[contains(@class, 'brugerbetingelser')]")
    terms_of_use_ch_xpath = (By.XPATH, "//a[contains(@class, 'nutzungsbedingungen')]")
    terms_of_use_ch_fr_xpath = (By.XPATH, "//a[contains(@class, 'politique-de-confidentialite')]")
    terms_of_use_german_xpath = (By.XPATH, "//a[contains(@class, 'nutzungsbedingungen')]")
    terms_of_use_serbia_xpath = (By.XPATH, "//a[contains(@class, 'uslovi-koriscenja')]")
    terms_of_use_slovakia_xpath = (By.XPATH, "//a[contains(@class, 'podmienky-pouzivania')]")
    terms_of_use_nl_xpath = (By.XPATH, "//a[contains(@class, 'leveringsvoorwaarden') and not(contains(@class, 'cook'))]")

    privacy_xpath = (By.XPATH, "//a[contains(@class, 'privacy')]")
    # have to change when site goes live
    privacy_italy_xpath = (By.XPATH, "//a[contains(@class, 'node-221')]")
    privacy_canada_fr_xpath = (By.XPATH, "//a[contains(@class, 'node-221')]")
    privacy_cz_cs_xpath = (By.XPATH, "//a[contains(@class, 'zasady-ochrany-osobnich-udaju')]")
    privacy_france_xpath = (By.XPATH, "//a[contains(@class, 'donnees-personnelles')]")
    privacy_norway_xpath = (By.XPATH, "//a[contains(@class, 'personvern-og-gdpr')]")
    privacy_austria_xpath = (By.XPATH, "//a[contains(@class, 'datenschutzerklaerung')]")
    privacy_portugal_xpath = (By.XPATH, "//a[contains(@class, 'politica-de-privacidade')]")
    privacy_spain_xpath = (By.XPATH, "//a[contains(@class, 'politica-de-privacidad')]")
    privacy_ch_xpath = (By.XPATH, "//a[contains(@class, 'datenschutzerklaerung')]")
    privacy_ch_fr_xpath = (By.XPATH, "//a[contains(@class, 'conditions-dutilisation')]")
    privacy_dk_xpath = (By.XPATH, "//a[contains(@class, 'brugerbetingelser-og-politikker-beskyttelse-og-behandling-af-personoplysninger')]")
    privacy_german_xpath = (By.XPATH, "//a[contains(@class, 'datenschutzerklaerung')]")
    privacy_serbia_xpath = (By.XPATH, "//a[contains(@class, 'politika-zastite-privatnosti')]")
    privacy_slovakia_xpath = (By.XPATH, "//a[contains(@class, 'o-nas-zasady-ochrany-osobnych-udajov')]")
    privacy_nl_xpath = (By.XPATH, "//a[contains(@class, 'privacyverklaring-voor-websites') and not(contains(@class, 'cook'))]")

    contacts_xpath = (By.XPATH, "//a[contains(@class, 'contacts')]")
    cookie_setting_id = (By.ID, "cookie-settings-button")
    accessibility_xpath = (By.XPATH, "//a[contains(@class, 'accessibility')]")
    open_source_xpath = (By.XPATH, "//a[contains(@class, 'open-source')]")

    search_icon_css = (By.CSS_SELECTOR, "li.nav-item.search > button")
    search_input_id = (By.XPATH, '//*[starts-with(@id,"edit-keyword")]')
    search_button_id = (By.ID, "edit-submit-global-search")
    global_search_css = (By.CSS_SELECTOR, "#ms-list-1 > button > span")
    search_input_footer_id = (By.ID, 'edit-keys')
    search_button_footer_css = (By.CSS_SELECTOR, 'form#search-block-form > div.form-actions > div > input')
    search_keyword = "medicine"
    novartis_logo = "logo.svg"
    external_popup_title = "You are now leaving the Novartis.com website"
    external_popup_desc = "This link will take you to a website to which our Privacy Policy does not apply. You are solely responsible for your interactions with that website."
    continue_button_txt = "Continue"
    cancel_button_txt = "Cancel"
    youtube_continue_page_css = (By.XPATH, "//button[@aria-label='Accept all']")
    navigate_submenu_list_xpath = (By.XPATH, "//*[@id='block-navigatetonovartis']/li")
    topics_submenu_list_xpath = (By.XPATH, "//*[@id='block-aboutnovartis']/li")
    explore_submenu_list_xpath = (By.XPATH, "//*[@id='block-contactus']/li")
    companies_submenu_list_xpath = (By.XPATH, "//*[@id='block-ourportfolio']/li")
    submenu_nav_link_css = (By.CSS_SELECTOR, ".nav-link")

    link_url_xpaths = [(By.XPATH, "//a[contains(@href,'/about') and contains(@class,'card_wrapper')]"), (By.XPATH, "//a[contains(@href,'/esg/access') and contains(@class,'card_wrapper')]"), (By.XPATH, "//a[contains(@href,'/research-development') and contains(@class,'card_wrapper')]"), (By.XPATH, "//a[contains(@href,'/research-development') and contains(@title,'Learn More')]"), (By.XPATH, "//a[contains(@href,'/stories/restoring-vision-and-hope-thousands-southeast-asia')]"), (By.XPATH, "//a[contains(@href,'/stories/toward-regrowing-cartilage')]"), (By.XPATH, "//a[contains(@href,'/stories/expanding-new-digital-healthcare-solution-across-chronic-heart-disease-management') and contains(@title,'Read the Story')]"), (By.XPATH, "//a[contains(@href,'/news/news-archive?type=media_release')]"), (By.XPATH, "//a[contains(@href,'/news/novartis-financial-results') and contains(@class,'card_wrapper')]"), (By.XPATH, "//a[contains(@href,'/coronavirus') and contains(@class,'card_wrapper')]"), (By.XPATH, "//a[contains(@href,'/patients-and-caregivers') and contains(@class,'card_wrapper')]"), (By.XPATH, "//a[contains(@href,'/about/strategy/people-and-culture')]"), (By.XPATH, "//a[contains(@href,'https://live.novartis.com')]"), (By.XPATH, "//a[contains(@title,'Learn More')]")]

    mega_menu_btn_css = (By.CSS_SELECTOR, ".menu > .nav-link")
    mega_menu_news_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]")
    mega_menu_about_xpath = (By.XPATH, "//li[contains(@class, 'dropdown-menu')]/a[contains(@href, '/about')]")
    mega_menu_career_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/careers') and not(contains(@target,'_self'))]")
    mega_menu_research_xpath = (By.XPATH,"//li[contains(@class, 'dropdown-menu')]/a[contains(@href, '/research-development')]")

    mega_menu_about_arrow_xpath = (By.XPATH, "//li[contains(@class, 'dropdown-menu')]/a[contains(@href, 'about')]//parent::li/p")
    mega_menu_news_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/news')]//parent::li/p[@class='we-icon']")
    mega_menu_career_arrow_xpath = (By.XPATH, "//li[contains(@class,'dropdown-menu')]/a[contains(@href,'/careers') and not(contains(@target,'_self'))]//parent::li/p[@class='we-icon']")
    mega_menu_research_arrow_xpath = (By.XPATH,"//li[contains(@class, 'dropdown-menu')]/a[contains(@href,'/research-development')]//parent::li/p[@class='we-icon']")

    mega_menu_media_library_xpath= (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'/media-library')]")
    mega_menu_career_search_xpath= (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'/career-search')]")
    mega_menu_stories_xpath= (By.XPATH, "//li[contains(@class, 'mega-menu')]/a[contains(@href,'/stories') and not(contains(@href, 'news')) and not(contains(@href, 'education'))]")
    mega_menu_news_archive_xapth= (By.XPATH, "//a[contains(@href,'/news/news-archive')]")
    mega_menu_product_xpath = (By.XPATH, "//li[contains(@class, 'we-mega-menu-li')]/a[contains(@href, '/about/products')]")
    mega_menu_pipeline_xpath = (By.XPATH,"(//li[contains(@class, 'we-mega-menu-li')]/a[contains(@href, '/research-development/novartis-pipeline')])[2]")
    
    image_elements_xpath = (By.XPATH, "//div[contains(@class, 'img-wrapper')]")
    image_title_css = (By.CSS_SELECTOR, ".card_title")

    carousel_elements_css = (By.CSS_SELECTOR, "ol.carousel-indicators > li")
    carousel_elements_migration_css = (By.CSS_SELECTOR, "ol.carousel-indicators > li")
    carousel_img_css = (By.CSS_SELECTOR, "#paragraph--2146 > div.carousel-inner > div.carousel-item")
    carousel_img_migration_css = (By.CSS_SELECTOR, "#paragraph--3996 > div.carousel-inner > div.carousel-item")
    carousel_link_css = (By.CSS_SELECTOR, "div > .container > div.carousel_inner--wrapper > h1 > a")
    carousel_link_sub_css = (By.CSS_SELECTOR, "div > .container > div.carousel_inner--wrapper > div > p > a")

    card_wrapper_css = (By.CSS_SELECTOR, "a.card_wrapper")
    card_img_parent_anchor_tag_xpath = (By.XPATH, "../../..")
    link_button_css = (By.CSS_SELECTOR, "a.link_button")
    all__news_css = (By.CSS_SELECTOR, "div.link_button_wrapper > a")
    banner_link_css = (By.CSS_SELECTOR, "h1.stripe_title > a")
    cookie_id = (By.ID, "onetrust-accept-btn-handler")
    footer_links_xpath = (By.XPATH, "//div[(@class = 'footer-nav-links')]/ul[not(contains(@id, 'block-novartistopmenu'))]/li/a")
    footerLinks_xpath = (By.XPATH,"//div[(@class = 'footer-nav-links')]/ul[not(contains(@block, 'block-novartistopmenu'))][not(contains(@block, 'block-ourportfolio'))]/li/a")
    sitemap_urls_css = (By.CSS_SELECTOR,'table.sitemap > tbody >tr >td:nth-child(1)')
    footer_link_portfolio_css = (By.CSS_SELECTOR,'#block-ourportfolio > li > a')
    footer_title_css = (By.CSS_SELECTOR, "#block-novartisglobal > h2")

    lang_selector_css = (By.CSS_SELECTOR, "#language-selector-header-block > div > a")
    choose_loc_css = (By.CSS_SELECTOR, ".ls-title > h2 > span")
    country_name_css = (By.CSS_SELECTOR, ".nav-pills > li > a > strong")
    country_list_css = (By.CSS_SELECTOR, ".tab-pane > .countries-list > li > a")
    images_css = (By.CSS_SELECTOR,'.img')

    footer_regions_xpath = (By.XPATH, "//div[contains(@class, 'col-lg-3')]/section[contains(@class, 'region-footer')]/nav")
    social_media_icons_xpath = (By.XPATH, "//a[contains(@class, 'social-media-link-icon')]")
    copyright_css = (By.CSS_SELECTOR, ".novartis-text")
    next_page_arrow_xpath = (By.XPATH, "//a[@rel='next']")
    prev_page_arrow_xpath = (By.XPATH, "//a[@rel='prev']")
    card_content_css = (By.CSS_SELECTOR,'.card_content')
    card_type_full_css = (By.CSS_SELECTOR,'.card_type_full')
    novartisLogo_css = (By.CSS_SELECTOR,'a.navbar-brand')
    footer_search_xpath = (By.XPATH, "//input[contains(@id, 'edit-keys')]")
    hero_box_css = (By.CSS_SELECTOR,".container>.carousel_inner--wrapper  ")
    footer_menu_titles_css = (By.CSS_SELECTOR, ".col-lg-3 > section.row > nav > div > h6")
    right_hand_rail_xpath = (By.XPATH,"//div[contains(@id,'right-hand-rail-block')]")
    footer_links_under_copyright_ul_xpath = (By.XPATH, "//ul[contains(@block, 'block-footerbottom')]")
    banner_image_xpath = (By.XPATH,"//img[contains(@src,'banner_image')]")
    social_media_icons_link_xpath = (By.XPATH, "//ul[contains(@class, 'social-media')]/li/a")
    terms_of_use_finland_xpath = (By.XPATH, "//a[contains(@class, 'kayttoehdot-tietosuojailmoitukset-ja-yhteisosaannot')]")
    privacy_finland_xpath = (By.XPATH, "//a[contains(@class, 'kayttoehdot-tietosuojailmoitukset-ja-yhteisosaannot')]")
    #available_url= "novartis-directory"
 


    def news_mega_menu(self, news_submenu,env_name,news_secondlevel_submenu):
        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_news_arrow_xpath)
            else:
                self.move_to_element(self.mega_menu_news_xpath)

            self.press_button(news_submenu)
        except:
            menu = Utilities.multi_language[env_name]['news']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name][news_secondlevel_submenu]
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))
            
    def cookie_handler(self):

        if self.driver.find_elements(*self.cookie_id):
            self.press_button(self.cookie_id)


    def career_mega_menu(self, career_submenu,env_name):
        self.press_button(self.mega_menu_btn_css)
        try:
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_career_arrow_xpath)
            else:
                self.move_to_element(self.mega_menu_career_xpath)

            self.press_button(career_submenu)
        except:
            menu = Utilities.multi_language[env_name]['careers']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                
               self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['career-search']
                
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))



    def about_product_mega_menu(self,env_name):

        self.press_button(self.mega_menu_btn_css)
        try:
            
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button(self.mega_menu_about_arrow_xpath)
            else:
                self.move_to_element(self.mega_menu_about_xpath)
            self.press_button(self.mega_menu_product_xpath)
            if self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                self.press_button((self.continue_button_css[0], self.continue_button_css[1]))

        except:
            menu = Utilities.multi_language[env_name]['about']
            if self.driver.get_window_size().get("width") <= 1050:
                self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]//parent::li/p[@class='we-icon']"))
            
            else:
                
                self.move_to_element((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
            submenu = Utilities.multi_language[env_name]['product']
                
            self.press_button((By.XPATH,f"//a[contains(@href, '{submenu}')]"))


    def about_pipeline_mega_menu(self):

        self.press_button(self.mega_menu_btn_css)
        
            
        if self.driver.get_window_size().get("width") <= 1050:
            self.press_button(self.mega_menu_research_arrow_xpath)
        else:
            self.move_to_element(self.mega_menu_research_xpath)
        self.press_button(self.mega_menu_pipeline_xpath)



    def mega_menu_landing_page(self,env_name,first_level_menu,str_first_level_menu):
        self.press_button(self.mega_menu_btn_css)
        try:
            self.press_button(first_level_menu)

        except:
            menu = Utilities.multi_language[env_name][str_first_level_menu]
            
            self.press_button((By.XPATH,f"//li[contains(@class,'dropdown-menu')]/a[contains(@href, '{menu}')]"))
                




    def hero_banner(self, by_locator_img, by_locator_hero_one, by_locator_hero_two, by_locator_css, css_prop):

        # img = self.get_elemet_attribute(by_locator_img, "src")
        text1 =  str(self.driver.find_element(by_locator_hero_one[0], by_locator_hero_one[1]).text.encode("utf-8"))[1:].replace("'", "")
        #second locator is CSS is now pointing to different element on the page (it's not explicit enough in selection)
        # text2 = ''
        if self.driver.find_elements(*by_locator_hero_two):
            text2 =  str(self.driver.find_element(by_locator_hero_two[0], by_locator_hero_two[1]).text.encode("utf-8"))[1:].replace("'", "")
        css_text= self.get_css_property(by_locator_css, css_prop)
        return text1, text2, css_text


    def hyperlink(self, by_locator):

        link_text = self.get_elemet_attribute(by_locator, "href")
        return link_text


    def card_links(self):

        cards = self.driver.find_elements(self.card_wrapper_css[0], self.card_wrapper_css[1])
        card_index = 0
        card_link_url_list = []
        card_link_current_url_list = []

        for card in cards:
            
            cards = self.driver.find_elements(self.card_wrapper_css[0], self.card_wrapper_css[1])
            card_link_url_list.append(cards[card_index].get_attribute("href"))
            card_url_target = cards[card_index].get_attribute("target")
            self.driver.execute_script("arguments[0].click()", cards[card_index])
            if card_url_target == "_blank":
                if self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                child = self.driver.window_handles[1]
                parent = self.driver.window_handles[0]
                self.driver.switch_to.window(child)
                card_link_current_url_list.append(self.driver.current_url)
                self.driver.close()
                self.driver.switch_to.window(parent)
            else:
                if self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                card_link_current_url_list.append(self.driver.current_url)
                self.driver.back()

            card_index = card_index + 1

        return card_link_url_list, card_link_current_url_list


    def links_button_ele(self, url):

        links_button = self.driver.find_elements(self.link_button_css[0], self.link_button_css[1])
        links_button_index = len(links_button) - 1
        links_button_url_list = []
        links_button_current_url_list = []

        for btn in links_button:
            
            links_button = self.driver.find_elements(self.link_button_css[0], self.link_button_css[1])
            links_button_url_list.append(links_button[links_button_index].get_attribute("href"))
            links_button_target = links_button[links_button_index].get_attribute("target")
            self.driver.execute_script("arguments[0].click()", links_button[links_button_index])
            if links_button_target == "_blank":
                if self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                child = self.driver.window_handles[1]
                parent = self.driver.window_handles[0]
                self.driver.switch_to.window(child)
                links_button_current_url_list.append(self.driver.current_url)
                self.driver.close()
                self.driver.switch_to.window(parent)
            else:
                if self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                links_button_current_url_list.append(self.driver.current_url)
                self.driver.get(url)
            links_button_index = links_button_index - 1

        return links_button_url_list, links_button_current_url_list

    def banner_links(self):

        banners = self.driver.find_elements(self.banner_link_css[0], self.banner_link_css[1])
        banner_index = 0
        banner_url_list = []
        banner_current_url_list = []

        for banner in banners:
            
            banners = self.driver.find_elements(self.banner_link_css[0], self.banner_link_css[1])
            banner_url_list.append(banners[banner_index].get_attribute("href"))
            banner_url_target = banners[banner_index].get_attribute("target")
            self.driver.execute_script("arguments[0].click()", banners[banner_index])
            if banner_url_target == "_blank":
                if self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                child = self.driver.window_handles[1]
                parent = self.driver.window_handles[0]
                self.driver.switch_to.window(child)
                banner_current_url_list.append(self.driver.current_url)
                self.driver.close()
                self.driver.switch_to.window(parent)
            else:
                if self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                banner_current_url_list.append(self.driver.current_url)
                self.driver.back()

            banner_index = banner_index + 1

        return banner_url_list, banner_current_url_list


    def collect_hyperlinks(self):

        hyperlink_elements = self.get_elements(BasePage.hyperlinks)
        return hyperlink_elements

    def external_link(self, by_locator,env_name):

        link_txt_list = []
        pop_up_logo_list = []
        pop_up_title_color_list = []
        font_weight_list = []
        font_family_list = []
        country_name_list = []
        pop_up_title_list = []
        pop_up_desc_list = []
        continue_btn_list = []
        continue_btn_clickable_list = []
        cancel_btn_list = []
        cancel_btn_clickable_list = []
        page_title_list = []

        social_media_icons = self.driver.find_elements(*by_locator)
        for icon in social_media_icons:
            if "mailto" not in icon.get_attribute("href"):
                link_txt_list.append(icon.text)
                self.driver.execute_script("arguments[0].click()", icon)
                pop_up_logo_list.append(self.get_elemet_attribute(self.pop_up_logo_css, "src"))
                pop_up_title_color_list.append(self.get_css_color(self.pop_up_title_css,'color'))
                font_weight_list.append(self.get_css_property(self.pop_up_title_css,'font-weight'))
                font_family_list.append(self.get_css_property(self.pop_up_title_css,'font-family'))
                country_name_list.append(Utilities.multi_language_popup[env_name])
                pop_up_title_list.append(self.get_element_text(self.pop_up_title_css))
                pop_up_desc_list.append(self.get_element_text(self.pop_up_body_css))
                continue_btn_list.append(self.get_element_text(self.continue_button_css))
                continue_btn_clickable_list.append(self.element_clickable(self.continue_button_css))
                cancel_btn_list.append(self.get_element_text(self.cancel_button_css))
                cancel_btn_clickable_list.append(self.element_clickable(self.cancel_button_css))
                self.press_button(self.cancel_button_css)
                page_title_list.append(self.driver.title)
       


        return link_txt_list, pop_up_logo_list, pop_up_title_list, pop_up_desc_list, continue_btn_list, continue_btn_clickable_list, cancel_btn_list, cancel_btn_clickable_list, page_title_list,pop_up_title_color_list,country_name_list,font_weight_list,font_family_list


    def youtube_videos(self, by_locator_one, by_locator_two):

        self.driver.switch_to.frame(self.driver.find_element(by_locator_one[0], by_locator_one[1]))        
        wait = WebDriverWait(self.driver, 60, 5, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(ec.element_to_be_clickable(self.play_pause_btn_css))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.play_pause_btn_css[0], self.play_pause_btn_css[1]))
        if "YouTube" not in by_locator_two[1]:
            try:
                element.click()
            except:
                self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.play_pause_btn_css[0], self.play_pause_btn_css[1]))
        video_render_state = self.get_elemet_attribute(self.render_state_css, "class")
        pause_clip =  self.get_elemet_attribute(self.large_play_button_css, "aria-label")
        
        play_pause_btn = self.get_elemet_attribute(self.play_pause_btn_css, "class")
        
        link = self.get_elemet_attribute(by_locator_two, "src")
        
        wait_time = 100000000
        while wait_time > 0:
            wait_time = wait_time - 1
        
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.play_pause_btn_css[0], self.play_pause_btn_css[1]))
        play_clip =  self.get_elemet_attribute(self.large_play_button_css, "aria-label")
        self.driver.switch_to.default_content()

        return pause_clip, play_pause_btn, link, play_clip, video_render_state;

    def get_image(self, by_locator):

        img = self.get_elemet_attribute(by_locator, "src")
        title =  self.get_elemet_attribute(by_locator, "title")
        self.press_button(by_locator)
        page_source = self.driver.page_source
        self.driver.back()
        return img,title,page_source;

    def footer_sections_get_titles(self):

        navigate = self.get_element_text((By.ID, "block-navigatetonovartis-menu"))
        topics = self.get_element_text((By.ID, "block-aboutnovartis-menu"))
        explore = self.get_element_text((By.ID, "block-contactus-menu"))
        companies = self.get_element_text((By.ID, "block-ourportfolio-menu"))

        return navigate, topics, explore, companies;

    def footer_sub_menu(self, by_locator):

        sub_menu_list = []
        elements = self.driver.find_elements(by_locator[0], by_locator[1])
        for element in elements:
            sub_menu_list.append(element.find_element(self.submenu_nav_link_css[0], self.submenu_nav_link_css[1]).text)

        return sub_menu_list;


    def explore_sub_menu_nav(self, by_locator):

        primary_url = self.get_elemet_attribute(by_locator, "href")
        self.press_button(by_locator)
        site_url = self.driver.current_url
        self.driver.back()

        return primary_url, site_url;

    def footer_links_under_copyright(self, by_locator):

        flag = 0
        alert = Alert(self.driver)
        primary_url_target = ''
        link_txt = str(self.get_element_text(by_locator).encode("utf-8"))[1:].replace("'","")
        print(str(link_txt.encode("utf-8"))[1:].replace("'",""))
        if link_txt == "Novartis Site Directory" or link_txt == "Novartis website directory" or link_txt == "\\xce\\x9a\\xce\\xb1\\xcf\\x84\\xce\\xac\\xce\\xbb\\xce\\xbf\\xce\\xb3\\xce\\xbf\\xcf\\x82 \\xce\\x99\\xcf\\x83\\xcf\\x84\\xcf\\x8c\\xcf\\x84\\xce\\xbf\\xcf\\x80\\xcf\\x89\\xce\\xbd \\xcf\\x84\\xce\\xb7\\xcf\\x82 Novartis" or link_txt == "Ovaj sajt je namenjen korisnicima u Srbiji" or link_txt == "Adres\\xc3\\xa1\\xc5\\x99 webu Novartis" or link_txt == "Adresar sajtova kompanije Novartis" or link_txt == "Webov\\xc3\\xbd adres\\xc3\\xa1r spolo\\xc4\\x8dnosti Novartis" or link_txt == "Novartis Webseiten" or link_txt == "Novartis muualla verkossa" or "dos sites da Novartis" in link_txt or link_txt == "Annuaire des sites Novartis" or link_txt == "Novartis webstedskatalog" or link_txt == "Novartis Webseiten" or link_txt == "Directorio de Novartis" or link_txt == "Overzicht Novartis websites" or link_txt == "\\xe5\\x85\\xa8\\xe7\\x90\\x83\\xe8\\xab\\xbe\\xe8\\x8f\\xaf\\xe7\\xb6\\xb2\\xe7\\xab\\x99\\xe7\\x9b\\xae\\xe9\\x8c\\x84" or link_txt=="Novartis andre nettsider":
            primary_url = self.get_elemet_attribute(self.site_directory_url_css, "href")
            primary_url_target = self.get_elemet_attribute(self.site_directory_url_css, "target")
            flag = 1
        else:    
            primary_url = self.get_elemet_attribute(by_locator, "href")
        self.press_button(by_locator)


        if  flag == 1 or primary_url in self.driver.current_url:
            if primary_url_target == "_blank":
                if len(alert.text) > 0:
                    alert.accept()
                    self.driver.refresh()
                elif self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                parent = self.driver.window_handles[0]
                child = self.driver.window_handles[1]
                self.driver.switch_to.window(child)
                site_url = self.driver.current_url
                right_hand_rail = len(self.driver.find_elements(*self.right_hand_rail_xpath))
                self.driver.close()
                self.driver.switch_to.window(parent)
            elif self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                site_url = self.driver.current_url
                right_hand_rail = len(self.driver.find_elements(*self.right_hand_rail_xpath))
                self.driver.back()
            else:
                
                site_url = self.driver.current_url
                right_hand_rail = len(self.driver.find_elements(*self.right_hand_rail_xpath))
                # time.sleep(4)
                self.driver.back()
        else:
            # self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
            if self.get_elemet_attribute(by_locator, "target") == "_blank":
                if len(alert.text) > 0:
                    alert.accept()
                    self.driver.refresh()
                elif self.driver.find_elements(self.continue_button_css[0], self.continue_button_css[1]):
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(self.continue_button_css[0], self.continue_button_css[1]))
                
                parent = self.driver.window_handles[0]
                child = self.driver.window_handles[1]
                self.driver.switch_to.window(child)
                site_url = self.driver.current_url
                right_hand_rail = len(self.driver.find_elements(*self.right_hand_rail_xpath))
                self.driver.close()
                self.driver.switch_to.window(parent)
                
            else:
                site_url = self.driver.current_url
                right_hand_rail = len(self.driver.find_elements(*self.right_hand_rail_xpath))
                self.driver.back()
        

        return link_txt, primary_url,site_url,right_hand_rail

    def footer_popup_disclaimer(self, by_locator):

        self.press_button(by_locator)
        self.press_button(self.continue_button_css)
        child = self.driver.window_handles[1]
        parent = self.driver.window_handles[0]
        self.driver.switch_to.window(child)

        if "Before you continue to YouTube" in self.driver.title:
            self.press_button(self.youtube_continue_page_css)
    
        count = 1
        while count <= 5:
            page_title = self.driver.title
            if page_title == "Twitter" or page_title == "Facebook" or page_title == "LinkedIn" or page_title == "Novartis - YouTube" or page_title == "Instagram":
                break
            count = count + 1

        self.driver.close()
        self.driver.switch_to.window(parent)

        return page_title;



    def click_search_icon(self):

        self.press_button(self.search_icon_css)

    def verify_search_window(self):

        
        # element = self.get_css_property(self.search_input_id, "border")
        # rgb = int(element.split('d')[1].split('(')[1].split(')')[0].split(', ')[0]), int(element.split('d')[1].split('(')[1].split(')')[0].split(', ')[1]), int(element.split('d')[1].split('(')[1].split(')')[0].split(', ')[2])
        # hex_code = self.rgb_to_hex(rgb)
        value_of_css = self.get_css_property(self.search_input_id,"border-top-color")
        hex_code = Color.from_string(value_of_css).hex
        search = self.get_elemet_attribute(self.search_input_id, "placeholder")

        return hex_code, search

    def global_search_display_status(self):

        global_search_status = self.is_displayed(self.global_search_css)
        return global_search_status

    def search_icon(self):

        search_icon = self.get_css_property(self.search_button_id, "background-image")
        return search_icon
        
    def search_text(self, text, by_locator):

        self.send_keys(self.search_input_id, text)
        self.press_button(self.search_button_id)
        search_txt = self.get_elemet_attribute(by_locator, "value")
        search_txt_url = self.driver.current_url

        return search_txt, search_txt_url


    def search_txt_footer(self, text, by_locator):

        self.send_keys(self.search_input_footer_id, text)
        self.press_button(self.search_button_footer_css)
        search_txt = self.get_elemet_attribute(by_locator, "value")
        search_txt_url = self.driver.current_url

        return search_txt, search_txt_url


    def carousel_ele(self, env_name):

        # carousel_elements = self.driver.find_elements(self.carousel_elements_css[0], self.carousel_elements_css[1])
        # images = self.driver.find_elements(self.carousel_img_css[0], self.carousel_img_css[1])

        carousel_elements, images = self.carousel_loc(env_name)

        index = 0
        banner_links = []
        active_dot_color_list = []
        inactive_dot_color_list = []
        active_carousel_list = []

        for carousel_element, image in zip(carousel_elements, images):

            wait_time = 500
            # carousel_elements = self.driver.find_elements(self.carousel_elements_css[0], self.carousel_elements_css[1])
            # images = self.driver.find_elements(self.carousel_img_css[0], self.carousel_img_css[1])
            carousel_elements, images = self.carousel_loc(env_name)
            try:
                carousel_elements[index].click()
            except:
                self.driver.execute_script("arguments[0].click()", carousel_elements[index])

            value_of_css = carousel_elements[index].value_of_css_property("background-color")
            color = Color.from_string(value_of_css).hex
            active_dot_color_list.append(color)
            if index == 0:
                value_of_css = carousel_elements[index+1].value_of_css_property("background-color")
                color = Color.from_string(value_of_css).hex
                inactive_dot_color_list.append(color)
                
            else:
                value_of_css = carousel_elements[index-1].value_of_css_property("background-color")
                color = Color.from_string(value_of_css).hex
                inactive_dot_color_list.append(color)
                    
            
            while wait_time > 0:
                if "active" in images[index].get_attribute("class"):
                    active_carousel_list.append(images[index].get_attribute("class"))
                    if len(images[index].find_elements(self.carousel_link_css[0], self.carousel_link_css[1])) > 0 and bool(WebDriverWait(images[index], 10).until(ec.element_to_be_clickable((self.carousel_link_css[0], self.carousel_link_css[1])))) == True:

                        banner_links.append(images[index].find_element(self.carousel_link_css[0], self.carousel_link_css[1]).get_attribute("href"))
                    elif len(images[index].find_elements(self.carousel_link_sub_css[0], self.carousel_link_sub_css[1])) > 0 and bool(WebDriverWait(images[index], 10).until(ec.element_to_be_clickable((self.carousel_link_sub_css[0], self.carousel_link_sub_css[1])))) == True:

                        banner_links.append(images[index].find_element(self.carousel_link_sub_css[0], self.carousel_link_sub_css[1]).get_attribute("href"))
                    break
                wait_time = wait_time - 1

            index = index + 1

        return banner_links, active_dot_color_list, inactive_dot_color_list, active_carousel_list


    def carousel_loc(self, env_name):

        if env_name == "global":
            carousel_elements = self.driver.find_elements(self.carousel_elements_css[0], self.carousel_elements_css[1])
            images = self.driver.find_elements(self.carousel_img_css[0], self.carousel_img_css[1])
            return carousel_elements, images
        else:
            carousel_elements = self.driver.find_elements(self.carousel_elements_migration_css[0], self.carousel_elements_migration_css[1])
            images = self.driver.find_elements(self.carousel_img_migration_css[0], self.carousel_img_migration_css[1])
            return carousel_elements, images


    def sitemap_validation(self):

        site_map_urls = []
        count = 0
        self.press_button(self.site_map_xpath)
        siteMap_urls = self.driver.find_elements(*self.sitemap_urls_css)
        for url in siteMap_urls:
            element = siteMap_urls[count].find_element(By.CSS_SELECTOR,'a')
            site_map_urls.append(element.get_attribute('href'))
            count += 1
        return site_map_urls


    def sitemap_node_url(self):

        site_map_urls = []
        count = 0
        self.press_button(self.site_map_xpath)
        siteMap_urls = self.driver.find_elements(*self.sitemap_urls_css)
        for url in siteMap_urls:
            element = siteMap_urls[count].find_element(By.CSS_SELECTOR,'a')
            site_map_urls.append(element.get_attribute('href'))
            count += 1
        return site_map_urls


    def verify_language_selector_color(self):

        blue_color_list = []
        blue_color = ''
        country_lists = self.driver.find_elements(*self.country_list_css)
        index = 0
        for country in country_lists:

            if index > 0:
                country_lists = self.driver.find_elements(*self.country_list_css)
                self.driver.execute_script("arguments[0].click()", country_lists[index])
            country_lists = self.driver.find_elements(*self.country_list_css)
            blue_color = country_lists[index].value_of_css_property("color")
            blue_color_list.append(Color.from_string(blue_color).hex)

            index = index + 1

        return blue_color_list

    def check_url(self):

        url_list = []
        country_code_list = []
        blue_color = ''
        country_lists = self.driver.find_elements(*self.country_list_css)
        index = 0
        for country in country_lists:

            country_lists = self.driver.find_elements(*self.country_list_css)
            self.driver.execute_script("arguments[0].click()", country_lists[index])
            country_lists = self.driver.find_elements(*self.country_list_css)
            country_code_list.append(country_lists[index].text.split("|")[1].replace(" ",""))
            url_list.append(self.driver.current_url)

            index = index + 1

        return url_list, country_code_list


    def images_validation(self):

        display_list = []
        alt_list = []
        title_list = []
        natural_width_list =[]
        index = 0 
        images = self.driver.find_elements(*self.images_css)
        if len(images) > 0 :
            for image in images:

                images = self.driver.find_elements(*self.images_css)
                display_list.append(images[index].get_attribute("src"))
                alt_list.append(images[index].get_attribute("alt"))
                title_list.append(images[index].get_attribute("title"))
                natural_width_list.append(images[index].get_attribute("naturalWidth"))
                index = index + 1

        return display_list, alt_list, title_list,natural_width_list



    def banner_image_validation(self):

        display_list = []
        alt_list = []
        title_list = []
        natural_width_list =[]
        index = 0 
        images = self.driver.find_elements(*self.banner_image_xpath)
        
        for image in images:

            images = self.driver.find_elements(*self.banner_image_xpath)
            display_list.append(images[index].get_attribute("src"))
            alt_list.append(images[index].get_attribute("alt"))
            title_list.append(images[index].get_attribute("title"))
            natural_width_list.append(images[index].get_attribute("naturalWidth"))
            index = index + 1

        return display_list, alt_list, title_list,natural_width_list
           
           






    