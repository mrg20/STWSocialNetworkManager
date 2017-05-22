from django.forms import ModelForm
from models import Box, Incidence


class BoxForm(ModelForm):
    class Meta:
        model = Box
        exclude = ('user', 'box_num', 'logged_into_network',)


class IncidenceForm(ModelForm):
    class Meta:
        model = Incidence
        exclude = ('user', 'date',)
