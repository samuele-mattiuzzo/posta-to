from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete


def uploadmodel_file_upload_to(instance, filename):
	'''
		Upload path
	'''
	return 'uploads/%s/%s' % (instance.user.id, filename)

class Post(models.Model):
	'''
		Base post class
		Image can be null (text only post)
	'''
	user = models.ForeignKey(User)
	image = models.FileField(upload_to=uploadmodel_file_upload_to, blank=True, null=True)
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	plus_votes = models.FloatField(default = 0.0)
	down_votes = models.FloatField(default = 0.0)

	def get_rating(self):

		'''
			Used in templates, for now
		'''
		rate_up = self.plus_votes/(self.plus_votes+self.down_votes) if self.plus_votes > 0.0 else 0.0
		rate_down = self.down_votes/(self.plus_votes+self.down_votes) if self.down_votes > 0.0 else 0.0
		
		if rate_up > 0.8 and self.down_votes == 0.0:
			return 'very_good'
		elif rate_up > 0.7:
			return 'good'
		elif rate_down > 0.8 and self.plus_votes == 0.0:
			return 'very_bad'
		elif rate_down > 0.7:
			return 'bad'
		else:
			return 'meh'

	def plus_vote(self):
		self.plus_votes += 1.0
		return self.plus_votes

	def down_vote(self):
		self.down_votes += 1.0
		return self.down_votes

class Comment(models.Model):
	'''
		Base comment class
	'''
				
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	


