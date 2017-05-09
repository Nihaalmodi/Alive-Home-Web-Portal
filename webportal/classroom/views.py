from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from jsonimport.models import timetable
from .forms import RoomForm
from django.views.decorators.csrf import csrf_exempt
@login_required(login_url="/login")
def index(request):
    return render(request, 'class/home.html')

@login_required(login_url="/login")
def get_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        rooms = form.data['room']

    time_table = timetable.objects.all()
    return render(request,'class/includes/table.html',{'rooms' : rooms, 'time_table' : time_table})
@csrf_exempt
def update(request):
    
    if request.method == 'POST':
        room = request.POST.get('room'),
        prof = request.POST.get('prof'),
        subject = request.POST.get('subject')
        subject_number = request.POST.get('subject_number')
        id=request.POST.get('id')
        p=timetable.objects.get(id=id)
        p.prof=prof[0]
        p.room=room[0]
        p.subject=subject
        p.subject_number=subject_number
        p.save()
        return HttpResponse("Success")
