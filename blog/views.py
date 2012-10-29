from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import PostForm, CommentForm
from models import Post, Comment

def view_posts(request, id=None):
	if id is not None:
		posts = Post.objects.exclude(id=int(id)).order_by('-date')
		current = Post.objects.get(id=int(id))
		coms = Comment.objects.filter(post=current)
	else:
		posts = Post.objects.all().order_by('-date')
		if len(posts) > 0:
			current = Post.objects.get(id=posts[0].id)
			coms = Comment.objects.filter(post=posts[0])
		else:
			current = None
			coms = None

	return render_to_response('posts.html',
		locals(), context_instance=RequestContext(request)
	)

@login_required
def new_post(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			form.save(request.user, title, content)
			return HttpResponseRedirect(reverse('blog.views.view_posts'))
	return render_to_response('new_post.html',
		locals(), context_instance=RequestContext(request)
	)

@login_required
def new_comment(request):
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			post = request['current']
			form.save(request.user, content, post)
			return HttpResponseRedirect(reverse('blog.views.view_posts'))
	return render_to_response('posts.html',
		locals(), context_instance=RequestContext(request)
	)