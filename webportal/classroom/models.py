from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class prof_subject(models.Model):
	prof = models.CharField(max_length = 20)
	subject_teaching = models.CharField(max_length=20)
	subject_number = models.CharField(max_length=10, blank=True, validators =[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
	
class students_registered(models.Model):
	subject_number = models.CharField(max_length=10, blank=True, validators =[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])
	student_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)