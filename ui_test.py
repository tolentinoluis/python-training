import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config

class TestUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        #options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=2')
        cls.driver = webdriver.Chrome('./webdriver/chromedriver.exe', options=options)
        cls.driver.implicitly_wait(20)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
