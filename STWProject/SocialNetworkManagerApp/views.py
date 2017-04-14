from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def profile_helloworld(request):
    return HttpResponse("You are now logged in (this is not permanent)")