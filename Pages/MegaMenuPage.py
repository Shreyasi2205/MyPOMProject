from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from Pages.BasePage import BasePage

class MegaMenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    mega_menu_button = (By.LINK_TEXT, "Menu")
    image_right_side = (By.CSS_SELECTOR, "#block-megamainblock > a.section-image > img")
    txt_under_image = (By.CSS_SELECTOR, "#block-megamainblock > a.section-content")

    about = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > a")
    about_subelement_name = ["Board of Directors", "Executive Committee", "Strategy", "Innovative Medicines", "Sandoz", "Diversity & Inclusion", "Quality", "Product", "Novartis and the European Union (EU)", "Awards and Recognition", "Academic Partnerships & External Innovation"]
    
    board_of_directors = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > a")
    more_from_board_of_directors = (By.CSS_SELECTOR, "div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > span")
    board_of_director_name = ["Joerg Reinhardt", "Enrico Vanni", "Nancy Andrews", "Ton Buechner", "Patrice Bula", "Elizabeth Doherty", "Ann Fudge", "Bridgette Heller", "Frans van Houten", "Simon Moroney", "Andreas von Planta", "Charles Sawyers", "William Winters", "Charlotte Pamer-Wieser"]

    executive_comittee = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(2) > a")
    executive_comittee_name = ["Vasant Narasimhan", "James Bradner", "Karen Hale", "Harry Kirsch", "Steffen Lang", "Klaus Moosmayer", "Richard Saynor", "Susanne Schaffert", "John Tsai", "Marie-France Tschudin", "Robert Weltevreden", "Bertrand Bodson", "Lutz Hegemann", "Natacha Theytaz", "Michael Willi", "Rob Kowalski"]

    strategy = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(3) > a")
    more_from_strategy = (By.CSS_SELECTOR, "div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(3) > div > span")
    strategy_one = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(3) > div > div > div > div > ul > li:nth-child(1) > a")
    strategy_two = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(3) > div > div > div > div > ul > li:nth-child(2) > a")
    strategy_name = ["People and Culture", "Data and Digital"]

    innovative_medicines = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(4) > a")
    more_from_innovative_medicines = (By.CSS_SELECTOR, "div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(4) > div > span")
    innovative_medicines_one = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(4) > div > div > div > div > ul > li:nth-child(1) > a")
    innovative_medicines_two = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(4) > div > div > div > div > ul > li:nth-child(2) > a")
    innovative_medicines_name = ["Novartis Oncology", "Novartis Pharmaceuticals"]

    healthcare_professionals = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(2) > a")
    medical_congress_and_event = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > a")
    global_product_portfolio = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li:nth-child(2) > a")
    novartis_pipeline = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li:nth-child(3) > a")
    managed_access_program = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li:nth-child(4) > a")
    more_from_manage_access_program = (By.CSS_SELECTOR, "div > ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li.we-mega-menu-li.dropdown-menu > div > span")
    managed_access_program_one = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li.we-mega-menu-li.dropdown-menu > div > div > div > div > ul > li > a")
    novartis_external_funding = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li:nth-child(5) > a")
    hcp_resource = (By.CSS_SELECTOR, "#block-mainnavigation > div > div > nav > div > ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li:nth-child(6) > a")


    def clickMegaMenuButton(self):
        self.click_button(self.mega_menu_button)

    def rightSideImgEle(self):
        assert "/sites/novartis_com/files/2021-09/scientist-q2-2021-hero-image.jpg" in self.get_elemet_attribute(self.image_right_side, 'src')
        assert "Homepage" in self.get_element_text(self.txt_under_image)

    def aboutEle(self):
        # self.press_button((By.CSS_SELECTOR, "div > nav > div > ul > li:nth-child(1) > p"))
        self.move_to_element(self.about)
        self.verify_css_property(self.about, "left", "text-align")
        self.verify_css_property(self.about, "700", "font-weight")
        assert self.element_clickable(self.about) == True
        assert "About" in self.get_element_text(self.about)
        count = 0
        for i in self.about_subelement_name:
            count = count + 1
            assert i in self.get_element_text((By.CSS_SELECTOR, f"#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child({count}) > a"))
        self.boardDirectorEle()
        self.executiveCommitteeEle()
        self.strategyEle()
        self.innovativeMedicineEle()
    

    def boardDirectorEle(self):
        # self.press_button((By.CSS_SELECTOR, "ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > p"))
        self.move_to_element(self.board_of_directors)
        count=0
        for i in self.board_of_director_name:
            count = count + 1
            assert i in self.get_element_text((By.CSS_SELECTOR, f"#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(1) > div > div > div > div > ul > li:nth-child({count}) > a"))

    def executiveCommitteeEle(self):
        # self.press_button((By.CSS_SELECTOR, "ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(2) > p"))
        self.move_to_element(self.executive_comittee)
        count=0
        for i in self.executive_comittee_name:
            count = count + 1
            assert i in self.get_element_text((By.CSS_SELECTOR, f"#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(2) > div > div > div > div > ul > li:nth-child({count}) > a"))

    def strategyEle(self):
        # self.press_button((By.CSS_SELECTOR, "ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(3) > p"))
        self.move_to_element(self.strategy)
        assert "Strategy" in self.get_element_text(self.strategy)
        count=0
        for i in self.strategy_name:
            count = count + 1
            assert i in self.get_element_text((By.CSS_SELECTOR, f"#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(3) > div > div > div > div > ul > li:nth-child({count}) > a"))

    def innovativeMedicineEle(self):
        self.move_to_element(self.innovative_medicines)
        assert "More from Innovative Medicines" in self.get_element_text(self.more_from_innovative_medicines)
        count=0
        for i in self.innovative_medicines_name:
            count = count + 1
            assert i in self.get_element_text((By.CSS_SELECTOR, f"#block-mainnavigation > div > div > nav > div > ul > li:nth-child(1) > div > div > div > div:nth-child(1) > ul > li:nth-child(4) > div > div > div > div > ul > li:nth-child({count}) > a"))


    def healthCareProfessionalEle(self):
        # self.press_button((By.CSS_SELECTOR, "div > nav > div > ul > li:nth-child(2) > p"))
        self.move_to_element(self.healthcare_professionals)
        self.verify_css_property(self.healthcare_professionals, "left", "text-align")
        assert self.element_clickable(self.healthcare_professionals) == True
        assert "Healthcare Professionals" in self.get_element_text(self.healthcare_professionals)
        assert "Medical Congresses and events" in self.get_element_text(self.medical_congress_and_event)
        assert "Global Product Portfolio" in self.get_element_text(self.global_product_portfolio)
        assert "Novartis Pipeline" in self.get_element_text(self.novartis_pipeline)
        self.manageAccessProgram()
        assert "Novartis external funding" in self.get_element_text(self.novartis_external_funding)
        assert "Healthcare professional resources by country" in self.get_element_text(self.hcp_resource)

    def manageAccessProgram(self):
        # self.press_button((By.CSS_SELECTOR, "ul > li:nth-child(2) > div > div > div > div:nth-child(1) > ul > li.we-mega-menu-li.dropdown-menu > p"))
        self.move_to_element(self.managed_access_program)
        assert "Managed Access Programs" in self.get_element_text(self.managed_access_program)
        assert "More from Managed Access Programs" in self.get_element_text(self.more_from_manage_access_program)
        assert "Novartis Gene Therapies Managed Access Program" in self.get_element_text(self.managed_access_program_one)


    

