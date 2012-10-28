from models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('user',)

	def save(self, user, title, content, plus_votes = 0, down_votes = 0, commit = True):
		post = super(PostForm, self).save(commit = False)
		post.user = user
		post.title = title
		post.content = content
		post.plus_votes = plus_votes
		post.down_votes = down_votes

		if commit:
			post.save()

		return post

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ('user', 'post',)

	def save(self, user, content, post, commit = True):
		comment = super(CommentForm, self).save(commit = False)
		comment.user = user
		comment.post = post
		comment.content = content

		if commit:
			comment.save()

		return comment