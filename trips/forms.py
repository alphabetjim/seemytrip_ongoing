from django import forms
from .models import Trip, TripDay


class TripForm(forms.ModelForm):
    """
    Form class for travellers to create a Trip
    """
    itinerary = forms.CharField(widget=forms.Textarea(attrs={'type': 'text','rows': 4, 'cols': 40}))
    trip_photo = forms.ImageField()
    startDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    endDate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Trip
        fields = ('name', 'region', 'excerpt', 'accomm_type', 'itinerary', 
            'interests', 'startDate', 'endDate', 'trip_photo',)


class TripDayForm(forms.ModelForm):
    """
    Form class for travellers to record a trip day's journal entry 
    """
    body = forms.CharField(widget=forms.Textarea(attrs={'type': 'text','rows': 4, 'cols': 40}))
    day_photo = forms.ImageField()
    day_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = TripDay
        fields = ('title', 'day_date','locations','excerpt', 'body', 'day_photo',)