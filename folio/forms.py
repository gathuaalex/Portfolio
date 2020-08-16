from django import forms

TITLE = [('MR', 'MR.'), ('MRS', 'MRS.')]
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30,widget=forms.Select(choices=TITLE))
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!',required=True
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')
            if "@" and "." not in email:
               raise forms.ValidationError("enter a valid email")
