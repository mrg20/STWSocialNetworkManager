from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.http import request
from django.views.generic import ListView, DetailView, CreateView

from views import CreateHomepage
from models import *

urlpatterns = [

    url(r'^',
        login_required(CreateHomepage.as_view(
            queryset=Box.objects.filter(box_num=1),
            context_object_name='box_list',
            template_name='homepage.html'
        )),
        name='homepage')




]