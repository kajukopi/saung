from django.db import models

class Blog(models.Model):

    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        db_table = 'blog'
    # renames the instances of the model
    # with their title name

    def __str__(self):
        return self.title

class Comment(models.Model):

    # fields of the model
    title = models.ForeignKey(Blog,on_delete=models.CASCADE ,related_name='title_comment')
    description = models.TextField()

    class Meta:
        db_table = 'comment'
    # renames the instances of the model
    # with their title name

    def __str__(self):
        return self.description
        