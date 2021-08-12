from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, "input[type ='submit']")


    def input_user_name(self, search_query):
        self.input_text(search_query, *self.USER_NAME)


    def input_password(self, search_query):
        self.input_text(search_query, *self.PASSWORD)


    def click_login_btn(self):
        self.click(*self.LOGIN_BTN)
