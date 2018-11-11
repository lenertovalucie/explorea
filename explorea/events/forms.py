from django import forms
from .models import Event, EventRun


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'location',
            'category'
        ]

class EventRunForm(forms.ModelForm):

    class Meta:
        model = EventRun
        fields = [
            'happens',
            'seats_available',
            'price'
        ]
