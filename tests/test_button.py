from components.navigation.sidebar import SideBar
from pages.centr_svyazi_main import CentrSvyaziMain
from pages.centr_svyazi import CentrSvyazi
from components.modals.search_modal import SearchModal
from main import BASE_URL


class TestLogo:

    def test_logo(self, centr_svyazi_main: CentrSvyaziMain, centr_svyazi_logo: CentrSvyazi):

        centr_svyazi_main.go_to(BASE_URL)
        centr_svyazi_logo.register_button.should_have_text("Центр Связи")

    def test_catalog(self, centr_svyazi_main: CentrSvyaziMain, catalog: SideBar, menu: SideBar):
        centr_svyazi_main.go_to(BASE_URL)
        catalog.click_catalog()
        menu.menu_is_opened()
