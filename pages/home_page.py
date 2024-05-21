from pages.base_page import *
class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'NavBarLogo': ('CSS', 'header.GlobalHeader h1.GlobalHeader__Logo'),
        'NavBarLogoLink': ('CSS', 'header.GlobalHeader h1.GlobalHeader__Logo a'),
        'NavBarLogoImage': ('CSS', 'header.GlobalHeader h1.GlobalHeader__Logo img')
    }

    def check_logo_available(self):
        try:
            logo_header = self.NavBarLogo
        finally:
            return True if logo_header else False