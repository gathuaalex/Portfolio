from django.forms import ModelForm
from .models import *
class Commentform(ModelForm):
    class Meta:
        model=Comment
        fields=('author','body')
