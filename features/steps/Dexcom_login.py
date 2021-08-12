from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given('Open Main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click Home User Button')
def open_main_page(context):
    context.app.main_page.click_home_user_btn()


@when('Input {search_query} Username')
def input_login(context, search_query):
    context.app.login_page.input_user_name(search_query)


@when('Input {search_query} Password')
def input_password(context, search_query):
    context.app.login_page.input_password(search_query)


@when('Click Login Button')
def click_login_button(context):
    context.app.login_page.click_login_btn()


@then('Page URL has {query} in it')
def verify_url_contains_query(context, query):
    context.driver.wait.until(EC.url_contains(query))















