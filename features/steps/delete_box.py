from __future__ import print_function
from behave import *

use_step_matcher("re")


@step("I want to see the information")
def step_impl(context):
    context.browser.visit(context.get_url('boxes:homepage'))
    context.browser.find_by_value('View Box').first.click()


@step("I delete it")
def step_impl(context):
    context.browser.find_by_value('Delete Box').last.click()


@then("I go to the homepage")
def step_impl(context):
    context.browser.find_by_tag('a').last.click()