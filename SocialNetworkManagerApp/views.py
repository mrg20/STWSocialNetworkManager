from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.views.generic import CreateView
from django.views.generic import ListView

from SocialNetworkManagerApp.Controller.TableSizeController import TableSizeController
from SocialNetworkManagerApp.forms import BoxForm
from models import Box


class ShowAllBox(ListView):
    model = Box
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(ShowAllBox, self).get_context_data(**kwargs)
        boxes = Box.objects.filter(user=self.request.user)
        counter = TableSizeController()
        context['user_box'] = list(boxes)
        context['num_boxes'] = range(len(boxes))
        context['counter'] = counter

        return context

    def post(self, request):
        return redirect("/box/"+request.POST.get("box_number", ""), box=request.POST.get("box_number", ""))


class ShowSingleBox(ListView):
    model = Box
    template_name = 'box.html'

    def get_context_data(self, **kwargs):
        context = super(ShowSingleBox, self).get_context_data(**kwargs)
        box_info = Box.objects.get(user=self.request.user, box_num=self.kwargs['pk'])
        context['box_info'] = box_info
        return context


class BoxCreate(CreateView):
    model = Box
    template_name = 'create_box.html'
    form_class = BoxForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.box_num=self.request.GET.get("box_number", "")
        return super(BoxCreate, self).form_valid(form)


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
