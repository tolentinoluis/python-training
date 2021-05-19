import pytest

import config
from ui_test import TestUI
from pages.login_page import LoginPage
from pages.home_page import HomePage

class Test_Wol_001(TestUI):

    def setUp(self):
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)
    
    def test_wol_login(self):
        self.login.open_login()
        self.login.login_user(config.user_email, config.user_password)
        self.home.navigate_to_locations()
        self.home.addington_location()
        self.home.get_addington_kiosks_status()