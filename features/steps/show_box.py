from behave import *

use_step_matcher("re")


@given("I am logged in as")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I have a registered box")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I want to see the information of it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass