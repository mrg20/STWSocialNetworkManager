from behave import *

use_step_matcher("re")


@given("I am logged in as")
def step_impl(context):
    from django.contrib.auth.models import User
    user_info = []
    for row in context.table:
        for heading in row.headings:
            user_info = row[heading]
    User.objects.create(username=user_info[0], password=user_info[1])


@step("I have a registered box")
def step_impl(context):
    from SocialNetworkManagerApp.models import Network
    from SocialNetworkManagerApp.models import Complement
    from SocialNetworkManagerApp.models import Box
    Network.objects.create()
    Complement.objects.create()
    Box.objects.create()

@then("I want to see the information of it")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass