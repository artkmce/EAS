from django import forms
from . import models


class trip_forms(forms.ModelForm):

    class Meta:
        model = models.AddTripDetails
        fields = ['date', 'time', 'source', 'waiting', 'destination', 'requestedby', 'amount']
