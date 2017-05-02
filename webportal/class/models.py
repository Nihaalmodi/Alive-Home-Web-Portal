from django.db import models

class timetable(models.Model):
    subject_number = models.CharField(max_length=10)
    room = models.CharField(max_length=5)
    day = models.CharField(max_length=10)
    start_time = models.IntegerField('Enter time in 24-hour format',max_length=2)
    end_time = models.IntegerField('Enter time in 24-hour format',max_length=2)
    prof = models.CharField('Enter proffessor name',max_length=20)
    def __str__(self):
        return (self.subject_number+' '+self.prof+' '+self.day)
