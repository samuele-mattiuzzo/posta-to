from models import Post
from django import forms

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('user',)

	def save(self, user, title, content, commit = True):
		post = super(PostForm, self).save(commit = False)
		post.user = user
		post.title = title
		post.content = content

		if commit:
			post.save()

		return post