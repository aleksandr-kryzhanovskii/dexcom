from pages.main_page import MainPage
from pages.login_page import LoginPage



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
