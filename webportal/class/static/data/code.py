from pprint import pprint
import json
from copy import deepcopy
file_open = open('data.csv','r')
file_read = file_open.read()
count = 0
timetable=[]
dictionary={
        'day':'RK',
        'prof':'RK',
        'subject':'RK',
        'subject_number':'RK',
        'time':'RK',
        'room':'RK',
}
counter=0
new_word=''
word_list=[]
for letter in file_read:
	if(letter==',' or letter=="\n"):
		word_list.append(new_word)
		new_word=''

	else:
		new_word=new_word+letter

with open('data.json','w') as file:
		timelist=[]
		for word in word_list:
			if(count==0):
				dictionary['day']=word
			if(count==1):
				dictionary['prof']=word
			if(count==2):
				dictionary['subject']=word
			if(count==3):
				dictionary['subject_number']=word
			if(count==4):
				dictionary['time']=word
			if(count==5):
				dictionary['room']=word
				count=-1
				timetable.append(deepcopy(dictionary))
			count=count+1
		json.dump(timetable, file)
		
		
