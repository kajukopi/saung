from django.contrib import admin
from .models import Blog,Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blog, BlogAdmin)
class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)
