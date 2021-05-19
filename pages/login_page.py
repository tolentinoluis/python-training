from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, driver):
        self.driver = driver
        self.textbox_username = '//*[@id="email_input"]'
        self.textbox_password = '//*[@id="password_input"]'
        self.button_login = '//*[@id="loginbutton"]'
        
    def open_login(self):
        self.open_url('/login')
    
    def login_user(self, username, password):
        self.enter_text(self.textbox_username, username)
        self.enter_text(self.textbox_password, password)
        self.click(self.button_login)
