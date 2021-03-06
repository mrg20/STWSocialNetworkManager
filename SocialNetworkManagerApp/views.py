from __future__ import print_function
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic.base import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from SocialNetworkManagerApp.controller.TableSizeController import TableSizeController
from SocialNetworkManagerApp.forms import BoxForm, IncidenceForm, ReviewForm
from SocialNetworkManagerApp.serializers import NetworkSerializer, ComplementSerializer, BoxSerializer
from models import Box, Incidence, Network, Complement, ReviewNetwork


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


class ReviewDetail(ListView):
    template_name = 'review.html'
    model = ReviewNetwork
    success_url="/"

    def get_context_data(self, **kwargs):
        context = super(ReviewDetail, self).get_context_data(**kwargs)
        self.__get_best_worst_reviews(context)
        reviews = ReviewNetwork.objects.order_by('date')
        context['reviews'] = reviews
        return context

    def __get_best_worst_reviews(self, context):
        networks = Network.objects.all()
        best_reviews = []
        worst_reviews = []
        for network in networks:
            top_bot_reviews = ReviewNetwork.objects.filter(network=network).order_by('rating')
            if top_bot_reviews.exists():
                best_reviews.append(top_bot_reviews.last)
                worst_reviews.append(top_bot_reviews.first)
        context['best_reviews'] = best_reviews
        context['worst_reviews'] = worst_reviews


class ReviewCreate(CreateView):
    model = ReviewNetwork
    template_name = 'review-create.html'
    form_class = ReviewForm
    success_url = "/review/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReviewCreate, self).form_valid(form)


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

    def post(self, request, *args, **kwargs):
        serializer = BoxSerializer(data=request.data)
        if serializer.is_valid() and Box.objects.filter(user=request.user,
                                                     box_num=request.POST['box_num']).exists():
            Box.objects.get(user=request.user, box_num=request.POST['box_num']).delete()
        return self.create(request, *args, **kwargs)


class APIBoxesDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    model = Box
    serializer_class = BoxSerializer

    def get_queryset(self):
        return Box.objects.filter(user=self.request.user)



