from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from meetings.models import Meeting, Room
from meetings.forms import MeetingForm

def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/details.html', {'meeting': meeting})


def room(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/rooms.html', {'rooms': rooms})


# MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {'form': form})
