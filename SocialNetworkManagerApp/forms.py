from django.forms import ModelForm
from models import Box, Incidence


class BoxForm(ModelForm):
    class Meta:
        model = Box
        exclude = ('box_num', 'user',)


class IncidenceForm(ModelForm):
    class Meta:
        model = Incidence
        exclude = ('user',)
