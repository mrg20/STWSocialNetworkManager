from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import *


urlpatterns = [

    url(r'^$',
        login_required(ShowAllBox.as_view()),
        name='homepage'),

    url(r'^box/(?P<pk>\d+)/$',
        login_required(ShowSingleBox.as_view()),
        name='box_detail'),

    url(r'^box/(?P<pk>\d+)/edit/$',
        login_required(EditBox.as_view()),
        name='box_edit'),

    url(r'^box/create/$',
        login_required(BoxCreate.as_view()),
        name='create_box')

]
