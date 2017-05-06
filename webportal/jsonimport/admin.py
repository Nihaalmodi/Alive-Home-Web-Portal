from django.contrib import admin
from jsonimport.models import timetable

# Register your models here.
class timetable_list(admin.ModelAdmin):
	list_display = ("day","prof","subject","time","room")

admin.site.register(timetable, timetable_list)	