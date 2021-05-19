from selenium import webdriver
from selenium.webdriver.support.ui import Select
import config

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, path):
        self.driver.get(f'{config.base_url}/{path}')
        self.driver.maximize_window()

    def click(self, element, index=0):
        self.find_elements(element)[index].click()

    def enter_text(self, element, text, index=0):
        self.find_elements(element)[index].clear()
        self.find_elements(element)[index].send_keys(text)

    def select_by_value(self, element, value):
        select_elements = Select(self.find_elements(element)[0])
        select_elements.select_by_value(value)

    def find_elements(self, element):
        if element.startswith('//'):
            return self.driver.find_elements_by_xpath(element)
        else:
            return self.driver.find_elements_by_css_selector(element)