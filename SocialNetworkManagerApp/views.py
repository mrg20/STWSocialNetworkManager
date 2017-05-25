from __future__ import print_function
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic.base import View
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from SocialNetworkManagerApp.controller.TableSizeController import TableSizeController
from SocialNetworkManagerApp.forms import BoxForm, IncidenceForm
from SocialNetworkManagerApp.serializers import NetworkSerializer, ComplementSerializer, BoxSerializer
from models import Box, Incidence, Network, Complement


class ShowAllBox(ListView):
    model = Box
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(ShowAllBox, self).get_context_data(**kwargs)
        boxes = Box.objects.filter(user=self.request.user).order_by('box_num')
        counter = TableSizeController()
        context['user_box'] = list(boxes)
        context['num_boxes'] = range(len(boxes))
        context['sections_iterator'] = counter

        return context


class ShowSingleBox(ListView):
    model = Box
    template_name = 'box.html'

    def get_context_data(self, **kwargs):
        context = super(ShowSingleBox, self).get_context_data(**kwargs)
        box_info = Box.objects.get(user=self.request.user, box_num=self.kwargs['pk'])
        context['box_info'] = box_info
        return context


class CreateBox(CreateView):
    model = Box
    template_name = 'create_box.html'
    form_class = BoxForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.box_num = self.kwargs["pk"]
        return super(CreateBox, self).form_valid(form)


class EditBox(CreateView):
    model = Box
    form_class = BoxForm
    template_name = 'edit_box.html'
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.box_num = self.kwargs["pk"]
        if super(EditBox, self).form_valid(form):
            Box.objects.filter(user=self.request.user, box_num=self.kwargs["pk"]).delete()

        return super(EditBox, self).form_valid(form)


class DeleteBox(View):
    model = Box

    def get(self, request, pk):
        Box.objects.filter(user=request.user, box_num=pk).delete()
        return render_to_response(template_name='delete_box.html')


class IncidenceCreate(CreateView):
    model = Incidence
    template_name = 'incidence.html'
    form_class = IncidenceForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncidenceCreate, self).form_valid(form)


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


'''------------------API--------------------'''


class APINetworksList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Network
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class APINetworksDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Network
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class APIComplementsList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Complement
    queryset = Complement.objects.all()
    serializer_class = ComplementSerializer


class APIComplementsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Complement
    queryset = Complement.objects.all()
    serializer_class = ComplementSerializer


class APIBoxesList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    model = Box
    serializer_class = BoxSerializer

    def get_queryset(self):
        return Box.objects.filter(user=self.request.user)


class APIBoxesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    model = Box
    serializer_class = BoxSerializer

    def get_queryset(self):
        return Box.objects.filter(user=self.request.user)

    def put(self, request, *args, **kwargs):
        serializer = BoxSerializer(data=request.data)
        if serializer.is_valid() and Box.objects.get(user=request.user,
                                                     box_num=serializer.cleaned_data['box_num']).exists():
            Box.objects.get(user=request.user, box_num=serializer.cleaned_data['box_num']).delete()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
