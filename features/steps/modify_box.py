from behave import *

use_step_matcher("re")


@step("I want to modify it")
def step_impl(context):
    context.browser.find_by_tag('a')


@step("I modify it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass