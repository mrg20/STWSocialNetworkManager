from behave import *

use_step_matcher("re")


@step("I want to modify it")
def step_impl(context):
    context.browser.find_by_value('Edit Box').first.click()


@then("I save edited box")
def step_impl(context):
    context.browser.find_by_value('Save edited box').first.click()