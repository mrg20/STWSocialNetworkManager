from django.conf.urls import url
from views import *


urlpatterns = [

    url(r'^',
        login_required(ShowAllBox.as_view()),
        name='homepage')




]
