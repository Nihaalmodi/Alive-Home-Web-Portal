from django.contrib import admin
from .models import prof_subject, students_registered

# Register your models here.
class prof_subject_list(admin.ModelAdmin):
	list_display = ("prof","subject_number","subject_teaching")

admin.site.register(prof_subject, prof_subject_list)

class students_registered_list(admin.ModelAdmin):
	list_display = ("email","student_name","subject_number")

admin.site.register(students_registered, students_registered_list)