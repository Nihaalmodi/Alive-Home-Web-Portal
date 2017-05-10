from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mass_mail
from jsonimport.models import timetable
from .models import prof_subject, students_registered
from .forms import RoomForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
@login_required(login_url="/login")
def index(request):
    return render(request, 'class/home.html',{'valid': ' '})

@login_required(login_url="/login")
def get_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        rooms = form.data['room']
        valid_rooms=['NR121','NR222'];
        rooms = rooms.upper();
        if(rooms not in valid_rooms):
            return render(request,'class/home.html', {'valid':'Please enter valid room no.'})
    time_table = timetable.objects.all()
    profsubject = prof_subject.objects.all()
    studentsregistered = students_registered.objects.all()
    return render(request,'class/includes/table.html',{'prof_subject':profsubject,'students_registered':students_registered ,'rooms' : rooms, 'time_table' : time_table})
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
@csrf_exempt
def send_emails(request):
    if request.method =='POST':
        room = request.POST.get('room'),
        prof = request.POST.get('prof'),
        subject = request.POST.get('subject')
        subject_number = request.POST.get('subject_number')
        id=request.POST.get('id')
        p = students_registered.objects.filter(subject_number=subject_number)
        mail_list=[]
        for x in range(0,p.count()):
            mail_list.append(p[x].email)
        subject='Change in time table'
        if(prof==''):
            message=subject+'('+subject_number+')'+"class has been cancelled which was on"+p.time
        else:
            message=subject+'('+subject_number+')'+'Class has been reschedules to'
        from_email='nihaalmodi53@gmial.com'
        send_mail(subject, message, from_email, mail_list, fail_silently=False,)
        return HttpResponse("Success")

