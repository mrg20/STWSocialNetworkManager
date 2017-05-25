from behave import *

use_step_matcher("parse")


@given("I go to the login page")
def step_impl(context):
    context.browser.visit(context.get_url('login'))


@step("I click into register")
def step_impl(context):
    context.browser.find_by_value('I am not registered').click()


@step('I register as "{username}" and "{passwordo}"')
def step_impl(context, username, passwordo):
    context.browser.fill("username", username)
    context.browser.fill("password1", passwordo)
    context.browser.fill("password2", passwordo)
    context.browser.find_by_value('Register').click()


@step("I go to the log in page")
def step_impl(context):
    context.browser.click_link_by_text('Please Login')