from app.application import  Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context):

    context.driver = webdriver.Chrome(executable_path='/Users/aleksandrkryzhanovskii/dexcom/features/chromedriver')

    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
