from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog
 
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
 
# creating a form
class BlogForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Blog
 
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]

