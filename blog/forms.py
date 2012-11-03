from models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('user', 'plus_votes', 'down_votes',)

	def save(self, user, commit = True):
		post = super(PostForm, self).save(commit = False)
		post.user = user
		if commit:
			post.save()

		return post

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ('user', )

	def save(self, user, content, post, commit = True):
		comment = super(CommentForm, self).save(commit = False)
		comment.user = user
		comment.post = post
		comment.content = content

		if commit:
			comment.save()

		return comment