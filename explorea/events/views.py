from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event, EventRun
from .forms import EventForm, EventRunForm


def index(request):
    return render(request, 'events/index.html')

def event_listing(request):
    events = Event.objects.all()

    return render(request, 'events/event_listing.html', {'events': events})

def event_detail(request, name):
    event = Event.objects.get(name=name)
    runs = EventRun.objects.filter(event=event)

    return render(request, 'events/event_detail.html', {'runs': runs, 'event':event})

def event_new(request):

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False) # Create, but don't save the new instance.
            new_form.host = request.user
            new_form.save()
            return redirect('events')

    form = EventForm()
    return render(request, 'events/event_new.html', {'form': form} )

def event_edit(request, name):
    event = Event.objects.get(name=name)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            return redirect('events')

    form = EventForm(instance=event)
    return render(request, 'events/event_edit.html', {'form': form} )

def event_delete(request, name):
    event = Event.objects.get(name=name).delete()

    return redirect('events')

def run_new(request, name):
    event = Event.objects.get(name=name)

    if request.method == 'POST':
        form = EventRunForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False) # Create, but don't save the new instance.
            new_form.event = event
            new_form.save()
            return redirect('events')

    form = EventRunForm()
    return render(request, 'events/run_new.html', {'form': form} )
