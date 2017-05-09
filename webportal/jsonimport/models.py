from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class timetable(models.Model):
	day = models.CharField(max_length=10)
	prof = models.CharField(max_length = 20, blank=True)
	subject = models.CharField(max_length = 20, blank=True)
	subject_number = models.CharField(max_length=10, blank=True, validators =[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
	room = models.CharField(max_length = 5, blank=True, validators=[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
	TIME_CHOICES=(
		('8am-8:55am','8am-8:55am'),
		('9am-9:55am','9am-9:55am'),
		('10am-10:55am','10am-10:55am'),
		('11am-11:55am','11am-11:55am'),
		('12pm-12:55pm','12pm-12:55pm'),
		('1pm-1:55pm','1pm-1:55pm'),
		('2pm-2:55pm','2pm-2:55pm'),
		('3pm-3:55pm','3pm-3:55pm'),
		('4pm-4:55pm','4pm-4:55pm'),
		('5pm-5:55pm','5pm-5:55pm')
	)
	time = models.CharField(max_length=20, choices= TIME_CHOICES, default='8:00am-8:55am')
