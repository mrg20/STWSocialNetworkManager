from django.forms import ModelForm
from models import Box


class BoxForm(ModelForm):
    class Meta:
        model = Box
        exclude = ('user', 'box_num', 'logged_into_network',)