from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event, EventRun
from .forms import EventForm, EventRunForm


def index(request):
    return render(request, 'events/index.html')

def event_listing(request):
    events = Event.objects.all()

    return render(request, 'events/event_listing.html', {'events': events})

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    runs = EventRun.objects.filter(event=event)

    return render(request, 'events/event_detail.html', {'runs': runs, 'event':event})

def create_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False) # Create, but don't save the new instance.
            new_form.host = request.user
            new_form.save()
            return redirect('events')

    form = EventForm()
    return render(request, 'events/create_event.html', {'form': form} )

def update_event(request, pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            return redirect('/events/detail/{}'.format(pk))

    form = EventForm(instance=event)
    return render(request, 'events/update_event.html', {'form': form} )

def delete_event(request, pk):
    event = Event.objects.get(id=pk).delete()

    return redirect('events')

def create_event_run(request, event_id):
    event = Event.objects.get(id=event_id)

    if request.method == 'POST':
        form = EventRunForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False) # Create, but don't save the new instance.
            new_form.event = event
            new_form.save()
            return redirect('/events/detail/{}'.format(event_id))

    form = EventRunForm()
    return render(request, 'events/create_even_run.html', {'form': form} )

def update_event_run(request, event_run_id):
    event_run = EventRun.objects.get(pk=event_run_id)

    if request.method == 'POST':
        form = EventRunForm(request.POST, instance=event_run)

        if form.is_valid():
            form.save()
            event_id = event_run.event.id
            return redirect('/events/detail/{}'.format(event_id))

    form = EventRunForm(instance=event_run)
    return render(request, 'events/update_event.html', {'form': form} )

def delete_event_run(request, event_run_id):
    event_run = EventRun.objects.get(id=event_run_id)
    event_id = event_run.event.id
    event_run.delete()

    return redirect('/events/detail/{}'.format(event_id))

