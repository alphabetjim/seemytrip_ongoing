from django import forms
from .models import Traveller


class TravellerForm(forms.ModelForm):
    """
    Form class for users to create their Traveller profile
    """
    firstname = forms.CharField(max_length = 50)
    lastname = forms.CharField(max_length = 50)
    bio = forms.CharField(widget = forms.Textarea(attrs = {'type': 'text','rows': 4, 'cols': 40}))
    profile_photo = forms.ImageField()

    class Meta:
        model = Traveller
        fields = ('firstname', 'lastname', 'bio', 'profile_photo')