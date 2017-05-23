from __future__ import print_function
from behave import *

use_step_matcher("re")


@given("I am logged in as")
def step_impl(context):
    from django.contrib.auth.models import User
    user_info = []
    for row in context.table:
        for heading in row.headings:
            user_info.append(row[heading])
    User.objects.create(username=user_info[0], password=user_info[1])
    context.browser.visit(context.get_url('login'))
    context.browser.fill("username", user_info[0])
    context.browser.fill("password", user_info[1])
    context.browser.find_by_tag('form').first.find_by_value('login').first.click()


@step("I have a registered box")
def step_impl(context):
    from SocialNetworkManagerApp.models import Network
    from SocialNetworkManagerApp.models import Complement
    from SocialNetworkManagerApp.models import Box
    from django.contrib.auth.models import User
    network = Network.objects.create(name='caralibro', description='libro de caras', network_url='fb.com')
    complement = Complement.objects.create(type='muro', id_network=network, description='muro del libro de caras')
    Box.objects.create(user=User.objects.get(username='usuari'), box_num=1, complement=complement)


@then("I want to see the information of it")
def step_impl(context):
    context.browser.visit(context.get_url('boxes:homepage'))
    context.browser.find_by_tag('p').find_by_tag('a').first.click()
