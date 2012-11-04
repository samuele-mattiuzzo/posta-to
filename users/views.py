from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from users.forms import UserSignupForm
from blog.models import Post, Comment

## custom libs import ##

def signup(request):
	'''
		User signup
	'''
	form = UserSignupForm()
	if request.POST:
		form = UserSignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			mail = form.cleaned_data['mail']

			user = User.objects.create_user(username, mail, password)
			user.save()
			return HttpResponseRedirect('/users/%d/%s' % (user.id, user.username))

	return render_to_response(
		'signup.html',
		locals(),
		context_instance=RequestContext(request)
	)

def profile(request, id, username):
	'''
		Profile page: displays posts and basic user infos
	'''
	us = User.objects.get(id=id)
	posts = Post.objects.filter(user=us).order_by('-date')
	user_posts = len(posts)

	return render_to_response(
		'profile.html',
		locals(),
		context_instance=RequestContext(request)
	)


def charts(request, id, username):
	'''
		Charts page: prepares data for googlecharts
		Displays a reputation pie and a post timeline with votes
	'''
	us = User.objects.get(id=id)
	posts = Post.objects.filter(user=us).order_by('-date')

	good_rep = 0.0
	bad_rep = 0.0
	if posts is not None:
		good_rep = sum([p.plus_votes for p in posts])
		bad_rep = sum([p.down_votes for p in posts])

	return render_to_response(
		'charts.html',
		locals(),
		context_instance=RequestContext(request)
	)