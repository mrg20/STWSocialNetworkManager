from __future__ import print_function
from behave import *

use_step_matcher("re")


@step("I want to see the information")
def step_impl(context):
    context.browser.visit(context.get_url('boxes:homepage'))
    context.browser.find_by_tag('p').find_by_tag('a').first.click()


@step("I delete it")
def step_impl(context):
    context.browser.find_by_tag('a').last.click()


@then("I go to the homepage")
def step_impl(context):
    context.browser.find_by_tag('a').last.click()