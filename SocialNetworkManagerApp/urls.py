from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import *


urlpatterns = [

    url(r'^$',
        login_required(ShowAllBox.as_view()),
        name='homepage'),

    url(r'^homepage/',
        login_required(ShowAllBox.as_view()),
        name='homepage'),

    url(r'^box/(?P<pk>\d+)/$',
        login_required(ShowSingleBox.as_view()),
        name='box_detail'),

    url(r'^new_box/$',
        login_required(BoxCreate.as_view(model=Box, success_url="/")),
        name='new_box')

]
