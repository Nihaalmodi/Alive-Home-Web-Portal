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
        name = request.POST.get('name'),
        prof = request.POST.get('prof'),
        subject = request.POST.get('subject')
        subject_number = request.POST.get('subject_number')
        id=request.POST.get('id')
        print(id)
        print(name)
    p=timetable.objects.get(id=id),
    p.name=new_assign
    p.prof=new_assign
    p.subject=new_assign
    p.subject_number=new_assign
    p.save()
