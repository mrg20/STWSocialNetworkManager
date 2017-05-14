from django.forms import ModelForm
from models import Box


class BoxForm(ModelForm):
    class Meta:
        model = Box
        exclude = ('box_num',)