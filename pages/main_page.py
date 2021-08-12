from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    HOME_USER_BTN = (By.CSS_SELECTOR, 'li.panel.home-user a')

    def open_main_page(self):
        self.open_url('https://clarity.dexcom.com/')

    def click_home_user_btn(self):
        self.click(*self.HOME_USER_BTN)


