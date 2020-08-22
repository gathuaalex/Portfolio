from django.forms import ModelForm
from .models import Contact_me

class Contact_me_form(ModelForm):
    class Meta:
        model = Contact_me
        fields = [
            'name', 'email', 'message'
        ]
