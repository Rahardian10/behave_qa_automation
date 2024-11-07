# pylint: disable=function-redefined
from behave import given, when, then # pylint: disable=no-name-in-module
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the login')
def step_impl(context):
    context.browser.implicitly_wait(10) 
    context.browser.get("https://demoqa.com/login")
    # assert(context.browser.title) == "Login"

@when('I enter valid credentials')
def step_impl(context):
    context.browser.find_element(By.ID, "userName").send_keys("tyo")
    context.browser.find_element(By.ID, "password").send_keys("Tyo123456*")
    time.sleep(5)
    # context.browser.find_element(By.ID, "login").click()
    login_button = WebDriverWait(context.browser, 10).until(
    EC.element_to_be_clickable((By.ID, "login")))
    login_button.click()
    time.sleep(5)

@then('I should be logged in')
def step_impl(context):
   element = context.browser.find_element(By.XPATH, '//*[@id="userName-label"]')
   assert element.is_displayed()
   time.sleep(5)