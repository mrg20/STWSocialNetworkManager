from behave import *

use_step_matcher("re")


@step("I click to create button")
def step_impl(context):
    context.browser.visit(context.get_url('boxes:homepage'))
    context.browser.find_by_value('New box').first.click()


@step("I complete the form")
def step_impl(context):
    from SocialNetworkManagerApp.models import Network
    from SocialNetworkManagerApp.models import Complement
    network = Network.objects.create(name='caralibro', description='libro de caras', network_url='fb.com')
    Complement.objects.create(type='muro', id_network=network, description='muro del libro de caras')
    context.browser.choose('complement', '1')


@then("I create the box")
def step_impl(context):
    context.browser.find_by_value('Save new box').first.click()