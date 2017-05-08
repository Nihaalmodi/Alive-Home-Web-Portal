from django import forms

class RoomForm(forms.Form):
	room = forms.CharField(max_length=5,label='Enter room')

