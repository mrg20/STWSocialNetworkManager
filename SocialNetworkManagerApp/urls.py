from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rest_framework.urlpatterns import format_suffix_patterns

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

    url(r'^box//(?P<pk>\d+)/create/$',
        login_required(CreateBox.as_view()),
        name='create_box'),

    url(r'^box/(?P<pk>\d+)/delete/$',
        login_required(DeleteBox.as_view()),
        name='delete_box'),

    url(r'^incidence/$',
        login_required(IncidenceCreate.as_view()),
        name='incidence')

]

urlpatterns += [
# RESTful API
    url(r'^api/restaurants/$',
        APINetworks.as_view(), name='networks')


]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])