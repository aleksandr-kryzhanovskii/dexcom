from selenium.webdriver.support.wait import WebDriverWait



class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_url(self, url,):
        self.driver.get(url)




