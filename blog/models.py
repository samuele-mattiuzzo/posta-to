from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	'''
		Base post class
		Extends the message class with few functionalities
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
		
		if rate_up > (rate_down + 0.3):
			return 'good'
		elif rate_down < (rate_up - 0.3):
			return 'bad'
		else:
			return 'meh'


class Comment(models.Model):
	user = models.ForeignKey(User)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	post = models.ForeignKey(Post)


