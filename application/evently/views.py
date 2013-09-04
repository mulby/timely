from django.views.generic import ListView
from evently.models import Event


class EventList(ListView):
    model = Event
