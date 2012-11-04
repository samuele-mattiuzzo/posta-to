from django.contrib.auth.models import User
from django import forms

class UserSignupForm(forms.Form):
	'''
		Simple registration form
	'''
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())
	mail = forms.EmailField()