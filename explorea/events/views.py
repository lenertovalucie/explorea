from django.http import HttpResponse
from django.shortcuts import render
from .models import Event, EventRun


def index(request):
    return render(request, 'events/index.html')

def event_listing(request):
    events = Event.objects.all()

    return render(request, 'events/event_listing.html', {'events': events})

def event_detail(request, name):
    event = Event.objects.get(name=name)
    runs = EventRun.objects.filter(event=event)

    return render(request, 'events/event_detail.html', {'runs': runs, 'event':event})