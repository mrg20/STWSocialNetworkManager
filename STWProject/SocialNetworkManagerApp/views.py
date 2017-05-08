from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.views.generic import ListView

from models import Box


class CreateHomepage(ListView):
    model = Box
    template_name = 'homepage.html'


    #query set here???

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateHomepage, self).form_valid(form)
    def logged_user(self):
        return self.request.user

def profile_helloworld(request):
    return HttpResponse("You are now logged in (this is not permanent)")


@login_required
def homepage(request):
    return HttpResponse("Only User treatment implemented")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
