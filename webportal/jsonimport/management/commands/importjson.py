from django.core.management.base import BaseCommand
import json
from jsonimport.models import timetable
class Command(BaseCommand):

    def handle(self, *args, **options):
        json_file=json.loads(open("./data.json").read())
        for dictionary in json_file:
        	obj=timetable.objects.create(
        		day = dictionary['day'],
        		prof = dictionary['prof'],
        		subject = dictionary['subject'],
        		subject_number = dictionary['subject_number'],
        		room = dictionary['room'],
        		time = dictionary['time']
        		)
        
