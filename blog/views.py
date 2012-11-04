from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

## custom libs import ##
from filetransfers.api import prepare_upload, serve_file
from google.appengine.api import images

from forms import PostForm, CommentForm
from models import Post, Comment

from random import choice

## base views ##

def view_posts(request):
	'''
		All posts ordered by date
	'''
	posts = Post.objects.all().order_by('-date')
	if len(posts):
		current = Post.objects.get(id=posts[0].id)
		coms = Comment.objects.filter(post=posts[0])
		next_random = choice(posts)

	return render_to_response(
		'posts.html',
		locals(), 
		context_instance=RequestContext(request)
	)

def view_post(request, id):
	'''
		Single post (id)
		Separated from view_posts(request) because of possible extensions
	'''
	posts = Post.objects.exclude(id=id).order_by('-date')
	current = Post.objects.get(id=id)
	if len(posts):
		coms = Comment.objects.filter(post=current)
		next_random = choice(posts)

	return render_to_response(
		'posts.html',
		locals(), 
		context_instance=RequestContext(request)
	)

def view_top_ranked(request):
	'''
		Top 15 users and posts
	'''
	top_posts = Post.objects.all().order_by('-plus_votes')[:15]

	return render_to_response(
		'top.html',
		locals(),
		context_instance=RequestContext(request)
	)

def view_comments(request, id):
	'''
		Lists all comments for a single post
	'''
	coms = Comment.objects.filter(post=current)
	return render_to_response(
		'posts.html',
		locals(), 
		context_instance=RequestContext(request)
	)


## login-based views ##
def download_handler(request, id):
	'''
		Serves the image file
	'''
	upload = get_object_or_404(Post, id=id) 
	return serve_file(request, upload.image, save_as=True)

@login_required
def new_post(request):
	'''
		Creates a new post with image
	'''
	form = PostForm()
	view_url = reverse('blog.views.new_post')
	upload_url, upload_data = prepare_upload(request, view_url)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			## need to add image resizing when uploading, templatetag generates too much overhead
			post = form.save(user=request.user)
			return HttpResponseRedirect('/posts/%d/' % post.id)
	
	return render_to_response(
		'new_post.html',
		locals(), 
		context_instance=RequestContext(request)
	)

@login_required
def delete_post(request, id):
	'''
		Deletes a post, handles comments and images deletion
	'''
	post = Post.objects.get(id=id)
	Post.objects.get(id=id).delete()
	Comment.objects.filter(post=id).delete()

	posts = Post.objects.all()
	if len(posts):
		next_random = choice(Post.objects.all())

	return render_to_response(
		'post_deleted.html',
		locals(),
		context_instance=RequestContext(request)
	)






