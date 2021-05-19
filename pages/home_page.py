from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class HomePage(BasePage):
    
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_locations = '//*[@id="body-home-index"]/div[1]/div/div/div/ul[1]/li[5]/a'
        self.button_manage_location = '//*[@id="body-home-index"]/div[1]/div/div/div/ul[1]/li[5]/ul/div/div[1]/div/div/a'
        self.viewbtn_addington_location = '//*[@id="1442"]/td[7]/a'
        self.signin_sidebar_button = '//*[@id="sidebar_kiosks"]/a'
        self.all_status = 'div[originalTitle]:not([class*="no-listing"])'

    def navigate_to_locations(self):
        self.click(self.dropdown_locations)
        self.click(self.button_manage_location)

    def addington_location(self):
        self.click(self.viewbtn_addington_location)
        self.click(self.signin_sidebar_button)

    def get_addington_kiosks_status(self):
        listings = []
        for index, listing in enumerate(self.find_elements(self.all_status)):
            listings.append({
                'data-original-title': int(listing.get_attribute('data-listingid')),
                'title': self.listing_title(index)
            })
        print(listings)
        return listings
