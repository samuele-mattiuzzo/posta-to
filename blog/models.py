from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	'''
		Base post class
	'''
	user = models.ForeignKey(User)
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	plus_votes = models.FloatField()
	down_votes = models.FloatField()

	def get_rating(self):

		'''
			Used in templates, for now
		'''

		if self.plus_votes == 0 and self.down_votes == 0:
			return ''

		rate_up = self.plus_votes/(self.plus_votes+self.down_votes)
		rate_down = self.down_votes/(self.plus_votes+self.down_votes)
		
		if rate_up > 0.7:
			return 'good'
		elif rate_down > 0.7:
			return 'bad'
		else:
			return 'meh'

	def up_vote(self):
		self.plus_votes += 1.0

	def down_vote(self):
		self.down_votes += 1.0


class Comment(models.Model):
	'''
		Base comment class
	'''
				
	user = models.ForeignKey(User)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	post = models.ForeignKey(Post)


