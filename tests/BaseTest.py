import pytest
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage
from Pages.MediaLibraryPage import MediaLibraryPage
from Pages.StoriesPage import StoriesPage
from Pages.NewsPage import NewsPage
from Pages.CareerSearchPage import CareerSearchPage
from Pages.CareerLandingPage import CareerLandingPage
from Pages.JobDetailsPage import JobDetailsPage
from Pages.ProductPage import ProductPage
from Pages.GlobalPipelinePage import GlobalPipelinePage
from Pages.SubscribePage import SubscribePage
from Pages.MegaMenuPage import MegaMenuPage
from Pages.NewsRoomPage import NewsRoomPage
from Pages.KeyReleasePage import KeyReleasePage
from Pages.BiographyPage import BiographyPage
from Pages.MediaReleasePage import MediaReleasePage
from Pages.FeaturedNewsPage import FeaturedNewsPage
from Pages.StoryDetailsPage import StoryDetailsPage
from Pages.InteriorPage import InteriorPage
from Pages.WebformPage import WebformPage
from Pages.ContactsPage import ContactsPage

@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("env")
class BaseTest:

    def setup_method(self):
        self.driver.set_window_size(1792, 1034)
        self.basePage = BasePage(self.driver)
        self.megaMenuPage = MegaMenuPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.searchPage = SearchPage(self.driver)
        self.mediaLibraryPage = MediaLibraryPage(self.driver)
        self.storiesPage = StoriesPage(self.driver)
        self.newsPage = NewsPage(self.driver)
        self.careerSearchPage = CareerSearchPage(self.driver)
        self.careerLandingPage = CareerLandingPage(self.driver)
        self.jobDetailsPage = JobDetailsPage(self.driver)
        self.productPage = ProductPage(self.driver)
        self.globalPipelinePage = GlobalPipelinePage(self.driver)
        self.subscribePage = SubscribePage(self.driver)
        self.newsRoomPage = NewsRoomPage(self.driver)
        self.keyReleasePage = KeyReleasePage(self.driver)
        self.bioGraphyPage = BiographyPage(self.driver)
        self.mediaReleasePage = MediaReleasePage(self.driver)
        self.featuredNewsPage = FeaturedNewsPage(self.driver)
        self.storyDetailsPage = StoryDetailsPage(self.driver)
        self.interiorPage = InteriorPage(self.driver)
        self.webformPage = WebformPage(self.driver)
        self.ContactsPage = ContactsPage(self.driver)
    
    # def tear_down(self):
    #     self.driver.get(self.env+"user/logout")