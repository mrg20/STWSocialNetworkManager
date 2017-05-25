from behave import *

use_step_matcher("re")


@step("I click to create incidence")
def step_impl(context):
    context.browser.visit(context.get_url('boxes:homepage'))
    context.browser.find_by_value('incidence').click()


@step("I fill all the camps")
def step_impl(context):
    browser = context.browser
    for row in context.table:
        for heading in row.headings:
            browser.fill(heading, row[heading])


@step("I create the incidence")
def step_impl(context):
    context.browser.find_by_value('Send incidence').first.click()