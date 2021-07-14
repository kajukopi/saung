from django import forms
from .models import Blog
 
 
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