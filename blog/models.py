from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Message(models.Model):
#	'''
#		Basic message class
#		Used for comments
#	'''
#	user = models.ForeignKey(User)
#	title = models.CharField(max_length = 100)
#	content = models.TextField()
#	date = models.DateTimeField(auto_now_add = True)

class Post(models.Model):
	'''
		Base post class
		Extends the message class with few functionalities
	'''
	user = models.ForeignKey(User)
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	comments = []
	tags = []
	plus_votes = 0
	down_votes = 0

class Comment(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length = 100)
	date = models.DateTimeField(auto_now_add = True)
	post = models.ForeignKey(Post)


