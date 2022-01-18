from behave import *
from selenium.webdriver.common.by import By
use_step_matcher(‘re’)

@then(‘There is a title shown on the page’)
def step_impl(context, link_id) :
            title_tag = context.browser.find_element(By.TAG_NAME, ‘h1’)
            assert title_tag.is_displayed()

@step(‘The title tag has content “(.*)”’)
def step_impl(context, context):
            title_tag = context.browser.find_element(By.TAG_NAME, ‘h1’)
            assert title_tag.text = content()
