from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Blog,Comment

# creating a form
class BlogForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(attrs={'rows': '10'}))
    	
	class Meta:
        # specify model to be used
		model = Blog
 
        # specify fields to be used
		fields = [
			"title",
			"description",
		]

class CommentForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(attrs={'rows': '10'}))
    	
	class Meta:
        # specify model to be used
		model = Comment
 
        # specify fields to be used
		fields = [
			"description",
		]

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name" , "email", "password1", "password2",  )

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
