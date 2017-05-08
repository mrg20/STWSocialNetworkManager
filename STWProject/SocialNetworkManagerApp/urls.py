from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.http import request
from django.views.generic import ListView, DetailView, CreateView
from views import *

urlpatterns = [

    url(r'^',
        login_required(ShowAllBox.as_view()),
        name='homepage')




]
