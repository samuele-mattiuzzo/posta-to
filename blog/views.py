from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from forms import PostForm, CommentForm
from models import Post, Comment

## base views ##

def view_posts(request, id=None):
	posts = Post.objects.all().order_by('-date')
	
	if len(posts) > 0:
		current = Post.objects.get(id=posts[0].id)
		coms = Comment.objects.filter(post=posts[0])
	else:
		current = None
		coms = None

	return render_to_response(
		'posts.html',
		locals(), 
		context_instance=RequestContext(request)
	)

def view_post(request, id=None):
	if id is not None:
		posts = Post.objects.exclude(id=int(id)).order_by('-date')
		current = Post.objects.get(id=int(id))
		coms = Comment.objects.filter(post=current)

	return render_to_response(
		'posts.html',
		locals(), 
		context_instance=RequestContext(request)
	)

def view_comments(request, id):
	coms = Comment.objects.filter(post=current)

	return render_to_response(
		'posts.html',
		locals(), 
		context_instance=RequestContext(request)
	)


## login-based views ##

@login_required
def new_post(request):
	form = PostForm()

	if request.method == 'POST':

		form = PostForm(request.POST)
		if form.is_valid():

			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			post = form.save(request.user, title, content)

			return HttpResponseRedirect('/posts/%d/' % post.id)

	return render_to_response(
		'new_post.html',
		locals(), 
		context_instance=RequestContext(request)
	)

@login_required
def delete_post(request, id):
	post = Post.objects.get(id=id)
	Post.objects.get(id=id).delete()
	Comment.objects.filter(post=id).delete()
	return render_to_response(
		'post_deleted.html',
		locals(),
		context_instance=RequestContext(request)
	)



@login_required
def new_comment(request):
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

	n = 0.0

	if request.is_ajax():

		post = Post.objects.get(id=int(id))

		if vote == 'plus':
			n = post.plus_vote()

		elif vote == 'down':
			n = post.down_vote()

		post.save()

	return HttpResponse(int(n))



