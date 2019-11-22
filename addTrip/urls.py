from django.conf.urls import url
from .views import addtrip

app_name = 'addTrip'

urlpatterns = [
    url(r'^$', addtrip, name='trip_forms')

]
