from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.views.generic import ListView

from models import Box


class ShowAllBox(ListView):
    model = Box
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(ShowAllBox, self).get_context_data(**kwargs)
        boxes = Box.objects.filter(user=self.request.user)
        counter = Counter()
        context['user_box'] = list(boxes)
        context['num_boxes'] = range(len(boxes))
        context['counter'] = counter

        return context


class Counter():
    def __init__(self):
        self.count = 0

    def __str__(self):
        return str(self.count)

    def increment(self):
        self.count += 1
        return ''

    def pair(self):
        return self.count % 2 == 0


def profile_helloworld(request):
    return HttpResponseRedirect('/')


'''@login_required
def homepage(request):
    return HttpResponse("Only User treatment implemented")'''


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
