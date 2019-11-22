from django.shortcuts import render
from django.shortcuts import render, redirect
from . import forms
from .models import AddTripDetails


def addtrip(request):

    if request.method == 'POST':
        form = forms.trip_forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('addTrip:trip_forms')
    else:
        form = forms.trip_forms

    return render(request, "addtrip.html", {'form': form})
