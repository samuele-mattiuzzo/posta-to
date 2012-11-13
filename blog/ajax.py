from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

## custom libs import ##

from forms import CommentForm
from models import Post, Comment

## move to an ajax view file maybe? ##
@login_required
def new_comment(request):
	'''
		Ajax view to append a comment
	'''
	comments = None
	status = "err"
	form = CommentForm()

	if request.is_ajax():
	
		form = CommentForm(request.POST)
		if form.is_valid():

			content = form.cleaned_data['content']
			p = form.cleaned_data['post']
			post = Post.objects.get(id=p.id)
			comments = Comment.objects.filter(post=post)

			if len(comments) < 15:
				comment = form.save(request.user, content, post)

				if comment:
					comments = Comment.objects.filter(post=post)
					msg = "Thank you for your comment!"
					status = "ok"
				else:
					msg = "Couldn't post your message. Try again later."
			else:
				msg = "Sorry, post limit reached"

		else:
			msg = "Your form contains errors: " + str(form.errors)


	else:
		msg = "Don't even think about it..."

	return render_to_response(
		'comments.html', 
		{'coms' : comments, 'msg' : msg, 'class' : status },
		context_instance=RequestContext(request)
	)

@login_required
def vote_post(request, id, vote):
	''' 
		Ajax view to cast a vote for a post
		@TODO: check if player already voted
	'''
	n = 0.0

	if request.is_ajax():

		post = Post.objects.get(id=id)

		if vote == 'plus':
			n = post.plus_vote()

		elif vote == 'down':
			n = post.down_vote()

		post.save()

	return HttpResponse(int(n))