from django.db import models
from datetime import date
from datetime import time


class AddTripDetails(models.Model):
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=25)
    waiting = models.CharField(max_length=35)
    destination = models.CharField(max_length=30)
    requestedby = models.CharField(max_length=20)
    amount = models.FloatField()

    def __str__(self):
        return self.date

