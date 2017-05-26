from behave import *

use_step_matcher("re")


@given("This user exists")
def step_impl(context):
    from django.contrib.auth.models import User
    user_info = []
    for row in context.table:
        for heading in row.headings:
            user_info.append(row[heading])
    User.objects.create_user(username=user_info[0], password=user_info[1])


@then("I log in")
def step_impl(context):
    user_info = []
    for row in context.table:
        for heading in row.headings:
            user_info.append(row[heading])
    context.browser.visit(context.get_url('login'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill("username", user_info[0])
    context.browser.fill("password", user_info[1])
    form.find_by_value('login').first.click()


@given("I want to log in as")
def step_impl(context):
    user_info = []
    for row in context.table:
        for heading in row.headings:
            user_info.append(row[heading])
    context.browser.visit(context.get_url('login'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill("username", user_info[0])
    context.browser.fill("password", user_info[1])
    form.find_by_value('login').first.click()



@step("The fields are invalid")
def step_impl(context):
    context.browser.find_by_text("Your  username  and  password  didn't  match.  Please  try  again.")


@then("I go to register page")
def step_impl(context):
    context.browser.find_by_value('I am not registered').click()