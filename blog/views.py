from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import PostForm
from models import Post

def view_all_posts(request):
	posts = Post.objects.all()
	return render_to_response('posts.html',
		locals(), context_instance=RequestContext(request)
	)

#def view_post():
#	pass

@login_required
def new_post(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			form.save(request.user, title, content)
			return HttpResponseRedirect(reverse('blog.views.view_all_posts'))
	return render_to_response('new_post.html',
		locals(), context_instance=RequestContext(request)
	)

'''
def edit_post():
	pass

def delete_post():
	pass

def new_comment():
	pass

def edit_post():
	pass

def delete_post():
	pass

def static_page():
	pass

'''