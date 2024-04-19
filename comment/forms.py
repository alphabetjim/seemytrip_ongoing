from django import forms
from .models import TripComment


class TripCommentForm(forms.ModelForm):
    """
    Form class for users to create a TripComment
    """
    class Meta:
        model = TripComment
        fields = ('body',)