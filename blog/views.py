from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.views.generic import TemplateView

## custom libs import ##
from filetransfers.api import prepare_upload, serve_file

from forms import PostForm, CommentForm
from models import Post, Comment

from random import choice

## base views ##

def view_posts(request):
	'''
		All posts ordered by date (can't get first post with id because of datastore basic indexing method)
	'''
	all_posts = Post.objects.all().order_by('-date')
	
	if all_posts:
		paginator = Paginator(all_posts, 7)
		posts = paginator.page(1)
		current = Post.objects.get(id=all_posts[0].id)
		coms = Comment.objects.filter(post=current).order_by('-date')
		next_random = choice(all_posts)

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
	all_posts = Post.objects.all().order_by('-date')
	
	if all_posts:
		paginator = Paginator(all_posts, 7)
		posts = paginator.page(1)
		current = Post.objects.get(id=id)
		coms = Comment.objects.filter(post=current).order_by('-date')
		next_random = choice(all_posts)

	return render_to_response(
		'posts.html',
		locals(), 
		context_instance=RequestContext(request)
	)

def paginate_posts(request, page):
	'''
		Returns a page of posts (for pagination)
	'''
	all_posts = Post.objects.all().order_by('-date')
	paginator = Paginator(all_posts, 2)

	posts = paginator.page(page)

	return render_to_response(
		'history.html',
		locals(), 
		context_instance=RequestContext(request)
	)

def view_comments(request, id):
	'''
		Lists all comments for a single post
	'''
	coms = Comment.objects.filter(post=current).order_by('-date')
	
	return render_to_response(
		'comments.html',
		locals(), 
		context_instance=RequestContext(request)
	)

def view_top_ranked(request):
	'''
		Top 15 posts
	'''
	top_posts = Post.objects.all().order_by('-plus_votes')[:15]

	return render_to_response(
		'top.html',
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
		@TODO: image resizing (and thumbnail generation, to avoid templatetag overhead)
	'''
	form = PostForm()
	view_url = reverse('blog.views.new_post')
	upload_url, upload_data = prepare_upload(request, view_url)

	print upload_data

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
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
	posts = Post.objects.all().order_by('-date')

	Post.objects.get(id=id).delete()

	if len(posts):
		next_random = choice(Post.objects.all())

	return render_to_response(
		'post_deleted.html',
		locals(),
		context_instance=RequestContext(request)
	)






